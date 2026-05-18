from flask import Flask,session
from flask_session import Session
#서버 측에서 세션을 저장하기 위한 확장 클래스

app = Flask(__name__)

app.secret_key = 'your_secret_key' # 나만 아는 세션 암호화 키 사용 => .env에서 핸들링
app.config['SESSION_TYPE']='filesystem' #나의 세션을 파일 / redis / memcahed / mongod 등등 다양한걸 지원함
app.config['SESSION_FILE_DIR'] = './.sessions' # 내가 정한 폴더명
app.config['SESSION_PERMANENT'] = False # 브라우저 닫히면 삭제
app.config['SESSION_USE_SIGNER'] = True # 세션 쿠키에 서명을 사용하겠다 ( 전자 서명, 전자봉투 처럼 탈취 방지용임 )

# 저장소를 만들고 나면 브라우저에는 SESSION ID만 쿠키로 전달됨.
# 실제 세션 데이터는 서버(filesystem/redis 등)에 저장됨.
# SESSION_USE_SIGNER=True 인 경우 SESSION ID에 서명을 추가하여
# 사용자가 임의로 변조했는지 검증할 수 있음.

# SESSION_USE_SIGNER=True 인 경우 Flask는 SECRET_KEY 기반의
# HMAC(SHA256 등) 서명을 사용하여 SESSION ID 위변조를 검증함.

Session(app)
# 이제 저장소를 지정하였음으로, 쿠키에 이제 데이터를 안 담아줌 => 리턴되는 쿠키에 sessionID가 저장됨

@app.route('/')
def set_session():
    
    if 'username' in session:
        return f"세션에서 당신의 정보를 찾았습니다. {session['username'], session['fullname'], session['hobby']}"
    
    session['username'] = 'spc2026'
    session['fullname'] = 'hong gil'
    session['dob'] = '2005/05/05'
    session['hobby'] = '유튜브하기, 쇼핑하기, 게임하기'
    return f"첫 방문 이시군요. 당신을 기억하겠습니다."

if __name__ == '__main__':
    app.run(debug=True)