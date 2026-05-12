#pip install flask
from flask import Flask

# 네이밍
app = Flask(__name__)

@app.route('/')
def home():
    return """
<html>
    <head>
        <title>타이틀</title>
        <style>
            p{
            color:blue
            }
        </style>
    </head>
    <body>
        <h1>웰컴투 마이 홈</h1>
        <p>여기는 텍스트 본문이 들어갑니다.</p>
        <p>여기는 텍스트 본문2이 들어갑니다.</p>
    </body>
</html>
"""
if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debuger=True) 에러 발생시 에러 경로 즉 디렉토리 경로 등 다 오픈됨 => 배포에선 뺌