from flask import Flask, request
application = Flask(__name__)


@application.route("/")
def hello():
    return 'Hello'

@application.route('/webhook')
def webhook():
    headers = {
    'Accept': 'application/vnd.tosslab.jandi-v2+json',
    'Content-Type': 'application/json'
    }
    #data = '{"body":"[[Naver]](http:naver.com) You have a new Pizza order.","connectColor":"#FAC11B","connectInfo":[{"title":"Topping","description":"Pepperoni"},\n{"title":"Location","description":"Empire State Building, 5th Ave, New York","imageUrl":"Url_to_text"}]}'
    #print(request.form['text'])
    #print('POST!')
    #data='{{"text":"{} {}"}}'.format(request.form['text'], request.form['text'])
    data={'body':'I am from webhook'}
    response=requests.post('https://wh.jandi.com/connect-api/webhook/11495160/86d7ab45df200b89fdedb99158472833', headers=headers, data=data)
    return 'textyo'


if __name__ == "__main__":
    application.run()
