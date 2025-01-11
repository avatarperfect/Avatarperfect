from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        photo = request.files["photo"]
        voice = request.files["voice"]
        video = request.files["video"]

        # Создаем папку uploads, если она отсутствует
        if not os.path.exists("static/uploads"):
            os.makedirs("static/uploads")

        photo.save("static/uploads/photo.jpg")
        voice.save("static/uploads/voice.mp3")
        video.save("static/uploads/video.mp4")

        return redirect(url_for("success"))

@app.route("/success")
def success():
    return "Данные успешно загружены! Создание аватара началось."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
