

import joblib
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors


input = str(input())


def model(input):

    df = pd.read_csv(
        'https://github.com/trackteam-spotify/data-science/blob/master/data/final_scaled_dataset.csv'
        )

    cluster = ['popularity', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'tempo']

    distortion = list()
    for k in range(1, 31): #started with range [1, 51] and narrowed down to this range
        kmeans = KMeans(n_clusters = k)
        kmeans.fit(df.loc[:, cluster])
        distortion.append(kmeans.inertia_) # append distortion value to list

    knn = NearestNeighbors(n_neighbors=16)
    features = ['popularity', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'tempo']
    x = df[features].values

    knn.fit(x)

    song_pick = x[input]

    distance, neighbors = knn.kneighbors(np.array([song_pick]))

    song_list = []
    for item in neighbors[0][1:]: # this way excludes itself
        row = df.iloc[item]
        song_list.append((row.track_name, row.artist_name))

    names = ['song', 'artist']

    new_playlist = pd.DataFrame(song_list, columns=names)

    joblib.dump(knn, '../../AppData/Roaming/JetBrains/PyCharmCE2020.3/scratches/model.pkl')

    model = joblib.load('../../AppData/Roaming/JetBrains/PyCharmCE2020.3/scratches/model.pkl')

    model.kneighbors(x[int(input)].reshape(1,-1))[1][0][1:]

    return new_playlist


model(input)
