import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from directories import Directory, directory_id


class Driver:
    def __init__(self) -> None:
        self.google_auth: GoogleAuth = GoogleAuth()
        self.google_auth.LocalWebserverAuth()

    def upload_file(
        self, filename: str, directory: Directory, temp_directory: str = "temp"
    ) -> dict:
        try:
            drive = GoogleDrive(self.google_auth)
            image = drive.CreateFile(
                {
                    "title": filename,
                    "parents": [
                        {"kind": "drive#fileLink", "id": directory_id[directory]}
                    ],
                }
            )
            image.SetContentFile(filename=os.path.join(temp_directory, filename))
            image.Upload()

            file_link = f"https://drive.google.com/file/d/{image['id']}/view"

            return {
                "status": "200 Success",
                "file_link": file_link,
                "file_id": image["id"],
            }
        except Exception as _ex:
            return {"status": "400 Error", "details": str(_ex)}

    def delete_file(self, filename: str, directory: Directory) -> dict:
        try:
            drive = GoogleDrive(self.google_auth)
            file_list = drive.ListFile(
                {"q": f"'{directory_id[directory]}' in parents and trashed=false"}
            ).GetList()

            for file in file_list:
                if file["title"] == filename:
                    file.Delete()
                    return {"status": "200 Success"}

            return {"status": "400 File not found"}

        except Exception as _ex:
            return {"status": "400 Error", "details": str(_ex)}

    def delete_file_by_id(self, file_id: str, directory: Directory) -> dict:
        try:
            drive = GoogleDrive(self.google_auth)
            file_list = drive.ListFile(
                {"q": f"'{directory_id[directory]}' in parents and trashed=false"}
            ).GetList()

            for file in file_list:
                if file["id"] == file_id:
                    file.Delete()
                    return {"status": "200 Success"}

            return {"status": "400 File not found"}

        except Exception as _ex:
            return {"status": "400 Error", "details": str(_ex)}
