from flask import Flask,session
from flask_session import Session
#서버 측에서 세션을 저장하기 위한 확장 클래스

app = Flask(__name__)

app.secret_key = 'your_secret_key' # 나만 아는 세션 암호화 키 사용 => .env에서 핸들링
app.config['SESSION_TYPE']='filesystem' #나의 세션을 파일 / redis / memcahed / mongod 등등 다양한걸 지원함
app.config['SESSION_FILE_DIR'] = './sessions' # 내가 정한 폴더명
app.config['SESSION_PERMANENT'] = False # 브라우저 닫히면 삭제
app.config['SESSION_USE_SIGNER'] = True # 세션 쿠키에 서명을 사용하겠다 ( 전자 서명, 전자봉투 처럼 탈취 방지용임 )
# base64 URL 이 아니라 이제 SHA256 같은 방식의 암호화를 통해서 HEX값을 보냄


Session(app)
# 이제 저장소를 지정하였음으로, 쿠키에 이제 데이터를 안 담아줌 => 리턴되는 쿠키에 sessionID가 저장됨

@app.route('/set-session')
def set_session():
    session['username'] = 'spc2026'
    session['fullname'] = 'hong gil'
    session['dob'] = '2005/05/05'
    session['hobby'] = '유튜브하기, 쇼팡하기, 게임하기'
    return f"세션 저장 완료 {session}"


@app.route("/get-session")
def get_session():
    if 'username' in session:
        return f"세션에서 당신의 정보를 찾았습니다. {session['username'], session['fullname'], session['hobby']}"
    return f"세션에 당신의 정보가 없습니다."


if __name__ == '__main__':
    app.run(debug=True)