import sys
from scripts.sql_db import *
import json
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import requests
from algorand_kits.create_account import create_account
from fastapi.middleware.cors import CORSMiddleware
from algorand_kits.asset_operations import create_asset, opt_in, transfer_asset
from scripts.utils import create_certificate, pin_file_to_ipfs

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/check")
def check():
    return "Your API is up!"


class receiver(BaseModel):
    address: str
    asset_id: str


class Table(BaseModel):
    db_name: str
    schema_name: str


class Data(BaseModel):

    trainee: str
    email: str
    asset: str
    status: str
    hashed:str
class Insert(BaseModel):

    db_name: str
    tb_data: Data
    table_name: str
    
class Update(BaseModel):

    asset: str
    status: str
    email: str
    hashed:str
class OptinUpdate(BaseModel):

    status: str
    remark: str
    asset: str

class CertificateData(BaseModel):
    full_name: str
    week: str

@app.get("/trainees")
def get_trainees():
    return fetch_trainees()

@app.get("/trainees_hash")
def get_trainees_hash():
    return fetch_trainees_hash()


@app.post("/create_certificate")
def create_certificate_api(data: CertificateData):
    try:
        ipfs_hash = create_certificate(data.full_name, data.week)
        return {"ipfs_hash": ipfs_hash}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/create_account")
def create_account_api():
    try:
        mnemonic = create_account()
        return {"mnemonic": mnemonic}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/mint")
def create_upload_file():

    # Set file path
    file_path = 'crt.jpg'

    # POST method
    headers = {'pinata_api_key': API_KEY, 'pinata_secret_api_key': API_SECRET}
    endpoint = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    if os.path.isfile(file_path):
        with open(file_path, 'rb') as filedata:
            response = requests.post(
                endpoint, headers=headers, files={'file': filedata})

    # Print result
    print(response.text)

    # Store hash
    hash = response.json()['IpfsHash']
    return hash
    # Now you can see your image on the IPFS : https://ipfs.stibits.com/<your_hash>


@app.post("/createDb")
def create_db(name: str):
    createDB(name)


@app.post("/createTable")
def create_table(table: Table):
    createTable(table.db_name, table.schema_name)


@app.post("/insert")
def insert(data: Insert):
    json_stream=(data.tb_data.json())
    insert_to_table(data.db_name, json_stream, data.table_name) 
    # return str(data.tb_data.json())
@app.post("/create_asset")
async def api_create_asset(m: str, receiver_pk: str, asset_name: str, ipfs: str):
    try:
        create_asset(m, receiver_pk, asset_name, ipfs)
        return {"message": "Asset created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/opt_in")
async def api_opt_in(trainee_m: str, asset_id: str):
    try:
        opt_in(trainee_m, asset_id)
        return {"message": "Opt-in operation successful"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/transfer_asset")
async def api_transfer_asset(sender_m: str, receiver_pk: str, asset_id: str):
    try:
        transfer_asset(sender_m, receiver_pk, asset_id)
        return {"message": "Asset transferred successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/update")
def update(data: Update):
    json_stream=(data.json())

    update_table("trainee", json_stream, "trainee")

@app.post("/optinUpdate")
def update(data: OptinUpdate):
    json_stream=(data.json())

    optin_update("trainee", json_stream, "trainee")

@app.get("/getall")
def get_all():
    return db_get_values()

@app.get("/getTrainee")
def get_trainee(asset):
    return db_get_values_by_asset(asset)

@app.get("/getCertificates")
def get_trainee(addr):
    return db_get_values_by_addr(addr)
