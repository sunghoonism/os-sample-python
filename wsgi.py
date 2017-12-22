from flask import Flask, request
application = Flask(__name__)

headers = {
    'Accept': 'application/vnd.tosslab.jandi-v2+json',
    'Content-Type': 'application/json',
}
#data = '{"body":"[[Naver]](http:naver.com) You have a new Pizza order.","connectColor":"#FAC11B","connectInfo":[{"title":"Topping","description":"Pepperoni"},\n{"title":"Location","description":"Empire State Building, 5th Ave, New York","imageUrl":"Url_to_text"}]}'
data = 'from alien'
@application.route("/")
def hello():
    return 'Hello'

@application.route("/webhook", methods=["POST"])
def webhook():
    if request.method == 'POST'
        print("POST!")
        requests.post('https://wh.jandi.com/connect-api/webhook/11495160/86d7ab45df200b89fdedb99158472833', headers=headers, data=data)
            return 'foo'
    return 'error'


if __name__ == "__main__":
    application.run()
