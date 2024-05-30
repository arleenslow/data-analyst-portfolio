import pandas as pd

# Load the datasets
user_data_path = 'My Streaming Activity.csv'
scrobble_features_path = 'Scrobble_Features.csv'

# Reading the CSV files into DataFrames
user_data = pd.read_csv(user_data_path)
scrobble_features = pd.read_csv(scrobble_features_path)

# Transforming the user data to get the number of users per genre
user_data['genre'] = user_data['Album']  # Assuming 'Album' can be used as a proxy for genre
genre_user_counts = user_data['genre'].value_counts().reset_index()
genre_user_counts.columns = ['genre', 'num_users']
genre_user_counts = genre_user_counts.sort_values(by='num_users', ascending=False)

print("Top genres by number of users:")
print(genre_user_counts.head())

# Identifying popular tracks from the Scrobble_Features dataset
popular_tracks = scrobble_features[['spotify_track_id', 'Song', 'Performer', 'spotify_track_popularity']]
popular_tracks = popular_tracks.sort_values(by='spotify_track_popularity', ascending=False).head(10)

print("Top 10 popular tracks:")
print(popular_tracks)

# Analyzing listening habits by device and hour (example with simulated 'device' column)
user_data['listening_time'] = pd.to_datetime(user_data['TimeStamp_UTC'])
user_data['hour'] = user_data['listening_time'].dt.hour
user_data['device'] = 'mobile'  # This should be replaced by actual device data

listening_habits = user_data.groupby(['device', 'hour']).size().reset_index(name='num_listens')
listening_habits = listening_habits.sort_values(by=['device', 'hour'])

print("Listening habits by device and hour:")
print(listening_habits)

# Calculating average energy and number of listens from Scrobble_Features dataset
avg_features = scrobble_features[['energy', 'spotify_track_popularity']].mean().reset_index()
avg_features.columns = ['feature', 'average_value']

print("Average energy and number of listens:")
print(avg_features)
