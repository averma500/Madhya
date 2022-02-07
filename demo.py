import random
import time
import webbrowser

while True:
    sites = random.choice(['youtube.com', 'facebook.com'])
    visit = 'https://{}'.format(sites)
    webbrowser.open(visit)
    time.sleep(2)
# while False:
#     time.sleep(0)