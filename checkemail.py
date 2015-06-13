#!/usr/bin/env python
import subprocess
from datetime import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler

def sendmessage(message):
    subprocess.Popen(['/usr/bin/notify-send', str(message)])
    return

def gmail_checker(username,password):
    import imaplib,re
    i=imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        i.login(username,password)
        x,y=i.status('INBOX','(MESSAGES UNSEEN)')
        messages=int(re.search('MESSAGES\s+(\d+)',y[0]).group(1))
        unseen=int(re.search('UNSEEN\s+(\d+)',y[0]).group(1))
        return (messages,unseen)
    except:
        return False,0


def tick():
    username = 'username'
    passwd = 'password'
    # messages unused here
    messages,unseen = gmail_checker(username, passwd)
    sendmessage("Gmail account %s has %i new messages" % (username,unseen))

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', minutes=5)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()  # Not strictly necessary if daemonic mode is enabled but should be done if possible