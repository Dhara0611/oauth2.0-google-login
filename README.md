# oauth2.0-google-login
A simple Flask web application that demonstrates **Google OAuth 2.0 authentication** using `authlib`.  
After signing in with Google, the app fetches basic profile data along with **gender and birthday information** using the **Google People API** and stores it in the Flask session.


---

## 🚀 Features

- Google OAuth 2.0 login
- OpenID Connect (`openid`, `profile`, `email`)
- Fetches user data from Google People API
  - Gender
  - Birthday
- Session-based login/logout
- Flask + Authlib integration

---

## 🛠 Tech Stack

- Python
- Flask
- Authlib
- Google OAuth 2.0
- Google People API

---

## 📁 Project Structure

```text
.
├── server.py
├── templates/
│   └── home.html
└── README.md
```
---

## 🔐 Prerequisites

1. Python 3.8+
2. A Google Cloud project
3. OAuth 2.0 Client ID (Web Application)
4. Enabled **Google People API**

---

## 📦 Installation

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies like Flask, authlib 

----
## 🔑 OAuth configuration- 

1. Go to Google Cloud Console
2. Create OAuth 2.0 credentials (Web Application)
3. Add Authorized Redirect URI:
```bash
http://localhost:5005/signin-google
```
4. Enable People API
5. Add required scopes:
    - openid
    - profile
    - email

-----

## ▶️ Running the Application 

```bash
python server.py
```

The app will start running on  **http://localhost:5005**

## Application Flow 

1. User clicks Login with Google
2. Redirected to Google OAuth consent screen
3. Google redirects back with authorization code
4. App exchanges code for access token
5. App calls Google People API
6. User data stored in Flask session
7. User redirected to home page
8. Logout - clears the user session and redirects to the home page

## 🚪 Routes 

| Route            | Description                    |
| ---------------- | -------------------------------|
| `/`              | Home page                      |
| `/google-login`  | redirects to google login      |
| `/signin-google` | OAuth callback- token exchange |
| `/logout`        | Clears session and logs out    |


