""" Audio class
"""

__version__ = "0.1"
__author__ = "Nahidul Islam"


import sounddevice as sd


class Audio:
    def __init__(self, audio, sr):
        self.__audio = audio
        self.__sr = sr

    def play(self):
        sd.play(self.__audio.reshape(len(self.__audio), 1), self.__sr)

    def __str__():
        print("Audio object.")


if __name__ == "__main__":
    print("Play audio file")
