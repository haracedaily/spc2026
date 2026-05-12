from flask import Flask, jsonify

app = Flask(__name__)

users = [
    { 'name': 'Alice', 'age':25, "phone": "123-456-7890"},
    { 'name': 'Bob', 'age':30, "phone": "123-456-7890"},
    { 'name': 'Charlie', 'age':26, "phone": "123-456-7890"}
]

@app.route('/')
def user():
    return jsonify(users) # 백엔드 list/dict 구조를 웹이 좋아하는 json오브젝트로 변환해서 보내줌

@app.route('/user/<name>')
def get_user_by_name(name):
    user=None
    for u in users:
        if u['name'].lower()==name.lower():
            user=u
    if user:
        return jsonify(user)
    else :
        return jsonify({"message":"Cannot find"})

if __name__ == '__main__':
    app.run(debug=True)