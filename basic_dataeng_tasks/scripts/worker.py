import time
import os

from utils.task_manager import TaskManager
from utils import files
from utils.constants import ORIGIN_FOLDER_PATH, DESTINY_FOLDER_PATH, HOST


class Worker:
    def __init__(self) -> None:
        self.counter = 0

    def run(self):
        while True:
            time.sleep(3)  # To slow down the process
            self._move_files()

    def _move_files(self):
        task = TaskManager.next(HOST)

        if not task:
            print("---No tasks to execute---")
            time.sleep(5)
        else:
            self._safe_handle_task(task)

    def _safe_handle_task(self, task: TaskManager):
        try:
            self._move_file(task.file_name)
        except Exception as ex:
            task.failed(ex)

        if (task.error is None or task.error == " "):
            self.counter += 1
            print(f"Moved file: {task.file_name}")
            task.destroy()

    def _move_file(self, file_name: str):
        origin_path = os.path.join(ORIGIN_FOLDER_PATH, file_name)
        destiny_path = os.path.join(DESTINY_FOLDER_PATH, file_name)
        files.move_file(origin_path, destiny_path)


if __name__ == '__main__':
    Worker().run()
