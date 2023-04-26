import threading
import time
import schedule
import pylast
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, render_template, jsonify

# Last.fm API credentials
API_KEY = 'YOUR API KEY'
API_SECRET = 'YOUR API SECRET'
SESSION_KEY = 'YOUR SESSION KEY'

# Set up the Last.fm API client
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, session_key=SESSION_KEY)

app = Flask(__name__)

# Global variable to store the most recently scrobbled track
last_scrobbled_track = None

# Global variable to store the Spinitron URL
spinitron_url = None

# Create an event object to control the scheduler thread
stop_event = threading.Event()

def run_scheduler():
    while not stop_event.is_set():
        schedule.run_pending()
        # Use a shorter sleep interval to allow for more responsive stopping
        stop_event.wait(timeout=1)

def scrobble_new_track():
    global last_scrobbled_track
    global spinitron_url

    message = "Checking for new track..."

    if not spinitron_url:
        return message

    # Fetch the HTML content of the Spinitron page
    response = requests.get(spinitron_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the specified line using the .spin-text class
    spin_text_element = soup.select_one('.spin-text')

    # Extract the track, artist, and album from the spin_text_element
    if spin_text_element:
        artist = spin_text_element.select_one('.artist').get_text(strip=True) if spin_text_element.select_one('.artist') else ''
        song = spin_text_element.select_one('.song').get_text(strip=True) if spin_text_element.select_one('.song') else ''
        release = spin_text_element.select_one('.release').get_text(strip=True) if spin_text_element.select_one('.release') else ''
        current_track = (song, artist, release)

        print("Current track:", current_track)  # Print the current track being processed

        # Check if the current track is different from the last scrobbled track
        if current_track != last_scrobbled_track:
            # Scrobble the track to Last.fm
            if current_track != last_scrobbled_track:
            # Scrobble the track to Last.fm
                if song and artist:
                    network.scrobble(artist=artist, title=song, album=release, timestamp=int(time.time()))
                    last_scrobbled_track = current_track
                    message = 'Scrobbled: ' + str(current_track)

    return message

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML page with the form

@app.route('/submit', methods=['POST'])
def submit():
    global spinitron_url
    spinitron_url = request.form['spinitron-url']  # Get the Spinitron URL from the form data
    
    # Perform an initial scrobble immediately after the URL is submitted
    scrobble_message = scrobble_new_track()

    return render_template('submit.html', message=scrobble_message)

@app.route('/latest_scrobble')
def latest_scrobble():
    global last_scrobbled_track
    if last_scrobbled_track:
        song, artist, release = last_scrobbled_track
        return jsonify({'song': song, 'artist': artist, 'release': release})
    return jsonify({'song': '', 'artist': '', 'release': ''})

if __name__ == '__main__':
    # Schedule the scrobble_new_track function to run every 2 minutes
    schedule.every(1).minutes.do(scrobble_new_track)

    # Start the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()

    try:
        # Start the Flask application
        app.run(debug=True, use_reloader=False)
    except KeyboardInterrupt:
        # Signal the scheduler thread to stop when the Flask application is terminated
        stop_event.set()
        scheduler_thread.join()


