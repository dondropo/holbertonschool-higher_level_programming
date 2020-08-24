#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email
as a parameter, and finally displays the body of the response.
- You are not allowed to import packages other than requests and sys
"""
import sys
import requests as rq


if __name__ == "__main__":
    r = rq.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
