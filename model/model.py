# -*- coding: utf-8 -*-
import requests
import json
class Server():
    SRV = "http://192.168.42.228:8000/"
    terminal = 0
    service_id = 0
    current = None
    length = 0
    server = None
    def __init__(self):
        Server.server = requests.session()

    def login(self, username, password):
        try:
            res = Server.server.post(self.SRV + "api-token-auth/",
                                     {"username": "{}".format(username), "password": "{}".format(password)})
            if res.status_code == 200:
                self.TOKEN = json.loads(res.content)['token']
                Server.server.headers = {'Authorization': 'token {}'.format(self.TOKEN)}
                return True
        except Exception as ex:
            print ex
            pass
        return False


    #services
    def get_services(self):
        r = Server.server.get(self.SRV + 'queserver/services/')
        return json.loads(r.content)


    def order_service(self,srv):
        res = Server.server.post(self.SRV + "queserver/new-client/",
                                {"service": "{}".format(srv)})
        if res.status_code == 200:
            return json.loads(res.content)
        else:
            return False