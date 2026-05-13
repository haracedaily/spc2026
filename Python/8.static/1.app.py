from flask import Flask,render_template,send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user')
def user():
    # 가공 없이 그대로 정적 파일 날려보내겠다 =>
    return send_from_directory('static','user.html')

if __name__ == '__main__':
    app.run(debug=True)# port=5001 로 포트 지정 가능 