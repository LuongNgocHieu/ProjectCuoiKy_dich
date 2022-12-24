import speech_recognition as sr
from googletrans import Translator

import sys

# Import PyQt5 modules
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
        QGridLayout, QLabel, QLineEdit,
        QComboBox, QCheckBox, QFileDialog,
        QTextEdit)

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

RECORD_TIMEOUT = 10
RECORD_PHRASE_TIME_LIMIT = 25

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle("My Translator")
        self.setFixedSize(444, 528)

        self.btn_translate = self.findChild(QtWidgets.QPushButton, 'btn_translate') # Find the button
        self.btn_translate.clicked.connect(self.translate) # Remember to pass the definition/method, not the return value!

        self.btn_record = self.findChild(QtWidgets.QPushButton, 'btn_record') # Find the button
        self.btn_record.clicked.connect(self.record) # Remember to pass the definition/method, not the return value!

        self.textbox_input = self.findChild(QtWidgets.QTextEdit, 'textbox_input') # Find the button
        self.textbox_output = self.findChild(QtWidgets.QTextEdit, 'textbox_output') # Find the button
        self.textbox_output.readOnly = True

        self.recorder = sr.Recognizer()
        self.recorder.dynamic_energy_threshold = False
        self.recorder.energy_threshold = 600

        self.show()

    def record(self):
        print("Speak Now")

        try:
            # use the microphone as source for input.
            with sr.Microphone() as source:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                self.recorder.adjust_for_ambient_noise(source, duration=0.2)

                #listens for the user's input
                audio2 = self.recorder.listen(source,
                    timeout=RECORD_TIMEOUT,
                    phrase_time_limit=RECORD_PHRASE_TIME_LIMIT)

                # Using google to recognize audio
                record_text = self.recorder.recognize_google(audio2)
                record_text = record_text.lower()
                self.textbox_input.setText(record_text)

                print("Did you say ", record_text)
                # engine = pyttsx3.init()
                # engine.say(record_text)
                # engine.runAndWait()

        except sr.WaitTimeoutError:
            print("Timeout; No speech was detected")

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")

    def translate(self):
        translator = Translator()
        translator = Translator()
        input_text = self.textbox_input.toPlainText()
        try:
            self.translate_text = translator.translate(input_text, dest='vietnamese').text
            self.textbox_output.setText(self.translate_text)
            print(self.translate_text)
        except Exception as e:
            print(e)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        sys.exit()

