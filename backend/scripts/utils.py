import cv2
import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

JWT = os.getenv('PINATA')

def create_certificate(full_name, week):
    # Get current date and format it
    date = datetime.now().strftime('%d/%m/%Y')

    certificate_background = cv2.imread("scripts/with_texts_2.png")

    cv2.putText(
        certificate_background,
        full_name,
        (150, 402),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (0, 0, 255),
        2,
    )

    cv2.putText(
        certificate_background,
        week,
        (145, 473),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (10, 10, 10),
        2,
    )

    cv2.putText(
        certificate_background,
        date,
        (280 , 748),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 0),
        2,
    )

    os.makedirs('generated', exist_ok=True)
    date = date.replace('/', '_')
    filename = f"generated/{full_name}_{week}_certificate.png"
    cv2.imwrite(filename, certificate_background)
    
    # Call pin_file_to_ipfs with the filename
    ipfs_hash = pin_file_to_ipfs(filename)

    return ipfs_hash  # return the IPFS hash

def pin_file_to_ipfs(filename):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {
        "Authorization": "Bearer " + JWT
    }
    metadata = {
        'name': 'name_certificate'
    }
    options = {
        'cidVersion': 0
    }
    upload_filename = os.path.basename(filename)
    with open(filename, 'rb') as f:
        multipart_data = MultipartEncoder(
            fields={
                'file': (upload_filename, f),
                'pinataMetadata': (None, json.dumps(metadata), 'application/json'),
                'pinataOptions': (None, json.dumps(options), 'application/json')
            }
        )
        headers['Content-Type'] = multipart_data.content_type
        response = requests.post(url, data=multipart_data, headers=headers)
    if response.status_code == 200:
        print(f"Successfully uploaded {upload_filename} certificate.")
        return response.json()["IpfsHash"]
    else:
        print(f"Failed to upload {upload_filename}'s certificate. Response: {response.text}")
        return None