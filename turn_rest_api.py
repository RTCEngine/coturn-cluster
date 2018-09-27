# -*- coding: utf-8 -*-
# author: leeoxiang

import uuid
import hmac
import hashlib
import base64
import time
import argparse



def generate(server,ttype,transport,secret):

    userid = uuid.uuid4().hex
    username = '%d:%s' % (int(time.time()) + 24*3600, userid)

    digest = hmac.new(secret,username,digestmod=hashlib.sha1).digest()
    credential = base64.b64encode(digest)

    uri = '%s:%s:3478?transport=%s' % (ttype,server,transport)

    return {
            'username':username,
            'uris':[uri],
            'credential':credential
        }


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--server', help='turn/stun server ip')
    parser.add_argument('--type', help='iceServer type, stun or turn')
    parser.add_argument('--transport', help='turn/sturn transport, udp or tcp')
    parser.add_argument('--secret', help='coturn server static_secret')
    args = parser.parse_args()

    iceserver = generate(args.server,args.type,args.transport,args.secret)

    print('iceServer == ')
    print(iceserver)


