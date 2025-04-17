import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("15578503", "6435225")) #optional
API_HASH = getenv("de14eccfa6fa8d7c2eee9656cc2bdc69", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("5525620445"))
MONGO_URL = getenv("mongodb+srv://Atul:Atul@cluster0.vjd7r1g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("7762470551:AAFbtj2V7aBnhy-q3vM6qqQ9DIAdeF6mLLI", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("BQDttYcAv_Lgda1aJnZ1tFnfZZ8i_170e3gqpRKvpiNrl_6Cfkttt7sTS-q8v05ec4TozfyNiqEmGMPJLUxaPwhZxuvsQHHT0uYVfRhyp96JppHc33JgYozW_2SI53QVwNtX4cSssdGj1m3n3F1HjgBXTYllpd7MO2sidtTbuHPYeG_i4igg8IUyyUsAZyHWUvmApwSgAfEDW1nwJUJXZC-7-_qdgF8s58YXF2HxElCihJQF2hgCSO_sxqsVqxNq3glkNk5M3VSzB_OA0h4S6hGud52C7elLvUNVOwzvslR5aGJnHvCdVp0o-0IMYYy0KdI_rRi53bjtxvy9fnV411i1yaFTuAAAAAFJWkbdAA", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
