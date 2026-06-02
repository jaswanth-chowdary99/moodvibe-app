"""
Seed MongoDB with curated mood-based recommendations — organized by language
Each mood: music/movies/anime with Telugu, Hindi, English, Tamil, Korean, Japanese picks
"""

import os
import urllib.parse
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

client = MongoClient(os.environ.get('MONGO_URI'))
db = client.get_default_database()
col = db['recommendations']


def mkurl(platform, title, artist=None):
    q = urllib.parse.quote(f'{title} {artist}' if artist else title)
    urls = {
        'Spotify': f'https://open.spotify.com/search/{q}',
        'Apple Music': f'https://music.apple.com/us/search?term={q}',
        'JioSaavn': f'https://www.jiosaavn.com/search/{q}',
        'Netflix': f'https://www.netflix.com/search/{q}',
        'Prime Video': f'https://www.primevideo.com/search?phrase={q}',
        'Disney+': f'https://www.disneyplus.com/search/{q}',
        'Crunchyroll': f'https://www.crunchyroll.com/search?q={q}',
        'Amazon': f'https://www.amazon.com/s?k={q}',
        'YouTube': f'https://www.youtube.com/results?search_query={q}',
        'Viki': f'https://www.viki.com/search?q={q}',
    }
    return urls.get(platform, f'https://www.google.com/search?q={q}')


# ============================================================
# HAPPY
# ============================================================
happy_music = [
    # Telugu
    {'title': 'Buttabomma', 'artist': 'Armaan Malik', 'genre': 'Telugu Pop', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'La La La', 'artist': 'DSP', 'genre': 'Telugu Dance', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Mella Mellaga', 'artist': 'DSP', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Cinema Choopista Mava', 'artist': 'DSP', 'genre': 'Telugu Pop', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Badtameez Dil', 'artist': 'Benny Dayal', 'genre': 'Bollywood Dance', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Gallan Goodiyaan', 'artist': 'Farhan Akhtar', 'genre': 'Bollywood Pop', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Kar Gayi Chull', 'artist': 'Badshah', 'genre': 'Bollywood Dance', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'London Thumakda', 'artist': 'Labh Janjua', 'genre': 'Bollywood Dance', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    # English
    {'title': 'Happy', 'artist': 'Pharrell Williams', 'genre': 'Pop', 'platform': 'Spotify'},
    {'title': 'Walking on Sunshine', 'artist': 'Katrina & The Waves', 'genre': 'Pop Rock', 'platform': 'Spotify'},
    {'title': 'Uptown Funk', 'artist': 'Bruno Mars', 'genre': 'Funk/Pop', 'platform': 'Spotify'},
    {'title': "Can't Stop the Feeling", 'artist': 'Justin Timberlake', 'genre': 'Pop', 'platform': 'Spotify'},
    {'title': 'Good as Hell', 'artist': 'Lizzo', 'genre': 'Pop/R&B', 'platform': 'Apple Music'},
    {'title': 'Shake It Off', 'artist': 'Taylor Swift', 'genre': 'Pop', 'platform': 'Spotify'},
    {'title': 'Dynamite', 'artist': 'BTS', 'genre': 'K-Pop', 'platform': 'Spotify'},
    {'title': 'Levitating', 'artist': 'Dua Lipa', 'genre': 'Pop', 'platform': 'Spotify'},
    # Tamil
    {'title': 'Vaathi Coming', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Dance', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Aaluma Doluma', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Mass', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Why This Kolaveri Di', 'artist': 'Dhanush', 'genre': 'Tamil Pop', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Vaathi Raid', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Dance', 'platform': 'JioSaavn', 'lang': 'Tamil'},
]
happy_movies = [
    # Telugu
    {'title': 'Pellichoopulu', 'genre': 'Romantic Comedy', 'year': 2016, 'rating': 7.9, 'platform': 'Prime Video', 'lang': 'Telugu'},
    {'title': 'Ala Vaikunthapurramuloo', 'genre': 'Action/Comedy', 'year': 2020, 'rating': 7.3, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'Bommarillu', 'genre': 'Romantic Comedy', 'year': 2006, 'rating': 7.8, 'platform': 'YouTube', 'lang': 'Telugu'},
    {'title': 'Happy Days', 'genre': 'Coming-of-age', 'year': 2007, 'rating': 7.4, 'platform': 'YouTube', 'lang': 'Telugu'},
    # Hindi
    {'title': '3 Idiots', 'genre': 'Comedy/Drama', 'year': 2009, 'rating': 8.4, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Zindagi Na Milegi Dobara', 'genre': 'Comedy/Drama', 'year': 2011, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Dil Chahta Hai', 'genre': 'Comedy/Drama', 'year': 2001, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Queen', 'genre': 'Comedy/Drama', 'year': 2013, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
    # English
    {'title': 'The Secret Life of Walter Mitty', 'genre': 'Adventure/Comedy', 'year': 2013, 'rating': 7.3, 'platform': 'Netflix'},
    {'title': 'Forrest Gump', 'genre': 'Drama/Romance', 'year': 1994, 'rating': 8.8, 'platform': 'Prime Video'},
    {'title': 'La La Land', 'genre': 'Musical/Romance', 'year': 2016, 'rating': 8.0, 'platform': 'Netflix'},
    {'title': 'The Grand Budapest Hotel', 'genre': 'Comedy', 'year': 2014, 'rating': 8.1, 'platform': 'Disney+'},
    {'title': 'Up', 'genre': 'Animation/Adventure', 'year': 2009, 'rating': 8.3, 'platform': 'Disney+'},
    {'title': 'Coco', 'genre': 'Animation/Musical', 'year': 2017, 'rating': 8.4, 'platform': 'Disney+'},
    {'title': 'Paddington 2', 'genre': 'Comedy/Family', 'year': 2017, 'rating': 7.8, 'platform': 'Netflix'},
    {'title': 'Mamma Mia!', 'genre': 'Musical/Comedy', 'year': 2008, 'rating': 6.4, 'platform': 'Netflix'},
    # Tamil
    {'title': 'Soorarai Pottru', 'genre': 'Drama', 'year': 2020, 'rating': 8.7, 'platform': 'Prime Video', 'lang': 'Tamil'},
    {'title': 'Vikram Vedha', 'genre': 'Action/Thriller', 'year': 2017, 'rating': 8.4, 'platform': 'Netflix', 'lang': 'Tamil'},
    # Korean
    {'title': 'Parasite', 'genre': 'Thriller/Comedy', 'year': 2019, 'rating': 8.5, 'platform': 'Netflix', 'lang': 'Korean'},
    {'title': 'The Host', 'genre': 'Action/Comedy', 'year': 2006, 'rating': 7.1, 'platform': 'Netflix', 'lang': 'Korean'},
]
happy_anime = [
    {'title': 'Spy x Family', 'genre': 'Comedy/Action', 'episodes': 25, 'rating': 8.6, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'KonoSuba', 'genre': 'Comedy/Isekai', 'episodes': 20, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Barakamon', 'genre': 'Slice of Life', 'episodes': 12, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Nichijou', 'genre': 'Comedy', 'episodes': 26, 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Daily Lives of High School Boys', 'genre': 'Comedy', 'episodes': 12, 'rating': 8.2, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'The Way of the Househusband', 'genre': 'Comedy', 'episodes': 10, 'rating': 7.4, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Silver Spoon', 'genre': 'Comedy/Slice of Life', 'episodes': 22, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'K-On!', 'genre': 'Music/Comedy', 'episodes': 13, 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Tanaka-kun is Always Listless', 'genre': 'Comedy/Slice of Life', 'episodes': 12, 'rating': 7.6, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Gekkan Shoujo Nozaki-kun', 'genre': 'Romance/Comedy', 'episodes': 12, 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': "Haven't You Heard? I'm Sakamoto", 'genre': 'Comedy', 'episodes': 12, 'rating': 7.5, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Azumanga Daioh', 'genre': 'Comedy/Slice of Life', 'episodes': 26, 'rating': 7.7, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
]

# ============================================================
# SAD
# ============================================================
sad_music = [
    # Telugu
    {'title': 'Aakaasam Enatido', 'artist': 'SP Balasubrahmanyam', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Undiporadhe', 'artist': 'Sid Sriram', 'genre': 'Telugu Soulful', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Kadalalle', 'artist': 'Sid Sriram', 'genre': 'Telugu Soulful', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Nuvvostanante Nenoddantana', 'artist': 'SP Balasubrahmanyam', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Tujhe Bhula Diya', 'artist': 'Mohit Chauhan', 'genre': 'Bollywood Sad', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Channa Mereya', 'artist': 'Arijit Singh', 'genre': 'Bollywood Sad', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Tum Hi Ho', 'artist': 'Arijit Singh', 'genre': 'Bollywood Romantic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Agar Tum Saath Ho', 'artist': 'Arijit Singh', 'genre': 'Bollywood Sad', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    # English
    {'title': 'Someone Like You', 'artist': 'Adele', 'genre': 'Pop/Soul', 'platform': 'Spotify'},
    {'title': 'Fix You', 'artist': 'Coldplay', 'genre': 'Alt Rock', 'platform': 'Spotify'},
    {'title': 'Hurt', 'artist': 'Johnny Cash', 'genre': 'Country', 'platform': 'Spotify'},
    {'title': 'Mad World', 'artist': 'Gary Jules', 'genre': 'Alt Rock', 'platform': 'Apple Music'},
    {'title': 'Skinny Love', 'artist': 'Bon Iver', 'genre': 'Indie Folk', 'platform': 'Spotify'},
    {'title': 'The Scientist', 'artist': 'Coldplay', 'genre': 'Alt Rock', 'platform': 'Spotify'},
    {'title': 'Someone You Loved', 'artist': 'Lewis Capaldi', 'genre': 'Pop', 'platform': 'Spotify'},
    {'title': 'Let Her Go', 'artist': 'Passenger', 'genre': 'Folk Pop', 'platform': 'Spotify'},
    # Tamil
    {'title': 'Nenjukulle', 'artist': 'AR Rahman', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Kannalane', 'artist': 'AR Rahman', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Munbe Vaa', 'artist': 'Shreya Ghoshal', 'genre': 'Tamil Romantic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Venmegam', 'artist': 'Harris Jayaraj', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
]
sad_movies = [
    # Telugu
    {'title': 'Sita Ramam', 'genre': 'Romantic Drama', 'year': 2022, 'rating': 8.6, 'platform': 'Prime Video', 'lang': 'Telugu'},
    {'title': 'Hi Nanna', 'genre': 'Romantic Drama', 'year': 2023, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'October', 'genre': 'Romantic Drama', 'year': 2018, 'rating': 7.6, 'platform': 'Prime Video', 'lang': 'Telugu'},
    {'title': 'Premam', 'genre': 'Romantic Drama', 'year': 2015, 'rating': 7.8, 'platform': 'Hotstar', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Aashiqui 2', 'genre': 'Romantic Drama', 'year': 2013, 'rating': 7.0, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Rockstar', 'genre': 'Romance/Music', 'year': 2011, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Tamasha', 'genre': 'Romance/Drama', 'year': 2015, 'rating': 7.3, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Kabir Singh', 'genre': 'Romantic Drama', 'year': 2019, 'rating': 7.1, 'platform': 'Netflix', 'lang': 'Hindi'},
    # English
    {'title': 'Grave of the Fireflies', 'genre': 'Animation/Drama', 'year': 1988, 'rating': 8.5, 'platform': 'Netflix'},
    {'title': 'The Pursuit of Happyness', 'genre': 'Drama', 'year': 2006, 'rating': 8.0, 'platform': 'Netflix'},
    {'title': 'Inside Out', 'genre': 'Animation/Drama', 'year': 2015, 'rating': 8.1, 'platform': 'Disney+'},
    {'title': '500 Days of Summer', 'genre': 'Romance/Drama', 'year': 2009, 'rating': 7.7, 'platform': 'Netflix'},
    {'title': 'A Walk to Remember', 'genre': 'Romance/Drama', 'year': 2002, 'rating': 7.4, 'platform': 'Netflix'},
    {'title': 'Me Before You', 'genre': 'Romance/Drama', 'year': 2016, 'rating': 7.4, 'platform': 'Netflix'},
    {'title': 'The Green Mile', 'genre': 'Drama/Fantasy', 'year': 1999, 'rating': 8.6, 'platform': 'Netflix'},
    {'title': 'Hachi: A Dog\'s Tale', 'genre': 'Drama/Family', 'year': 2009, 'rating': 8.1, 'platform': 'Netflix'},
    # Tamil
    {'title': '96', 'genre': 'Romantic Drama', 'year': 2018, 'rating': 8.5, 'platform': 'Prime Video', 'lang': 'Tamil'},
    {'title': 'Vinnaithaandi Varuvaayaa', 'genre': 'Romantic Drama', 'year': 2010, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Tamil'},
    # Korean
    {'title': 'A Moment to Remember', 'genre': 'Romance/Drama', 'year': 2004, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Korean'},
    {'title': 'Miracle in Cell No. 7', 'genre': 'Drama/Comedy', 'year': 2013, 'rating': 8.2, 'platform': 'Netflix', 'lang': 'Korean'},
]
sad_anime = [
    {'title': 'Your Lie in April', 'genre': 'Romance/Drama', 'episodes': 22, 'rating': 8.6, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Violet Evergarden', 'genre': 'Drama', 'episodes': 13, 'rating': 8.6, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Anohana', 'genre': 'Drama', 'episodes': 11, 'rating': 8.3, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Clannad: After Story', 'genre': 'Romance/Drama', 'episodes': 24, 'rating': 8.9, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'I Want to Eat Your Pancreas', 'genre': 'Romance/Drama', 'rating': 8.6, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'March Comes in Like a Lion', 'genre': 'Drama', 'episodes': 22, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'To Your Eternity', 'genre': 'Drama/Fantasy', 'episodes': 20, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Made in Abyss', 'genre': 'Adventure/Drama', 'episodes': 13, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Wolf Children', 'genre': 'Fantasy/Drama', 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Given', 'genre': 'Music/Drama', 'episodes': 11, 'rating': 8.3, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'The Garden of Words', 'genre': 'Romance/Drama', 'rating': 7.5, 'platform': 'Netflix', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Orange', 'genre': 'Romance/Drama', 'episodes': 13, 'rating': 7.7, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
]

# ============================================================
# ENERGETIC
# ============================================================
energetic_music = [
    # Telugu
    {'title': 'Pushpa Pushpa', 'artist': 'DSP', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Top Lechipoddi', 'artist': 'Thaman S', 'genre': 'Telugu Hype', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Dandaalayyaa', 'artist': 'Kaala Bhairava', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Jaragandi', 'artist': 'Thaman S', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Malhari', 'artist': 'Vishal Dadlani', 'genre': 'Bollywood Mass', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Bhaag Milkha Bhaag', 'artist': 'Siddharth Mahadevan', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Brothers Anthem', 'artist': 'Vishal Dadlani', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Zinda', 'artist': 'Siddharth Mahadevan', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    # English
    {'title': 'Lose Yourself', 'artist': 'Eminem', 'genre': 'Hip Hop', 'platform': 'Spotify'},
    {'title': 'Thunderstruck', 'artist': 'AC/DC', 'genre': 'Hard Rock', 'platform': 'Spotify'},
    {'title': "Don't Stop Me Now", 'artist': 'Queen', 'genre': 'Rock', 'platform': 'Spotify'},
    {'title': 'Blinding Lights', 'artist': 'The Weeknd', 'genre': 'Synthpop', 'platform': 'Spotify'},
    {'title': 'Eye of the Tiger', 'artist': 'Survivor', 'genre': 'Rock', 'platform': 'Spotify'},
    {'title': 'Sicko Mode', 'artist': 'Travis Scott', 'genre': 'Hip Hop', 'platform': 'Spotify'},
    {'title': 'Levels', 'artist': 'Avicii', 'genre': 'EDM', 'platform': 'Spotify'},
    {'title': 'Radioactive', 'artist': 'Imagine Dragons', 'genre': 'Alt Rock', 'platform': 'Spotify'},
    # Tamil
    {'title': 'Vaathi Coming', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Dance', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Aaluma Doluma', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Mass', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Vaathi Raid', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Dance', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Beast Mode', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Hype', 'platform': 'JioSaavn', 'lang': 'Tamil'},
]
energetic_movies = [
    # Telugu
    {'title': 'RRR', 'genre': 'Action/Drama', 'year': 2022, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'Pushpa: The Rise', 'genre': 'Action/Drama', 'year': 2021, 'rating': 7.6, 'platform': 'Prime Video', 'lang': 'Telugu'},
    {'title': 'Baahubali: The Beginning', 'genre': 'Action/Fantasy', 'year': 2015, 'rating': 8.0, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'KGF Chapter 1', 'genre': 'Action/Drama', 'year': 2018, 'rating': 7.6, 'platform': 'Prime Video', 'lang': 'Telugu'},
    # Hindi
    {'title': 'War', 'genre': 'Action/Thriller', 'year': 2019, 'rating': 6.5, 'platform': 'Prime Video', 'lang': 'Hindi'},
    {'title': 'Dhoom', 'genre': 'Action/Thriller', 'year': 2004, 'rating': 6.6, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Tiger Zinda Hai', 'genre': 'Action/Thriller', 'year': 2017, 'rating': 6.2, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Bhaag Milkha Bhaag', 'genre': 'Sports/Biography', 'year': 2013, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Hindi'},
    # English
    {'title': 'Mad Max: Fury Road', 'genre': 'Action/Sci-Fi', 'year': 2015, 'rating': 8.1, 'platform': 'Netflix'},
    {'title': 'John Wick', 'genre': 'Action/Thriller', 'year': 2014, 'rating': 7.4, 'platform': 'Prime Video'},
    {'title': 'Spider-Man: Into the Spider-Verse', 'genre': 'Animation/Action', 'year': 2018, 'rating': 8.4, 'platform': 'Netflix'},
    {'title': 'The Dark Knight', 'genre': 'Action/Thriller', 'year': 2008, 'rating': 9.0, 'platform': 'Netflix'},
    {'title': 'Kill Bill: Vol. 1', 'genre': 'Action', 'year': 2003, 'rating': 8.2, 'platform': 'Netflix'},
    {'title': 'Top Gun: Maverick', 'genre': 'Action/Drama', 'year': 2022, 'rating': 8.2, 'platform': 'Prime Video'},
    {'title': 'Mission: Impossible - Fallout', 'genre': 'Action/Thriller', 'year': 2018, 'rating': 7.7, 'platform': 'Netflix'},
    {'title': 'Spider-Man: No Way Home', 'genre': 'Action/Adventure', 'year': 2021, 'rating': 8.2, 'platform': 'Netflix'},
    # Tamil
    {'title': 'Vikram', 'genre': 'Action/Thriller', 'year': 2022, 'rating': 7.6, 'platform': 'Hotstar', 'lang': 'Tamil'},
    {'title': 'Master', 'genre': 'Action/Thriller', 'year': 2021, 'rating': 7.2, 'platform': 'Prime Video', 'lang': 'Tamil'},
    # Korean
    {'title': 'The Gangster, the Cop, the Devil', 'genre': 'Action/Crime', 'year': 2019, 'rating': 6.9, 'platform': 'Netflix', 'lang': 'Korean'},
    {'title': 'Train to Busan', 'genre': 'Action/Horror', 'year': 2016, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Korean'},
]
energetic_anime = [
    {'title': 'Demon Slayer', 'genre': 'Action/Fantasy', 'episodes': 26, 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Jujutsu Kaisen', 'genre': 'Action/Supernatural', 'episodes': 24, 'rating': 8.6, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'My Hero Academia', 'genre': 'Action/Superhero', 'episodes': 13, 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Mob Psycho 100', 'genre': 'Action/Comedy', 'episodes': 12, 'rating': 8.6, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Gurren Lagann', 'genre': 'Mecha/Action', 'episodes': 27, 'rating': 8.3, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Haikyuu!!', 'genre': 'Sports', 'episodes': 25, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Kengan Ashura', 'genre': 'Action/Martial Arts', 'episodes': 24, 'rating': 8.0, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Kill la Kill', 'genre': 'Action/Comedy', 'episodes': 24, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Fire Force', 'genre': 'Action/Supernatural', 'episodes': 24, 'rating': 7.7, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'One Piece', 'genre': 'Action/Adventure', 'episodes': 1100, 'rating': 8.7, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Naruto Shippuden', 'genre': 'Action/Adventure', 'episodes': 500, 'rating': 8.3, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Baki', 'genre': 'Action/Martial Arts', 'episodes': 26, 'rating': 7.6, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
]

# ============================================================
# CALM
# ============================================================
calm_music = [
    # Telugu
    {'title': 'Samajavaragamana', 'artist': 'Sid Sriram', 'genre': 'Telugu Classical', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Inkem Inkem', 'artist': 'Sid Sriram', 'genre': 'Telugu Romantic', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Amma', 'artist': 'Ilaiyaraaja', 'genre': 'Telugu Devotional', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Tharagathi Gadhi', 'artist': 'Radhan', 'genre': 'Telugu Indie', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Tum Se Hi', 'artist': 'Mohit Chauhan', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Kun Faya Kun', 'artist': 'AR Rahman', 'genre': 'Bollywood Sufi', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Phir Le Aaya Dil', 'artist': 'Arijit Singh', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Ilahi', 'artist': 'Arijit Singh', 'genre': 'Bollywood Chill', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    # English
    {'title': 'Weightless', 'artist': 'Marconi Union', 'genre': 'Ambient', 'platform': 'Spotify'},
    {'title': 'Sunset Lover', 'artist': 'Petit Biscuit', 'genre': 'Chillwave', 'platform': 'Spotify'},
    {'title': 'Nuvole Bianche', 'artist': 'Ludovico Einaudi', 'genre': 'Neo-classical', 'platform': 'Apple Music'},
    {'title': 'Holocene', 'artist': 'Bon Iver', 'genre': 'Indie Folk', 'platform': 'Spotify'},
    {'title': 'Bloom', 'artist': 'The Paper Kites', 'genre': 'Indie Folk', 'platform': 'Spotify'},
    {'title': 'River Flows in You', 'artist': 'Yiruma', 'genre': 'Neo-classical', 'platform': 'Spotify'},
    {'title': 'Sweater Weather', 'artist': 'The Neighbourhood', 'genre': 'Indie', 'platform': 'Spotify'},
    {'title': 'Intro', 'artist': 'The xx', 'genre': 'Indie', 'platform': 'Spotify'},
    # Tamil
    {'title': 'Munbe Vaa', 'artist': 'Shreya Ghoshal', 'genre': 'Tamil Romantic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Nenjukulle', 'artist': 'AR Rahman', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Kannalane', 'artist': 'AR Rahman', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Venmegam', 'artist': 'Harris Jayaraj', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
]
calm_movies = [
    # Telugu
    {'title': 'Jersey', 'genre': 'Sports Drama', 'year': 2019, 'rating': 8.5, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'Mahanati', 'genre': 'Biographical Drama', 'year': 2018, 'rating': 8.5, 'platform': 'Prime Video', 'lang': 'Telugu'},
    {'title': 'C/O Kancharapalem', 'genre': 'Drama/Romance', 'year': 2018, 'rating': 8.5, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'Okkadu', 'genre': 'Action/Romance', 'year': 2003, 'rating': 7.3, 'platform': 'YouTube', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Taare Zameen Par', 'genre': 'Drama/Family', 'year': 2007, 'rating': 8.4, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Swades', 'genre': 'Drama', 'year': 2004, 'rating': 8.2, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Dear Zindagi', 'genre': 'Drama', 'year': 2016, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Piku', 'genre': 'Comedy/Drama', 'year': 2015, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Hindi'},
    # English
    {'title': 'My Neighbor Totoro', 'genre': 'Animation/Fantasy', 'year': 1988, 'rating': 8.2, 'platform': 'Netflix'},
    {'title': 'Chef', 'genre': 'Comedy/Drama', 'year': 2014, 'rating': 7.3, 'platform': 'Netflix'},
    {'title': 'Little Women', 'genre': 'Drama/Romance', 'year': 2019, 'rating': 7.8, 'platform': 'Netflix'},
    {'title': 'Before Sunrise', 'genre': 'Romance/Drama', 'year': 1995, 'rating': 8.1, 'platform': 'Prime Video'},
    {'title': 'Spirited Away', 'genre': 'Animation/Fantasy', 'year': 2001, 'rating': 8.6, 'platform': 'Netflix'},
    {'title': 'Lost in Translation', 'genre': 'Drama', 'year': 2003, 'rating': 7.7, 'platform': 'Netflix'},
    {'title': 'Midnight in Paris', 'genre': 'Comedy/Fantasy', 'year': 2011, 'rating': 7.7, 'platform': 'Netflix'},
    {'title': 'The Remains of the Day', 'genre': 'Drama/Romance', 'year': 1993, 'rating': 7.8, 'platform': 'Netflix'},
    # Tamil
    {'title': 'Soorarai Pottru', 'genre': 'Drama', 'year': 2020, 'rating': 8.7, 'platform': 'Prime Video', 'lang': 'Tamil'},
    {'title': '96', 'genre': 'Romantic Drama', 'year': 2018, 'rating': 8.5, 'platform': 'Prime Video', 'lang': 'Tamil'},
    # Korean
    {'title': 'Little Forest', 'genre': 'Drama/Slice of Life', 'year': 2018, 'rating': 7.5, 'platform': 'Netflix', 'lang': 'Korean'},
    {'title': 'The Way Home', 'genre': 'Drama/Family', 'year': 2002, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Korean'},
]
calm_anime = [
    {'title': 'Mushishi', 'genre': 'Supernatural/Slice of Life', 'episodes': 26, 'rating': 8.7, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': "Natsume's Book of Friends", 'genre': 'Supernatural/Slice of Life', 'episodes': 13, 'rating': 8.3, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Flying Witch', 'genre': 'Slice of Life', 'episodes': 12, 'rating': 7.5, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Aria the Animation', 'genre': 'Sci-Fi/Slice of Life', 'episodes': 13, 'rating': 7.8, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Non Non Biyori', 'genre': 'Slice of Life/Comedy', 'episodes': 12, 'rating': 8.0, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Yuru Camp', 'genre': 'Slice of Life', 'episodes': 12, 'rating': 8.3, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Hyouka', 'genre': 'Mystery/Slice of Life', 'episodes': 22, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Bartender', 'genre': 'Slice of Life/Drama', 'episodes': 11, 'rating': 7.6, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Kamichu!', 'genre': 'Slice of Life/Fantasy', 'episodes': 12, 'rating': 7.3, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Somali and the Forest Spirit', 'genre': 'Fantasy/Slice of Life', 'episodes': 12, 'rating': 7.4, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Tamayura', 'genre': 'Slice of Life', 'episodes': 12, 'rating': 7.3, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': "Poco's Udon World", 'genre': 'Slice of Life', 'episodes': 12, 'rating': 7.2, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
]

# ============================================================
# ROMANTIC
# ============================================================
romantic_music = [
    # Telugu
    {'title': 'Oosupodu', 'artist': 'Karthik', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Manasa Manasa', 'artist': 'Sid Sriram', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Nee Kavitha', 'artist': 'Chaitan Bharadwaj', 'genre': 'Telugu Indie', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Inkem Inkem Kavale', 'artist': 'Sid Sriram', 'genre': 'Telugu Romantic', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Tum Hi Ho', 'artist': 'Arijit Singh', 'genre': 'Bollywood Romantic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Raataan Lambiyan', 'artist': 'Jubin Nautiyal', 'genre': 'Bollywood Romantic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Kesariya', 'artist': 'Arijit Singh', 'genre': 'Bollywood Romantic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Shayad', 'artist': 'Arijit Singh', 'genre': 'Bollywood Romantic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    # English
    {'title': 'Perfect', 'artist': 'Ed Sheeran', 'genre': 'Pop', 'platform': 'Spotify'},
    {'title': 'All of Me', 'artist': 'John Legend', 'genre': 'R&B/Soul', 'platform': 'Spotify'},
    {'title': "Can't Help Falling in Love", 'artist': 'Elvis Presley', 'genre': 'Classic Pop', 'platform': 'Spotify'},
    {'title': 'Thinking Out Loud', 'artist': 'Ed Sheeran', 'genre': 'Pop', 'platform': 'Spotify'},
    {'title': 'A Thousand Years', 'artist': 'Christina Perri', 'genre': 'Pop', 'platform': 'Spotify'},
    {'title': 'Make You Feel My Love', 'artist': 'Adele', 'genre': 'Pop/Soul', 'platform': 'Spotify'},
    {'title': 'You Are the Reason', 'artist': 'Calum Scott', 'genre': 'Pop', 'platform': 'Spotify'},
    {'title': 'Wonderful Tonight', 'artist': 'Eric Clapton', 'genre': 'Rock', 'platform': 'Spotify'},
    # Tamil
    {'title': 'Munbe Vaa', 'artist': 'Shreya Ghoshal', 'genre': 'Tamil Romantic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Nenjukulle', 'artist': 'AR Rahman', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Vinnaithaandi Varuvaayaa', 'artist': 'AR Rahman', 'genre': 'Tamil Romantic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Kannalane', 'artist': 'AR Rahman', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
]
romantic_movies = [
    # Telugu
    {'title': 'Fidaa', 'genre': 'Romantic Drama', 'year': 2017, 'rating': 7.4, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'Geetha Govindam', 'genre': 'Romantic Comedy', 'year': 2018, 'rating': 7.2, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'Arjun Reddy', 'genre': 'Romantic Drama', 'year': 2017, 'rating': 8.0, 'platform': 'Prime Video', 'lang': 'Telugu'},
    {'title': 'Ninnu Kori', 'genre': 'Romantic Drama', 'year': 2017, 'rating': 7.3, 'platform': 'Netflix', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Dilwale Dulhania Le Jayenge', 'genre': 'Romance/Drama', 'year': 1995, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Jab We Met', 'genre': 'Romantic Comedy', 'year': 2007, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Yeh Jawaani Hai Deewani', 'genre': 'Romance/Drama', 'year': 2013, 'rating': 7.2, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Barfi!', 'genre': 'Romance/Comedy', 'year': 2012, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
    # English
    {'title': 'The Notebook', 'genre': 'Romance/Drama', 'year': 2004, 'rating': 7.8, 'platform': 'Netflix'},
    {'title': 'Pride & Prejudice', 'genre': 'Romance/Drama', 'year': 2005, 'rating': 7.8, 'platform': 'Netflix'},
    {'title': 'Before Sunset', 'genre': 'Romance/Drama', 'year': 2004, 'rating': 8.1, 'platform': 'Prime Video'},
    {'title': 'Notting Hill', 'genre': 'Romance/Comedy', 'year': 1999, 'rating': 7.2, 'platform': 'Netflix'},
    {'title': 'About Time', 'genre': 'Romance/Sci-Fi', 'year': 2013, 'rating': 7.8, 'platform': 'Netflix'},
    {'title': 'Love Actually', 'genre': 'Romance/Comedy', 'year': 2003, 'rating': 7.6, 'platform': 'Netflix'},
    {'title': 'When Harry Met Sally', 'genre': 'Romance/Comedy', 'year': 1989, 'rating': 7.7, 'platform': 'Netflix'},
    {'title': 'Crazy Rich Asians', 'genre': 'Romance/Comedy', 'year': 2018, 'rating': 7.0, 'platform': 'Netflix'},
    # Tamil
    {'title': '96', 'genre': 'Romantic Drama', 'year': 2018, 'rating': 8.5, 'platform': 'Prime Video', 'lang': 'Tamil'},
    {'title': 'Vinnaithaandi Varuvaayaa', 'genre': 'Romantic Drama', 'year': 2010, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Tamil'},
    # Korean
    {'title': 'Tune in for Love', 'genre': 'Romance/Drama', 'year': 2019, 'rating': 7.2, 'platform': 'Netflix', 'lang': 'Korean'},
    {'title': 'My Sassy Girl', 'genre': 'Romance/Comedy', 'year': 2001, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Korean'},
]
romantic_anime = [
    {'title': 'Toradora!', 'genre': 'Romance/Comedy', 'episodes': 25, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Kaguya-sama: Love is War', 'genre': 'Romance/Comedy', 'episodes': 12, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Horimiya', 'genre': 'Romance/Slice of Life', 'episodes': 13, 'rating': 8.2, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Fruits Basket', 'genre': 'Romance/Drama', 'episodes': 25, 'rating': 8.6, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'My Dress-Up Darling', 'genre': 'Romance/Comedy', 'episodes': 12, 'rating': 8.0, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Lovely Complex', 'genre': 'Romance/Comedy', 'episodes': 24, 'rating': 8.0, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Kimi ni Todoke', 'genre': 'Romance/Slice of Life', 'episodes': 25, 'rating': 8.0, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Nana', 'genre': 'Romance/Drama', 'episodes': 47, 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Golden Time', 'genre': 'Romance/Comedy', 'episodes': 24, 'rating': 7.7, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Snow White with the Red Hair', 'genre': 'Romance/Fantasy', 'episodes': 24, 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Wotakoi', 'genre': 'Romance/Comedy', 'episodes': 11, 'rating': 7.6, 'platform': 'Amazon', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Your Name', 'genre': 'Romance/Fantasy', 'rating': 8.4, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
]

# ============================================================
# ANGRY
# ============================================================
angry_music = [
    # Telugu
    {'title': 'Dandaalayyaa', 'artist': 'Kaala Bhairava', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Beast Mode', 'artist': 'Thaman S', 'genre': 'Telugu Hype', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Saami Saami', 'artist': 'DSP', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Oo Antava', 'artist': 'Indravathi Chauhan', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Challa', 'artist': 'Javed Ali', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Sadda Haq', 'artist': 'Mohit Chauhan', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Yeh Jawaani Hai Deewani Rock', 'artist': 'Pritam', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Dhan Te Nan', 'artist': 'Vishal Bhardwaj', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    # English
    {'title': 'Killing in the Name', 'artist': 'Rage Against the Machine', 'genre': 'Metal/Rap', 'platform': 'Spotify'},
    {'title': 'Break Stuff', 'artist': 'Limp Bizkit', 'genre': 'Nu Metal', 'platform': 'Spotify'},
    {'title': 'Given Up', 'artist': 'Linkin Park', 'genre': 'Alt Metal', 'platform': 'Spotify'},
    {'title': 'Duality', 'artist': 'Slipknot', 'genre': 'Metal', 'platform': 'Spotify'},
    {'title': 'In the End', 'artist': 'Linkin Park', 'genre': 'Nu Metal', 'platform': 'Spotify'},
    {'title': 'Chop Suey!', 'artist': 'System of a Down', 'genre': 'Metal', 'platform': 'Spotify'},
    {'title': 'Down with the Sickness', 'artist': 'Disturbed', 'genre': 'Metal', 'platform': 'Spotify'},
    {'title': 'Last Resort', 'artist': 'Papa Roach', 'genre': 'Nu Metal', 'platform': 'Spotify'},
    # Tamil
    {'title': 'Aaluma Doluma', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Mass', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Vaathi Raid', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Hype', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Beast Mode', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Hype', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Vikram Theme', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Mass', 'platform': 'JioSaavn', 'lang': 'Tamil'},
]
angry_movies = [
    # Telugu
    {'title': 'Temper', 'genre': 'Action Drama', 'year': 2015, 'rating': 7.2, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'Arjun Reddy', 'genre': 'Romantic Drama', 'year': 2017, 'rating': 8.0, 'platform': 'Prime Video', 'lang': 'Telugu'},
    {'title': 'Pokiri', 'genre': 'Action/Thriller', 'year': 2006, 'rating': 7.9, 'platform': 'YouTube', 'lang': 'Telugu'},
    {'title': 'Simhadri', 'genre': 'Action/Drama', 'year': 2003, 'rating': 7.2, 'platform': 'YouTube', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Gangs of Wasseypur', 'genre': 'Crime/Drama', 'year': 2012, 'rating': 8.2, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Kabir Singh', 'genre': 'Romantic Drama', 'year': 2019, 'rating': 7.1, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Agneepath', 'genre': 'Action/Drama', 'year': 2012, 'rating': 6.9, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Baaghi', 'genre': 'Action/Romance', 'year': 2016, 'rating': 5.4, 'platform': 'Netflix', 'lang': 'Hindi'},
    # English
    {'title': 'Fight Club', 'genre': 'Drama/Thriller', 'year': 1999, 'rating': 8.8, 'platform': 'Netflix'},
    {'title': 'The Raid', 'genre': 'Action', 'year': 2011, 'rating': 7.6, 'platform': 'Netflix'},
    {'title': 'Oldboy', 'genre': 'Thriller/Action', 'year': 2003, 'rating': 8.4, 'platform': 'Netflix'},
    {'title': 'Gladiator', 'genre': 'Action/Drama', 'year': 2000, 'rating': 8.5, 'platform': 'Prime Video'},
    {'title': '300', 'genre': 'Action/War', 'year': 2006, 'rating': 7.6, 'platform': 'Netflix'},
    {'title': 'Joker', 'genre': 'Drama/Thriller', 'year': 2019, 'rating': 8.2, 'platform': 'Netflix'},
    {'title': 'The Departed', 'genre': 'Crime/Thriller', 'year': 2006, 'rating': 8.5, 'platform': 'Netflix'},
    {'title': 'No Country for Old Men', 'genre': 'Thriller/Crime', 'year': 2007, 'rating': 8.1, 'platform': 'Netflix'},
    # Tamil
    {'title': 'Vikram Vedha', 'genre': 'Action/Thriller', 'year': 2017, 'rating': 8.4, 'platform': 'Netflix', 'lang': 'Tamil'},
    {'title': 'Kaithi', 'genre': 'Action/Thriller', 'year': 2019, 'rating': 8.5, 'platform': 'Netflix', 'lang': 'Tamil'},
    # Korean
    {'title': 'Old Boy', 'genre': 'Thriller/Action', 'year': 2003, 'rating': 8.4, 'platform': 'Netflix', 'lang': 'Korean'},
    {'title': 'I Saw the Devil', 'genre': 'Thriller/Action', 'year': 2010, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Korean'},
]
angry_anime = [
    {'title': 'Attack on Titan', 'genre': 'Action/Dark Fantasy', 'episodes': 25, 'rating': 9.0, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Berserk', 'genre': 'Dark Fantasy/Action', 'episodes': 25, 'rating': 8.7, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Vinland Saga', 'genre': 'Action/Drama', 'episodes': 24, 'rating': 8.7, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Black Lagoon', 'genre': 'Action/Crime', 'episodes': 12, 'rating': 8.0, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Tokyo Ghoul', 'genre': 'Action/Horror', 'episodes': 12, 'rating': 7.8, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Parasyte', 'genre': 'Action/Horror', 'episodes': 24, 'rating': 8.3, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Devilman Crybaby', 'genre': 'Action/Horror', 'episodes': 10, 'rating': 7.8, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Dororo', 'genre': 'Action/Supernatural', 'episodes': 24, 'rating': 8.2, 'platform': 'Amazon', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Hellsing Ultimate', 'genre': 'Action/Horror', 'episodes': 10, 'rating': 8.2, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Akame ga Kill!', 'genre': 'Action/Fantasy', 'episodes': 24, 'rating': 7.6, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Elfen Lied', 'genre': 'Action/Horror', 'episodes': 13, 'rating': 7.5, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Claymore', 'genre': 'Action/Fantasy', 'episodes': 26, 'rating': 7.8, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
]

# ============================================================
# NOSTALGIC
# ============================================================
nostalgic_music = [
    # Telugu
    {'title': 'Priyatama Priyatama', 'artist': 'Ilaiyaraaja', 'genre': 'Telugu Classic', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Vennello Godari', 'artist': 'SP Balasubrahmanyam', 'genre': 'Telugu Classic', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Nee Navvule', 'artist': 'SP Balasubrahmanyam', 'genre': 'Telugu Classic', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Muddabanthi Navvulo', 'artist': 'SP Balasubrahmanyam', 'genre': 'Telugu Classic', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Kuch Kuch Hota Hai', 'artist': 'Udit Narayan', 'genre': 'Bollywood Classic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Tujhe Dekha To', 'artist': 'Kumar Sanu', 'genre': 'Bollywood Classic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Pehla Nasha', 'artist': 'Udit Narayan', 'genre': 'Bollywood Classic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Mere Sapno Ki Rani', 'artist': 'Kishore Kumar', 'genre': 'Bollywood Retro', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    # English
    {'title': 'Bohemian Rhapsody', 'artist': 'Queen', 'genre': 'Rock', 'platform': 'Spotify'},
    {'title': 'Hotel California', 'artist': 'Eagles', 'genre': 'Rock', 'platform': 'Spotify'},
    {'title': 'September', 'artist': 'Earth, Wind & Fire', 'genre': 'Funk/Disco', 'platform': 'Spotify'},
    {'title': 'Take on Me', 'artist': 'a-ha', 'genre': 'Synth Pop', 'platform': 'Spotify'},
    {'title': 'Africa', 'artist': 'Toto', 'genre': 'Pop Rock', 'platform': 'Spotify'},
    {'title': 'Dreams', 'artist': 'Fleetwood Mac', 'genre': 'Rock', 'platform': 'Spotify'},
    {'title': "Don't Stop Believin'", 'artist': 'Journey', 'genre': 'Rock', 'platform': 'Spotify'},
    {'title': 'Sweet Child O\' Mine', 'artist': 'Guns N\' Roses', 'genre': 'Rock', 'platform': 'Spotify'},
    # Tamil
    {'title': 'Roja Roja', 'artist': 'SP Balasubrahmanyam', 'genre': 'Tamil Classic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Kadhal Rojave', 'artist': 'SP Balasubrahmanyam', 'genre': 'Tamil Classic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Mukkabla', 'artist': 'AR Rahman', 'genre': 'Tamil Dance', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Chinna Chinna Aasai', 'artist': 'Minmini', 'genre': 'Tamil Classic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
]
nostalgic_movies = [
    # Telugu
    {'title': 'Eega', 'genre': 'Fantasy/Thriller', 'year': 2012, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'Malliswari', 'genre': 'Comedy/Romance', 'year': 2004, 'rating': 7.5, 'platform': 'YouTube', 'lang': 'Telugu'},
    {'title': 'Shankar Dada MBBS', 'genre': 'Comedy/Drama', 'year': 2004, 'rating': 7.3, 'platform': 'YouTube', 'lang': 'Telugu'},
    {'title': 'Pokiri', 'genre': 'Action/Thriller', 'year': 2006, 'rating': 7.9, 'platform': 'YouTube', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Dilwale Dulhania Le Jayenge', 'genre': 'Romance/Drama', 'year': 1995, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Kuch Kuch Hota Hai', 'genre': 'Romance/Drama', 'year': 1998, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Kabhi Khushi Kabhie Gham', 'genre': 'Drama/Family', 'year': 2001, 'rating': 7.4, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Hum Aapke Hain Koun', 'genre': 'Romance/Family', 'year': 1994, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Hindi'},
    # English
    {'title': 'Stand By Me', 'genre': 'Drama/Coming-of-age', 'year': 1986, 'rating': 8.1, 'platform': 'Netflix'},
    {'title': 'The Breakfast Club', 'genre': 'Drama/Coming-of-age', 'year': 1985, 'rating': 7.8, 'platform': 'Netflix'},
    {'title': 'Toy Story', 'genre': 'Animation/Adventure', 'year': 1995, 'rating': 8.3, 'platform': 'Disney+'},
    {'title': 'Back to the Future', 'genre': 'Sci-Fi/Adventure', 'year': 1985, 'rating': 8.5, 'platform': 'Netflix'},
    {'title': 'E.T. the Extra-Terrestrial', 'genre': 'Sci-Fi/Family', 'year': 1982, 'rating': 7.9, 'platform': 'Netflix'},
    {'title': 'The Lion King', 'genre': 'Animation/Adventure', 'year': 1994, 'rating': 8.5, 'platform': 'Disney+'},
    {'title': 'Indiana Jones: Raiders of the Lost Ark', 'genre': 'Adventure/Action', 'year': 1981, 'rating': 8.4, 'platform': 'Netflix'},
    {'title': 'Ghostbusters', 'genre': 'Comedy/Fantasy', 'year': 1984, 'rating': 7.8, 'platform': 'Netflix'},
    # Tamil
    {'title': 'Roja', 'genre': 'Romance/Thriller', 'year': 1992, 'rating': 8.0, 'platform': 'YouTube', 'lang': 'Tamil'},
    {'title': 'Bombay', 'genre': 'Romance/Drama', 'year': 1995, 'rating': 7.7, 'platform': 'YouTube', 'lang': 'Tamil'},
    # Korean
    {'title': 'The Classic', 'genre': 'Romance/Drama', 'year': 2003, 'rating': 7.7, 'platform': 'Netflix', 'lang': 'Korean'},
    {'title': 'Joint Security Area', 'genre': 'Thriller/Drama', 'year': 2000, 'rating': 7.7, 'platform': 'Netflix', 'lang': 'Korean'},
]
nostalgic_anime = [
    {'title': 'Cowboy Bebop', 'genre': 'Sci-Fi/Action', 'episodes': 26, 'rating': 8.8, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Samurai Champloo', 'genre': 'Action/Adventure', 'episodes': 26, 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Dragon Ball Z', 'genre': 'Action/Adventure', 'episodes': 291, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Neon Genesis Evangelion', 'genre': 'Mecha/Drama', 'episodes': 26, 'rating': 8.3, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Yu Yu Hakusho', 'genre': 'Action/Supernatural', 'episodes': 112, 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Great Teacher Onizuka', 'genre': 'Comedy/Drama', 'episodes': 43, 'rating': 8.7, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Slam Dunk', 'genre': 'Sports/Comedy', 'episodes': 101, 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Rurouni Kenshin', 'genre': 'Action/Adventure', 'episodes': 95, 'rating': 8.3, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Trigun', 'genre': 'Sci-Fi/Action', 'episodes': 26, 'rating': 8.2, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Inuyasha', 'genre': 'Action/Adventure', 'episodes': 167, 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Cardcaptor Sakura', 'genre': 'Magical Girl', 'episodes': 70, 'rating': 8.0, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Sailor Moon', 'genre': 'Magical Girl', 'episodes': 46, 'rating': 7.7, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
]

# ============================================================
# ANXIOUS
# ============================================================
anxious_music = [
    # Telugu
    {'title': 'Ennen Ennen', 'artist': 'Pradeep Kumar', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Neekem Kaavaalaa', 'artist': 'Shreya Ghoshal', 'genre': 'Telugu Soft', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Manasu Maree', 'artist': 'Chaitan Bharadwaj', 'genre': 'Telugu Indie', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Emai Poyave', 'artist': 'Radhan', 'genre': 'Telugu Indie', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Agar Tum Saath Ho', 'artist': 'Arijit Singh', 'genre': 'Bollywood Sad', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Phir Le Aaya Dil', 'artist': 'Arijit Singh', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Channa Mereya', 'artist': 'Arijit Singh', 'genre': 'Bollywood Sad', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Kabira', 'artist': 'Arijit Singh', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    # English
    {'title': 'Breathe Me', 'artist': 'Sia', 'genre': 'Pop/Alt', 'platform': 'Spotify'},
    {'title': 'Everybody Hurts', 'artist': 'R.E.M.', 'genre': 'Alt Rock', 'platform': 'Spotify'},
    {'title': 'The Sound of Silence', 'artist': 'Simon & Garfunkel', 'genre': 'Folk Rock', 'platform': 'Spotify'},
    {'title': 'Creep', 'artist': 'Radiohead', 'genre': 'Alt Rock', 'platform': 'Spotify'},
    {'title': 'Hallelujah', 'artist': 'Jeff Buckley', 'genre': 'Alt Rock', 'platform': 'Spotify'},
    {'title': 'Nothing Else Matters', 'artist': 'Metallica', 'genre': 'Rock', 'platform': 'Spotify'},
    {'title': 'Fast Car', 'artist': 'Tracy Chapman', 'genre': 'Folk', 'platform': 'Spotify'},
    {'title': 'Teardrop', 'artist': 'Massive Attack', 'genre': 'Trip Hop', 'platform': 'Spotify'},
    # Tamil
    {'title': 'Nenjukulle', 'artist': 'AR Rahman', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Munbe Vaa', 'artist': 'Shreya Ghoshal', 'genre': 'Tamil Romantic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Venmegam', 'artist': 'Harris Jayaraj', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Kannalane', 'artist': 'AR Rahman', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
]
anxious_movies = [
    # Telugu
    {'title': 'C/O Kancharapalem', 'genre': 'Drama/Romance', 'year': 2018, 'rating': 8.5, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'Mental Madhilo', 'genre': 'Romantic Drama', 'year': 2017, 'rating': 7.0, 'platform': 'YouTube', 'lang': 'Telugu'},
    {'title': 'Ala Modalaindi', 'genre': 'Romantic Drama', 'year': 2011, 'rating': 7.6, 'platform': 'YouTube', 'lang': 'Telugu'},
    {'title': 'Pelli Choopulu', 'genre': 'Romantic Comedy', 'year': 2016, 'rating': 7.9, 'platform': 'Prime Video', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Dear Zindagi', 'genre': 'Drama', 'year': 2016, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Tamasha', 'genre': 'Romance/Drama', 'year': 2015, 'rating': 7.3, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Queen', 'genre': 'Comedy/Drama', 'year': 2013, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Zindagi Na Milegi Dobara', 'genre': 'Comedy/Drama', 'year': 2011, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
    # English
    {'title': 'Soul', 'genre': 'Animation/Drama', 'year': 2020, 'rating': 8.0, 'platform': 'Disney+'},
    {'title': 'Good Will Hunting', 'genre': 'Drama', 'year': 1997, 'rating': 8.3, 'platform': 'Netflix'},
    {'title': 'The Perks of Being a Wallflower', 'genre': 'Drama/Coming-of-age', 'year': 2012, 'rating': 8.0, 'platform': 'Netflix'},
    {'title': 'A Beautiful Mind', 'genre': 'Drama/Biography', 'year': 2001, 'rating': 8.2, 'platform': 'Netflix'},
    {'title': 'The Truman Show', 'genre': 'Comedy/Drama', 'year': 1998, 'rating': 8.1, 'platform': 'Netflix'},
    {'title': 'Into the Wild', 'genre': 'Drama/Adventure', 'year': 2007, 'rating': 8.1, 'platform': 'Netflix'},
    {'title': 'Cast Away', 'genre': 'Drama/Adventure', 'year': 2000, 'rating': 7.8, 'platform': 'Netflix'},
    {'title': 'The Secret Life of Walter Mitty', 'genre': 'Adventure/Comedy', 'year': 2013, 'rating': 7.3, 'platform': 'Netflix'},
    # Tamil
    {'title': 'Soorarai Pottru', 'genre': 'Drama', 'year': 2020, 'rating': 8.7, 'platform': 'Prime Video', 'lang': 'Tamil'},
    {'title': '96', 'genre': 'Romantic Drama', 'year': 2018, 'rating': 8.5, 'platform': 'Prime Video', 'lang': 'Tamil'},
    # Korean
    {'title': 'It\'s Okay to Not Be Okay', 'genre': 'Drama/Romance', 'year': 2020, 'rating': 8.6, 'platform': 'Netflix', 'lang': 'Korean'},
    {'title': 'My Mister', 'genre': 'Drama', 'year': 2018, 'rating': 9.0, 'platform': 'Netflix', 'lang': 'Korean'},
]
anxious_anime = [
    {'title': 'March Comes in Like a Lion', 'genre': 'Drama/Slice of Life', 'episodes': 22, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Welcome to the NHK', 'genre': 'Drama/Psychological', 'episodes': 24, 'rating': 8.3, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'A Silent Voice', 'genre': 'Drama', 'rating': 8.9, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': "Komi Can't Communicate", 'genre': 'Comedy/Slice of Life', 'episodes': 12, 'rating': 7.8, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'ReLIFE', 'genre': 'Romance/Sci-Fi', 'episodes': 13, 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'The Pet Girl of Sakurasou', 'genre': 'Romance/Comedy', 'episodes': 24, 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Serial Experiments Lain', 'genre': 'Sci-Fi/Psychological', 'episodes': 13, 'rating': 8.0, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Paranoia Agent', 'genre': 'Mystery/Psychological', 'episodes': 13, 'rating': 7.8, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'The Tatami Galaxy', 'genre': 'Comedy/Drama', 'episodes': 11, 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Ping Pong the Animation', 'genre': 'Sports/Drama', 'episodes': 11, 'rating': 8.6, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Boogiepop and Others', 'genre': 'Mystery/Psychological', 'episodes': 18, 'rating': 7.2, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Colorful', 'genre': 'Drama', 'rating': 7.7, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
]

# ============================================================
# MOTIVATED
# ============================================================
motivated_music = [
    # Telugu
    {'title': 'Rise Up', 'artist': 'Anirudh Ravichander', 'genre': 'Telugu Pop', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Jaragandi Jaragandi', 'artist': 'Thaman S', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Dangal Title Track', 'artist': 'Daler Mehndi', 'genre': 'Telugu/Bollywood', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Top Lechipoddi', 'artist': 'Thaman S', 'genre': 'Telugu Hype', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Brothers Anthem', 'artist': 'Vishal Dadlani', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Zinda', 'artist': 'Siddharth Mahadevan', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Bhaag Milkha Bhaag', 'artist': 'Siddharth Mahadevan', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Chak De India', 'artist': 'Sukhwinder Singh', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    # English
    {'title': 'Stronger', 'artist': 'Kanye West', 'genre': 'Hip Hop', 'platform': 'Spotify'},
    {'title': 'Remember the Name', 'artist': 'Fort Minor', 'genre': 'Hip Hop', 'platform': 'Spotify'},
    {'title': 'Till I Collapse', 'artist': 'Eminem', 'genre': 'Hip Hop', 'platform': 'Spotify'},
    {'title': 'Power', 'artist': 'Kanye West', 'genre': 'Hip Hop', 'platform': 'Spotify'},
    {'title': 'Unstoppable', 'artist': 'Sia', 'genre': 'Pop', 'platform': 'Spotify'},
    {'title': 'Hall of Fame', 'artist': 'The Script', 'genre': 'Pop Rock', 'platform': 'Spotify'},
    {'title': 'Gonna Fly Now', 'artist': 'Bill Conti', 'genre': 'Soundtrack', 'platform': 'Spotify'},
    {'title': 'Lose Yourself', 'artist': 'Eminem', 'genre': 'Hip Hop', 'platform': 'Spotify'},
    # Tamil
    {'title': 'Vaathi Coming', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Dance', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Vikram Theme', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Mass', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Beast Mode', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Hype', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Aaluma Doluma', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Mass', 'platform': 'JioSaavn', 'lang': 'Tamil'},
]
motivated_movies = [
    # Telugu
    {'title': 'Maharshi', 'genre': 'Drama', 'year': 2019, 'rating': 7.2, 'platform': 'Prime Video', 'lang': 'Telugu'},
    {'title': 'Guru', 'genre': 'Drama/Biography', 'year': 2007, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'Nani\'s Gang Leader', 'genre': 'Action/Comedy', 'year': 2019, 'rating': 7.2, 'platform': 'Netflix', 'lang': 'Telugu'},
    {'title': 'Krishna Vrinda Vihari', 'genre': 'Comedy/Drama', 'year': 2022, 'rating': 6.8, 'platform': 'Netflix', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Dangal', 'genre': 'Sports/Drama', 'year': 2016, 'rating': 8.4, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Bhaag Milkha Bhaag', 'genre': 'Sports/Biography', 'year': 2013, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Chak De! India', 'genre': 'Sports/Drama', 'year': 2007, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Lakshya', 'genre': 'War/Drama', 'year': 2004, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Hindi'},
    # English
    {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'year': 1994, 'rating': 9.3, 'platform': 'Netflix'},
    {'title': 'Rocky', 'genre': 'Sports/Drama', 'year': 1976, 'rating': 8.1, 'platform': 'Netflix'},
    {'title': 'Whiplash', 'genre': 'Drama/Music', 'year': 2014, 'rating': 8.5, 'platform': 'Netflix'},
    {'title': 'The Wolf of Wall Street', 'genre': 'Drama/Comedy', 'year': 2013, 'rating': 8.2, 'platform': 'Netflix'},
    {'title': 'The Pursuit of Happyness', 'genre': 'Drama', 'year': 2006, 'rating': 8.0, 'platform': 'Netflix'},
    {'title': 'Moneyball', 'genre': 'Sports/Drama', 'year': 2011, 'rating': 7.6, 'platform': 'Netflix'},
    {'title': 'Slumdog Millionaire', 'genre': 'Drama/Romance', 'year': 2008, 'rating': 8.0, 'platform': 'Netflix'},
    {'title': 'The Social Network', 'genre': 'Drama/Biography', 'year': 2010, 'rating': 7.7, 'platform': 'Netflix'},
    # Tamil
    {'title': 'Soorarai Pottru', 'genre': 'Drama', 'year': 2020, 'rating': 8.7, 'platform': 'Prime Video', 'lang': 'Tamil'},
    {'title': 'Master', 'genre': 'Action/Thriller', 'year': 2021, 'rating': 7.2, 'platform': 'Prime Video', 'lang': 'Tamil'},
    # Korean
    {'title': 'Miracle in Cell No. 7', 'genre': 'Drama/Comedy', 'year': 2013, 'rating': 8.2, 'platform': 'Netflix', 'lang': 'Korean'},
    {'title': '1987: When the Day Comes', 'genre': 'Drama/History', 'year': 2017, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Korean'},
]
motivated_anime = [
    {'title': 'Haikyuu!!', 'genre': 'Sports', 'episodes': 25, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Blue Lock', 'genre': 'Sports', 'episodes': 24, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'One Punch Man', 'genre': 'Action/Comedy', 'episodes': 12, 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Megalo Box', 'genre': 'Sports/Sci-Fi', 'episodes': 13, 'rating': 7.7, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Run with the Wind', 'genre': 'Sports/Drama', 'episodes': 23, 'rating': 8.3, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Rising of the Shield Hero', 'genre': 'Action/Isekai', 'episodes': 25, 'rating': 8.0, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Hajime no Ippo', 'genre': 'Sports', 'episodes': 76, 'rating': 8.7, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Diamond no Ace', 'genre': 'Sports', 'episodes': 75, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Bakuman', 'genre': 'Comedy/Drama', 'episodes': 25, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Assassination Classroom', 'genre': 'Action/Comedy', 'episodes': 22, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Major', 'genre': 'Sports', 'episodes': 154, 'rating': 8.2, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'The Royal Tutor', 'genre': 'Comedy', 'episodes': 12, 'rating': 7.3, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
]

# ============================================================
# MELANCHOLY
# ============================================================
melancholy_music = [
    # Telugu
    {'title': 'Adiga Adiga', 'artist': 'Sid Sriram', 'genre': 'Telugu Soulful', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Entho Ento', 'artist': 'Sid Sriram', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Ninne Ninne', 'artist': 'Sid Sriram', 'genre': 'Telugu Soulful', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    {'title': 'Kanulanu Thaake', 'artist': 'Sid Sriram', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Tujhe Bhula Diya', 'artist': 'Mohit Chauhan', 'genre': 'Bollywood Sad', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Channa Mereya', 'artist': 'Arijit Singh', 'genre': 'Bollywood Sad', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Kabira', 'artist': 'Arijit Singh', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    {'title': 'Phir Le Aaya Dil', 'artist': 'Arijit Singh', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
    # English
    {'title': 'The Night We Met', 'artist': 'Lord Huron', 'genre': 'Indie Folk', 'platform': 'Spotify'},
    {'title': 'Exit Music (For a Film)', 'artist': 'Radiohead', 'genre': 'Alt Rock', 'platform': 'Spotify'},
    {'title': 'How to Disappear Completely', 'artist': 'Radiohead', 'genre': 'Alt Rock', 'platform': 'Spotify'},
    {'title': 'Space Song', 'artist': 'Beach House', 'genre': 'Dream Pop', 'platform': 'Spotify'},
    {'title': 'Cherry Wine', 'artist': 'Hozier', 'genre': 'Indie Folk', 'platform': 'Spotify'},
    {'title': 'My Immortal', 'artist': 'Evanescence', 'genre': 'Alt Rock', 'platform': 'Spotify'},
    {'title': 'Youth', 'artist': 'Daughter', 'genre': 'Indie Folk', 'platform': 'Spotify'},
    {'title': 'Wish You Were Here', 'artist': 'Pink Floyd', 'genre': 'Rock', 'platform': 'Spotify'},
    # Tamil
    {'title': 'Nenjukulle', 'artist': 'AR Rahman', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Munbe Vaa', 'artist': 'Shreya Ghoshal', 'genre': 'Tamil Romantic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Kannalane', 'artist': 'AR Rahman', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
    {'title': 'Venmegam', 'artist': 'Harris Jayaraj', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
]
melancholy_movies = [
    # Telugu
    {'title': 'Ala Modalaindi', 'genre': 'Romantic Drama', 'year': 2011, 'rating': 7.6, 'platform': 'YouTube', 'lang': 'Telugu'},
    {'title': 'Lakshmi', 'genre': 'Drama', 'year': 2018, 'rating': 7.3, 'platform': 'YouTube', 'lang': 'Telugu'},
    {'title': 'Premam', 'genre': 'Romantic Drama', 'year': 2015, 'rating': 7.8, 'platform': 'Hotstar', 'lang': 'Telugu'},
    {'title': 'Hi Nanna', 'genre': 'Romantic Drama', 'year': 2023, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Telugu'},
    # Hindi
    {'title': 'Rockstar', 'genre': 'Romance/Music', 'year': 2011, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Tamasha', 'genre': 'Romance/Drama', 'year': 2015, 'rating': 7.3, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Aashiqui 2', 'genre': 'Romantic Drama', 'year': 2013, 'rating': 7.0, 'platform': 'Netflix', 'lang': 'Hindi'},
    {'title': 'Anand', 'genre': 'Drama', 'year': 1971, 'rating': 8.8, 'platform': 'YouTube', 'lang': 'Hindi'},
    # English
    {'title': 'Eternal Sunshine of the Spotless Mind', 'genre': 'Sci-Fi/Romance', 'year': 2004, 'rating': 8.3, 'platform': 'Netflix'},
    {'title': 'Her', 'genre': 'Sci-Fi/Romance', 'year': 2013, 'rating': 8.0, 'platform': 'Netflix'},
    {'title': 'Blade Runner 2049', 'genre': 'Sci-Fi/Drama', 'year': 2017, 'rating': 8.0, 'platform': 'Netflix'},
    {'title': 'Call Me by Your Name', 'genre': 'Romance/Drama', 'year': 2017, 'rating': 7.9, 'platform': 'Netflix'},
    {'title': 'Manchester by the Sea', 'genre': 'Drama', 'year': 2016, 'rating': 7.8, 'platform': 'Netflix'},
    {'title': 'A Star Is Born', 'genre': 'Drama/Music', 'year': 2018, 'rating': 7.6, 'platform': 'Netflix'},
    {'title': 'Blue Valentine', 'genre': 'Romance/Drama', 'year': 2010, 'rating': 7.4, 'platform': 'Netflix'},
    {'title': 'The Fault in Our Stars', 'genre': 'Romance/Drama', 'year': 2014, 'rating': 7.7, 'platform': 'Netflix'},
    # Tamil
    {'title': '96', 'genre': 'Romantic Drama', 'year': 2018, 'rating': 8.5, 'platform': 'Prime Video', 'lang': 'Tamil'},
    {'title': 'Vinnaithaandi Varuvaayaa', 'genre': 'Romantic Drama', 'year': 2010, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Tamil'},
    # Korean
    {'title': 'A Moment to Remember', 'genre': 'Romance/Drama', 'year': 2004, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Korean'},
    {'title': 'Always', 'genre': 'Romance/Drama', 'year': 2011, 'rating': 7.5, 'platform': 'Netflix', 'lang': 'Korean'},
]
melancholy_anime = [
    {'title': 'Plastic Memories', 'genre': 'Sci-Fi/Romance', 'episodes': 13, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Angel Beats!', 'genre': 'Action/Drama', 'episodes': 13, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Erased', 'genre': 'Mystery/Drama', 'episodes': 12, 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': '5 Centimeters per Second', 'genre': 'Romance/Drama', 'rating': 7.6, 'platform': 'Netflix', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Maquia', 'genre': 'Fantasy/Drama', 'rating': 8.0, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'The Wind Rises', 'genre': 'Drama/Romance', 'rating': 7.8, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Whisper of the Heart', 'genre': 'Romance/Drama', 'rating': 7.8, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Only Yesterday', 'genre': 'Drama/Slice of Life', 'rating': 7.7, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'In This Corner of the World', 'genre': 'Drama/War', 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Hotarubi no Mori e', 'genre': 'Romance/Fantasy', 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
    {'title': 'Grave of the Fireflies', 'genre': 'Drama/War', 'rating': 8.5, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
    {'title': 'Colorful', 'genre': 'Drama', 'rating': 7.7, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
]


# ============================================================
# ASSEMBLE AND SEED
# ============================================================
data = {
    'happy': {'music': happy_music, 'movies': happy_movies, 'anime': happy_anime},
    'sad': {'music': sad_music, 'movies': sad_movies, 'anime': sad_anime},
    'energetic': {'music': energetic_music, 'movies': energetic_movies, 'anime': energetic_anime},
    'calm': {'music': calm_music, 'movies': calm_movies, 'anime': calm_anime},
    'romantic': {'music': romantic_music, 'movies': romantic_movies, 'anime': romantic_anime},
    'angry': {'music': angry_music, 'movies': angry_movies, 'anime': angry_anime},
    'nostalgic': {'music': nostalgic_music, 'movies': nostalgic_movies, 'anime': nostalgic_anime},
    'anxious': {'music': anxious_music, 'movies': anxious_movies, 'anime': anxious_anime},
    'motivated': {'music': motivated_music, 'movies': motivated_movies, 'anime': motivated_anime},
    'melancholy': {'music': melancholy_music, 'movies': melancholy_movies, 'anime': melancholy_anime},
}

print('Dropping existing recommendations...')
col.drop()

docs = []
for mood, categories in data.items():
    for category, items in categories.items():
        for item in items:
            item['mood'] = mood
            item['category'] = category
            item['url'] = mkurl(item['platform'], item['title'], item.get('artist'))
            docs.append(item)

col.insert_many(docs)

# Count by language
langs = {}
for d in docs:
    lang = d.get('lang', 'English')
    langs[lang] = langs.get(lang, 0) + 1

print(f'\nSeeded {len(docs)} recommendations')
print(f'  - {sum(1 for d in docs if d["category"] == "music")} music')
print(f'  - {sum(1 for d in docs if d["category"] == "movies")} movies')
print(f'  - {sum(1 for d in docs if d["category"] == "anime")} anime')
print(f'\nBy language:')
for lang, count in sorted(langs.items(), key=lambda x: -x[1]):
    print(f'  - {lang}: {count}')
