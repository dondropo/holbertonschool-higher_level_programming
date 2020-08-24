#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response.
- You are not allowed to import packages other than requests and sys
 """
import sys
import requests as rq


if __name__ == "__main__":
        r = rq.get(sys.argv[1])
        if r.status_code >= 400:
            print('Error code: {}'.format(r.status_code))
        else:
            print(r.text)
