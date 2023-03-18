import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ChildApp(GridLayout):
    def __init__(self):
        super(ChildApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='Student Name'))
        self.student_name = TextInput()
        self.add_widget(self.student_name)

        self.press = Button(text='Submit')
        self.press.bind(on_press=self.submit)
        self.add_widget(self.press)

    def submit(self, instance):
        user_data = UserData()
        user_data.name = self.student_name.text
        print(user_data)


class ParentApp(App):
    def build(self):
        return ChildApp()


class UserData:
    def __init__(self):
        self.name = None

    def __str__(self):
        return f'Student name: {self.name}\n'


if __name__ == '__main__':
    ParentApp().run()
