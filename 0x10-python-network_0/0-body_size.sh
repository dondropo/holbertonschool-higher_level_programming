#!/bin/bash
# sends a request to that URL
curl -sI "$1" | awk '$1=="Content-Length:" {print $2}'
