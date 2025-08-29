from googletrans import LANGUAGES
from googletrans import Translator
print(LANGUAGES)
t = Translator()

a= t.translate("em dep qua",src="vi",dest="en")
b = a.text
