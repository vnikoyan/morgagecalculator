from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MortgagecalculatorApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Mortgage Calculator", halign="center")


MortgagecalculatorApp().run()