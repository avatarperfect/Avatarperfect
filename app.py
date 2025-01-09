
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Your Perfect Avatar from Future!</h1><p>More features coming soon...</p>"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
