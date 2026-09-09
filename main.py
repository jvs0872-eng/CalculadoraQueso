from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.core.window import Window

Window.clearcolor = (0.15, 0.15, 0.15, 1)

class CalculadoraQueso(TabbedPanel):
    def __init__(self, **kwargs):
        super(CalculadoraQueso, self).__init__(**kwargs)
        self.do_default_tab = False
        
        # --- CASO 1: Conozco Peso -> Calculo Precio ---
        tab1 = TabbedPanelHeader(text='1. Precio')
        layout1 = BoxLayout(orientation='vertical', padding=25, spacing=10)

        layout1.add_widget(Label(text='[b]Precio del Kg en Bs (Q):[/b]', markup=True, color=(1, 1, 1, 1), font_size='16sp', size_hint_y=None, height=30))
        self.q1_input = TextInput(input_type='number', input_filter='float', multiline=False, hint_text='Ej: 6220 (Bs)', size_hint_y=None, height=45, font_size='18sp')
        layout1.add_widget(self.q1_input)

        layout1.add_widget(Label(text='[b]Peso en gramos:[/b]', markup=True, color=(1, 1, 1, 1), font_size='16sp', size_hint_y=None, height=30))
        self.peso1_input = TextInput(input_type='number', input_filter='float', multiline=False, hint_text='Ej: 500 (g)', size_hint_y=None, height=45, font_size='18sp')
        layout1.add_widget(self.peso1_input)

        btn_calc1 = Button(text='Calcular Precio', background_color=(0.1, 0.4, 0.8, 1), bold=True, size_hint_y=None, height=50)
        btn_calc1.bind(on_press=self.calcular_caso_1)
        layout1.add_widget(btn_calc1)

        btn_clear1 = Button(text='Limpiar campos', background_color=(0.6, 0.2, 0.2, 1), bold=True, size_hint_y=None, height=40)
        btn_clear1.bind(on_press=self.limpiar_caso_1)
        layout1.add_widget(btn_clear1)

        self.resultado1_label = Label(text='Precio: - Bs', color=(0.2, 1, 0.2, 1), font_size='24sp', bold=True)
        layout1.add_widget(self.resultado1_label)

        tab1.content = layout1
        self.add_widget(tab1)

        # --- CASO 2: Conozco Precio -> Calculo Peso ---
        tab2 = TabbedPanelHeader(text='2. Peso')
        layout2 = BoxLayout(orientation='vertical', padding=25, spacing=10)

        layout2.add_widget(Label(text='[b]Precio del Kg en Bs (Q):[/b]', markup=True, color=(1, 1, 1, 1), font_size='16sp', size_hint_y=None, height=30))
        self.q2_input = TextInput(input_type='number', input_filter='float', multiline=False, hint_text='Ej: 6220 (Bs)', size_hint_y=None, height=45, font_size='18sp')
        layout2.add_widget(self.q2_input)

        layout2.add_widget(Label(text='[b]Precio a cobrar en Bs:[/b]', markup=True, color=(1, 1, 1, 1), font_size='16sp', size_hint_y=None, height=30))
        self.precio2_input = TextInput(input_type='number', input_filter='float', multiline=False, hint_text='Ej: 3110 (Bs)', size_hint_y=None, height=45, font_size='18sp')
        layout2.add_widget(self.precio2_input)

        btn_calc2 = Button(text='Calcular Peso', background_color=(0.1, 0.4, 0.8, 1), bold=True, size_hint_y=None, height=50)
        btn_calc2.bind(on_press=self.calcular_caso_2)
        layout2.add_widget(btn_calc2)

        btn_clear2 = Button(text='Limpiar campos', background_color=(0.6, 0.2, 0.2, 1), bold=True, size_hint_y=None, height=40)
        btn_clear2.bind(on_press=self.limpiar_caso_2)
        layout2.add_widget(btn_clear2)

        self.resultado2_label = Label(text='Peso: - gramos', color=(0.2, 1, 0.2, 1), font_size='24sp', bold=True)
        layout2.add_widget(self.resultado2_label)

        tab2.content = layout2
        self.add_widget(tab2)

    def calcular_caso_1(self, instance):
        try:
            q = float(self.q1_input.text)
            peso = float(self.peso1_input.text)
            precio_final = (peso * q) / 1000.0
            self.resultado1_label.text = f"Precio: {precio_final:.2f} Bs"
        except ValueError:
            self.resultado1_label.text = "Error: Ingrese números"

    def calcular_caso_2(self, instance):
        try:
            q = float(self.q2_input.text)
            precio = float(self.precio2_input.text)
            peso_final = (precio * 1000.0) / q
            self.resultado2_label.text = f"Peso: {peso_final:.2f} gramos"
        except ValueError:
            self.resultado2_label.text = "Error: Ingrese números"

    def limpiar_caso_1(self, instance):
        self.q1_input.text = ''
        self.peso1_input.text = ''
        self.resultado1_label.text = 'Precio: - Bs'

    def limpiar_caso_2(self, instance):
        self.q2_input.text = ''
        self.precio2_input.text = ''
        self.resultado2_label.text = 'Peso: - gramos'

class QuesoApp(App):
    def build(self):
        self.title = 'Calculadora de Queso'
        return CalculadoraQueso()

if __name__ == '__main__':
    QuesoApp().run()
