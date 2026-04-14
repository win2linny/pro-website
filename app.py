import random
from datetime import date
from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('index.html', verse=selected_verse, days=days_married)

# New Route for Your Bio
@app.route('/about-john')
def about_john():
    return render_template('about_john.html')

# New Route for Your Wife's Bio
@app.route('/about-wife')
def about_wife():
    return render_template('about_wife.html')

if __name__ == '__main__':
    # We use port 80 here because Docker maps it to 8080 outside
    app.run(host='0.0.0.0', port=80)
