import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


class Azure_Storage:
    def __init__(self) -> None:
        self.connection_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_str)
        self.container_name = str(uuid.uuid4())
        self.container_client = self.blob_service_client.create_container(self.container_name)

    def create_file(self) -> None:
        file = open("test.txt", "w")
        file.write("Hello, World!")
        file.close()
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=f"test.txt"
        )
        with open("./test.txt", "rb") as data:
            blob_client.upload_blob(data)

    def find_file(self) -> None:
        # iterate over all of the containers to find the files
        blobs_list = self.container_client.list_blobs()
        for blob in blobs_list:
            print(blob.name + "\n")

    def download_file(self) -> None:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=f"test.txt"
        )
        download_file_path = "./downloaded_test.txt"
        with open(download_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())


