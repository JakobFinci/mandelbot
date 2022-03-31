"""
The Mandelbot+ is the intellectual property of Eliyahu Suskind and Pris Morales.

Mandelbot Alpha is the data scraping and visualization half of the Mandelbot Plus.
"""
import sys
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
import config
# Import revelant libraries

all_track_data = []
track_danceability = []
track_energy = []
track_key = []
track_loudness = []
track_speechiness = []
track_acousticness = []
track_instrumentalness = []
track_liveness = []
track_valence = []
track_tempo = []
track_timesig = []
track_dur_min = []
all_track_titles = []
# Create revelant lists to hold data
client_credentials_manager = SpotifyClientCredentials(config.CLIENT_ID, config.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# Authenticate
results = sp.playlist_tracks("1HiUueFJ4aOAnq9zdvjJCc")
tracks = results['items']
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])
# Scrape entire playlist from Spotify
track_uris = [x["track"]["uri"] for x in tracks]
# Pull track URI data from database playlist
for string in track_uris:
    all_track_data.append(sp.audio_features(string[14:]))
# Aggregate all track data
for dictionary in all_track_data:
    track_danceability.append(dictionary[0]["danceability"])
    track_energy.append(dictionary[0]["energy"])
    track_key.append(dictionary[0]["key"])
    track_loudness.append(dictionary[0]["loudness"])
    track_speechiness.append(dictionary[0]["speechiness"])
    track_acousticness.append(dictionary[0]["acousticness"])
    track_instrumentalness.append(dictionary[0]["instrumentalness"])
    track_liveness.append(dictionary[0]["liveness"])
    track_valence.append(dictionary[0]["valence"])
    track_tempo.append(dictionary[0]["tempo"])
    track_timesig.append(dictionary[0]["time_signature"])
    track_dur_min.append(int(dictionary[0]["duration_ms"])/60000)
    # Divide by 60,000 to convert ms to min
for track in tracks:
    all_track_titles.append(track["track"]["name"])
    # Find categorical data on songs to aid in ease of data analysis
# Sort all data into lists for numpy
all_track_chars = []
# Create list for compiling
all_track_chars.append(all_track_titles)
all_track_chars.append(track_danceability)
all_track_chars.append(track_energy)
all_track_chars.append(track_key)
all_track_chars.append(track_loudness)
all_track_chars.append(track_speechiness)
all_track_chars.append(track_acousticness)
all_track_chars.append(track_instrumentalness)
all_track_chars.append(track_liveness)
all_track_chars.append(track_valence)
all_track_chars.append(track_tempo)
all_track_chars.append(track_timesig)
all_track_chars.append(track_dur_min)
# Compile all lists together for CSV conversion
df = pd.DataFrame(all_track_chars)
df.to_csv('all_track_chars.csv', index=False, header=False)

sys.path.append("..")
if os.path.exists("all_track_chars.csv"):
    os.remove("all_track_chars.csv")
sys.path.append("-")
# Fix for when Mandelbot Alpha erroneously writes CSV files
# outside of src when run in Jupyter

##########################################################
# A collection of functions for track data visualization #
##########################################################

border_ys = []
border_xs = []
CURR_X = -10
for _ in range(0, 44):
    border_ys.append(-14)
    border_xs.append(CURR_X)
    CURR_X += 5
# Create lists for border line in loudness scatterplot

def create_louds():
    """
    Create a loudness scatterplot

    Returns:
        A relevant matplotlib graph
    """
    plt.plot(track_loudness, "ro", border_xs, border_ys, 'r--')
    plt.text(150 ,-27, "Point = nᵗʰ song")
    plt.title("Song Loudness")
    plt.xlabel("Song Index")
    plt.ylabel("Loudness")
    return plt.show()


def create_svi():
    """
    Create a speechiness vs instrumentalness scatterplot

    Returns:
        A relevant matplotlib graph
    """
    plt.plot(track_speechiness, track_instrumentalness, "ro")
    plt.text(0.3, 0.2, "Point = nᵗʰ song")
    plt.title("Speechiness vs Instrumentalness")
    plt.ylabel("Instrumentalness")
    plt.xlabel("Speechiness")
    return plt.show()


def create_contextg():
    """
    Create a scatterplot comparing the two contextual song
    measurements: liveness and acousticness

    Returns:
        A relevant matplotlib graph
    """
    plt.plot(track_liveness, track_acousticness, "ro")
    plt.text(0.6, 0.7, "Point = nᵗʰ song")
    plt.title("Liveness vs Acousticness")
    plt.ylabel("Acousticness")
    plt.xlabel("Liveness")
    return plt.show()


def create_tve():
    """
    Create a tempo vs energy scatterplot

    Returns:
        A relevant matplotlib graph
    """
    plt.plot(track_tempo, track_energy, "ro")
    plt.text(160, 0.1, "Point = nᵗʰ song")
    plt.title("Tempo vs Energy")
    plt.ylabel("Energy")
    plt.xlabel("Tempo")
    return plt.show()


def create_vvd():
    """
    Create a valence vs danceability scatterplot

    Returns:
        A relevant matplotlib graph
    """
    plt.plot(track_valence, track_danceability, "ro")
    plt.text(0.7, 0.1, "Point = nᵗʰ song")
    plt.title("Valence vs Danceability")
    plt.ylabel("Danceability")
    plt.xlabel("Valence")
    return plt.show()


def create_keyh():
    """
    Create a histogram displaying all the keys of the mandelbrot
    tracks

    Returns:
        A relevant matplotlib graph
    """
    plt.hist(track_key, 12, density=1, facecolor='g')
    plt.title("Histogram of Key")
    plt.ylabel("Probability")
    plt.xlabel("Key")
    plt.grid(True)
    return plt.show()


def create_timeh():
    """
    Create a histogram displaying all the song durations in minutes
    of the mandelbrot tracks

    Returns:
        A relevant matplotlib graph
    """
    plt.hist(track_dur_min, 50, density=1, facecolor='g')
    plt.title("Histogram of Song Duration in Minutes")
    plt.ylabel("Probability")
    plt.xlabel("Song Duration (min)")
    plt.grid(True)
    return plt.show()


def create_timesigh():
    """
    Create a histogram displaying all the song time signatures
    of the mandelbrot tracks

    Returns:
        A relevant matplotlib graph
    """
    plt.hist(track_timesig, 10, density=1, facecolor='g')
    plt.title("Histogram of Time Signatures")
    plt.ylabel("Probability")
    plt.xlabel("Time Signature")
    plt.grid(True)
    return plt.show()


def create_all_graphs():
    """
    Creates all relevant graphs

    Returns:
        All relevant matplotlib graphs
    """
    return create_svi(), create_louds(), create_contextg(), create_tve(),\
        create_vvd(), create_keyh(), create_timeh(), create_timesigh()
