# ☁️ GitHub Cloud Connector

A simple, high-performance REST API built with Python and FastAPI. This project is a cloud connector that securely authenticates a user with GitHub and fetches their repository data.

It was built to demonstrate:
- **External API Integration** (Fetching data from GitHub's REST API)
- **Secure Authentication** (Using GitHub's native OAuth 2.0 flow - Bonus Objective)
- **Clean Code Architecture** (Modular routing and service logic)

---

## 🚀 Features

* **OAuth 2.0 Authentication:** Secure login flow without hardcoding or storing any passwords.
* **Fetch Repositories:** Pulls a clean, formatted list of the authenticated user's public and private repositories.
* **Error Handling:** Gracefully handles invalid tokens or failed API requests.

---

## 🛠️ Setup Instructions

Follow these steps to run the project on your local machine.

### 1. Clone the repository
Open your terminal and run:
```bash
git clone [https://github.com/cuadarsh07/github-cloud-connector.git](https://github.com/cuadarsh07/github-cloud-connector.git)
cd github-cloud-connector

2. Set up a Virtual EnvironmentIt is best practice to run this in an isolated environment.For Windows:Bashpython -m venv venv
venv\Scripts\activate
For Mac/Linux:Bashpython3 -m venv venv
source venv/bin/activate
3. Install DependenciesInstall FastAPI, Uvicorn, and other required packages:Bashpip install -r requirements.txt
4. Configure Environment VariablesYou need to provide your own GitHub OAuth credentials to test the login.Go to your GitHub Settings -> Developer Settings -> OAuth Apps.Create a new app (set the Callback URL to http://localhost:8000/callback).In the root folder of this project, create a file named exactly .env.Add your credentials to the .env file like this:Code snippetGITHUB_CLIENT_ID=your_client_id_here
GITHUB_CLIENT_SECRET=your_client_secret_here
🏃‍♂️ How to Run the ProjectOnce your setup is complete and your .env file is ready, start the local server:Bashuvicorn main:app --reload
The server will start running at http://localhost:8000.📡 API EndpointsOnce the server is running, you can access the following endpoints:MethodEndpointDescriptionGET/Shows a welcome message and directs you to the login page.GET/loginRedirects you to GitHub's official authorization page.GET/callbackHandles the OAuth redirect and exchanges the code for a secure access token.GET/repos?token={your_token}Fetches and displays a list of your GitHub repositories using the provided token.
