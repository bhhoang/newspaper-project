import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

class SignUpScreen(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(SignUpScreen, self).__init__(**kwargs)
        # Set columns
        self.cols = 1
        self.row_force_default=True
        self.row_default_height=180
        self.col_force_default=True
        self.col_default_width=100
        # Create 2nd grid layout
        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height=50,
            col_force_default=True,
            col_default_width=400,
        )
        self.top_grid.cols = 2

        self.top_grid.add_widget(Label(text="Name: "))
        # Create text input box
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Date of Birth: "))
        # Create text input box
        self.dob = TextInput(multiline=False)
        self.top_grid.add_widget(self.dob)

        self.top_grid.add_widget(Label(text="Email: "))
        # Create text input box
        self.email = TextInput(multiline=False)
        self.top_grid.add_widget(self.email)

        # Add widgets
        self.top_grid.add_widget(Label(text="Username: "))
        # Create text input box
        self.username = TextInput(multiline=False)
        self.top_grid.add_widget(self.username)

        # Add widgets
        self.top_grid.add_widget(Label(text="Password: "))
        # Create text input box
        self.password = TextInput(password=True, multiline=False)
        self.top_grid.add_widget(self.password)

        self.top_grid.add_widget(Label(text="Confirm password: "))
        # Create text input box
        self.confirm_password = TextInput(password=True, multiline=False)
        self.top_grid.add_widget(self.confirm_password)

        # Add the new grid layout to the app
        self.add_widget(self.top_grid)

        # Create a sign in button
        self.sign_in_button = Button(text="Sign Up",
                                     font_size=30,
                                     size_hint_y=None,
                                     height=50,
                                     size_hint_x=None,
                                     width=200)
        self.sign_in_button.bind(on_press=self.pressed)
        self.add_widget(self.sign_in_button)

    def pressed(self, instance):

        # Clear input boxes
        self.name.text = ""
        self.dob.text = ""
        self.email.text = ""
        self.username.text = ""
        self.password.text = ""
        self.confirm_password.text = ""


class MyApp(App):
        def build(self):
            return SignUpScreen()

if __name__ == '__main__':
    MyApp().run()
