from fastapi import FastAPI
from utils.supabase_client import supabase

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Sceneset API is running"}

@app.get("/users")
def get_users():
    response = supabase.table("users").select("*").execute()
    return response.data
