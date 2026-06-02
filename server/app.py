"""
MoodVibe — Flask Backend
Mood-based movie, music & anime recommender with MongoDB
"""

import os
import random
import csv
import io
from datetime import datetime, timedelta
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
favorites_col = db['favorites']
polls_col = db['polls']
journal_col = db['journal']

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

# Mood quotes
MOOD_QUOTES = {
    'happy': [
        "Happiness is not by chance, but by choice.",
        "Collect moments, not things.",
        "Your vibe attracts your tribe.",
    ],
    'sad': [
        "It's okay to not be okay sometimes.",
        "Tears are words the heart can't express.",
        "After every storm, there's a rainbow waiting.",
    ],
    'energetic': [
        "Channel that energy into something amazing.",
        "You're unstoppable when you're fired up.",
        "Go hard or go home.",
    ],
    'calm': [
        "Peace comes from within. Do not seek it without.",
        "Inhale confidence, exhale doubt.",
        "Stillness is the key to everything.",
    ],
    'romantic': [
        "Love is the poetry of the senses.",
        "Every love story is beautiful, but ours is my favorite.",
        "You're my favorite notification.",
    ],
    'angry': [
        "Use that fire to fuel your greatness.",
        "Anger is a signal, not a solution.",
        "Breathe. It's just a bad day, not a bad life.",
    ],
    'nostalgic': [
        "The good old days were called good for a reason.",
        "Nostalgia is a file that removes the rough edges from the good old days.",
        "Sometimes you have to look back to see how far you've come.",
    ],
    'anxious': [
        "You've survived 100% of your worst days so far.",
        "This too shall pass.",
        "Worrying means you suffer twice.",
    ],
    'motivated': [
        "The only way to do great work is to love what you do.",
        "Dream big, start small, act now.",
        "Your only limit is your mind.",
    ],
    'melancholy': [
        "There's a kind of beauty in sadness.",
        "Melancholy is the pleasure of being sad.",
        "Even the darkest night will end and the sun will rise.",
    ],
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


@app.route('/api/quote/<mood>')
def get_quote(mood):
    if mood not in MOODS:
        return jsonify({'error': 'Invalid mood'}), 400
    quotes = MOOD_QUOTES.get(mood, [])
    quote = random.choice(quotes) if quotes else "Go with the flow."
    return jsonify({'mood': mood, 'quote': quote})


@app.route('/api/favorites', methods=['GET'])
def get_favorites():
    items = list(favorites_col.find().sort('createdAt', -1))
    for item in items:
        item['_id'] = str(item['_id'])
        if 'createdAt' in item:
            item['createdAt'] = item['createdAt'].isoformat()
    return jsonify(items)


@app.route('/api/favorites', methods=['POST'])
def add_favorite():
    data = request.get_json()
    item_id = data.get('itemId')
    if not item_id:
        return jsonify({'error': 'itemId required'}), 400

    existing = favorites_col.find_one({'itemId': item_id})
    if existing:
        return jsonify({'message': 'Already in favorites'}), 200

    fav = {
        'itemId': item_id,
        'title': data.get('title', ''),
        'artist': data.get('artist', ''),
        'genre': data.get('genre', ''),
        'platform': data.get('platform', ''),
        'url': data.get('url', ''),
        'category': data.get('category', ''),
        'mood': data.get('mood', ''),
        'lang': data.get('lang', ''),
        'rating': data.get('rating'),
        'episodes': data.get('episodes'),
        'dub': data.get('dub'),
        'createdAt': datetime.utcnow(),
    }
    result = favorites_col.insert_one(fav)
    fav['_id'] = str(result.inserted_id)
    fav['createdAt'] = fav['createdAt'].isoformat()
    return jsonify(fav), 201


@app.route('/api/favorites/<item_id>', methods=['DELETE'])
def remove_favorite(item_id):
    result = favorites_col.delete_one({'itemId': item_id})
    if result.deleted_count == 0:
        return jsonify({'error': 'Not found'}), 404
    return jsonify({'message': 'Removed'})


@app.route('/api/stats')
def get_stats():
    from collections import Counter
    items = list(history_col.find().sort('createdAt', -1))
    for item in items:
        item['_id'] = str(item['_id'])
        if 'createdAt' in item:
            item['createdAt'] = item['createdAt'].isoformat()

    mood_counts = Counter(i['mood'] for i in items)
    total = len(items)

    # Streak calculation
    streak = 0
    if items:
        current_mood = items[0]['mood']
        for item in items:
            if item['mood'] == current_mood:
                streak += 1
            else:
                break

    # Most frequent mood
    most_frequent = mood_counts.most_common(1)[0][0] if mood_counts else None

    return jsonify({
        'total': total,
        'moodCounts': dict(mood_counts),
        'mostFrequent': most_frequent,
        'currentStreak': streak,
        'recentHistory': items[:10],
    })


@app.route('/api/calendar')
def get_calendar():
    """Get mood history grouped by date for the last 90 days."""
    days = int(request.args.get('days', 90))
    since = datetime.utcnow() - timedelta(days=days)
    items = list(history_col.find({'createdAt': {'$gte': since}}).sort('createdAt', -1))

    calendar = {}
    for item in items:
        date_key = item['createdAt'].strftime('%Y-%m-%d')
        if date_key not in calendar:
            calendar[date_key] = {'moods': [], 'count': 0}
        calendar[date_key]['moods'].append(item['mood'])
        calendar[date_key]['count'] += 1

    # Find dominant mood per day
    from collections import Counter
    for date_key in calendar:
        mood_counts = Counter(calendar[date_key]['moods'])
        calendar[date_key]['dominant'] = mood_counts.most_common(1)[0][0]

    return jsonify({'calendar': calendar, 'days': days})


# Curated mood combos
MOOD_COMBOS = {
    'happy': [
        {'movie': 'Zindagi Na Milegi Dobara', 'music': 'Senorita — Shankar Ehsaan Loy', 'snack': 'Ice cream sundae', 'vibe': 'Road trip energy'},
        {'movie': 'The Intern', 'music': 'Happy — Pharrell Williams', 'snack': 'Fruit smoothie bowl', 'vibe': 'Feel-good afternoon'},
    ],
    'sad': [
        {'movie': 'Tamasha', 'music': 'Agar Tum Saath Ho — Arijit Singh', 'snack': 'Hot chocolate + blanket', 'vibe': 'Let it out, then heal'},
        {'movie': 'Inside Out', 'music': 'Fix You — Coldplay', 'snack': 'Warm cookies', 'vibe': 'It\'s okay to feel'},
    ],
    'energetic': [
        {'movie': 'RRR', 'music': 'Naatu Naatu — Rahul Sipligunj', 'snack': 'Protein shake + trail mix', 'vibe': 'Unstoppable mode'},
        {'movie': 'Baby Driver', 'music': 'Blinding Lights — The Weeknd', 'snack': 'Loaded nachos', 'vibe': 'Full throttle'},
    ],
    'calm': [
        {'movie': 'Before Sunrise', 'music': 'Sunset Lover — Petit Biscuit', 'snack': 'Green tea + dark chocolate', 'vibe': 'Slow down & breathe'},
        {'movie': 'Your Name', 'music': 'Sparkle — RADWIMPS', 'snack': 'Matcha latte', 'vibe': 'Peaceful evening'},
    ],
    'romantic': [
        {'movie': 'Sita Ramam', 'music': 'Thuli Thuli — Haricharan', 'snack': 'Wine + strawberries', 'vibe': 'Date night at home'},
        {'movie': 'The Notebook', 'music': 'Perfect — Ed Sheeran', 'snack': 'Chocolate fondue', 'vibe': 'Classic romance'},
    ],
    'angry': [
        {'movie': 'Vikram', 'music': 'Vikram Theme — Anirudh', 'snack': 'Spicy wings', 'vibe': 'Let it burn (productively)'},
        {'movie': 'John Wick', 'music': 'Lose Yourself — Eminem', 'snack': 'Crunchy chips', 'vibe': 'Channel the rage'},
    ],
    'nostalgic': [
        {'movie': 'Mouna Ragam', 'music': 'Roja Kaadhal Rojave — SPB', 'snack': 'Childhood candy + chai', 'vibe': 'Golden era feels'},
        {'movie': 'Stand By Me', 'music': 'Don\'t Stop Believin\' — Journey', 'snack': 'PB&J sandwich', 'vibe': 'Back to simpler times'},
    ],
    'anxious': [
        {'movie': 'Kung Fu Panda', 'music': 'Weightless — Marconi Union', 'snack': 'Herbal tea + almonds', 'vibe': 'Inner peace mode'},
        {'movie': 'Finding Nemo', 'music': 'Here Comes The Sun — Beatles', 'snack': 'Warm soup', 'vibe': 'Just keep swimming'},
    ],
    'motivated': [
        {'movie': 'MS Dhoni: The Untold Story', 'music': 'Lakshya Title Track — Shankar Mahadevan', 'snack': 'Black coffee + banana', 'vibe': 'Grindset activated'},
        {'movie': 'The Pursuit of Happyness', 'music': 'Stronger — Kanye West', 'snack': 'Energy balls', 'vibe': 'Nothing stops you'},
    ],
    'melancholy': [
        {'movie': 'October', 'music': 'The Night We Met — Lord Huron', 'snack': 'Chamomile tea', 'vibe': 'Beautiful sadness'},
        {'movie': 'A Silent Voice', 'music': 'LiSA — Shirushi', 'snack': 'Warm milk + honey', 'vibe': 'Quiet reflection'},
    ],
}


@app.route('/api/combos/<mood>')
def get_combos(mood):
    if mood not in MOODS:
        return jsonify({'error': 'Invalid mood'}), 400
    combos = MOOD_COMBOS.get(mood, [])
    return jsonify({'mood': mood, 'combos': combos})


@app.route('/api/polls', methods=['GET'])
def get_polls():
    """Get active polls."""
    now = datetime.utcnow()
    polls = list(polls_col.find({'expiresAt': {'$gt': now}}).sort('createdAt', -1).limit(5))
    for poll in polls:
        poll['_id'] = str(poll['_id'])
        poll['createdAt'] = poll['createdAt'].isoformat()
        poll['expiresAt'] = poll['expiresAt'].isoformat()
    return jsonify(polls)


@app.route('/api/polls', methods=['POST'])
def create_poll():
    """Create a new poll."""
    data = request.get_json()
    mood = data.get('mood')
    if not mood or mood not in MOODS:
        return jsonify({'error': 'Invalid mood'}), 400

    # Generate poll options from recommendations
    categories = ['music', 'movies', 'anime']
    options = []
    for cat in categories:
        items = list(recommendations_col.aggregate([
            {'$match': {'mood': mood, 'category': cat}},
            {'$sample': {'size': 2}},
            {'$project': {'mood': 0}},
        ]))
        for item in items:
            item['_id'] = str(item['_id'])
            options.append({
                'id': item['_id'],
                'title': item.get('title', ''),
                'category': cat,
                'votes': 0,
            })

    poll = {
        'mood': mood,
        'question': f"Pick your vibe {mood} choice!",
        'options': options[:6],
        'totalVotes': 0,
        'createdAt': datetime.utcnow(),
        'expiresAt': datetime.utcnow() + timedelta(hours=24),
    }
    result = polls_col.insert_one(poll)
    poll['_id'] = str(result.inserted_id)
    poll['createdAt'] = poll['createdAt'].isoformat()
    poll['expiresAt'] = poll['expiresAt'].isoformat()
    return jsonify(poll), 201


@app.route('/api/polls/<poll_id>/vote', methods=['POST'])
def vote_poll(poll_id):
    """Vote on a poll option."""
    data = request.get_json()
    option_id = data.get('optionId')
    if not option_id:
        return jsonify({'error': 'optionId required'}), 400

    from bson import ObjectId
    try:
        result = polls_col.update_one(
            {'_id': ObjectId(poll_id), 'options.id': option_id},
            {'$inc': {'options.$.votes': 1, 'totalVotes': 1}}
        )
    except Exception:
        return jsonify({'error': 'Invalid poll ID'}), 400

    if result.modified_count == 0:
        return jsonify({'error': 'Poll or option not found'}), 404

    poll = polls_col.find_one({'_id': ObjectId(poll_id)})
    poll['_id'] = str(poll['_id'])
    poll['createdAt'] = poll['createdAt'].isoformat()
    poll['expiresAt'] = poll['expiresAt'].isoformat()
    return jsonify(poll)


@app.route('/api/reverse-lookup', methods=['POST'])
def reverse_lookup():
    """Find what mood a title matches."""
    data = request.get_json()
    query = data.get('query', '').strip()
    if not query:
        return jsonify({'error': 'Query required'}), 400

    # Search by title (case-insensitive partial match)
    results = list(recommendations_col.find(
        {'title': {'$regex': query, '$options': 'i'}}
    ).limit(10))

    for r in results:
        r['_id'] = str(r['_id'])

    if not results:
        # Try genre search
        results = list(recommendations_col.find(
            {'genre': {'$regex': query, '$options': 'i'}}
        ).limit(10))
        for r in results:
            r['_id'] = str(r['_id'])

    return jsonify({'query': query, 'results': results})


@app.route('/api/history/clear', methods=['DELETE'])
def clear_history():
    result = history_col.delete_many({})
    return jsonify({'deleted': result.deleted_count})


@app.route('/api/history/export')
def export_history():
    items = list(history_col.find().sort('createdAt', -1))
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['mood', 'confidence', 'source', 'date'])
    for item in items:
        writer.writerow([
            item.get('mood', ''),
            item.get('confidence', ''),
            item.get('source', ''),
            item.get('createdAt', '').isoformat() if isinstance(item.get('createdAt'), datetime) else item.get('createdAt', ''),
        ])
    return output.getvalue(), 200, {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename=moodvibe_history.csv'
    }


@app.route('/api/journal', methods=['GET'])
def get_journal():
    items = list(journal_col.find().sort('createdAt', -1).limit(50))
    for item in items:
        item['_id'] = str(item['_id'])
        if 'createdAt' in item:
            item['createdAt'] = item['createdAt'].isoformat()
    return jsonify(items)


@app.route('/api/journal', methods=['POST'])
def add_journal():
    data = request.get_json()
    entry = {
        'mood': data.get('mood', ''),
        'note': data.get('note', '').strip(),
        'createdAt': datetime.utcnow(),
    }
    if not entry['note']:
        return jsonify({'error': 'Note required'}), 400
    result = journal_col.insert_one(entry)
    entry['_id'] = str(result.inserted_id)
    entry['createdAt'] = entry['createdAt'].isoformat()
    return jsonify(entry), 201


@app.route('/api/journal/<entry_id>', methods=['DELETE'])
def delete_journal(entry_id):
    from bson import ObjectId
    try:
        result = journal_col.delete_one({'_id': ObjectId(entry_id)})
    except Exception:
        return jsonify({'error': 'Invalid ID'}), 400
    if result.deleted_count == 0:
        return jsonify({'error': 'Not found'}), 404
    return jsonify({'message': 'Deleted'})


# --- Seed Polls (run once) ---

@app.route('/api/seed-polls', methods=['POST'])
def seed_polls():
    """Create sample polls for each mood."""
    from bson import ObjectId
    polls_col.delete_many({})
    now = datetime.utcnow()

    for mood in MOODS:
        options = []
        for cat in ['music', 'movies', 'anime']:
            items = list(recommendations_col.aggregate([
                {'$match': {'mood': mood, 'category': cat}},
                {'$sample': {'size': 2}},
                {'$project': {'mood': 0}},
            ]))
            for item in items:
                item['_id'] = str(item['_id'])
                options.append({
                    'id': item['_id'],
                    'title': item.get('title', ''),
                    'category': cat,
                    'votes': random.randint(0, 50),
                })

        poll = {
            'mood': mood,
            'question': f"What's your ultimate {mood} pick?",
            'options': options[:6],
            'totalVotes': sum(o['votes'] for o in options[:6]),
            'createdAt': now,
            'expiresAt': now + timedelta(hours=48),
        }
        polls_col.insert_one(poll)

    return jsonify({'message': f'Seeded {len(MOODS)} polls'})


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
