# FTPCombo - XML Credentials Extractor

This Python script extracts and decodes credentials from XML files. It is designed to search through a specified folder, process XML files to find encoded credentials, decode them, and save them to an output file.

## Features

- Recursively searches for XML files in a specified folder.
- Extracts host, port, user, and password information from XML files.
- Decodes base64 encoded passwords.
- Saves the extracted credentials to an output file, ensuring no duplicates.
- Automatically handles naming conflicts for the output file.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ftpcombo.git
    cd ftpcombo
    ```

2. Create a virtual environment and activate it (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```bash
    python extract_credentials.py
    ```

2. Follow the prompt to enter the folder path where XML files are located.

3. The script will process the XML files and save the extracted credentials to an output file in the user's home directory (e.g., `~/ftp.txt`). If the file already exists, a new file with an incremented suffix will be created (e.g., `~/ftp1.txt`, `~/ftp2.txt`, etc.).

### Example

```bash
Enter the folder path to search for XML files: /path/to/xml/files
Using output file: /home/user/ftp.txt
Found 3 XML files.
Processing /path/to/xml/files/server1.xml...
Extracted and saved credentials from /path/to/xml/files/server1.xml.
Processing /path/to/xml/files/server2.xml...
Extracted and saved credentials from /path/to/xml/files/server2.xml.
Processing /path/to/xml/files/server3.xml...
Extracted and saved credentials from /path/to/xml/files/server3.xml.
Credentials extraction completed.
