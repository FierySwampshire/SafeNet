from discord import SyncWebhook
from fastapi import FastAPI
import pylocate as pl

app = FastAPI()

def get_location(raw_dump):
    return pl.parse(raw_dump)


@app.post("/send")
def send_warning():
    address, crime_type = get_location()
    webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1015581794478870571/cyFCEqMxzcNAKQrX3sTB4AgMg2hRRfJmHjd8JwsfNnySNoSXaMURcqhecFXAklqZyQ5z")
    webhook.send(f"Warning: Crime Detected at {address}")