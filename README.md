# SpinLast

SpinLast is a Python script and web front end for scrobbling live radio station tracks from Spinitron to Last.fm. 

## Installation

Set up a directory structure on your local computer that looks like this:


    SpinLast/
    ├── getSessionKey.py
    ├── SpinLast.py 
    └── static/
        ├── styles.css
    └── templates/
        ├── index.html
        └── submit.html
    

## Usage

First, sign up for a Last.fm API account here, and record your Last.fm API Key and Shared Secret somewhere safe: https://www.last.fm/api/account/create 

Edit the getSessionKey.py file to include your API Key and Shared Secret.
```python3
# Script vars
CONNECT = True
API_KEY = "YOUR_API_KEY"
API_SEC = "YOUR_API_SECRET"
UPDATE = False
STOP = False
ASKMOC = False
DEBUG = False
```
From the command line, navigate to the SpinLast directory and run getSessionKey.py and follow it's instructions to get your permanent Last.fm Session Key.
```bash
python3 getSessionKey.py
```
Edit the SpinLast.py file to include your API Key, Shared Secret, and Session Key.
```python3
# Last.fm API credentials
API_KEY = 'REPLACE WITH YOUR KEY'
API_SECRET = 'REPLACE WITH YOUR SECRET'
SESSION_KEY = 'REPLACE WITH YOUR SESSION KEY'
```

From the command line, navigate to the SpinLast directory and run the SpinLast.py application.
```bash
python3 SpinLast.py
```
Visit the self-hosted website at http://localhost:5000/ and submit any Spinatron URL (like https://spinitron.com/KXLU/) to start scrobbling automatically. 

The application will continue running and the webpage will display the most recently scrobbled track as the Spinitron playlist plays in real time. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
