import pyrebase

config = {
    "apiKey":        "YOUR_API_KEY",
    "authDomain":    "YOUR_PROJECT_ID.firebaseapp.com",
    "databaseURL":   "https://YOUR_DATABASE_NAME.firebaseio.com",
    "storageBucket": "YOUR_PROJECT_ID.appspot.com",
}
firebase = pyrebase.initialize_app(config)
auth     = firebase.auth()
database = firebase.database()
