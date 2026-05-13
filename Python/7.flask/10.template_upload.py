from flask import Flask,jsonify,request, render_template
import os

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs(app.config['UPLOAD_FOLDER'],exist_ok=True)

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

@app.route('/upload',methods=['post'])
def upload_file():
    file = request.files['photo']
    print(file)
    filename = file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    return "파일 잘 받음"
if __name__ == "__main__":
    app.run(debug=True)