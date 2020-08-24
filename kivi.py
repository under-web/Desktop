from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window


Window.size = (480, 853)

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')





from kivymd.theming import ThemeManager



def get_ingridents(m):
	nitro = str(10 * m / 1000)
	salt = str(15 * m / 1000)
	starts = str(0.5 * m / 1000)
	dextrose = str(5 * m / 1000)
	salting_time = str(round(m / 500 * 2))

	return {'nitro': nitro, 'salt': salt,
	'starts': starts, 'dextrose': dextrose,
	'time': salting_time}


class Container(GridLayout):
	
	def calculate(self):
		try:
			mass = int(self.text_input.text)
		except:
			mass = 0

		ingridents = get_ingridents(mass)


		self.salt.text = ingridents.get('salt')
		self.nitro.text = ingridents.get('nitro')
		self.sugars.text = ingridents.get('dextrose')
		self.starts.text = ingridents.get('starts')
		self.time.text = ingridents.get('time')

class MyApp(App):
	theme_cls = ThemeManager()
	title = 'Coppa app'

	def build(self):
		self.theme_cls.theme_style = 'Light'
		return Container()

if __name__ == "__main__":
	MyApp().run()
