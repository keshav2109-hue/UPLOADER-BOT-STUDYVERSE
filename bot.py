# ©️ MADHAV-SHARMA | @Madhav_IzPro | STUDYVERSE_NETWORK_SV | @MadhavX_IzPro | keshav-2109-hue/UPLOADER-BOT-STUDYVERSE

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/keshav-2109-hue/UPLOADER-BOT-STUDYVERSE

import os
from plugins.config import Config
from pyrogram import Client

if __name__ == "__main__" :
    
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Client = Client("@UploaderStudyVerseBot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    upload_boost=True,
    sleep_threshold=300,
    plugins=plugins)
    print("🎊 I AM ALIVE 🎊  • Support @StudyVerse_Network_SV")
    Client.run()
