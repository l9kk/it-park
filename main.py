from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import ContactForm, ContactFormResponse
from db import contact_form_collection
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/feedback", response_model=ContactFormResponse)
async def submit_contact_form(form_data: ContactForm):
    try:
        form_dict = form_data.model_dump()
        form_dict["created_at"] = datetime.utcnow()

        result = contact_form_collection.insert_one(form_dict)

        return {
            "status": "success",
            "message": "Contact form submitted successfully",
            "form_id": str(result.inserted_id)
        }
    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail="An error occurred"
        )
