import uuid
from pathlib import Path
from threading import Thread
from typing.io import IO

import config


class BaseFileUploader:
    """
    Базовый класс для валидации, нормализации и выгрузки файлов от клиента.
    """

    def __init__(self, upload_folder: Path = config.UPLOAD_DIR):
        """
        Parameters
        ----------
        upload_folder : Path
            Путь к директории для сохранения файлов.
        """
        self._UPLOAD_SUB_FOLDER = upload_folder

    def _make_unique_path(self, base_name: Path) -> Path:
        """
        Создаёт уникальный путь для сохренения изображения на основе
        UUID-идентификатора (uuid1).

        Parameters
        ----------
        base_name : Path
            Имя файла и его расширение.

        Returns
        -------
        Path
            Путь к сохраняемому файлу, с уникальным именем.
        """
        unique_hash = uuid.uuid1().hex
        stem_name = base_name.resolve().stem
        suffixes = "".join([suffix for suffix in base_name.suffixes])
        unique_path = Path(
            self._UPLOAD_SUB_FOLDER,
            f"{stem_name}_{unique_hash}{suffixes}"
        )
        return unique_path

    def save_file(self, save_path_to_file: Path, saved_file: IO) -> Path:
        """
        Запускает процесс сохранеия файла от клиента в новом потоке, через класс MultiThreadUploader.

        Parameters
        ----------
        save_path_to_file : Path
            Путь к сохраняемому файлу, с уникальным именем.
        saved_file : IO
            Дескриптор файла, для записи.

        Returns
        -------
        Path
            Путь к сохраненному файлу.
        """
        unique_path = self._make_unique_path(save_path_to_file)
        thread = MultiThreadUploader(unique_path, saved_file)
        thread.start()
        return unique_path


class MultiThreadUploader(Thread):
    def __init__(
            self,
            save_path_to_file: Path,
            saved_file: IO,
            chunk_size: int = 1024
    ):
        """
        Parameters
        ----------
        save_path_to_file : Path
            Путь к сохраняемому файлу, с уникальным именем.
        saved_file : IO
            Дескриптор файла, для записи.

        Returns
        -------
        Path
            Путь к сохраненному файлу.
        """
        Thread.__init__(self)
        self._path_to_file = save_path_to_file
        self._file = saved_file
        self._chunk_size = chunk_size

    def run(self):
        with open(self._path_to_file, "wb") as file_handler:
            while True:
                chunk = self._file.read(self._chunk_size)
                if not chunk:
                    break
                file_handler.write(chunk)


class ImageUploader(BaseFileUploader):
    """TODO: Implement specific image processing logic when loading"""

    def __init__(self, upload_folder: Path = config.UPLOAD_DIR):
        super().__init__(upload_folder)
        self._UPLOAD_SUB_FOLDER = Path(self._UPLOAD_SUB_FOLDER, "images")
