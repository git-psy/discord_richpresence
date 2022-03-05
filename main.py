import time
from pypresence import Presence

client_id = "926421445213552702"
rpc = Presence(client_id=client_id)
def test():
    try:
        try:
            rpc.update(buttons=[
                {"label": "Mon site",
                 "url": "https://git-psy.github.io/index.html"},
                {"label": "Mon Github",
                 "url": "https://github.com/git-psy/"}],
                details="Bijour,",
                state="Et toi, ca vas ?",
                small_image="small_image",
                small_text="Musique !",
                large_image = "large_image",
                large_text="Html, le language de base pour créer un site web...")

        except:
            rpc.connect()
            rpc.update(buttons=[
                {"label": "Mon site",
                 "url": "https://git-psy.github.io/index.html"},
                {"label": "Mon Github",
                 "url": "https://github.com/git-psy/"}],
                details="Bijour,",
                state="Et toi, ca vas ?",
                small_image="small_image",
                small_text="Musique !",
                large_image = "large_image",
                large_text="Html, le language de base pour créer un site web...")
    except:pass
while 1:
    test()
    time.sleep(15)
