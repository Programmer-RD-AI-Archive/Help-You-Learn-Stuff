# import base64

# def encode(message: str) -> bytes:
#     """
#     Encode string for privacy and encryption.
#     """
#     msg_bytes = message.encode("latin-1")
#     string_bytes = base64.b64encode(msg_bytes)
#     string = string_bytes.decode("latin-1")
#     return string

# {
#     '{"info":{"1":["trtret","gerger"]},"yourdiv":"<div class': '\\"mb-3\\"><label for=\\"1-Label\\" class=\\"form-label\\"><input type=\\"text\\" class=\\"form-control\\" id=\\"1-Input-Name\\"></label><input type=\\"text\\" class=\\"form-control\\" id=\\"1-Content\\"></div>"}'
# }

# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
# tag = soup.b

# new_tag = soup.new_tag("b")
# new_tag.string = "example.com"
# a_tag.i.replace_with(new_tag)
import os
import uuid

from azure.storage.blob import (
    BlobClient,
    BlobServiceClient,
    ContainerClient,
    __version__,
)

# yourdiv.replace(str(all_input[0]), info[str(idx)][0])
from bs4 import BeautifulSoup, Tag

# new_tag = soup.new_tag("h1")
# new_tag.string = "example.com"
# a_tag.i.replace_with(new_tag)

# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup, "html.parser")
# a_tag = soup.a


class Azure_Storage:
    def __init__(self, ) -> None:
        self.connection_str = "DefaultEndpointsProtocol=https;AccountName=helpyoulearnstuff;AccountKey=WMruG6IqnwGspaRB9vIL+SmhTwzM3iPE7cRtjHkikxpa7WJo5EvQ+rIqjFZIgoPqwmEvOCZ/4KSf42yVX8kkQQ==;EndpointSuffix=core.windows.net"
        self.blob_service_client = BlobServiceClient.from_connection_string(
            self.connection_str)
        print(self.blob_service_client.list_blobs())
        self.container_name = str("cources")
        self.container_client = self.blob_service_client.create_container(
            self.container_name)

    def create_file(self, file_rb, file_name_in_the_cloud) -> None:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=file_name_in_the_cloud)
        blob_client.upload_blob(file_rb)

    def find_file(self) -> None:
        # iterate over all of the containers to find the files
        blobs_list = self.container_client.list_blobs()
        files = []
        for blob in blobs_list:
            files.append(blob.name)
        return files

    def download_file(self, file_name_in_the_cloud) -> None:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=file_name_in_the_cloud)
        return blob_client.download_blob().readall()


info = '{"1": ["trtret", "gerger"]}'
info = bytes(info, encoding="utf-8")
print(info)
azure_storage = Azure_Storage()
# azure_storage.create_file(file_name_in_the_cloud="/a/testa.json", file_rb=info)
# azure_storage.find_file()
# azure_storage.download_file()
