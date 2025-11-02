from django.utils.deconstruct import deconstructible
from django.core.files.storage import Storage
from supabase import create_client, Client

supabase: Client = create_client("https://jyvpolkvpfnmjhejbszp.supabase.co",
                                 "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp5dnBvbGt2cGZubWpoZWpic3pwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwODE3NjgzOCwiZXhwIjoyMDIzNzUyODM4fQ.sFJTvmb6pGU_fTvIBTIYUgYwCh6q-aSGec8jGH1KhS8")


@deconstructible
class CustomFileStorage(Storage):
    print(print("-----------------------------------------"), Storage)

    def _open(self, name, mode='rb'):
        print("Open--------------------------")
        print(self)
        print(name)
        print("-----------------------------")
        pass

    def _save(self, name, content):
        file = content.read()
        path = str(name)
        response = supabase.storage.from_("Main").upload(file=file, path=path)
        return path

    def get_valid_name(self, name):
        # Implement any necessary filename validation or modification
        # Return a valid filename

        return name
        pass

    def exists(self, name):
        fileInfo = name.split("/")
        newName = name
        extenstion = ""
        if len(fileInfo) > 1:
            newName = fileInfo[1]
            extenstion = fileInfo[0]

        fileList = supabase.storage.from_('Main').list(extenstion)

        for file in fileList:
            fileName = file["name"]
            print(fileName)
            if newName == str(fileName):
                supabase.storage.from_('Main').remove(name)

        return False
        pass

    def url(self, name):
        fileInfo = name.split("/")
        newName = name
        extenstion = ""
        if len(fileInfo) > 1:
            newName = fileInfo[1]
            extenstion = fileInfo[0]

        fileList = supabase.storage.from_('Main').list(extenstion)

        for file in fileList:
            fileName = file["name"]
            print(fileName)
            if newName == str(fileName):
                url = supabase.storage.from_('Main').get_public_url(name)
                return url

        return "https://th.bing.com/th/id/OIP.rjDxGOQZlu4DIRl5M8Li5gAAAA?rs=1&pid=ImgDetMain"