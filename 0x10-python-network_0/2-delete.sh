#!/bin/bash
# a Bash script that sends a DELETE request to the URL & displays the response
curl -s "$1" -X "DELETE"
