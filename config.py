
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN',1745313525:AAHEjKFI6PYKV1f5bg7HgzpXT4mMfPqaRkg)
    APP_ID = os.environ.get('APP_ID',2361573)
    API_HASH = os.environ.get('API_HASH',116203ba585711bffe7c2692c82cd3e2)

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('1629499623','1098504493').split(',')]

    DOWNLOAD_DIR = 'downloads'
