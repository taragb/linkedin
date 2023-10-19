# main.py
import pdb
from fastapi import FastAPI
from models.base import Base, engine, SessionLocal
from models.user import User
from models.linkedin_contact import LinkedInContact


import os
print("TEST TEST TEST TEST TEST")
print(os.listdir("/Users/tarabalakrishnan/ProgrammingWork/linkedin/backend/models"))


def init_db():
    Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    init_db()
    # ... other startup code


@app.get("/")
async def read_root():
    return {"Hello": "World"}
