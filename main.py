from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.label import Label

# Меняем шрифт по умолчанию
LabelBase.register(name="Roboto",
                   fn_regular="fonts/Roboto/Roboto-Thin.ttf")


class WeatherApp(App):

    def build(self):
        label = Label(text="Hello weather!",
                      font_size=50)
        return label


if __name__ == "__main__":
    app = WeatherApp()
    app.run()

