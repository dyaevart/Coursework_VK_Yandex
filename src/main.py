from pprint import pprint
from global_vars import GlobalVars
from vk_api_client import VKAPIClient
from yandex_disk_api_client import YandexDiskAPIClient


GlobalVars.initialize()

vk_client = VKAPIClient(GlobalVars.VK_TOKEN, GlobalVars.VK_USER_ID)
yandex_client = YandexDiskAPIClient(GlobalVars.YANDEX_TOKEN)

photos_list = vk_client.get_photos_data("wall")
# pprint(photos_list)
files_names = vk_client.download_photos(photos_list)
# pprint(files_names)
yandex_client.create_folder("testFolderFromVK")
yandex_client.upload_files("testFolderFromVK", files_names)