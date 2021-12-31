import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here

except Exception as ex:
    print('Exception:')
    print(ex)

class Azure_Storage:
    def __init__(self):
        self.connection_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        print(self.connection_str)
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_str)
        self.container_name = str(uuid.uuid4())
        self.container_client = self.blob_service_client.create_container(self.container_name)

    def create_file(self):
        file = open("test.txt", "w")
        file.write("Hello, World!")
        file.close()
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=f"test.txt"
        )
        with open("./test.txt", "rb") as data:
            blob_client.upload_blob(data)


azure_storage = Azure_Storage()
azure_storage.create_file()
