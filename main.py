import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import httpx
from dotenv import load_dotenv
from github_service import fetch_user_repos

# Load secrets from your .env file securely
load_dotenv()

CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

app = FastAPI(title="GitHub Cloud Connector")

@app.get("/")
def home():
    return {"message": "Welcome to the GitHub Connector! Go to http://localhost:8000/login to authenticate."}

@app.get("/login")
def login_to_github():
    # Step 1: Redirect the user to GitHub's login page
    # We request 'repo' scope so we can read repositories later
    github_auth_url = f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&scope=repo"
    return RedirectResponse(github_auth_url)

@app.get("/callback")
async def github_callback(code: str):
    # Step 2: GitHub sends the user back here with a temporary 'code'
    # Step 3: We exchange this 'code' for an 'access_token'
    token_url = "https://github.com/login/oauth/access_token"
    headers = {"Accept": "application/json"}
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code
    }
    
    # Make a secure, asynchronous POST request to GitHub
    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, json=payload, headers=headers)
        
    data = response.json()
    
    # Error handling just in case something went wrong
    if "access_token" not in data:
        raise HTTPException(status_code=400, detail=f"Failed to authenticate: {data}")
        
    access_token = data["access_token"]
    
    # Boom! We have the token. For testing, we will just display it.
    # (Later, we will use this token to fetch your repos!)
    return {
        "message": "Authentication Successful! Bonus point achieved.", 
        "access_token": access_token
    }

@app.get("/repos")
async def get_my_repos(token: str):
    # Call our modular service function
    raw_repos = await fetch_user_repos(token)
    
    # GitHub returns a MASSIVE amount of data. Let's filter it to look clean and professional.
    clean_repos = [
        {
            "name": repo["name"], 
            "url": repo["html_url"], 
            "private": repo["private"]
        } 
        for repo in raw_repos
    ]
    
    return {
        "total_repos": len(clean_repos), 
        "repositories": clean_repos
    }