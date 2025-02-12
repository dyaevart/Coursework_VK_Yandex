import requests
import os
import json
from global_vars import GlobalVars
from tqdm import tqdm

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
        uploaded_files_list=[]
        for file_name in tqdm(files_names, desc = "Uploading photos to Yandex Disk ..."):
            params = {"path": f"{target_folder}/{file_name}"}
            response = requests.get(self._build_url("resources/upload"), params=params, headers=self.get_common_headers())
            if (response.status_code == 409):
                print("Папка с таким именем уже есть на Диске")
                break
            file_href = response.json()["href"]

            with open(file_name, "rb") as f:
                requests.put(file_href, files={"file": f})
                uploaded_files_list.append({"file_name": file_name, "size": os.path.getsize(file_name)})

        with open('uploaded_files_list.json', 'w', encoding='utf-8') as f:
            json.dump(uploaded_files_list, f, ensure_ascii=False, indent=4)
