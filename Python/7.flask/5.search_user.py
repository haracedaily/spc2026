from flask import Flask,jsonify,request

app=Flask(__name__)

users = [
    { 'name': 'Alice', 'age':25, "phone": "123-456-7890"},
    { 'name': 'Bob', 'age':30, "phone": "123-456-7890"},
    { 'name': 'Charlie', 'age':26, "phone": "123-456-7890"},
    { 'name': 'Drain', 'age':25, "phone": "123-456-7890"},
]

@app.route("/")
def home():
    return "home"

@app.route("/search")
def search_user():
    result = users
    #Query parameter use name, age, phone
    # print('name' in users[0].keys())
    # print([k for k in request.args.keys() if k in users[0].keys()])
    # matched = [k for k in request.args.keys() if k in users[0].keys()]
    # print(matched)
    # for key in request.args.keys():
    #     # TDD 테스트 케이스 먼저 고민하고 통과할 코드를 고민하는 방법
    #     if users[key] == request.args.get(key):
    #         result = 
    q = request.args.get("q")
    a = request.args.get("a",type=int)
    p = request.args.get("p")   
    print(q is None)
    print(a is not None)
    print(p)
    if(q):
        result = [user for user in result if user["name"].lower() == q.lower()]
    if(a):
        result = [user for user in result if user["age"]==int(a)]
    if(p):
        result = [user for user in result if user["phone"].startswith(p)]
    # for user in users:
    #     if (q is not None&user["name"].lower()==q.lower())&(a is not None&user["age"].startswith(a))&(p is not None&user["phone"]==p):
    #         if result is None:
    #             result = []
    #         result.append(user)
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)