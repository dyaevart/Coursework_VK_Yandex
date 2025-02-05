from dotenv import load_dotenv
import os
import argparse


class GlobalVars:

    YANDEX_TOKEN = ""
    YANDEX_BASE_URL = 'https://cloud-api.yandex.net/v1/disk'
    VK_TOKEN = ""
    VK_VERSION = "5.199"
    VK_USER_ID = 955514984
    VK_BASE_URL = 'https://api.vk.com/method'

    @classmethod
    def initialize(cls):
        parser = argparse.ArgumentParser(description="Пример скрипта с параметрами")
        parser.add_argument("--vk_id", type=str, required=False, help="ID аккаунта от VK")
        parser.add_argument("--vk_token", type=str, required=False, help="Токен от VK")
        parser.add_argument("--yandex_token", type=str, required=False, help="Токен от Yandex Disk")
        args = parser.parse_args()

        if args.vk_token is not None and args.yandex_token is not None:
            cls.VK_USER_ID = args.vk_id
            cls.VK_TOKEN = args.vk_token
            cls.YANDEX_TOKEN = args.yandex_token
        else:
            load_dotenv()
            cls.VK_USER_ID = os.getenv("VK_USER_ID")
            cls.VK_TOKEN = os.getenv("VK_TOKEN")
            cls.YANDEX_TOKEN = os.getenv("YANDEX_TOKEN")
