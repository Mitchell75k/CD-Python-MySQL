from flask import Flask # type: ignore
from flask import session # type: ignore #this is for sessions, we use this to encrypt our session, and its also necesarry for flash messages

app = Flask(__name__)
app.secret_key = "shhhhhh" #this is for sessions, we use this to encrypt our session