import requests
from pprint import pprint
from src.global_vars import GlobalVars


class YandexDiskAPIClient:

    def __init__(self, token):
        self.token = token

    def get_common_headers(self):
        return {
            "Authorization": "OAuth " + self.token
        }

    def _build_url(self, api_method):
        return f"{GlobalVars.YANDEX_BASE_URL}/{api_method}"

    def create_folder(self, folder_name):
        params = {"path": folder_name}
        requests.put(self._build_url("resources"), params=params, headers=self.get_common_headers())

    def upload_files(self, target_folder, files_names):
        files_hrefs = []

        for file_name in files_names:
            params = {"path": f"{target_folder}/{file_name}"}
            response = requests.get(self._build_url("resources/upload"), params=params, headers=self.get_common_headers())
            file_href = response.json()["href"]

            with open(file_name, "rb") as f:
                requests.put(file_href, files={"file": f})