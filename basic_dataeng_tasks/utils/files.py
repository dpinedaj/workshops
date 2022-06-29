import os
import random
import shutil
from typing import List

from utils.mocker import fake_dataframe
from utils.constants import BIG_FILE_SIZE, MEDIUM_FILE_SIZE, SMALL_FILE_SIZE


def create_random_size_csv(file_path: str) -> None:
    sizes = [
        BIG_FILE_SIZE,
        MEDIUM_FILE_SIZE,
        SMALL_FILE_SIZE
    ]
    size = random.choice(sizes)
    df = fake_dataframe(size)
    df.to_csv(file_path, index=False)


def list_files_in_path(folder_path: str) -> List[str]:
    return os.listdir(folder_path)


def move_file(origin_path: str, destiny_path: str) -> None:
    shutil.move(origin_path, destiny_path)


def remove_all_files_in_folder(folder_path: str) -> None:
    for path in list_files_in_path(folder_path):
        new_path = os.path.join(folder_path, path)
        os.remove(new_path)


def remove_folder(folder_path: str) -> None:
    shutil.rmtree(folder_path)


def create_folder(folder_path: str) -> None:
    os.makedirs(folder_path, exist_ok=True)


def get_len_path(folder_path: str) -> int:
    return len(list_files_in_path(folder_path))
