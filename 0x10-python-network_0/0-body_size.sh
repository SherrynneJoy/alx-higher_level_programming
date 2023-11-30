#!/bin/bash
#a Bash script that takes in URL, sends a request and gives the content length

curl -sI "$1" | grep -i Content-Length
