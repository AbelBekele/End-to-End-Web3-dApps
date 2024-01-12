import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

JWT = os.getenv('PINATA')
src = "with_texts.png"

def pin_file_to_ipfs():
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    filename = f"with_texts.png"
    headers = {
        "pinataMetadata": '{"name": "' + 'name' + '_certificate"}',
        "Authorization": "Bearer " + JWT
    }
    with open(filename, 'rb') as f:
        response = requests.post(url, files={"file": f}, headers=headers)
    if response.status_code == 200:
        print(f"Successfully uploaded name certificate.")
        return response.json()["IpfsHash"]
    else:
        print(f"Failed to upload name's certificate. Response: {response.text}")
        return None

pin_file_to_ipfs()

