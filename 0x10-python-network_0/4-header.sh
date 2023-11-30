#!/bin/bash
#a Bash script that takes in a URL as an argument, sends GET and displays body
curl -s "$1" -H "X-School-User-Id: 98"
