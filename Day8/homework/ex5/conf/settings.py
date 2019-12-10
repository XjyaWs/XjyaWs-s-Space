import os

BASE_PATH = os.path.dirname(
            os.path.dirname(__file__)
)

TARGET_PATH = os.path.join(
            os.path.dirname(BASE_PATH), 'target_file'
)

SAVED_PATH = os.path.join(BASE_PATH, 'saved')
