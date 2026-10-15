
from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# 部落格文章資料
posts = [
    {
        "id": 1,
        "title": "我的第一篇文章",
        "author": "Green",
        "content": "歡迎來到我的 Flask 部落格！"
    },
    {
        "id": 2,
        "title": "學習 Python Flask",
        "author": "Green",
        "content": "今天開始學習如何使用 Flask 建立網站。"
    }
]

# 首頁：顯示所有文章
@app.route("/")
def index():
    return render_template("index.html", posts=posts)


# 新增文章
@app.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        content = request.form.get("content", "").strip()

        if not title or not author or not content:
            return "所有欄位都必須填寫", 400

        new_post = {
            "id": max((p["id"] for p in posts), default=0) + 1,
            "title": title,
            "author": author,
            "content": content
        }

        posts.append(new_post)

        return redirect(url_for("index"))

    return render_template("add.html")


# 顯示單篇文章
@app.route("/post/<int:post_id>")
def show_post(post_id):
    for post in posts:
        if post["id"] == post_id:
            return render_template("post.html", post=post)

    abort(404)


if __name__ == "__main__":
    app.run(debug=True)
