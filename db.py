from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION")

client = MongoClient(MONGODB_CONNECTION_STRING)

db = client.contact_form_db

contact_form_collection = db.contact_forms