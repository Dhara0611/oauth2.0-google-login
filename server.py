from flask import Flask , url_for, session, redirect, render_template
from authlib.integrations.flask_client import OAuth
import json
import requests

app = Flask(__name__)

appConf = {
    "OAUTH_CLIENT_ID":"1078512040778-3ojru83rt56eulc5uqt8dt64rjrrls35.apps.googleusercontent.com",
    "OAUTH2_CLIENT_SECRET" :"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",
    "OAUTH2_META_URL": "https://accounts.google.com/.well-known/openid-configuration",
    #FLASK SECRET IS USED FOR ENCRYPTING AND THIS SHOULD BE SECRET AT THE SERVER 
    "FLASK_SECRET":"68519ebc-8714-4de6-9e5a-6b699f3282b8",
    "FLASK_PORT":5005
}

app.secret_key = appConf.get("FLASK_SECRET")

#creating OAuth client 
#It attaches OAuth capability to your Flask app and creates a manager object that can hold one or more OAuth clients.
oauth = OAuth(app)

#used https://developers.google.com/identity/protocols/oauth2/scopes to get scopes
#web app client that follows aouth 2.0 
#The OAuth provider is fixed when you call oauth.register() — routes only trigger it.
oauth.register("myApp",
               client_id=appConf.get("OAUTH_CLIENT_ID"),
               client_secret=appConf.get("OAUTH2_CLIENT_SECRET"),
               server_metadata_url=appConf.get("OAUTH2_META_URL"),
               client_kwargs={
                   "scope": "openid profile email https://www.googleapis.com/auth/user.birthday.read https://www.googleapis.com/auth/user.gender.read",
                   "prompt":"login"  #new
               }
               )


@app.route("/")
def home():
    return render_template("home.html", session=session.get("user"),
                           pretty = json.dumps(session.get("user"), indent = 4))


@app.route("/google-login")
def googlelogin():
    session.pop("user", None)   #new
    return oauth.myApp.authorize_redirect(redirect_uri=url_for("googleCallback", _external=True))

@app.route("/signin-google")
def googleCallback():
    # fetch access token and id token using authorization code
    # google people API - https://developers.google.com/people/api/rest/v1/people/get
    # Google OAuth 2.0 playground - https://developers.google.com/oauthplayground
    token = oauth.myApp.authorize_access_token()

    # fetch user data with access token
    personDataUrl = "https://people.googleapis.com/v1/people/me?personFields=genders,birthdays" 
    personData = requests.get(personDataUrl, headers={
        "Authorization": f"Bearer {token['access_token']}"
    }).json()
    token["personData"] = personData

    # set complete user information in the session
    session["user"] = token

    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=appConf.get("FLASK_PORT"), debug=True)




