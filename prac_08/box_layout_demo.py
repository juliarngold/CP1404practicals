# import random
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    # def handle_pressed(self):
    #     if random.randint(1, 10) <= 5:
    #         self.root.ids.output_label.text = "ouch!!"
    #     else:
    #         self.root.ids.output_label.text = "stop that!!"

    def handle_greet(self):
        # print("test")
        # self.root.ids.output_label.text = "Hello "
        name = self.root.ids.input_name.text  # Get text from the input field
        self.root.ids.output_label.text = f"Hello {name}"  # Update label text with the input

    def handle_clear(self):
        # Clear the input field and the output label
        self.root.ids.input_name.text = ''  # Reset TextInput to blank
        self.root.ids.output_label.text = ''  # Reset Label to blank

BoxLayoutDemo().run()
