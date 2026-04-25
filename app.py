import random
import requests
from datetime import date
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Your PocketBase URL
PB_URL = "http://66.228.58.24/api/collections/prayers/records"

verses = [
    "For I know the plans I have for you, declares the Lord. — Jeremiah 29:11",
    "I can do all things through Christ who strengthens me. — Philippians 4:13",
    "Trust in the Lord with all your heart and lean not on your own understanding. — Proverbs 3:5",
    "The Lord is my shepherd; I shall not want. — Psalm 23:1",
    "But seek first the kingdom of God and his righteousness. — Matthew 6:33"
]

@app.route('/')
def home():
    selected_verse = random.choice(verses)
    wedding_day = date(2025, 5, 2)
    today = date.today()
    days_married = (today - wedding_day).days
    
    # Fetch existing prayers from PocketBase to show on the page
    try:
        response = requests.get(PB_URL, timeout=3)
        prayers = response.json().get('items', [])
    except:
        prayers = []

    return render_template('index.html', verse=selected_verse, days=days_married, prayers=prayers)

# This route handles the "Submit" button and clears the box
@app.route('/submit-prayer', methods=['POST'])
def submit_prayer():
    prayer_text = request.form.get('prayer_text')
    
    if prayer_text:
        # Send the prayer to your PocketBase "filing cabinet"
        payload = {
            "text": prayer_text,
            "is_answered": False,
            "category": "General"
        }
        requests.post(PB_URL, json=payload, timeout=3)
    
    # This "redirect" is what clears the text box by refreshing the page
    return redirect(url_for('home'))

@app.route('/about-john')
def about_john():
    return render_template('about_john.html')

@app.route('/about-wife')
def about_wife():
    return render_template('about_wife.html')

if __name__ == "__main__":
    # This tells Flask to use the keys we got from Certbot
    # Note: I removed the "://" from the path
    app.run(
        host='0.0.0.0', 
        port=443, 
        threaded=True, 
        ssl_context=(
            '/etc/letsencrypt/live/familyfaithtracker.com/fullchain.pem', 
            '/etc/letsencrypt/live/familyfaithtracker.com/privkey.pem'
        )
    )

