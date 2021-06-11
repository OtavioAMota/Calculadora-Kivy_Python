from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class inclement(BoxLayout):
    def calcular(self, calcula):
        if calcula:
            try:
                self.display.text = str(eval(calcula))
            except Exception:
                self.display.text = "Erro"


class Calculadora(App):
    def build(self):
        return inclement()


Calculadora().run()
