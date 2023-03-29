import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

class LoginScreen(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(LoginScreen, self).__init__(**kwargs)
        # Set columns
        self.cols = 1
        self.row_force_default=True
        self.row_default_height=78
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

        # Add the new grid layout to the app
        self.add_widget(self.top_grid)

        # Create a sign in button
        self.sign_in_button = Button(text="Sign In",
                                     font_size=30,
                                     size_hint_y=None,
                                     height=50,
                                     size_hint_x=None,
                                     width=200)
        self.sign_in_button.bind(on_press=self.pressed)
        self.add_widget(self.sign_in_button)

    def pressed(self, instance):
        username = self.username.text
        password = self.password.text
        self.add_widget(Label(text=f"Success! Welcome back {username}!"))

        # Clear input boxes
        self.username.text = ""
        self.password.text = ""


class MyApp(App):
        def build(self):
            return LoginScreen()

if __name__ == '__main__':
    MyApp().run()

#name, dob, email, username, password, confirm password