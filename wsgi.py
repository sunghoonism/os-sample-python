import os

@application.route("/")
os.system("curl -X POST https://wh.jandi.com/connect-api/webhook/11495160/86d7ab45df200b89fdedb99158472833 \
-H "Accept: application/vnd.tosslab.jandi-v2+json" \
-H "Content-Type: application/json" \
--data-binary '{"body":"[[PizzaHouse]](http://url_to_text) You have a new Pizza order.","connectColor":"#FAC11B","connectInfo":[{"title":"Topping","description":"Pepperoni"},
{"title":"Location","description":"Empire State Building, 5th Ave, New York","imageUrl":"Url_to_text"}]}')

if __name__ == "__main__":
    application.run()
