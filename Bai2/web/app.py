from flask import Flask, render_template, request, redirect
from config import BaseConfig
from models import db, Post
import time

app = Flask(__name__)
app.config.from_object(BaseConfig)

db.init_app(app)

with app.app_context():
    time.sleep(5)      # đợi PostgreSQL sẵn sàng
    db.create_all()    # tạo bảng nếu chưa tồn tại


@app.route("/", methods=["GET"])
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template("index.html", posts=posts)


@app.route("/submit", methods=["POST"])
def submit():
    text = request.form["text"]
    post = Post(text=text)
    db.session.add(post)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
