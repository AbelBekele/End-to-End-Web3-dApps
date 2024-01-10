from dotenv import load_dotenv
from openai import OpenAI
import os 
from pathlib import Path
import json
import requests
from PIL import Image
from io import BytesIO
import uuid

DATA_DIR = Path.cwd() / "responses"

DATA_DIR.mkdir(exist_ok=True)

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt="I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS, White background Design a minimalist, futuristic certificate with a red theme. The certificate should be straight-facing, occupy the full screen, and have extremely minimal details. The design may feature subtle, elegant patterns around the edges, but the center and 95% of the certificate should be pure white. No other elements should be present. Make the most of it white. Make the center blank!"

response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

# Get the image from the URL
response = requests.get(image_url)

# Open the image
img = Image.open(BytesIO(response.content))

# Generate a unique identifier
unique_id = uuid.uuid4()

# Save the image to a PNG file with a unique name
img.save(DATA_DIR / f"certificate_{unique_id}.png")