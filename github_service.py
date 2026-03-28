import httpx
from fastapi import HTTPException

async def fetch_user_repos(access_token: str):
    # GitHub's official API endpoint for getting the authenticated user's repos
    url = "https://api.github.com/user/repos"
    
    # We pass the VIP token in the headers so GitHub knows it's you
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Securely call GitHub
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        
    # Proper error handling (another requirement for the assignment!)
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, 
            detail="Failed to fetch repositories from GitHub. Check your token."
        )
        
    return response.json()