# SpinLast

SpinLast is a Python script and web front end for scrobbling live radio station tracks from Spinitron to Last.fm. 

## Installation

Set up a directory structure on your local computer that looks like this:


    SpinLast/
    ├── SpinLast.py 
    └── static/
        ├── styles.css
    └── templates/
        ├── index.html
        └── submit.html
    

## Usage

From the command line, navigate to the SpinLast directory and start the app.
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
