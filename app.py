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

        # Сохраняем файлы
        photo.save(os.path.join("static/uploads", photo.filename))
        voice.save(os.path.join("static/uploads", voice.filename))
        video.save(os.path.join("static/uploads", video.filename))

        return redirect(url_for("success"))

@app.route("/success")
def success():
    return "Данные успешно загружены! Создание аватара началось."

# Привязываем приложение к динамическому порту Heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
