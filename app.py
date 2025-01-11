from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions', methods=['POST'])
def questions():
    return render_template('questions.html')

@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    return "Спасибо! Аватар создан!"

if __name__ == "__main__":
    app.run(debug=False)
