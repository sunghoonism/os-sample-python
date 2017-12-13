from flask import Flask, request, session
application = Flask(__name__)

headers = {
    'Accept': 'application/vnd.tosslab.jandi-v2+json',
    'Content-Type': 'application/json',
}
data = '{"body":"[[Naver]](http:naver.com) You have a new Pizza order.","connectColor":"#FAC11B","connectInfo":[{"title":"Topping","description":"Pepperoni"},\n{"title":"Location","description":"Empire State Building, 5th Ave, New York","imageUrl":"Url_to_text"}]}'

@application.route("/")
def hello():
    if request.method == 'POST':
        user_input = request.form['user_input']
        session['foo'] = 'bar'
    elif request.method == 'GET':
        session['foo'] = 'macarena'
    return session['foo']
    

if __name__ == "__main__":
    application.run()
