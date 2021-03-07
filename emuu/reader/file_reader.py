""" Remote Data dowloader
"""

__version__ = "0.1"
__author__ = "Nahidul Islam"

from pathlib import Path


class FileReader:
    def __init__(self, path):
        if path is None:
            raise Exception("File path is not given")
        self._path = Path(path)
        self.__files = [x for x in self._path.glob("*")]

    def get_file_name(self, index=0):
        if len(self.__files) == 0:
            raise Exception("Empty directory")
        return self.__files[index].name

    def get_file_path(self, index=None):
        if len(self.__files) == 0:
            raise Exception("Empty directory")
        if index is None:
            raise Exception("File index is required.")
        return self._path / self.get_file_name(index)

    def get_total_number_of_files(self):
        return len(self.__files)


if __name__ == "__main__":
    fr = FileReader("/Volumes/NAHID/thesis/development")
    print(fr.get_file_path(22))
