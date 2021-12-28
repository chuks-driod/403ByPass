#!/bin/evn python

from types import MethodType
import requests
from bs4 import BeautifulSoup
import re
import http
import subprocess

from requests.models import HTTPError


class Bypass:
    def __init__(self, url):
        self.target_url = url

    ip_list = ["localhost", "127.0.0.1"]

    def byPass403(self, url):
        # if url == None:
        #     url = self.target_url
        response = requests.get(url)
        responseStatus = http.HTTPStatus(403)
        resStatus = http.HTTPStatus(401)  

        response_status_code =  response.status_code == responseStatus or response.status_code == resStatus
        print(f"{response.status_code} Access Deny On GET Method....")

        if response_status_code:
            access_deny = requests.post(url)
            if access_deny.status_code == http.HTTPStatus(403) or access_deny.status_code == http.HTTPStatus(401):
                print(f"{access_deny.status_code} Access Deny On POST Method....")
        if response_status_code:
            acces_deny = requests.put(url)
            if acces_deny.status_code == http.HTTPStatus(401) or acces_deny.status_code == http.HTTPStatus(403):
                print(f"{access_deny.status_code} Access Deny On PUT Method....")
        if response_status_code:
            access_deny = requests.delete(url)
            if access_deny.status_code == http.HTTPStatus(403) or access_deny.status_code == http.HTTPStatus(401):
                print(f"{access_deny.status_code} Access Deny On DELETE Method....")
        if response_status_code:
            access_deny = requests.head(url)
            if access_deny.status_code  == responseStatus or access_deny.status_code == resStatus:
                print(f"{access_deny.status_code} Access Deny On HEAD Method....")
        if response_status_code:
            access_deny = requests.options(url)
            if access_deny.status_code == resStatus or access_deny.status_code == responseStatus:
                print(f"{access_deny.status_code} Access Deny On OPTIONS Method....")
        if response_status_code:
            access_deny = requests.patch(url)
            if access_deny.status_code == responseStatus or access_deny == resStatus:
                print(f"{access_deny.status_code} Access Deny On PATCH Method..")
        if response_status_code:
            print(f'\n[**] Tested Requests On == > ["GET","POST", "CONNECT", "DELETE", "PUT", "TRACE", "PACTH", "HEAD"]\n\n')

    def host_header(self, url=None):
        if url == None:
            url = self.target_url
            tested_headers = self.byPass403(url)
            
            response = requests.get(url)
            print(response.headers)
    # def ip_ping(self, url=None):
    #     if url == None:
    #         url = self.target_url
    #         tested_headers = self.byPass403(url)
    #         ping = subprocess.call("ping prestmit.com", shell=True)
    #         print(ping)
    #         target_ip = re.findall('[1-9]', str(ping))
    #         print(target_ip)            