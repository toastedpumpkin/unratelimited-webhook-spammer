import requests
import time

wbhk = input("webhook: ")
pyld = input("payload: ")
lolsponsor = input("github.com/toastedpumpkin/discord-webhook-spammer")

def function():
    requests.post(wbhk,json={'content': pyld,})
    requests.post(wbhk,json={'content': lolsponsor,})

while True:
    function()
    time.sleep(1)
    print("sent :3")
