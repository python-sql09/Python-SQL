# Exercise 4: Pop Music Evolution
import csv
from collections import defaultdict, Counter

def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def artists_in_multiple_decades(data):
    artist_decades = defaultdict(set)
    for row in data:
        artist = row['ARTIST']
        year = int(row['YEAR'])
        decade = (year // 10) * 10
        artist_decades[artist].add(decade)
    
    multi_decade_artists = {artist: decades for artist, decades in artist_decades.items() if len(decades) > 1}
    return multi_decade_artists

def artist_with_most_songs(data):
    artist_count = Counter(row['ARTIST'] for row in data)
    most_common_artist = artist_count.most_common(1)[0]
    return most_common_artist

def cluster_with_most_songs(data):
    cluster_count = Counter(row['Cluster ID'] for row in data)
    most_common_cluster = cluster_count.most_common(1)[0]
    return most_common_cluster

def genres_within_each_cluster(data):
    clusters = defaultdict(set)
    for row in data:
        cluster_id = row['Cluster ID']
        genre = row['Genre']
        clusters[cluster_id].add(genre)
    return clusters

def era_with_most_songs(data):
    era_count = Counter(((int(row['YEAR']) // 10) * 10) for row in data)
    most_common_era = era_count.most_common(1)[0]
    return most_common_era

def main():
    file_path = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/evolutionPopUSA_MainData.csv'
    data = read_csv(file_path)
    
    # Find artists that had songs on the Pop USA playlist in two different decades
    multi_decade_artists = artists_in_multiple_decades(data)
    print("Artists with songs in two different decades:")
    for artist, decades in multi_decade_artists.items():
        print(f"{artist}: {sorted(decades)}")
    
    # Identify the artist with the most songs on the Pop USA playlist
    artist_most_songs = artist_with_most_songs(data)
    print(f"\nArtist with the most songs: {artist_most_songs[0]} ({artist_most_songs[1]} songs)")

    # Identify the cluster with the most songs
    most_songs_cluster = cluster_with_most_songs(data)
    print(f"\nCluster with the most songs: Cluster {most_songs_cluster[0]} ({most_songs_cluster[1]} songs)")

    # Identify the genres within each cluster
    genres_by_cluster = genres_within_each_cluster(data)
    print("\nGenres within each cluster:")
    for cluster_id, genres in genres_by_cluster.items():
        print(f"Cluster {cluster_id}: {', '.join(genres)}")
    
    # Identify the era with the most songs
    most_songs_era = era_with_most_songs(data)
    print(f"\nEra with the most songs: {most_songs_era[0]}s ({most_songs_era[1]} songs)")

if __name__ == "__main__":
    main()