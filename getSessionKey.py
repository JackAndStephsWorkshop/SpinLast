import hashlib
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# Defaults
NAME_SCRIPT = "Last.fm Session Key Generator"
VERSION = "0.1"
AUTHOR = "Mx. Jack Nelson"

SCHEMA = "https"
AUTH_URL = "www.last.fm/api/auth"
API_URL = "ws.audioscrobbler.com/2.0/"
HOST = "post.audioscrobbler.com"
SIG_URL = "DONT USE THIS VARIABLE"

KEYTYPE = "desktop"
CONF = "~/.config/moc-scrobbler/moc-scrobbler.conf"

# Script vars
CONNECT = True
API_KEY = "YOUR_API_KEY"
API_SEC = "YOUR_API_SECRET"
UPDATE = False
STOP = False
ASKMOC = False
DEBUG = False

# Working config stuff
if CONNECT:
    # Configure mode

    # First: Get signature.

    # Second sign request

    # Generate API_TK_SIG
    API_TK_SIG = hashlib.md5(f"api_key{API_KEY}methodauth.getToken{API_SEC}".encode('utf-8')).hexdigest()

    # Third: Authorize to build token with auth.getToken
    response = requests.get(f"{SCHEMA}://{API_URL}?method=auth.getToken&api_key={API_KEY}&api_sig={API_TK_SIG}")
    TOKEN_XML = response.text

    # Parse XML response
    root = ET.fromstring(TOKEN_XML)
    STAT = root.get('status')

    if STAT == 'ok':
        TOKEN = root.find('token').text
    else:
        if STAT == 'failed':
            print("Error. Worse, programmer is too lazy to know what kind of error")
        else:
            print("Error: Unknown.")
        print("Aborting.")
        print("Look for an error here:")
        print(TOKEN_XML)
        exit(1)

    URL = f"{SCHEMA}://{AUTH_URL}?api_key={API_KEY}&token={TOKEN}"
    input(f"Please access the URL {URL} and grant Last.fm Session Key Generator access to your profile so posting can begin.\n"
          "When you have authorized the application press any key to continue...")

    # Get a permanent session token next

    # Generate API_SES_SIG
    SIGNME = f"api_key{API_KEY}methodauth.getSessiontoken{TOKEN}{API_SEC}"
    API_SES_SIG = hashlib.md5(SIGNME.encode('utf-8')).hexdigest()

    # Submitting the URL
    url = f"{SCHEMA}://{API_URL}?method=auth.getSession&api_key={API_KEY}&token={TOKEN}&api_sig={API_SES_SIG}"
    response = requests.get(url)
    SESSION_XML = response.text

    # Parse XML response
    root = ET.fromstring(SESSION_XML)
    STAT = root.get('status')
    if STAT == 'ok':
        SESSION_KEY = root.find('session/key').text
    else:
        print("Error:")
        print(SESSION_XML)
        print("Aborting.")
        exit(1)

    print(SESSION_KEY)

# New stuff
print('Config done.')
print("Click to Rick")

artist = "Rick Astley"
track = "Never Gonna Give You Up"
TS = int(datetime.now().timestamp())

TOSIGN = f"api_key{API_KEY}artist{artist}methodtrack.scrobblesk{SESSION_KEY}timestamp{TS}track{track}{API_SEC}"
API_SIG = hashlib.md5(TOSIGN.encode('utf-8')).hexdigest()

data = {
    "api_key": API_KEY,
    "api_sig": API_SIG,
    "artist": artist,
    "method": "track.scrobble",
    "sk": SESSION_KEY,
    "timestamp": TS,
    "track": track
}

response = requests.post(f"{SCHEMA}://{API_URL}/", data=data)
RESPONSE_XML = response.text
print(RESPONSE_XML)
