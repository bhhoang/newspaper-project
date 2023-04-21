from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi
import json


class ProfileWindow(QDialog):
       def __init__(self, news):
              super(ProfileWindow, self).__init__()
              loadUi("./views/profile.ui", self)
              self.show()
              self.stackedWidget.setCurrentWidget(self.profile_page)
              self.state = json.loads(open("./cache/state.json", 'r').read())
              self.name_display.setText(self.state.get("name"))
              self.email_display.setText(self.state.get("email"))
              self.gender_display.setText(self.state.get("gender", "Not set"))
              if self.state.get("expertise") == []:
                     self.expertise_display.setText("Not set")
              self.bio_display.setText(self.state.get("bio", "Not set"))
              dob_list = self.state.get("dob").split("/")
              self.day_display.setText(dob_list[0])
              self.month_display.setText(dob_list[1])
              self.year_display.setText(dob_list[2])
              self.expertise_display.setText(self.state.get("expertise"))
              self.edit_profile_button.clicked.connect(lambda: self.edit_profile(news))
       
       def edit_profile(self, news):
              self.stackedWidget.setCurrentWidget(self.edit_page)
              self.setWindowTitle("Edit profile")
              self.name_edit.setPlainText(self.state.get("name"))
              self.email_edit.setPlainText(self.state.get("email"))
              dob_list = self.state.get("dob").split("/")
              self.gender_edit.setCurrentText(self.state.get("gender"))
              self.day_edit.setValue(int(dob_list[0]))
              self.month_edit.setValue(int(dob_list[1]))
              self.year_edit.setValue(int(dob_list[2]))
              self.expertise_edit.setCurrentText(self.state.get("expertise"))
              self.bio_edit.setPlainText(self.state.get("bio"))
              self.show()
              self.confirm_buttons.accepted.connect(lambda: self.submit(news))
              self.confirm_buttons.rejected.connect(self.cancel)

       def submit(self, news):
              name = self.name_edit.toPlainText()
              email = self.email_edit.toPlainText()
              gender = self.gender_edit.currentText()

              dob_day = self.day_edit.value()
              dob_month = self.month_edit.value()
              dob_year = self.year_edit.value()
              dob = str(dob_day) + "/" + str(dob_month) + "/" + str(dob_year)

              expertise = self.expertise_edit.currentText()
              bio = self.bio_edit.toPlainText()
              
              # print({
              #        "username": self.state.get("username"),
              #        "password": self.state.get("password"),
              #        "expires": self.state.get("expires"),
              #        "name": name,
              #        "email": email,
              #        "id": self.state.get("id"),
              #        "gender": gender,
              #        "dob": dob,
              #        "expertise": expertise,
              #        "bio": bio,
              # })

              # Update state.json
              state = {
                     "username": self.state.get("username"),
                     # "password": self.state.get("password"),
                     "expires": self.state.get("expires"),
                     "name": name,
                     "email": email,
                     "id": self.state.get("id"),
                     "gender": gender,
                     "dob": dob,
                     "expertise": expertise,
                     "bio": bio,
              }
              with open("./cache/state.json", 'w') as f:
                     f.write(json.dumps(state))

              # Update on DB and controller's current_author
              news.set_name(name)
              news.set_email(email)
              news.set_gender(gender)
              news.set_dob(dob)
              news.set_expertise(expertise)
              news.set_bio(bio)
              self.close()

       def cancel(self):
              self.stackedWidget.setCurrentWidget(self.profile_page)
