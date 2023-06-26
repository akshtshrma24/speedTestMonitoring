import time
from ftplib import FTP
from http.server import HTTPServer, BaseHTTPRequestHandler

import requests


# Define a global counter variable
def upload_speed() -> float:
    print("TESTING UPLOAD", flush=True)
    server = "ftp.dlptest.com"
    username = "dlpuser"
    password = "rNrKYTX9g7z3RgJRmxWuGHbeu"
    local_file_path = "./10mb.txt"  
    remote_file_name = "10mb.txt"  
    try:
        ftp = FTP(server, username, password, timeout=30)

        start = time.time()
        with open(local_file_path, "rb") as file:
            ftp.storbinary(f"STOR {remote_file_name}", file)
        ftp.quit()
        return (time.time() - start) / 10 
    except: 
        return -1

def download_speed() -> float:
    print("TESTING DOWNLOAD", flush=True)
    try:
        url = "https://dlptest.com/10-MB-Test.docx"
        headers = {
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'Referer': 'https://dlptest.com/',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"macOS"',
        }
        start_time = time.time()
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            return (time.time() - start_time) / 10 
    except:
        return -1
    return -1

def is_up() -> float:
    print("TESTING IS UP", flush=True)
    try:
        url = "https://google.com"
        response = requests.get(url)
        if(response.status_code == 200): return 1
    except:
        return 0
    return 0


# Custom request handler that serves metrics
class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Prepare the metrics response
        if self.path == "/metrics":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            # Format the metrics response
            metrics_response = f"upload_speed {upload_speed()}\n"
            metrics_response += f"download_speed {download_speed()}\n"
            metrics_response += f"is_up {is_up()}\n"
            self.wfile.write(metrics_response.encode())

# Define the server address and port
server_address = ("", 8000)

# Create the HTTP server with the custom request handler
httpd = HTTPServer(server_address, MetricsHandler)

# Start the server
print("Server started on port 8000...")
httpd.serve_forever()
