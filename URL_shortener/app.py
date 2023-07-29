from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)
url_map = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    short_code = generate_short_code()
    short_url = request.host_url + short_code
    url_map[short_code] = long_url
    return render_template('result.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_long_url(short_code):
    if short_code in url_map:
        long_url = url_map[short_code]
        return redirect(long_url)
    else:
        return "Short URL not found.", 404

def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code

if __name__ == "__main__":
    app.run()

