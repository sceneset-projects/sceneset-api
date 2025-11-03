from fastapi import FastAPI
from utils.supabase_client import supabase

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Sceneset API is running"}

@app.get("/users")
def get_users():
    try:
        response = supabase.table("users").select("*").execute()
        return response.data
    except Exception as e:
        print("🔥 Supabase error:", e)
        return {"error": str(e)}
