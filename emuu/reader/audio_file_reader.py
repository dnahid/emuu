""" Read audio file
"""

__version__ = "0.1"
__author__ = "Nahidul Islam"


import librosa
from emuu.reader.file_reader import FileReader
from emuu.reader.audio import Audio


class AudioFileReader(FileReader):
    def __init__(self, path):
        super().__init__(path)

    # read audio file with librosa arguments
    def get(self, index=None, **kwargs):
        if index is None:
            raise ("Index of the file is not given.")
        x, sr = librosa.load(self.get_file_path(index), **kwargs)
        return Audio(x, sr)


if __name__ == "__main__":
    afr = AudioFileReader("/Volumes/NAHID/thesis/development")
    print(afr.get_file_path(1))
    # audio = afr.get(1, offset=1.0, duration=5)
    audio = afr.get(1)
    audio.play()
