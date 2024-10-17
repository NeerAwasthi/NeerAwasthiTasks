import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation="vertical", padding=30, spacing=10)
        
        head_label = Label(text="Python User Registration App", font_size=26, bold=True, height=40)

        # Adding labels and input fields
        name_label = Label(text="Name", font_size=18)
        self.name_input = TextInput(multiline=False, font_size=18)
        
        email_label = Label(text="Email", font_size=18)
        self.email_input = TextInput(multiline=False, font_size=18)
        
        password_label = Label(text="Password", font_size=18)
        self.Password_Input = TextInput(multiline=False, font_size=18, password=True)
        
        confirm_label = Label(text="Confirm Password", font_size=18)
        self.confirm_input = TextInput(multiline=False, font_size=18, password=True)
        
        phone_label = Label(text="Phone Number", font_size=18)
        self.phone_input = TextInput(multiline=False, font_size=18)

        address_label = Label(text="Address", font_size=18)
        self.address_input = TextInput(multiline=False, font_size=18)

        # Button
        submit_button = Button(text='Register', font_size=18, on_press=self.register)

        # Adding all widgets to layout
        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(password_label)
        layout.add_widget(self.Password_Input)                              
        layout.add_widget(confirm_label)
        layout.add_widget(self.confirm_input)
        layout.add_widget(phone_label)
        layout.add_widget(self.phone_input)
        layout.add_widget(address_label)
        layout.add_widget(self.address_input)
        layout.add_widget(submit_button)

        return layout

    def register(self, instance):
        # Collect information
        name = self.name_input.text
        email = self.email_input.text
        password = self.Password_Input.text
        confirm_password = self.confirm_input.text
        phone = self.phone_input.text
        address = self.address_input.text

        # Validation
        if name.strip() == '' or email.strip() == '' or password.strip() == '' or confirm_password.strip() == '' or phone.strip() == '' or address.strip() == '':
            message = "Please fill in all fields"
        elif password != confirm_password:
            message = "Passwords do not match"
        else:
            filename = name + '.txt'
            with open(filename, 'w') as file:
                file.write('Name: {}\n'.format(name))
                file.write('Email: {}\n'.format(email))
                file.write('Password: {}\n'.format(password))
                file.write('Phone: {}\n'.format(phone))
                file.write('Address: {}\n'.format(address))
            message = "Registration successful!\nName: {}\nEmail: {}\nPhone: {}\nAddress: {}".format(name, email, phone, address)

        # Popup to display registration status
        popup = Popup(title="Registration Status", content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == "__main__":
    RegistrationApp().run()