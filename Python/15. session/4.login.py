from flask import Flask, render_template, request, session, redirect, url_for
# from flask_session Session은 더이상 안함, 저장소를 지정하는 거지 코드 너무 늘어나서 더 이상 하진 않지만 실무적으로는 한다
# 나중엔 이게 DB에서 대체함
app = Flask(__name__)

app.secret_key='my-random-key'  #세션 쓸때 키

users = [
    {'name':'Alice', 'id': 'alice','pw':'alice'},
    {'name':'Bob', 'id': 'bob','pw':'bob1234'},
    {'name':'Charlie', 'id': 'charlie','pw':'hello'}
]

# 1. 사용자가 비밀번호 바꾸는 기능을 추가한다
# 1-1. method를 POST로 확장
# 1-2. users 안에서 나의 비번을 바꾼다.
# 1-3. 성공적으로 변경되면 나의 profile에서 확인한다
# 1-4. '비밀번호 변경' 을 눌렀을때 성공적으로 변경되었음을 알려준다 (사용자 피드백)

@app.route('/profile',methods=['POST'])
def change_pw():
    pw = request.form.get('pw')
    user = session.get('user')
    for u in users:
        if u['id'] == user['id']:
            u['pw']=pw
            user = u
            session['user']=u
            message = '성공적으로 비밀번호가 변경되었습니다.'
            # return render_template('profile.html', user=user, message = message)
            return redirect(url_for('profile'))

    
    return render_template('profile.html', user=user)

@app.route('/profile')
def profile():
    user = session.get('user')
    if not user:
        return redirect( url_for('home') )
    return render_template('profile.html', user=user)

@app.route('/dashboard')
def welcome():
    user = session.get('user')
    return render_template('dashboard.html', name=user['name'])

@app.route('/logout')
def logout():
    session.pop('user',None)
    print('?')
    # pop에서 해당 키가 없을땐 무시 ( 오류 방지용 )
    return redirect(url_for('home'))

@app.route('/', methods=['GET'])
def home():
    if session.get('user'):
        return redirect(url_for('welcome'))
# 로그인이 아닐때 즉 첫방문
    return render_template('index.html')

@app.route('/', methods=['POST'])
def login():
    error = None
    user = session.get('user')
    id = request.form.get('id')
    pw = request.form.get('pw')
    if id:
        user = next((u for u in users if u['id'] == id and u['pw'] == pw), None)
        # user = [u for u in Users if u['id'] == id and u['pw'] == pw]
    # user db에서 이 사용자 매칭
    # 사용자가 있으면 세션에 저장한다.
    if user:
        session['user'] = user #로그인한 사용자
        return redirect(url_for('welcome'))
    elif id:
        error = 'Invalid ID or PW'
        return render_template('index.html', error=error)

if __name__=='__main__':
    app.run(debug=True)