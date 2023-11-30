#!/bin/bash
#script that takes in a URL, sends a POST request, and displays the body
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
