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

response = client.images.edit(
  model="dall-e-2",
  image=open("original.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS, White background Design a minimalist, futuristic certificate with a red theme. Just patterns nothing else. Make it modern don't add anyother thing",
  n=1,
  size="1024x1024"
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