from API import *


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
