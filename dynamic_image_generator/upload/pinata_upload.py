import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

JWT = os.getenv('PINATA')
src = "cer.png"



def pin_file_to_ipfs():
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    filename = f"cer.png"
    headers = {
        "Authorization": "Bearer " + JWT
    }
    metadata = {
        'name': 'name_certificate'
    }
    options = {
        'cidVersion': 0
    }
    with open(filename, 'rb') as f:
        multipart_data = MultipartEncoder(
            fields={
                'file': (filename, f),
                'pinataMetadata': (None, json.dumps(metadata), 'application/json'),
                'pinataOptions': (None, json.dumps(options), 'application/json')
            }
        )
        headers['Content-Type'] = multipart_data.content_type
        response = requests.post(url, data=multipart_data, headers=headers)
    if response.status_code == 200:
        print(f"Successfully uploaded name certificate.")
        return response.json()["IpfsHash"]
    else:
        print(f"Failed to upload name's certificate. Response: {response.text}")
        return None