import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from mindmeld.components.nlp import NaturalLanguageProcessor
nlp = NaturalLanguageProcessor('.')
nlp.build()
print(nlp.process('I do a lot of sport'))
print(type(nlp.process('When does Elm Street close?')))
