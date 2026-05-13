from flask import Flask,jsonify,request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/login',methods=['POST'])
def login():
    print(request.form)
    print(request.form.get('id'))
    id=request.form.get('id')
    pw=request.form.get('pw')
    print(f"입력한 ID는 {id} PW는 {pw}")
    
    return render_template('login.html',name=id)

if __name__ == "__main__":
    app.run(debug=True)