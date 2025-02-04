import requests
import os
from urllib.parse import urlparse
from pprint import pprint
from global_vars import GlobalVars
from tqdm import tqdm


class VKAPIClient:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_common_params(self):
        return {
            "access_token": self.token,
            "v": GlobalVars.VK_VERSION
        }

    def _build_url(self, api_method):
        return f"{GlobalVars.VK_BASE_URL}/{api_method}"


    def get_photos_data(self, photo_type):
        params = self.get_common_params()
        params.update({"owner_id": self.user_id, "album_id": photo_type, "extended": 1})
        response = requests.get(self._build_url("photos.get"), params=params).json()

        photos_list = []
        for item in tqdm(response["response"]["items"], desc="Creating photos list ..."):
            photos_list.append({
                "id": item["id"],
                "likes": item["likes"]["count"],
                "url": item["sizes"][-1]["url"],
                "extension": os.path.splitext(urlparse(item["sizes"][-1]["url"]).path)[1]
                })
        return photos_list

    def download_photos(self, photo_data):
        files_names=[]
        for photo in tqdm(photo_data, desc="Downloading photos from VK ..."):
            response = requests.get(photo["url"])
            filename = str(photo["id"]) + "_" + str(photo["likes"]) + photo["extension"]
            with open(filename, "wb") as f:
                f.write(response.content)
            files_names.append(filename)
        return files_names