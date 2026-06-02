"""
Add more recommendations to existing database — NO DROP, only inserts
Target: 25+ music, 25+ movies, 20+ anime per mood across all languages
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


extra = {
    'happy': {
        'music': [
            # More Telugu
            {'title': 'Ramuloo Ramulaa', 'artist': 'Thaman S', 'genre': 'Telugu Dance', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Saami Saami', 'artist': 'DSP', 'genre': 'Telugu Dance', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Mind Block', 'artist': 'Thaman S', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Pilla Raa', 'artist': 'Anup Rubens', 'genre': 'Telugu Pop', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Nashe Si Chadh Gayi', 'artist': 'Arijit Singh', 'genre': 'Bollywood Dance', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'The Breakup Song', 'artist': 'Arijit Singh', 'genre': 'Bollywood Dance', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Abhi Toh Party Shuru Hui Hai', 'artist': 'Badshah', 'genre': 'Bollywood Dance', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Cutiepie', 'artist': 'Nakash Aziz', 'genre': 'Bollywood Pop', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Kala Chashma', 'artist': 'Badshah', 'genre': 'Bollywood Dance', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            # More English
            {'title': 'On Top of the World', 'artist': 'Imagine Dragons', 'genre': 'Alt Rock', 'platform': 'Spotify'},
            {'title': 'Best Day of My Life', 'artist': 'American Authors', 'genre': 'Indie Pop', 'platform': 'Spotify'},
            {'title': 'Sugar', 'artist': 'Maroon 5', 'genre': 'Pop', 'platform': 'Spotify'},
            {'title': 'Party in the USA', 'artist': 'Miley Cyrus', 'genre': 'Pop', 'platform': 'Spotify'},
            {'title': 'Good Feeling', 'artist': 'Flo Rida', 'genre': 'Pop/Hip Hop', 'platform': 'Spotify'},
            {'title': 'Treasure', 'artist': 'Bruno Mars', 'genre': 'Pop/Funk', 'platform': 'Spotify'},
            # More Tamil
            {'title': 'Arabic Kuthu', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Dance', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            {'title': 'Chellamma', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Pop', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            {'title': 'Enjoy Enjaami', 'artist': 'Dhee', 'genre': 'Tamil Indie', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            # Korean
            {'title': 'Dynamite', 'artist': 'BTS', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Butter', 'artist': 'BTS', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Boy With Luv', 'artist': 'BTS', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'TT', 'artist': 'TWICE', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Feel My Rhythm', 'artist': 'Red Velvet', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
        ],
        'movies': [
            # More Telugu
            {'title': 'Raja The Great', 'genre': 'Action/Comedy', 'year': 2017, 'rating': 6.8, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'F2: Fun and Frustration', 'genre': 'Comedy', 'year': 2019, 'rating': 6.9, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Bheeshma', 'genre': 'Action/Comedy', 'year': 2020, 'rating': 6.7, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Jathi Ratnalu', 'genre': 'Comedy', 'year': 2021, 'rating': 7.4, 'platform': 'Prime Video', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Munna Bhai M.B.B.S.', 'genre': 'Comedy/Drama', 'year': 2003, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Hera Pheri', 'genre': 'Comedy', 'year': 2000, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Chhichhore', 'genre': 'Comedy/Drama', 'year': 2019, 'rating': 8.2, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Bajrangi Bhaijaan', 'genre': 'Drama/Comedy', 'year': 2015, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
            # More English
            {'title': 'The Intern', 'genre': 'Comedy/Drama', 'year': 2015, 'rating': 7.1, 'platform': 'Netflix'},
            {'title': 'The Truman Show', 'genre': 'Comedy/Drama', 'year': 1998, 'rating': 8.1, 'platform': 'Netflix'},
            {'title': 'Ratatouille', 'genre': 'Animation/Comedy', 'year': 2007, 'rating': 8.1, 'platform': 'Disney+'},
            {'title': 'The Princess Bride', 'genre': 'Fantasy/Comedy', 'year': 1987, 'rating': 8.1, 'platform': 'Disney+'},
            {'title': 'School of Rock', 'genre': 'Comedy/Music', 'year': 2003, 'rating': 7.1, 'platform': 'Netflix'},
            {'title': 'Legally Blonde', 'genre': 'Comedy', 'year': 2001, 'rating': 6.4, 'platform': 'Netflix'},
            # More Tamil
            {'title': 'Comali', 'genre': 'Comedy/Drama', 'year': 2019, 'rating': 7.2, 'platform': 'Prime Video', 'lang': 'Tamil'},
            {'title': 'Kaththi', 'genre': 'Action/Drama', 'year': 2014, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Tamil'},
            {'title': 'Thuppakki', 'genre': 'Action/Thriller', 'year': 2012, 'rating': 7.5, 'platform': 'Netflix', 'lang': 'Tamil'},
            # More Korean
            {'title': 'Extreme Job', 'genre': 'Action/Comedy', 'year': 2019, 'rating': 7.1, 'platform': 'Netflix', 'lang': 'Korean'},
            {'title': 'Midnight Runners', 'genre': 'Action/Comedy', 'year': 2017, 'rating': 7.2, 'platform': 'Netflix', 'lang': 'Korean'},
        ],
        'anime': [
            {'title': 'Hinamatsuri', 'genre': 'Comedy/Sci-Fi', 'episodes': 12, 'rating': 8.0, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Grand Blue Dreaming', 'genre': 'Comedy', 'episodes': 12, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Asobi Asobase', 'genre': 'Comedy', 'episodes': 12, 'rating': 8.0, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Saiki K.', 'genre': 'Comedy/Supernatural', 'episodes': 120, 'rating': 8.4, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'The Disastrous Life of Saiki K.', 'genre': 'Comedy', 'episodes': 24, 'rating': 8.4, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Bocchi the Rock!', 'genre': 'Music/Comedy', 'episodes': 12, 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
        ],
    },
    'sad': {
        'music': [
            # More Telugu
            {'title': 'Oosupodu', 'artist': 'Karthik', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Yemaindi Ee Vela', 'artist': 'Karthik', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Nuvvu Nenu', 'artist': 'SP Balasubrahmanyam', 'genre': 'Telugu Classic', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Inthena Inthena', 'artist': 'Sid Sriram', 'genre': 'Telugu Soulful', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Hamari Adhuri Kahani', 'artist': 'Arijit Singh', 'genre': 'Bollywood Sad', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Phir Mohabbat', 'artist': 'Arijit Singh', 'genre': 'Bollywood Sad', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Muskurane', 'artist': 'Arijit Singh', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Tera Ban Jaunga', 'artist': 'Akhil Sachdeva', 'genre': 'Bollywood Romantic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            # More English
            {'title': 'When I Was Your Man', 'artist': 'Bruno Mars', 'genre': 'Pop/R&B', 'platform': 'Spotify'},
            {'title': 'Say Something', 'artist': 'A Great Big World', 'genre': 'Pop', 'platform': 'Spotify'},
            {'title': 'Jealous', 'artist': 'Labrinth', 'genre': 'R&B', 'platform': 'Spotify'},
            {'title': 'Before You Go', 'artist': 'Lewis Capaldi', 'genre': 'Pop', 'platform': 'Spotify'},
            {'title': 'Yesterday', 'artist': 'The Beatles', 'genre': 'Rock', 'platform': 'Spotify'},
            {'title': 'Nothing Compares 2 U', 'artist': "Sinéad O'Connor", 'genre': 'Pop', 'platform': 'Spotify'},
            # More Tamil
            {'title': 'Po Nee Po', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            {'title': 'Aaromale', 'artist': 'Alphons Joseph', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            # Korean
            {'title': 'Spring Day', 'artist': 'BTS', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Through the Night', 'artist': 'IU', 'genre': 'K-Pop Ballad', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'If You', 'artist': 'BIGBANG', 'genre': 'K-Pop Ballad', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Dear Name', 'artist': 'IU', 'genre': 'K-Pop Ballad', 'platform': 'Spotify', 'lang': 'Korean'},
        ],
        'movies': [
            # More Telugu
            {'title': 'Nandini Nursing Home', 'genre': 'Drama', 'year': 2016, 'rating': 6.8, 'platform': 'YouTube', 'lang': 'Telugu'},
            {'title': 'Oopiri', 'genre': 'Drama/Comedy', 'year': 2016, 'rating': 8.0, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Manam', 'genre': 'Drama/Fantasy', 'year': 2014, 'rating': 8.0, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Anand', 'genre': 'Romantic Drama', 'year': 2004, 'rating': 7.5, 'platform': 'YouTube', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Kal Ho Naa Ho', 'genre': 'Romance/Drama', 'year': 2003, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'My Name Is Khan', 'genre': 'Drama', 'year': 2010, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Devdas', 'genre': 'Romance/Drama', 'year': 2002, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Haider', 'genre': 'Drama/Thriller', 'year': 2014, 'rating': 8.0, 'platform': 'Netflix', 'lang': 'Hindi'},
            # More English
            {'title': 'Schindler\'s List', 'genre': 'Drama/History', 'year': 1993, 'rating': 8.9, 'platform': 'Netflix'},
            {'title': 'Marley & Me', 'genre': 'Comedy/Drama', 'year': 2008, 'rating': 7.1, 'platform': 'Netflix'},
            {'title': 'The Notebook', 'genre': 'Romance/Drama', 'year': 2004, 'rating': 7.8, 'platform': 'Netflix'},
            {'title': 'If Beale Street Could Talk', 'genre': 'Drama/Romance', 'year': 2018, 'rating': 7.1, 'platform': 'Netflix'},
            # More Tamil
            {'title': 'Raja Rani', 'genre': 'Romantic Drama', 'year': 2013, 'rating': 7.4, 'platform': 'Hotstar', 'lang': 'Tamil'},
            {'title': 'Vaaranam Aayiram', 'genre': 'Drama/Romance', 'year': 2008, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Tamil'},
            # More Korean
            {'title': 'The Beauty Inside', 'genre': 'Romance/Fantasy', 'year': 2015, 'rating': 7.5, 'platform': 'Netflix', 'lang': 'Korean'},
            {'title': 'On Your Wedding Day', 'genre': 'Romance/Drama', 'year': 2018, 'rating': 7.3, 'platform': 'Netflix', 'lang': 'Korean'},
        ],
        'anime': [
            {'title': 'Rascal Does Not Dream of Bunny Girl Senpai', 'genre': 'Romance/Supernatural', 'episodes': 13, 'rating': 8.2, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Re:Zero', 'genre': 'Isekai/Drama', 'episodes': 25, 'rating': 8.2, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Steins;Gate', 'genre': 'Sci-Fi/Drama', 'episodes': 24, 'rating': 8.8, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Tokyo Magnitude 8.0', 'genre': 'Drama/Disaster', 'episodes': 11, 'rating': 7.7, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Ef: A Tale of Memories', 'genre': 'Romance/Drama', 'episodes': 12, 'rating': 7.8, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Now and Then, Here and There', 'genre': 'Sci-Fi/Drama', 'episodes': 13, 'rating': 7.8, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
        ],
    },
    'energetic': {
        'music': [
            # More Telugu
            {'title': 'Butta Bomma', 'artist': 'Thaman S', 'genre': 'Telugu Dance', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Ramuloo Ramulaa', 'artist': 'Thaman S', 'genre': 'Telugu Dance', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Mind Block', 'artist': 'Thaman S', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Blockbuster', 'artist': 'Devi Sri Prasad', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Malhari', 'artist': 'Vishal Dadlani', 'genre': 'Bollywood Mass', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Diljit Dosanjh - Born to Shine', 'artist': 'Diljit Dosanjh', 'genre': 'Punjabi Pop', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Naina Da Kya Kasoor', 'artist': 'Amit Trivedi', 'genre': 'Bollywood Pop', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Ainvayi Ainvayi', 'artist': 'Salim-Sulaiman', 'genre': 'Bollywood Dance', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            # More English
            {'title': 'Pump It', 'artist': 'Black Eyed Peas', 'genre': 'Pop/Hip Hop', 'platform': 'Spotify'},
            {'title': 'Bangarang', 'artist': 'Skrillex', 'genre': 'EDM', 'platform': 'Spotify'},
            {'title': 'Warriors', 'artist': 'Imagine Dragons', 'genre': 'Alt Rock', 'platform': 'Spotify'},
            {'title': "X Gon' Give It to Ya", 'artist': 'DMX', 'genre': 'Hip Hop', 'platform': 'Spotify'},
            {'title': 'Stronger', 'artist': 'Kanye West', 'genre': 'Hip Hop', 'platform': 'Spotify'},
            {'title': 'Run This Town', 'artist': 'Jay-Z', 'genre': 'Hip Hop', 'platform': 'Spotify'},
            # More Tamil
            {'title': 'Arabic Kuthu', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Dance', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            {'title': 'Jalabulajangu', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Dance', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            # Korean
            {'title': 'Idol', 'artist': 'BTS', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Fire', 'artist': 'BTS', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Ddu-Du Ddu-Du', 'artist': 'BLACKPINK', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'How You Like That', 'artist': 'BLACKPINK', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'God\'s Menu', 'artist': 'Stray Kids', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
        ],
        'movies': [
            # More Telugu
            {'title': 'Baahubali 2: The Conclusion', 'genre': 'Action/Fantasy', 'year': 2017, 'rating': 8.2, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Sye Raa Narasimha Reddy', 'genre': 'Action/History', 'year': 2019, 'rating': 6.8, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Akhanda', 'genre': 'Action/Drama', 'year': 2021, 'rating': 6.5, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Ala Vaikunthapurramuloo', 'genre': 'Action/Comedy', 'year': 2020, 'rating': 7.3, 'platform': 'Netflix', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Pathaan', 'genre': 'Action/Thriller', 'year': 2023, 'rating': 6.5, 'platform': 'Prime Video', 'lang': 'Hindi'},
            {'title': 'Bang Bang', 'genre': 'Action/Thriller', 'year': 2014, 'rating': 5.6, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Don', 'genre': 'Action/Thriller', 'year': 2006, 'rating': 6.5, 'platform': 'Netflix', 'lang': 'Hindi'},
            # More English
            {'title': 'Baby Driver', 'genre': 'Action/Crime', 'year': 2017, 'rating': 7.6, 'platform': 'Netflix'},
            {'title': 'Fast Five', 'genre': 'Action/Crime', 'year': 2011, 'rating': 7.3, 'platform': 'Netflix'},
            {'title': 'The Matrix', 'genre': 'Sci-Fi/Action', 'year': 1999, 'rating': 8.7, 'platform': 'Netflix'},
            {'title': 'Deadpool', 'genre': 'Action/Comedy', 'year': 2016, 'rating': 8.0, 'platform': 'Disney+'},
            # More Tamil
            {'title': 'Vikram', 'genre': 'Action/Thriller', 'year': 2022, 'rating': 7.6, 'platform': 'Hotstar', 'lang': 'Tamil'},
            {'title': 'Beast', 'genre': 'Action/Comedy', 'year': 2022, 'rating': 5.8, 'platform': 'Netflix', 'lang': 'Tamil'},
            {'title': 'Mankatha', 'genre': 'Action/Thriller', 'year': 2011, 'rating': 7.5, 'platform': 'Netflix', 'lang': 'Tamil'},
            # Korean
            {'title': 'Snowpiercer', 'genre': 'Sci-Fi/Action', 'year': 2013, 'rating': 7.1, 'platform': 'Netflix', 'lang': 'Korean'},
            {'title': 'The Villainess', 'genre': 'Action/Thriller', 'year': 2017, 'rating': 6.6, 'platform': 'Netflix', 'lang': 'Korean'},
        ],
        'anime': [
            {'title': 'Dragon Ball Super', 'genre': 'Action/Adventure', 'episodes': 131, 'rating': 7.8, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Fairy Tail', 'genre': 'Action/Fantasy', 'episodes': 175, 'rating': 7.7, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Black Clover', 'genre': 'Action/Fantasy', 'episodes': 170, 'rating': 7.8, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Sword Art Online', 'genre': 'Action/Sci-Fi', 'episodes': 25, 'rating': 7.5, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Bleach', 'genre': 'Action/Supernatural', 'episodes': 366, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Hunter x Hunter', 'genre': 'Action/Adventure', 'episodes': 148, 'rating': 9.0, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
        ],
    },
    'calm': {
        'music': [
            # More Telugu
            {'title': 'Ee Hridayam', 'artist': 'Karthik', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Ninne Ninne', 'artist': 'Sid Sriram', 'genre': 'Telugu Soulful', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Choosi Chudangane', 'artist': 'Sid Sriram', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Mellaga Tellarindoi', 'artist': 'Karthik', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Raabta', 'artist': 'Arijit Singh', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Tum Se Hi', 'artist': 'Mohit Chauhan', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Samjhawan', 'artist': 'Arijit Singh', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Gerua', 'artist': 'Arijit Singh', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            # More English
            {'title': 'Clair de Lune', 'artist': 'Debussy', 'genre': 'Classical', 'platform': 'Spotify'},
            {'title': 'Gymnopédie No.1', 'artist': 'Erik Satie', 'genre': 'Classical', 'platform': 'Spotify'},
            {'title': 'Strawberry Swing', 'artist': 'Coldplay', 'genre': 'Alt Rock', 'platform': 'Spotify'},
            {'title': 'Electric Feel', 'artist': 'MGMT', 'genre': 'Indie Pop', 'platform': 'Spotify'},
            {'title': 'Put Your Records On', 'artist': 'Corinne Bailey Rae', 'genre': 'Soul', 'platform': 'Spotify'},
            {'title': 'Tadow', 'artist': 'Masego', 'genre': 'R&B/Jazz', 'platform': 'Spotify'},
            # More Tamil
            {'title': 'Ennodu Nee Irundhaal', 'artist': 'Sid Sriram', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            {'title': 'Aagayam Theepidicha', 'artist': 'Pradeep Kumar', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            # Korean
            {'title': 'Eight', 'artist': 'IU', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Palette', 'artist': 'IU', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Star', 'artist': 'Heize', 'genre': 'K-Pop R&B', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Rain', 'artist': 'Taeyeon', 'genre': 'K-Pop Ballad', 'platform': 'Spotify', 'lang': 'Korean'},
        ],
        'movies': [
            # More Telugu
            {'title': 'Fidaa', 'genre': 'Romantic Drama', 'year': 2017, 'rating': 7.4, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Geetha Govindam', 'genre': 'Romantic Comedy', 'year': 2018, 'rating': 7.2, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Shatamanam Bhavati', 'genre': 'Family Drama', 'year': 2017, 'rating': 7.2, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Ninnu Kori', 'genre': 'Romantic Drama', 'year': 2017, 'rating': 7.3, 'platform': 'Netflix', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Barfi!', 'genre': 'Romance/Comedy', 'year': 2012, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Wake Up Sid', 'genre': 'Drama/Romance', 'year': 2009, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Yeh Jawaani Hai Deewani', 'genre': 'Romance/Drama', 'year': 2013, 'rating': 7.2, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Lootera', 'genre': 'Romance/Drama', 'year': 2013, 'rating': 7.4, 'platform': 'Netflix', 'lang': 'Hindi'},
            # More English
            {'title': 'Kiki\'s Delivery Service', 'genre': 'Animation/Fantasy', 'year': 1989, 'rating': 7.8, 'platform': 'Netflix'},
            {'title': 'The Sound of Music', 'genre': 'Musical/Drama', 'year': 1965, 'rating': 8.1, 'platform': 'Disney+'},
            {'title': 'Amélie', 'genre': 'Comedy/Romance', 'year': 2001, 'rating': 8.3, 'platform': 'Netflix'},
            {'title': 'The Secret Garden', 'genre': 'Fantasy/Drama', 'year': 2020, 'rating': 6.5, 'platform': 'Netflix'},
            # More Tamil
            {'title': 'Kadaikutty Singam', 'genre': 'Family Drama', 'year': 2018, 'rating': 6.8, 'platform': 'Hotstar', 'lang': 'Tamil'},
            {'title': 'Velaiilla Pattadhari', 'genre': 'Drama/Action', 'year': 2014, 'rating': 7.5, 'platform': 'Netflix', 'lang': 'Tamil'},
            # Korean
            {'title': 'Little Forest', 'genre': 'Drama/Slice of Life', 'year': 2018, 'rating': 7.5, 'platform': 'Netflix', 'lang': 'Korean'},
            {'title': 'The Poet and the Boy', 'genre': 'Drama/Comedy', 'year': 2017, 'rating': 7.0, 'platform': 'Netflix', 'lang': 'Korean'},
        ],
        'anime': [
            {'title': 'Spice and Wolf', 'genre': 'Romance/Adventure', 'episodes': 13, 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Usagi Drop', 'genre': 'Slice of Life', 'episodes': 11, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Barakamon', 'genre': 'Slice of Life/Comedy', 'episodes': 12, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Sweetness and Lightning', 'genre': 'Slice of Life', 'episodes': 12, 'rating': 7.5, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Laid-Back Camp', 'genre': 'Slice of Life', 'episodes': 12, 'rating': 8.3, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Natsume\'s Book of Friends Season 2', 'genre': 'Supernatural/Slice of Life', 'episodes': 13, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
        ],
    },
    'romantic': {
        'music': [
            # More Telugu
            {'title': 'Choosi Chudangane', 'artist': 'Sid Sriram', 'genre': 'Telugu Romantic', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Emai Poyave', 'artist': 'Radhan', 'genre': 'Telugu Indie', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Nee Kavitha', 'artist': 'Chaitan Bharadwaj', 'genre': 'Telugu Indie', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Mellaga Tellarindoi', 'artist': 'Karthik', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Tum Mile', 'artist': 'Neeraj Shridhar', 'genre': 'Bollywood Romantic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Hasi', 'artist': 'Ami Mishra', 'genre': 'Bollywood Romantic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Janam Janam', 'artist': 'Arijit Singh', 'genre': 'Bollywood Romantic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Main Rang Sharbaton Ka', 'artist': 'Atif Aslam', 'genre': 'Bollywood Romantic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            # More English
            {'title': 'At Last', 'artist': 'Etta James', 'genre': 'Jazz/Soul', 'platform': 'Spotify'},
            {'title': 'No One', 'artist': 'Alicia Keys', 'genre': 'R&B', 'platform': 'Spotify'},
            {'title': 'Just the Way You Are', 'artist': 'Billy Joel', 'genre': 'Pop', 'platform': 'Spotify'},
            {'title': 'Endless Love', 'artist': 'Lionel Richie', 'genre': 'R&B', 'platform': 'Spotify'},
            {'title': 'I Will Always Love You', 'artist': 'Whitney Houston', 'genre': 'Pop/Soul', 'platform': 'Spotify'},
            {'title': 'The Way You Look Tonight', 'artist': 'Frank Sinatra', 'genre': 'Jazz', 'platform': 'Spotify'},
            # More Tamil
            {'title': 'Uyire Uyire', 'artist': 'Anuradha Sriram', 'genre': 'Tamil Romantic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            {'title': 'Venmathiye', 'artist': 'Unni Menon', 'genre': 'Tamil Romantic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            # Korean
            {'title': 'Love Shot', 'artist': 'EXO', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'What is Love?', 'artist': 'TWICE', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Euphoria', 'artist': 'BTS', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Love Poem', 'artist': 'IU', 'genre': 'K-Pop Ballad', 'platform': 'Spotify', 'lang': 'Korean'},
        ],
        'movies': [
            # More Telugu
            {'title': 'Arya', 'genre': 'Romantic Drama', 'year': 2004, 'rating': 7.5, 'platform': 'YouTube', 'lang': 'Telugu'},
            {'title': 'Ye Maaya Chesave', 'genre': 'Romantic Drama', 'year': 2010, 'rating': 7.4, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Oohalu Gusagusalade', 'genre': 'Romantic Comedy', 'year': 2014, 'rating': 7.0, 'platform': 'YouTube', 'lang': 'Telugu'},
            {'title': 'Premam', 'genre': 'Romantic Drama', 'year': 2016, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Veer-Zaara', 'genre': 'Romance/Drama', 'year': 2004, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Mohabbatein', 'genre': 'Romance/Musical', 'year': 2000, 'rating': 7.0, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Hum Dil De Chuke Sanam', 'genre': 'Romance/Drama', 'year': 1999, 'rating': 7.5, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Kabhi Khushi Kabhie Gham', 'genre': 'Romance/Drama', 'year': 2001, 'rating': 7.4, 'platform': 'Netflix', 'lang': 'Hindi'},
            # More English
            {'title': 'To All the Boys I\'ve Loved Before', 'genre': 'Romance/Comedy', 'year': 2018, 'rating': 7.0, 'platform': 'Netflix'},
            {'title': 'The Vow', 'genre': 'Romance/Drama', 'year': 2012, 'rating': 6.7, 'platform': 'Netflix'},
            {'title': 'Sweet Home Alabama', 'genre': 'Romance/Comedy', 'year': 2002, 'rating': 6.2, 'platform': 'Netflix'},
            {'title': 'Sleepless in Seattle', 'genre': 'Romance/Comedy', 'year': 1993, 'rating': 6.8, 'platform': 'Netflix'},
            # More Tamil
            {'title': 'Minnale', 'genre': 'Romantic Drama', 'year': 2001, 'rating': 7.4, 'platform': 'YouTube', 'lang': 'Tamil'},
            {'title': 'Alaipayuthey', 'genre': 'Romantic Drama', 'year': 2000, 'rating': 8.0, 'platform': 'Netflix', 'lang': 'Tamil'},
            # Korean
            {'title': 'Architecture 101', 'genre': 'Romance/Drama', 'year': 2012, 'rating': 7.3, 'platform': 'Netflix', 'lang': 'Korean'},
            {'title': 'Love 911', 'genre': 'Romance/Comedy', 'year': 2012, 'rating': 6.7, 'platform': 'Netflix', 'lang': 'Korean'},
        ],
        'anime': [
            {'title': 'Oreimo', 'genre': 'Romance/Comedy', 'episodes': 12, 'rating': 7.0, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Say "I Love You"', 'genre': 'Romance/Slice of Life', 'episodes': 13, 'rating': 7.4, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Romeo x Juliet', 'genre': 'Romance/Fantasy', 'episodes': 24, 'rating': 7.3, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Kamisama Kiss', 'genre': 'Romance/Supernatural', 'episodes': 13, 'rating': 7.8, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Special A', 'genre': 'Romance/Comedy', 'episodes': 24, 'rating': 7.3, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'My Little Monster', 'genre': 'Romance/Comedy', 'episodes': 13, 'rating': 7.5, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
        ],
    },
    'angry': {
        'music': [
            # More Telugu
            {'title': 'Saami Saami', 'artist': 'DSP', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Oo Antava', 'artist': 'Indravathi Chauhan', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Blockbuster', 'artist': 'Devi Sri Prasad', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Mass Biryani', 'artist': 'Thaman S', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Sultan', 'artist': 'Vishal Dadlani', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Dangal Title Track', 'artist': 'Daler Mehndi', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Ganpath', 'artist': 'Vishal Mishra', 'genre': 'Bollywood Mass', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            # More English
            {'title': 'Faint', 'artist': 'Linkin Park', 'genre': 'Alt Metal', 'platform': 'Spotify'},
            {'title': 'Du Hast', 'artist': 'Rammstein', 'genre': 'Industrial Metal', 'platform': 'Spotify'},
            {'title': 'Ace of Spades', 'artist': 'Motörhead', 'genre': 'Metal', 'platform': 'Spotify'},
            {'title': 'Bodies', 'artist': 'Drowning Pool', 'genre': 'Metal', 'platform': 'Spotify'},
            {'title': 'Warrior', 'artist': 'Disturbed', 'genre': 'Metal', 'platform': 'Spotify'},
            # More Tamil
            {'title': 'Vikram Theme', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Mass', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            {'title': 'Jalabulajangu', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Dance', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            # Korean
            {'title': 'Daechwita', 'artist': 'Agust D', 'genre': 'K-Pop Hip Hop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'UGH!', 'artist': 'BTS', 'genre': 'K-Pop Hip Hop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Mic Drop', 'artist': 'BTS', 'genre': 'K-Pop Hip Hop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Kick It', 'artist': 'NCT 127', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
        ],
        'movies': [
            # More Telugu
            {'title': 'Nayak', 'genre': 'Action/Drama', 'year': 2001, 'rating': 7.3, 'platform': 'YouTube', 'lang': 'Telugu'},
            {'title': 'Indra', 'genre': 'Action/Drama', 'year': 2002, 'rating': 7.0, 'platform': 'YouTube', 'lang': 'Telugu'},
            {'title': 'Chatrapathi', 'genre': 'Action/Drama', 'year': 2005, 'rating': 7.2, 'platform': 'YouTube', 'lang': 'Telugu'},
            {'title': 'Tiger Nageswara Rao', 'genre': 'Action/Thriller', 'year': 2023, 'rating': 6.0, 'platform': 'Netflix', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Singham', 'genre': 'Action/Drama', 'year': 2011, 'rating': 6.8, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Simmba', 'genre': 'Action/Comedy', 'year': 2018, 'rating': 6.0, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Rowdy Rathore', 'genre': 'Action/Comedy', 'year': 2012, 'rating': 5.5, 'platform': 'Netflix', 'lang': 'Hindi'},
            # More English
            {'title': 'John Wick: Chapter 2', 'genre': 'Action/Thriller', 'year': 2017, 'rating': 7.5, 'platform': 'Netflix'},
            {'title': 'The Equalizer', 'genre': 'Action/Thriller', 'year': 2014, 'rating': 7.2, 'platform': 'Netflix'},
            {'title': 'Wanted', 'genre': 'Action/Thriller', 'year': 2008, 'rating': 6.7, 'platform': 'Netflix'},
            # More Tamil
            {'title': 'Petta', 'genre': 'Action/Drama', 'year': 2019, 'rating': 7.2, 'platform': 'Netflix', 'lang': 'Tamil'},
            {'title': 'Jailer', 'genre': 'Action/Comedy', 'year': 2023, 'rating': 7.1, 'platform': 'Prime Video', 'lang': 'Tamil'},
            # Korean
            {'title': 'The Man from Nowhere', 'genre': 'Action/Thriller', 'year': 2010, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Korean'},
            {'title': 'A Bittersweet Life', 'genre': 'Action/Drama', 'year': 2005, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Korean'},
        ],
        'anime': [
            {'title': 'Afro Samurai', 'genre': 'Action', 'episodes': 5, 'rating': 7.4, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Drifters', 'genre': 'Action/Fantasy', 'episodes': 12, 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Inuyashiki', 'genre': 'Action/Sci-Fi', 'episodes': 11, 'rating': 7.5, 'platform': 'Amazon', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Gantz', 'genre': 'Action/Horror', 'episodes': 13, 'rating': 7.2, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Blade of the Immortal', 'genre': 'Action/Samurai', 'episodes': 24, 'rating': 7.2, 'platform': 'Amazon', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Basilisk', 'genre': 'Action/Ninja', 'episodes': 24, 'rating': 7.4, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
        ],
    },
    'nostalgic': {
        'music': [
            # More Telugu
            {'title': 'Muddabanthi Navvulo', 'artist': 'SP Balasubrahmanyam', 'genre': 'Telugu Classic', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Nee Navvule', 'artist': 'SP Balasubrahmanyam', 'genre': 'Telugu Classic', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Chilaka Yekkada', 'artist': 'SP Balasubrahmanyam', 'genre': 'Telugu Classic', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Tholi Prema', 'artist': 'SP Balasubrahmanyam', 'genre': 'Telugu Classic', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Ek Ladki Ko Dekha Toh Aisa Laga', 'artist': 'Kumar Sanu', 'genre': 'Bollywood Classic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Dil To Pagal Hai', 'artist': 'Udit Narayan', 'genre': 'Bollywood Classic', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Lag Ja Gale', 'artist': 'Lata Mangeshkar', 'genre': 'Bollywood Retro', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Chura Liya Hai Tumne', 'artist': 'Mohammed Rafi', 'genre': 'Bollywood Retro', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            # More English
            {'title': 'Summer of \'69', 'artist': 'Bryan Adams', 'genre': 'Rock', 'platform': 'Spotify'},
            {'title': 'Everybody Wants to Rule the World', 'artist': 'Tears for Fears', 'genre': 'Synth Pop', 'platform': 'Spotify'},
            {'title': 'Time After Time', 'artist': 'Cyndi Lauper', 'genre': 'Pop', 'platform': 'Spotify'},
            {'title': 'Video Killed the Radio Star', 'artist': 'The Buggles', 'genre': 'New Wave', 'platform': 'Spotify'},
            {'title': 'Livin\' on a Prayer', 'artist': 'Bon Jovi', 'genre': 'Rock', 'platform': 'Spotify'},
            {'title': 'Under Pressure', 'artist': 'Queen & David Bowie', 'genre': 'Rock', 'platform': 'Spotify'},
            # More Tamil
            {'title': 'Roja Roja', 'artist': 'SP Balasubrahmanyam', 'genre': 'Tamil Classic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            {'title': 'Kadhal Rojave', 'artist': 'SP Balasubrahmanyam', 'genre': 'Tamil Classic', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            # Korean
            {'title': 'I Believe', 'artist': 'Shinhwa', 'genre': 'K-Pop Classic', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Gee', 'artist': 'Girls\' Generation', 'genre': 'K-Pop Classic', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Sorry Sorry', 'artist': 'Super Junior', 'genre': 'K-Pop Classic', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Mirotic', 'artist': 'TVXQ', 'genre': 'K-Pop Classic', 'platform': 'Spotify', 'lang': 'Korean'},
        ],
        'movies': [
            # More Telugu
            {'title': 'Okkadu', 'genre': 'Action/Romance', 'year': 2003, 'rating': 7.3, 'platform': 'YouTube', 'lang': 'Telugu'},
            {'title': 'Athadu', 'genre': 'Action/Thriller', 'year': 2005, 'rating': 7.8, 'platform': 'YouTube', 'lang': 'Telugu'},
            {'title': 'Chatrapathi', 'genre': 'Action/Drama', 'year': 2005, 'rating': 7.2, 'platform': 'YouTube', 'lang': 'Telugu'},
            {'title': 'Magadheera', 'genre': 'Action/Fantasy', 'year': 2009, 'rating': 7.9, 'platform': 'YouTube', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Main Hoon Na', 'genre': 'Action/Comedy', 'year': 2004, 'rating': 7.0, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Dhoom', 'genre': 'Action/Thriller', 'year': 2004, 'rating': 6.6, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Mujhse Dosti Karoge!', 'genre': 'Romance/Drama', 'year': 2002, 'rating': 5.8, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Kabhi Alvida Naa Kehna', 'genre': 'Romance/Drama', 'year': 2006, 'rating': 6.2, 'platform': 'Netflix', 'lang': 'Hindi'},
            # More English
            {'title': 'The Karate Kid', 'genre': 'Drama/Action', 'year': 1984, 'rating': 7.3, 'platform': 'Netflix'},
            {'title': 'Ferris Bueller\'s Day Off', 'genre': 'Comedy', 'year': 1986, 'rating': 7.8, 'platform': 'Netflix'},
            {'title': 'The Goonies', 'genre': 'Adventure/Comedy', 'year': 1985, 'rating': 7.8, 'platform': 'Netflix'},
            {'title': 'Ghostbusters', 'genre': 'Comedy/Fantasy', 'year': 1984, 'rating': 7.8, 'platform': 'Netflix'},
            # More Tamil
            {'title': 'Gentleman', 'genre': 'Action/Thriller', 'year': 1993, 'rating': 7.5, 'platform': 'YouTube', 'lang': 'Tamil'},
            {'title': 'Indian', 'genre': 'Action/Drama', 'year': 1996, 'rating': 7.8, 'platform': 'YouTube', 'lang': 'Tamil'},
            # Korean
            {'title': 'My Sassy Girl', 'genre': 'Romance/Comedy', 'year': 2001, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Korean'},
            {'title': 'Taegukgi', 'genre': 'War/Drama', 'year': 2004, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Korean'},
        ],
        'anime': [
            {'title': 'Mobile Suit Gundam', 'genre': 'Mecha/Action', 'episodes': 43, 'rating': 7.8, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Ranma ½', 'genre': 'Comedy/Romance', 'episodes': 161, 'rating': 7.7, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Fist of the North Star', 'genre': 'Action', 'episodes': 152, 'rating': 7.8, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'City Hunter', 'genre': 'Action/Comedy', 'episodes': 51, 'rating': 7.8, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Urusei Yatsura', 'genre': 'Comedy/Sci-Fi', 'episodes': 195, 'rating': 7.6, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Dirty Pair', 'genre': 'Sci-Fi/Comedy', 'episodes': 26, 'rating': 7.2, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
        ],
    },
    'anxious': {
        'music': [
            # More Telugu
            {'title': 'Inthena Inthena', 'artist': 'Sid Sriram', 'genre': 'Telugu Soulful', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Choosi Chudangane', 'artist': 'Sid Sriram', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Ee Hridayam', 'artist': 'Karthik', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Kabira', 'artist': 'Arijit Singh', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Naina Da Kya Kasoor', 'artist': 'Amit Trivedi', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Iktara', 'artist': 'Amit Trivedi', 'genre': 'Bollywood Indie', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Kun Faya Kun', 'artist': 'AR Rahman', 'genre': 'Bollywood Sufi', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            # More English
            {'title': 'Unwell', 'artist': 'Matchbox Twenty', 'genre': 'Alt Rock', 'platform': 'Spotify'},
            {'title': 'Under the Bridge', 'artist': 'Red Hot Chili Peppers', 'genre': 'Alt Rock', 'platform': 'Spotify'},
            {'title': 'Scars to Your Beautiful', 'artist': 'Alessia Cara', 'genre': 'Pop', 'platform': 'Spotify'},
            {'title': 'Rise', 'artist': 'Eddie Vedder', 'genre': 'Rock', 'platform': 'Spotify'},
            {'title': 'Breathe (2 AM)', 'artist': 'Anna Nalick', 'genre': 'Pop/Alt', 'platform': 'Spotify'},
            # More Tamil
            {'title': 'Po Nee Po', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            {'title': 'Aaromale', 'artist': 'Alphons Joseph', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            # Korean
            {'title': 'Lonely', 'artist': '2NE1', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Breathe', 'artist': 'Lee Hi', 'genre': 'K-Pop R&B', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Can\'t Love You Anymore', 'artist': 'IU', 'genre': 'K-Pop R&B', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Blue', 'artist': 'BIGBANG', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
        ],
        'movies': [
            # More Telugu
            {'title': 'Ala Modalaindi', 'genre': 'Romantic Drama', 'year': 2011, 'rating': 7.6, 'platform': 'YouTube', 'lang': 'Telugu'},
            {'title': 'Arjun Reddy', 'genre': 'Romantic Drama', 'year': 2017, 'rating': 8.0, 'platform': 'Prime Video', 'lang': 'Telugu'},
            {'title': 'Premam', 'genre': 'Romantic Drama', 'year': 2016, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Udaan', 'genre': 'Drama', 'year': 2010, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Lakshmi', 'genre': 'Drama', 'year': 2014, 'rating': 7.5, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Black', 'genre': 'Drama', 'year': 2005, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Hindi'},
            # More English
            {'title': 'Inside Out 2', 'genre': 'Animation/Comedy', 'year': 2024, 'rating': 7.6, 'platform': 'Disney+'},
            {'title': 'Silver Linings Playbook', 'genre': 'Drama/Romance', 'year': 2012, 'rating': 7.7, 'platform': 'Netflix'},
            {'title': 'The Perks of Being a Wallflower', 'genre': 'Drama/Coming-of-age', 'year': 2012, 'rating': 8.0, 'platform': 'Netflix'},
            # More Tamil
            {'title': 'Vaaranam Aayiram', 'genre': 'Drama/Romance', 'year': 2008, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Tamil'},
            {'title': 'Aayirathil Oruvan', 'genre': 'Adventure/Drama', 'year': 2010, 'rating': 7.3, 'platform': 'YouTube', 'lang': 'Tamil'},
            # Korean
            {'title': 'My Mister', 'genre': 'Drama', 'year': 2018, 'rating': 9.0, 'platform': 'Netflix', 'lang': 'Korean'},
            {'title': 'Reply 1988', 'genre': 'Drama/Comedy', 'year': 2015, 'rating': 9.0, 'platform': 'Netflix', 'lang': 'Korean'},
        ],
        'anime': [
            {'title': 'Neon Genesis Evangelion', 'genre': 'Mecha/Psychological', 'episodes': 26, 'rating': 8.3, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Perfect Blue', 'genre': 'Psychological/Thriller', 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Paprika', 'genre': 'Sci-Fi/Psychological', 'rating': 8.1, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Texhnolyze', 'genre': 'Sci-Fi/Psychological', 'episodes': 22, 'rating': 7.5, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Haibane Renmei', 'genre': 'Fantasy/Drama', 'episodes': 13, 'rating': 8.0, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Kino\'s Journey', 'genre': 'Adventure/Philosophy', 'episodes': 13, 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
        ],
    },
    'motivated': {
        'music': [
            # More Telugu
            {'title': 'Blockbuster', 'artist': 'Devi Sri Prasad', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Mass Biryani', 'artist': 'Thaman S', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Mind Block', 'artist': 'Thaman S', 'genre': 'Telugu Mass', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Chak De India', 'artist': 'Sukhwinder Singh', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Lakshya Title Track', 'artist': 'Shankar Mahadevan', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Aashayein', 'artist': 'Salim Merchant', 'genre': 'Bollywood Inspirational', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Sultan Title Track', 'artist': 'Vishal Dadlani', 'genre': 'Bollywood Rock', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            # More English
            {'title': 'Started from the Bottom', 'artist': 'Drake', 'genre': 'Hip Hop', 'platform': 'Spotify'},
            {'title': 'All I Do Is Win', 'artist': 'DJ Khaled', 'genre': 'Hip Hop', 'platform': 'Spotify'},
            {'title': 'Champions', 'artist': 'Queen', 'genre': 'Rock', 'platform': 'Spotify'},
            {'title': 'We Will Rock You', 'artist': 'Queen', 'genre': 'Rock', 'platform': 'Spotify'},
            {'title': 'Born to Run', 'artist': 'Bruce Springsteen', 'genre': 'Rock', 'platform': 'Spotify'},
            # More Tamil
            {'title': 'VIP Title Track', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Rock', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            {'title': 'Ethir Neechal', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Pop', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            # Korean
            {'title': 'Not Today', 'artist': 'BTS', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'DNA', 'artist': 'BTS', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Power', 'artist': 'EXO', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Shine', 'artist': 'PENTAGON', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
        ],
        'movies': [
            # More Telugu
            {'title': 'Krishna Vrinda Vihari', 'genre': 'Comedy/Drama', 'year': 2022, 'rating': 6.8, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Vakeel Saab', 'genre': 'Drama/Thriller', 'year': 2021, 'rating': 6.5, 'platform': 'Prime Video', 'lang': 'Telugu'},
            {'title': 'Nani\'s Gang Leader', 'genre': 'Action/Comedy', 'year': 2019, 'rating': 7.2, 'platform': 'Netflix', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Lakshya', 'genre': 'War/Drama', 'year': 2004, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Iqbal', 'genre': 'Sports/Drama', 'year': 2005, 'rating': 8.0, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Mary Kom', 'genre': 'Sports/Biography', 'year': 2014, 'rating': 6.8, 'platform': 'Netflix', 'lang': 'Hindi'},
            # More English
            {'title': 'The Imitation Game', 'genre': 'Drama/Biography', 'year': 2014, 'rating': 8.0, 'platform': 'Netflix'},
            {'title': 'Hidden Figures', 'genre': 'Drama/Biography', 'year': 2016, 'rating': 7.8, 'platform': 'Netflix'},
            {'title': 'The Theory of Everything', 'genre': 'Drama/Biography', 'year': 2014, 'rating': 7.7, 'platform': 'Netflix'},
            {'title': 'Rush', 'genre': 'Sports/Drama', 'year': 2013, 'rating': 8.1, 'platform': 'Netflix'},
            # More Tamil
            {'title': 'Irudhi Suttru', 'genre': 'Sports/Drama', 'year': 2016, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Tamil'},
            {'title': 'Kanaa', 'genre': 'Sports/Drama', 'year': 2018, 'rating': 7.2, 'platform': 'Netflix', 'lang': 'Tamil'},
            # Korean
            {'title': 'Secretly Greatly', 'genre': 'Action/Comedy', 'year': 2013, 'rating': 7.0, 'platform': 'Netflix', 'lang': 'Korean'},
            {'title': 'The Attorney', 'genre': 'Drama/History', 'year': 2013, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Korean'},
        ],
        'anime': [
            {'title': 'Ping Pong the Animation', 'genre': 'Sports/Drama', 'episodes': 11, 'rating': 8.6, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Cross Game', 'genre': 'Sports/Romance', 'episodes': 50, 'rating': 8.5, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Chihayafuru', 'genre': 'Sports/Drama', 'episodes': 25, 'rating': 8.2, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Baby Steps', 'genre': 'Sports', 'episodes': 25, 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Initial D', 'genre': 'Sports/Racing', 'episodes': 26, 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Kuroko\'s Basketball', 'genre': 'Sports', 'episodes': 25, 'rating': 7.9, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
        ],
    },
    'melancholy': {
        'music': [
            # More Telugu
            {'title': 'Inthena Inthena', 'artist': 'Sid Sriram', 'genre': 'Telugu Soulful', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Choosi Chudangane', 'artist': 'Sid Sriram', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Ee Hridayam', 'artist': 'Karthik', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            {'title': 'Yemaindi Ee Vela', 'artist': 'Karthik', 'genre': 'Telugu Melody', 'platform': 'JioSaavn', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Agar Tum Saath Ho', 'artist': 'Arijit Singh', 'genre': 'Bollywood Sad', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Hamari Adhuri Kahani', 'artist': 'Arijit Singh', 'genre': 'Bollywood Sad', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Phir Mohabbat', 'artist': 'Arijit Singh', 'genre': 'Bollywood Sad', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            {'title': 'Muskurane', 'artist': 'Arijit Singh', 'genre': 'Bollywood Melody', 'platform': 'JioSaavn', 'lang': 'Hindi'},
            # More English
            {'title': 'Exile', 'artist': 'Taylor Swift', 'genre': 'Indie Folk', 'platform': 'Spotify'},
            {'title': 'Liability', 'artist': 'Lorde', 'genre': 'Pop', 'platform': 'Spotify'},
            {'title': 'Landslide', 'artist': 'Fleetwood Mac', 'genre': 'Rock', 'platform': 'Spotify'},
            {'title': 'The Blower\'s Daughter', 'artist': 'Damien Rice', 'genre': 'Folk', 'platform': 'Spotify'},
            {'title': 'Viva la Vida', 'artist': 'Coldplay', 'genre': 'Alt Rock', 'platform': 'Spotify'},
            {'title': 'Skinny Love', 'artist': 'Bon Iver', 'genre': 'Indie Folk', 'platform': 'Spotify'},
            # More Tamil
            {'title': 'Po Nee Po', 'artist': 'Anirudh Ravichander', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            {'title': 'Aaromale', 'artist': 'Alphons Joseph', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            {'title': 'Ennodu Nee Irundhaal', 'artist': 'Sid Sriram', 'genre': 'Tamil Melody', 'platform': 'JioSaavn', 'lang': 'Tamil'},
            # Korean
            {'title': 'Spring Day', 'artist': 'BTS', 'genre': 'K-Pop', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Through the Night', 'artist': 'IU', 'genre': 'K-Pop Ballad', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'If You', 'artist': 'BIGBANG', 'genre': 'K-Pop Ballad', 'platform': 'Spotify', 'lang': 'Korean'},
            {'title': 'Dear Name', 'artist': 'IU', 'genre': 'K-Pop Ballad', 'platform': 'Spotify', 'lang': 'Korean'},
        ],
        'movies': [
            # More Telugu
            {'title': 'Sita Ramam', 'genre': 'Romantic Drama', 'year': 2022, 'rating': 8.6, 'platform': 'Prime Video', 'lang': 'Telugu'},
            {'title': 'Hi Nanna', 'genre': 'Romantic Drama', 'year': 2023, 'rating': 7.9, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'Premam', 'genre': 'Romantic Drama', 'year': 2016, 'rating': 7.8, 'platform': 'Netflix', 'lang': 'Telugu'},
            {'title': 'October', 'genre': 'Romantic Drama', 'year': 2018, 'rating': 7.6, 'platform': 'Prime Video', 'lang': 'Telugu'},
            # More Hindi
            {'title': 'Aashiqui 2', 'genre': 'Romantic Drama', 'year': 2013, 'rating': 7.0, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Kabir Singh', 'genre': 'Romantic Drama', 'year': 2019, 'rating': 7.1, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Devdas', 'genre': 'Romance/Drama', 'year': 2002, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Hindi'},
            {'title': 'Lootera', 'genre': 'Romance/Drama', 'year': 2013, 'rating': 7.4, 'platform': 'Netflix', 'lang': 'Hindi'},
            # More English
            {'title': 'Lost in Translation', 'genre': 'Drama/Romance', 'year': 2003, 'rating': 7.7, 'platform': 'Netflix'},
            {'title': 'Her', 'genre': 'Sci-Fi/Romance', 'year': 2013, 'rating': 8.0, 'platform': 'Netflix'},
            {'title': 'Call Me by Your Name', 'genre': 'Romance/Drama', 'year': 2017, 'rating': 7.9, 'platform': 'Netflix'},
            {'title': 'Blue Valentine', 'genre': 'Romance/Drama', 'year': 2010, 'rating': 7.4, 'platform': 'Netflix'},
            # More Tamil
            {'title': '96', 'genre': 'Romantic Drama', 'year': 2018, 'rating': 8.5, 'platform': 'Prime Video', 'lang': 'Tamil'},
            {'title': 'Vinnaithaandi Varuvaayaa', 'genre': 'Romantic Drama', 'year': 2010, 'rating': 7.6, 'platform': 'Netflix', 'lang': 'Tamil'},
            # Korean
            {'title': 'A Moment to Remember', 'genre': 'Romance/Drama', 'year': 2004, 'rating': 8.1, 'platform': 'Netflix', 'lang': 'Korean'},
            {'title': 'Always', 'genre': 'Romance/Drama', 'year': 2011, 'rating': 7.5, 'platform': 'Netflix', 'lang': 'Korean'},
        ],
        'anime': [
            {'title': 'Anohana', 'genre': 'Drama', 'episodes': 11, 'rating': 8.3, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Clannad', 'genre': 'Romance/Drama', 'episodes': 24, 'rating': 8.2, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Clannad: After Story', 'genre': 'Romance/Drama', 'episodes': 24, 'rating': 8.9, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
            {'title': 'Your Lie in April', 'genre': 'Romance/Drama', 'episodes': 22, 'rating': 8.6, 'platform': 'Crunchyroll', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'Violet Evergarden', 'genre': 'Drama', 'episodes': 13, 'rating': 8.6, 'platform': 'Netflix', 'dub': 'Both', 'lang': 'Japanese'},
            {'title': 'March Comes in Like a Lion', 'genre': 'Drama/Slice of Life', 'episodes': 22, 'rating': 8.4, 'platform': 'Crunchyroll', 'dub': 'Sub', 'lang': 'Japanese'},
        ],
    },
}


# Insert extra items (skip duplicates by checking existing titles)
existing_titles = set()
for doc in col.find({}, {'title': 1, 'mood': 1, 'category': 1}):
    existing_titles.add((doc['title'], doc['mood'], doc['category']))

new_docs = []
skipped = 0
for mood, categories in extra.items():
    for category, items in categories.items():
        for item in items:
            key = (item['title'], mood, category)
            if key in existing_titles:
                skipped += 1
                continue
            item['mood'] = mood
            item['category'] = category
            item['url'] = mkurl(item['platform'], item['title'], item.get('artist'))
            new_docs.append(item)
            existing_titles.add(key)

if new_docs:
    col.insert_many(new_docs)

total = col.count_documents({})
print(f'Added {len(new_docs)} new recommendations (skipped {skipped} duplicates)')
print(f'Total in database: {total}')

# Count by language
langs = {}
for doc in col.find({}, {'lang': 1}):
    lang = doc.get('lang', 'English')
    langs[lang] = langs.get(lang, 0) + 1

print(f'\nBy language:')
for lang, count in sorted(langs.items(), key=lambda x: -x[1]):
    print(f'  - {lang}: {count}')
