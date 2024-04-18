# Google Drive File Upload Script (copy_single.py)

This Python script is designed to upload files to Google Drive using the Google Drive API. It is especially useful for automating the uploading of files from a local location to a specific folder in Google Drive.

## Prerequisites

1. **PyDrive2**: This script utilizes the PyDrive2 library to interact with the Google Drive API. Make sure you have PyDrive2 installed in your Python environment. You can install it using `pip install PyDrive2`.

2. **Google API Credentials**: To use the Google Drive API, you need to create Google API credentials and enable access to the Google Drive API in your Google Cloud Platform account. Follow the instructions in the official Google documentation to obtain the necessary credentials.

## Usage

1. **Configure File Path to Copy**: Before running the script, ensure you have the local file path that you want to copy to Google Drive.

2. **Configure Destination Folder**: Before running the script, ensure you have the ID of the Google Drive folder you want to upload the files to. This ID can be found in the URL of the Google Drive folder.

3. **Running the Script**: Once you have configured the destination folder ID, you can execute the script by providing the path to the local directory containing the files you want to upload and the ID of the destination folder in Google Drive.

```
python copy_single.py
```

4. **Authentication**: The script will initiate a local web server to authenticate your Google account. Follow the instructions in the console to complete the authentication process.

5. **Uploading Files**: Once authenticated, the script will look for the file that you defined in the script. If it finds the file, it will upload it to the destination folder in Google Drive.

## Additional Notes

- Ensure that the file you want to upload exists in the specified directory and has the correct name.
- If the file is not found in the specified directory, the script will display a warning message.

---


---

# Google Drive MD5 Checksum Verification Script (md5_check_colab.ipynb)

This Python script verifies MD5 checksums of files stored in a Google Drive folder. It reads a file named `md5sums.txt`, which contains MD5 checksums along with filenames, calculates the MD5 checksum of each file in the specified folder, and compares it with the original checksums.

## Prerequisites

1. **Google Colab**: This script is designed to run in Google Colab environment, as it utilizes the `google.colab` library for mounting Google Drive. Make sure you have access to Google Colab and a Google account.

2. **MD5 File Format**: The script is intended to work on an MD5.txt file that has the following format:

```
48be2f320d90ed  X204SC23084418-Z01-F010_01.tar
532f86e3r8db61  X204SC23084418-Z01-F010_02.tar
199e5fd2bb4668  X204SC23084418-Z01-F010_03.tar
```

## Usage

1. **Mount Google Drive**: Before running the script, you need to mount your Google Drive by executing the following code snippet in a Google Colab notebook:

```python
from google.colab import drive
drive.mount('/content/drive')
```

2. **Specify Folder Path**: Set the `folder_path` variable to the path of the Google Drive folder containing the files and the `md5sums` file.

3. **Specify MD5 File Name**: Set the `MD5 filename` variable to the filename of your `md5sums` file.

4. **Run the Script**: Execute the script in a Google Colab notebook.

## File Structure

Ensure that your Google Drive folder has the following structure:

```
- Your_Google_Drive_Folder/
  - md5sums.txt
  - File1
  - File2
  - ...
```

## Notes

- The script reads MD5 checksums and filenames from `md5sums.txt`, calculates MD5 checksums of files in the specified folder, and compares them.
- If a checksum doesn't match, it will display a warning message indicating a mismatch.