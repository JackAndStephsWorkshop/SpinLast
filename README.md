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

From the command line, navigate to the SpinLast directory and run getSessionKey.py to get your permanent Last.fm Session Key.
```bash
python3 SpinLast.py
```
Edit the SpinLast.py file to include your API Key, Shared Secret, and Session Key.

From the command line, navigate to the SpinLast directory and run the SpinLast.py application.
```bash
python3 SpinLast.py
```
Visit the self-hosted website at http://localhost:5000/ and submit any Spinatron URL to start scrobbling automatically. 

The application will continue running and display the most recently scrobbled track as the Spinitron playlist plays in real time. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
