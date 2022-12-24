import googletrans
import speech_recognition
import gtts
import playsound
print(googletrans.LANGUAGES)
input_lang = 'en'
output_lang = "vi"
recognizer = speech_recognition.Recognizer()



with sr.AudioFile(filename) as source:
    voice = recognizer.listen(source,offset=3,duration=30)
    text= recognizer.recognize_google(voice,language=input_lang)
    print(text)

translator = googletrans.Translator()
translation = translator.translate(text, dest = output_lang)
print(translation.text)

converted_audio = gtts.gTTS(translation.text, lang = output_lang)
converted_audio.save('sound.mp3')
playsound.playsound('sound.mp3')