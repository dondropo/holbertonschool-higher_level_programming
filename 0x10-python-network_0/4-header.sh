#!/bin/bash
# Takes in a URL as an argument, sends a GET request to the URL
curl -sbL -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
