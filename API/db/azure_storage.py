from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


class Azure_Storage:
    def __init__(self, container_name) -> None:
        self.connection_str = "DefaultEndpointsProtocol=https;AccountName=helpyoulearnstuff;AccountKey=WMruG6IqnwGspaRB9vIL+SmhTwzM3iPE7cRtjHkikxpa7WJo5EvQ+rIqjFZIgoPqwmEvOCZ/4KSf42yVX8kkQQ==;EndpointSuffix=core.windows.net"
        self.blob_service_client = BlobServiceClient.from_connection_string(
            conn_str=self.connection_str
        )
        self.container_name = str(container_name)
        try:
            self.container_client = self.blob_service_client.create_container(self.container_name)
        except:
            pass

    def create_file(self, file_rb, file_name_in_the_cloud) -> None:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=file_name_in_the_cloud
        )
        blob_client.upload_blob(file_rb, overwrite=True)

    def find_file(self) -> None:
        # iterate over all of the containers to find the files
        blobs_list = self.container_client.list_blobs()
        files = []
        for blob in blobs_list:
            files.append(blob.name)
        return files

    def download_file(self, file_name_in_the_cloud) -> None:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=file_name_in_the_cloud
        )
        return blob_client.download_blob().readall()

    def delete_blob(self) -> None:
        self.container_client.delete_container()
