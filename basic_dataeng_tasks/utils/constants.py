from requests import get

HOST = get('https://api.ipify.org').text
MAX_FILES_IN_PATH = 100
DB_URL = "postgresql://sqluser:PasswordO1.@workshops.postgres.database.azure.com/postgres?sslmode=require"
BIG_FILE_SIZE = 1000
MEDIUM_FILE_SIZE = 100
SMALL_FILE_SIZE = 10
ORIGIN_FOLDER_PATH = "source"
DESTINY_FOLDER_PATH = "destiny"
