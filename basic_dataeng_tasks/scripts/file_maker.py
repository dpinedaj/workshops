import os
import time

from utils.constants import (
    MAX_FILES_IN_PATH,
    ORIGIN_FOLDER_PATH,
    DESTINY_FOLDER_PATH)
from utils import files
from utils.task_manager import TaskManager


class FileMaker:

    def __init__(self) -> None:
        self.counter = 0

    @property
    def new_origin_file(self):
        return os.path.join(ORIGIN_FOLDER_PATH, str(self.counter) + ".csv")

    def run(self):
        try:
            self._create_base_folders()
            self._run()
        except KeyboardInterrupt:
            print("\nCleanning Data...")
        finally:
            self._remove_folders()

    def _run(self):
        while True:
            self._handle_files_logic()

    def _handle_files_logic(self):
        if files.get_len_path(DESTINY_FOLDER_PATH) >= MAX_FILES_IN_PATH:
            files.remove_all_files_in_folder(DESTINY_FOLDER_PATH)
        else:
            self._create_files()

    def _create_files(self):
        while files.get_len_path(ORIGIN_FOLDER_PATH) < MAX_FILES_IN_PATH:
            files.create_random_size_csv(self.new_origin_file)
            print(f"Created file: {self.new_origin_file}")
            self.counter += 1
        print("There's no space to write")
        time.sleep(10)

    def _create_base_folders(self):
        files.create_folder(ORIGIN_FOLDER_PATH)
        files.create_folder(DESTINY_FOLDER_PATH)

    def _remove_folders(self):
        files.remove_folder(ORIGIN_FOLDER_PATH)
        files.remove_folder(DESTINY_FOLDER_PATH)
        TaskManager.truncate()


if __name__ == "__main__":
    FileMaker().run()
