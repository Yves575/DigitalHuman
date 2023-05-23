from furhat_remote_api import FurhatRemoteAPI
import warnings
from mindmeld.components.nlp import NaturalLanguageProcessor

warnings.filterwarnings("ignore", category=DeprecationWarning)
nlp = NaturalLanguageProcessor('.')
nlp.load()
print(nlp.process('I do a lot of sport'))
print(type(nlp.process('When does Elm Street close?')))


furhat = FurhatRemoteAPI("localhost")
furhat.set_voice(name='Matthew')

def main():
    while True:
        # Start listening
        print("Furhat is listening...")
        speech_text = furhat.listen()

        if speech_text is None:
            continue
        data = nlp.process(speech_text.message)
        furhat.say(text="You said " + data["text"] + ". The domain of this sentence is " + data["domain"] + ". And the intent found is " + data["intent"], blocking=True)
        speech_text = ""
        

if __name__ == "__main__":
    main()
