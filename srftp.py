import os
import xml.etree.ElementTree as ET
import base64

def decode_base64(encoded_str):
    return base64.b64decode(encoded_str).decode('utf-8')

def extract_credentials_from_xml(file_path):
    credentials = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for server in root.findall('.//Server'):
            host = server.find('Host').text.strip() if server.find('Host') is not None else ''
            port = server.find('Port').text.strip() if server.find('Port') is not None else ''
            user = server.find('User').text.strip() if server.find('User') is not None else ''
            encoded_pass = server.find('Pass').text.strip() if server.find('Pass') is not None else ''
            password = decode_base64(encoded_pass) if encoded_pass else ''
            if host and port and user and password:
                credentials.append((host, port, user, password))
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
    return credentials

def save_credentials_to_file(credentials, output_file):
    with open(output_file, 'a', encoding='utf-8') as f:
        for cred in credentials:
            f.write(f"Server: {cred[0]}:{cred[1]}\n")
            f.write(f"Username: {cred[2]}\n")
            f.write(f"Password: {cred[3]}\n")
            f.write("=" * 15 + "\n")
    print(f"Credentials saved to {output_file}")

def find_xml_files(folder_path):
    xml_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.xml'):
                xml_files.append(os.path.join(root, file))
    return xml_files

def process_xml_files(folder_path, output_file):
    xml_files = find_xml_files(folder_path)
    print(f"Found {len(xml_files)} XML files.")
    processed_credentials = set()
    for xml_file in xml_files:
        print(f"Processing {xml_file}...")
        credentials = extract_credentials_from_xml(xml_file)
        unique_credentials = [cred for cred in credentials if cred not in processed_credentials]
        save_credentials_to_file(unique_credentials, output_file)
        processed_credentials.update(unique_credentials)
        print(f"Extracted and saved credentials from {xml_file}.")

def get_next_output_file(output_file):
    base_name, ext = os.path.splitext(output_file)
    counter = 1
    while os.path.exists(f"{base_name}{counter}{ext}"):
        counter += 1
    return f"{base_name}{counter}{ext}"

if __name__ == "__main__":
    folder_path = input("Enter the folder path to search for XML files: ")
    output_file = os.path.expanduser("~/ftp.txt")
    
    if os.path.exists(output_file):
        output_file = get_next_output_file(output_file)
    
    print(f"Using output file: {output_file}")
    
    process_xml_files(folder_path, output_file)
    print("Credentials extraction completed.")
