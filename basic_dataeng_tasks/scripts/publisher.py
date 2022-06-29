import random
import time
from typing import List

from utils import files
from utils.constants import ORIGIN_FOLDER_PATH, HOST
from utils.sql import session
from utils.task_manager import TaskManager


class Publisher:
    def __init__(self) -> None:
        self.done_list = set()

    def run(self):
        while True:
            self._add_files_to_table()

    def _add_files_to_table(self):
        files_list = files.list_files_in_path(ORIGIN_FOLDER_PATH)
        if len(files_list) > 0:
            self._publish_file(files_list)
        else:
            print("---No files to publish---")
            time.sleep(5)

    def _publish_file(self, files_list: List[str]):
        file_name = random.choice(files_list)
        _id = file_name.split(".")[0]
        if _id not in self.done_list:
            task_manager = TaskManager(
                id=_id,
                file_name=file_name,
                fails=False,
                processing=False,
                error=" ",
                host=HOST
            )
            session.add(task_manager)
            session.commit()
            print("added file: " + file_name)
            self.done_list.add(_id)


if __name__ == "__main__":
    Publisher().run()
