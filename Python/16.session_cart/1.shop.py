from flask import Flask,render_template,session,request,redirect,flash, url_for

app = Flask(__name__)

users = [
    {
        "name": "Alice",
        "id": "alice",
        "pw": "alice"
    },
    {
        "name": "Bob",
        "id": "bob",
        "pw": "bob1234"
    },
    {
        "name": "Charlie",
        "id": "charlie",
        "pw": "hello"
    }
]
@app.route('/')
def home():
    if session.get('user'):
        return render_template('login.html')
    return render_template('instructure/main.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        id = request.form.id
        pw = request.form.pw
        user = next((u for u in users if u['id']==id and u['pw']==pw), None)
        if user :
            session['user'] = user
            flash(message="로그인 성공")
            return redirect(url_for('home'))
        return render_template('login.html')
    
@app.route('/product')
def product():
    return render_template('instructure/product.html')
    
if __name__ == '__main__':
    app.run(debug=True)
