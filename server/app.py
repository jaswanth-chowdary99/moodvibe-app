"""
MoodVibe — Flask Backend
Mood-based movie, music & anime recommender with MongoDB
"""

import os
import random
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

app = Flask(__name__, static_folder='../client/dist', static_url_path='')
CORS(app)

# MongoDB
client = MongoClient(os.environ.get('MONGO_URI'))
db = client['mood-recommender']
recommendations_col = db['recommendations']
history_col = db['moodhistories']

# Mood metadata
MOODS = {
    'happy': {'emoji': '😊', 'color': '#FFD93D', 'label': 'Happy'},
    'sad': {'emoji': '😢', 'color': '#6B7FB5', 'label': 'Sad'},
    'energetic': {'emoji': '⚡', 'color': '#FF6B6B', 'label': 'Energetic'},
    'calm': {'emoji': '🧘', 'color': '#4ECDC4', 'label': 'Calm'},
    'romantic': {'emoji': '❤️', 'color': '#FF69B4', 'label': 'Romantic'},
    'angry': {'emoji': '🔥', 'color': '#E74C3C', 'label': 'Angry'},
    'nostalgic': {'emoji': '🌅', 'color': '#F4A460', 'label': 'Nostalgic'},
    'anxious': {'emoji': '😰', 'color': '#9B59B6', 'label': 'Anxious'},
    'motivated': {'emoji': '💪', 'color': '#2ECC71', 'label': 'Motivated'},
    'melancholy': {'emoji': '🌧️', 'color': '#5B7DB1', 'label': 'Melancholy'},
}

# Keywords for text sentiment analysis
MOOD_KEYWORDS = {
    'happy': ['happy', 'joy', 'excited', 'great', 'amazing', 'wonderful', 'fantastic', 'love', 'fun', 'laugh', 'smile', 'celebrate', 'santosham', 'anandam', 'super'],
    'sad': ['sad', 'crying', 'tears', 'heartbreak', 'lonely', 'depressed', 'miss', 'lost', 'hurt', 'pain', 'grief', 'badha', 'edupu', 'kashtam'],
    'energetic': ['energetic', 'pumped', 'hype', 'ready', 'go', 'active', 'alive', 'fired up', 'adrenaline', 'workout', 'energy', 'power', 'mass', 'josh'],
    'calm': ['calm', 'peaceful', 'relax', 'quiet', 'serene', 'tranquil', 'zen', 'breathe', 'easy', 'mellow', 'shanti', 'spastha', 'peace', 'cool'],
    'romantic': ['love', 'romantic', 'date', 'crush', 'heart', 'sweet', 'cuddle', 'together', 'valentine', 'partner', 'prema', 'ishq', 'pyar'],
    'angry': ['angry', 'furious', 'rage', 'mad', 'hate', 'frustrated', 'annoyed', 'pissed', 'irritated', 'livid', 'kopam', 'krodham'],
    'nostalgic': ['nostalgia', 'remember', 'childhood', 'memories', 'old days', 'back then', 'vintage', 'classic', 'throwback', 'gurthu', 'retro', 'pata'],
    'anxious': ['anxious', 'worried', 'nervous', 'stressed', 'overwhelmed', 'panic', 'fear', 'uncertain', 'restless', 'bhayam', 'tension'],
    'motivated': ['motivated', 'determined', 'goals', 'hustle', 'grind', 'achieve', 'success', 'ambitious', 'driven', 'strong', 'power', 'win'],
    'melancholy': ['melancholy', 'bittersweet', 'wistful', 'longing', 'yearning', 'pensive', 'reflective', 'contemplative', 'bada', 'soch', 'dard'],
}


# --- API Routes ---

@app.route('/api/moods')
def get_moods():
    return jsonify(MOODS)


@app.route('/api/languages/<mood>')
def get_languages(mood):
    """Get available languages for a mood."""
    if mood not in MOODS:
        return jsonify({'error': 'Invalid mood'}), 400
    langs = recommendations_col.distinct('lang', {'mood': mood})
    # Remove None, add 'All'
    langs = [l for l in langs if l]
    return jsonify({'languages': ['all'] + sorted(langs)})


@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    mood = data.get('mood')
    category = data.get('category', 'all')
    lang = data.get('lang', 'all')
    count = data.get('count', 6)

    if not mood or mood not in MOODS:
        return jsonify({'error': 'Invalid mood'}), 400

    categories = ['music', 'movies', 'anime'] if category == 'all' else [category]
    results = {}

    for cat in categories:
        match_stage = {'mood': mood, 'category': cat}
        if lang != 'all':
            match_stage['lang'] = lang

        pipeline = [
            {'$match': match_stage},
            {'$sample': {'size': count}},
            {'$project': {'mood': 0}},
        ]
        items = list(recommendations_col.aggregate(pipeline))
        for item in items:
            item['_id'] = str(item['_id'])
        results[cat] = items

    return jsonify({'mood': mood, 'category': category, 'lang': lang, 'recommendations': results})


@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    text_lower = text.lower()
    scores = {}

    for mood, keywords in MOOD_KEYWORDS.items():
        score = 0
        for keyword in keywords:
            if keyword in text_lower:
                score += 1
                if f' {keyword} ' in f' {text_lower} ':
                    score += 0.5
        if score > 0:
            scores[mood] = score

    if not scores:
        best_mood, confidence = 'calm', 0.3
    else:
        best_mood = max(scores, key=scores.get)
        max_score = scores[best_mood]
        confidence = round(min(0.5 + (max_score * 0.1), 1.0), 2)

    # Log to history
    history_col.insert_one({
        'mood': best_mood,
        'confidence': confidence,
        'source': 'text',
        'createdAt': datetime.utcnow(),
    })

    return jsonify({'mood': best_mood, 'confidence': confidence})


@app.route('/api/history', methods=['GET'])
def get_history():
    items = list(history_col.find().sort('createdAt', -1).limit(50))
    for item in items:
        item['_id'] = str(item['_id'])
        if 'createdAt' in item:
            item['createdAt'] = item['createdAt'].isoformat()
    return jsonify(items)


@app.route('/api/history', methods=['POST'])
def log_history():
    data = request.get_json()
    entry = {
        'mood': data.get('mood'),
        'confidence': data.get('confidence', 1.0),
        'source': data.get('source', 'manual'),
        'createdAt': datetime.utcnow(),
    }
    result = history_col.insert_one(entry)
    entry['_id'] = str(result.inserted_id)
    entry['createdAt'] = entry['createdAt'].isoformat()
    return jsonify(entry)


# --- Serve React ---

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/<path:path>')
def serve_static(path):
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
