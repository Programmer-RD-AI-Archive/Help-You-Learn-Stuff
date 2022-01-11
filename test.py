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

# del tag["class"]
# del tag["id"]


# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
# tag = soup.b
# del tag["class"]
# del tag["id"]

# yourdiv.replace(str(all_input[0]), info[str(idx)][0])
from bs4 import BeautifulSoup, Tag

# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup, "html.parser")
# a_tag = soup.a
# a_tag.string = "a"

# new_tag = soup.new_tag("h1")
# new_tag.string = "example.com"
# a_tag.i.replace_with(new_tag)

# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup, "html.parser")
# a_tag = soup.a

# new_tag = soup.new_tag("b")
# new_tag.string = "example.com"
# a_tag.i.replace_with(new_tag)
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import os


class Azure_Storage:
    def __init__(self, container_name) -> None:
        self.connection_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_str)
        self.container_name = container_name
        self.container_client = self.blob_service_client.create_container(self.container_name)

    def create_file(self, blob_name, file_rb) -> None:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=blob_name
        )
        blob_client.upload_blob(file_rb)

    def find_file(self) -> None:
        # iterate over all of the containers to find the files
        blobs_list = self.container_client.list_blobs()
        blobs = []
        for blob in blobs_list:
            blobs.append(blob)
        return blobs

    def download_file(self, file_name) -> None:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=file_name
        )
        return blob_client.download_blob().readall()


a_storage = Azure_Storage()

f = open("run.py", "rb")
print(f.read())
