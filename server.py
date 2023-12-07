import socket
import hashlib
import os
import shutil
from lorem import text

def generate_fixed_size_file(file_path, size_kb):
    # Generate a fixed-length string to ensure the exact file size
    fixed_text = ""
    while len(fixed_text.encode('utf-8')) < size_kb * 1024:
        fixed_text += text()

    # Trim the text to exactly match the required size
    fixed_text = fixed_text[:size_kb * 1024]

    with open(file_path, 'wb') as file:
        file.write(fixed_text.encode('utf-8'))

def calculate_checksum(file_path):
    sha256 = hashlib.sha256()
    md5 = hashlib.md5()

    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            sha256.update(chunk)
            md5.update(chunk)

    return sha256.hexdigest(), md5.hexdigest()

def main():
    host = '127.0.0.1'
    port = 12345

    file_name = 'random_text_file.txt'  # File name without directory
    file_size_kb = 1  # Fixed file size in KB

    # Use an absolute path within the container for the file
    container_file_path = '/serverdata/' + file_name

    sha256_checksum, md5_checksum = "", ""

    generate_fixed_size_file(container_file_path, file_size_kb)
    sha256_checksum, md5_checksum = calculate_checksum(container_file_path)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Server listening on {host}:{port}")
        print(f"File name: {file_name}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")

            with open(container_file_path, 'rb') as file:
                file_data = file.read()

            # Send checksums and file content to the client
            file_info = f"{sha256_checksum}\n{md5_checksum}\n".encode() + file_data
            conn.sendall(file_info)

    print("File and server script completed.")

if __name__ == "__main__":
    main()
