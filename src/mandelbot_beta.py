"""
The Mandelbot+ is the intellectual property of Eliyahu Suskind and Pris Morales.

Mandelbot Beta is the machine learning half of the Mandelbot Plus.
"""
import time
import pandas as pd
import spotipy
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from IPython.core.display import clear_output
from spotipy import SpotifyClientCredentials, util
import config

REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'playlist-modify-public'
SCOPE_PLAYLIST = 'playlist-modify-public'
SCOPE_USER = 'user-library-modify'
SCOPE_PLAYING = 'user-read-currently-playing'

# Credentials to access the Spotify Music Data
manager = SpotifyClientCredentials(config.CLIENT_ID, config.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=manager)

# Credentials to access to the spotify user's playlist, favorite songs, etc.
token = util.prompt_for_user_token(
    config.USERNAME, SCOPE, config.CLIENT_ID, config.CLIENT_SECRET, REDIRECT_URI)
spt = spotipy.Spotify(auth=token)


def get_songs_features(ids): #pylint: disable=too-many-locals
    """
    Acquire the audio features of songs.

    Args:
        ids: A string representing the songs' ids.

    Returns:
        Each song track with its corresponding audio features.
    """

    meta = sp.track(ids)
    features = sp.audio_features(ids)

    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    ids = meta['id']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    valence = features[0]['valence']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    key = features[0]['key']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, ids, release_date, popularity, length,
             danceability, acousticness, energy, instrumentalness, liveness,
             valence, loudness, speechiness, tempo, key, time_signature]
    columns = ['name', 'album', 'artist', 'id', 'release_date', 'popularity',
               'length', 'danceability', 'acousticness', 'energy',
               'instrumentalness', 'liveness', 'valence', 'loudness',
               'speechiness', 'tempo', 'key', 'time_signature']
    return track, columns


def download_playlist(id_playlist, n_songs):
    """
    Acquire the audio features of songs in a given playlist with a limit of
    100 songs.

    Args:
        id_playlist: A string representing the playlist' id.
        n_songs: An integer representing the number of songs to download.

    Returns:
        Each song track with its corresponding audio features.
    """
    songs_id = []
    tracks = []

    for i in range(0, n_songs, 100):
        playlist = spt.playlist_tracks(id_playlist, limit=100, offset=i)

        for songs in playlist['items']:
            songs_id.append(songs['track']['id'])

    counter = 1
    for ids in songs_id:

        time.sleep(.6)
        track, columns = get_songs_features(ids)
        tracks.append(track)

        print(f"Song {counter} Added:")
        print(f"{track[0]} By {track[2]} from the album {track[1]}")
        clear_output(wait=True)
        counter += 1

    clear_output(wait=True)
    print("Music Downloaded!")

    return tracks, columns

tracks, columns = download_playlist(
    '1HiUueFJ4aOAnq9zdvjJCc', 100)

df1_mandelbot = pd.DataFrame(tracks, columns=columns)
df1_mandelbot.head()
df1_mandelbot.to_csv('data/df1_mandelbot.csv', index=False)

df1_mandelbot = pd.read_csv('data/df1_mandelbot.csv')
df_mandelbot = pd.concat([df1_mandelbot], 0)
df_mandelbot = df_mandelbot[['name', 'album', 'artist', 'id', 'release_date',
                             'popularity', 'danceability', 'energy', 'valence',
                             'loudness']]
col_features = df_mandelbot.columns[6:]
X = MinMaxScaler().fit_transform(df_mandelbot[col_features])
kmeans = KMeans(init="k-means++", n_clusters=2, random_state=15).fit(X)
df_mandelbot['kmeans'] = kmeans.labels_

# group the data frame by the k-means result labels
df_mandelbot.groupby(['kmeans']).mean()

# make the data clusters into new variables
cluster_0 = df_mandelbot[df_mandelbot['kmeans'] == 0]
cluster_1 = df_mandelbot[df_mandelbot['kmeans'] == 1]
cluster_0.to_csv("data/cluster0.csv", index=False)
cluster_1.to_csv("data/cluster1.csv", index=False)
df_mandelbot.to_csv("data/df_mandelbot.csv", index=False)

# Credentials to access the actual song played
token_actual = util.prompt_for_user_token(
    config.USERNAME, SCOPE_PLAYING, config.CLIENT_ID, config.CLIENT_SECRET, REDIRECT_URI)
sp_actual = spotipy.Spotify(auth=token_actual)

# Credentials to access the library music
token_user = util.prompt_for_user_token(
    config.USERNAME, SCOPE_USER, config.CLIENT_ID, config.CLIENT_SECRET, REDIRECT_URI)
sp_user = spotipy.Spotify(auth=token_user)

# Credentials to access the music from the playlists
token_playlist = util.prompt_for_user_token(
    config.USERNAME, SCOPE_PLAYLIST, config.CLIENT_ID, config.CLIENT_SECRET, REDIRECT_URI)
sp_playlist = spotipy.Spotify(auth=token_playlist)
cluster_0 = pd.read_csv("data/cluster0.csv")
cluster_1 = pd.read_csv("data/cluster1.csv")
ids_0 = cluster_0['id'].tolist()
ids_1 = cluster_1['id'].tolist()
energetic_mandelbot = sp_playlist.user_playlist_create(
    config.USERNAME, "The Energetic Mandelbot Blend")
calm_mandelbot = sp_playlist.user_playlist_create(
    config.USERNAME, "The Calm Mandelbot Blend")
sp_playlist.user_playlist_add_tracks(config.USERNAME, energetic_mandelbot, ids_0)
sp_playlist.user_playlist_add_tracks(config.USERNAME, calm_mandelbot, ids_1)
