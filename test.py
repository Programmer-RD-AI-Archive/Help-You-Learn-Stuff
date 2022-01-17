# import base64

from azure.storage.blob import BlobServiceClient, __version__


class Azure_Storage:
    def __init__(
        self,
    ) -> None:
        self.connection_str = "DefaultEndpointsProtocol=https;AccountName=helpyoulearnstuff;AccountKey=WMruG6IqnwGspaRB9vIL+SmhTwzM3iPE7cRtjHkikxpa7WJo5EvQ+rIqjFZIgoPqwmEvOCZ/4KSf42yVX8kkQQ==;EndpointSuffix=core.windows.net"
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_str)
        # print(self.blob_service_client.list_blobs())
        self.container_name = str("cources")
        self.container_client = self.blob_service_client.create_container(self.container_name)

    def create_file(self, file_rb, file_name_in_the_cloud) -> None:
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=file_name_in_the_cloud
        )
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
            container=self.container_name, blob=file_name_in_the_cloud
        )
        return blob_client.download_blob().readall()


info = '{"1": ["trtret", "gerger"]}'
info = bytes(info, encoding="utf-8")
azure_storage = Azure_Storage()
