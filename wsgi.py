import uncurl

print uncurl.parse("curl -X POST https://wh.jandi.com/connect-api/webhook/11495160/86d7ab45df200b89fdedb99158472833 
-H "Accept: application/vnd.tosslab.jandi-v2+json" 
-H "Content-Type: application/json" 
--data-binary '{"body":"You have a new Pizza order.","connectColor"}')
