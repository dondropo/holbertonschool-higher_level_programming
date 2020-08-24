#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import requests as rq


response = rq.get('https://intranet.hbtn.io/status')
print('Body response:')
print('\t- type: {}'.format(response))
print('\t- content: {}'.format(response.text))
