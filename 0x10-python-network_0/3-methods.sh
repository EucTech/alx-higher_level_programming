#!/bin/bash
# this is a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | grep -i Allow | cut -b 8-
