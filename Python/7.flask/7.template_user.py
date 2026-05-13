from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    user_names = ["홍길동","고길동","김길동","이길동"]
    return render_template('users.html', names = user_names)

if __name__ == "__main__":
    app.run(debug=True)