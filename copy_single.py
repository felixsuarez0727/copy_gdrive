from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os
import threading

def upload_files_to_drive(directory_path, folder_id):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # Crea una autenticación local del servidor web

    drive = GoogleDrive(gauth)

    file_path = os.path.join(directory_path, "file_name.txt")
    if os.path.exists(file_path):
        gfile = drive.CreateFile({"title": os.path.basename(file_path), "parents": [{"id": folder_id}]})
        gfile.SetContentFile(file_path)
        print("Upload running!")
        gfile.Upload()
    else:
        print("El archivo no se encuentra en el directorio especificado.")

upload_files_to_drive('/mnt/home/users/oncoh_011_ibima/dtello/data/raw_data/204SC23084418_LP2/204SC23084418-Z01-F010_trimmed', '1gxGrp_24wfklhkDyr1NK2M8EqgcY7uIx')
