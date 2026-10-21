from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, filename):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self, filename):
        print("Google Drive: uploaded", filename)

    def download_file(self, filename):
        print("Google Drive: downloaded", filename)

    def delete_file(self, filename):
        print("Google Drive: deleted", filename)


class Dropbox(CloudStorage):
    def upload_file(self, filename):
        print("Dropbox: uploaded", filename)

    def download_file(self, filename):
        print("Dropbox: downloaded", filename)

    def delete_file(self, filename):
        print("Dropbox: deleted", filename)


for storage in [GoogleDrive(), Dropbox()]:
    storage.upload_file("document.pdf")
    storage.download_file("document.pdf")
    storage.delete_file("document.pdf")
