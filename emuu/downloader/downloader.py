""" Remote Data dowloader
"""

__version__ = "0.1"
__author__ = "Nahidul Islam"

import requests
import urllib
from pathlib import Path
import threading
from tqdm import tqdm
import py7zr
from emuu.helper.config_helper import ConfigHelper


class Downloader:
    def __init__(self, source_url=None, destination_path=None):
        ch = ConfigHelper()
        self.__source_url = ch.get_base_url() if source_url is None else source_url
        self.__destination_path = ch.get_destination_path() if destination_path is None else destination_path
        self.__files = ch.get_file_names()

    def download(self, index=None):
        files = self.__files[:] if index is None else self.__files[index : index + 1]
        for i in range(len(files)):
            thread = threading.Thread(target=self.__download_file, args=[files[i]])
            thread.start()

    def __download_file(self, file):
        CHUNK_SIZE = 1024
        destination_dir = Path(self.__destination_path)
        file_path = destination_dir / file
        # create dir if doesn't exist.
        if not destination_dir.exists():
            destination_dir.mkdir()
        req = requests.get(urllib.parse.urljoin(self.__source_url, file), stream=True)
        file_size = (
            int(req.headers["Content-Length"]) if req.headers["Content-Type"] == "application/octet-stream" else 102400
        )
        with open(file_path, "wb+") as out_file:
            for chunk in tqdm(
                iterable=req.iter_content(chunk_size=CHUNK_SIZE),
                total=file_size / CHUNK_SIZE,
                unit="kB",
                desc=file,
            ):
                if chunk:
                    out_file.write(chunk)
        # unzip the zipped file
        print(file_path.suffix)
        if file_path.suffix == ".7z":
            with py7zr.SevenZipFile(file_path, "r") as archive:
                archive.extractall(path=self.__destination_path)
            file_path.unlink()  # remove the zipped file


if __name__ == "__main__":
    dl = Downloader(destination_path="/Volumes/NAHID/thesis")
    dl.download(0)
