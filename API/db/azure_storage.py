from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


class Azure_Storage:
    def __init__(self, container_name) -> None:
        self.connection_str = "DefaultEndpointsProtocol=https;AccountName=helpyoulearnstuff;AccountKey=WMruG6IqnwGspaRB9vIL+SmhTwzM3iPE7cRtjHkikxpa7WJo5EvQ+rIqjFZIgoPqwmEvOCZ/4KSf42yVX8kkQQ==;EndpointSuffix=core.windows.net"
        self.blob_service_client = BlobServiceClient.from_connection_string(
            conn_str=self.connection_str)
        self.container_name = str(container_name)
        try:
            self.container_client = self.blob_service_client.create_container(
                self.container_name)
        except:
            pass

<<<<<<< Updated upstream
    def create_file(self, file_rb, file_name_in_the_cloud) -> None:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=file_name_in_the_cloud)
        blob_client.upload_blob(file_rb, overwrite=True)
=======
    def create_file(self, file_rb, file_name_in_the_cloud) -> list:
        try:
            blob_client = self.blob_service_client.get_blob_client(
                container=self.container_name, blob=file_name_in_the_cloud
            )
            blob_client.upload_blob(file_rb, overwrite=True)
            return [True, blob_client]
        except Exception as e:
            return [False, e]
>>>>>>> Stashed changes

    def find_file(self) -> list:
        try:
            blobs_list = self.container_client.list_blobs()
            files = []
            for blob in blobs_list:
                files.append(blob.name)
            return files
        except Exception as e:
            return []

<<<<<<< Updated upstream
    def download_file(self, file_name_in_the_cloud) -> None:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=file_name_in_the_cloud)
        return blob_client.download_blob().readall()
=======
    def download_file(self, file_name_in_the_cloud) -> str:
        try:
            blob_client = self.blob_service_client.get_blob_client(
                container=self.container_name, blob=file_name_in_the_cloud
            )
            return blob_client.download_blob().readall().decode("utf-8")
        except Exception as e:
            return e
>>>>>>> Stashed changes

    def delete_blob(self) -> bool:
        try:
            self.container_client.delete_container()
            return True
        except Exception as e:
            return False
