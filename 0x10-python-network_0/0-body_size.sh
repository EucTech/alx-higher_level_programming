#!/bin/bash
# A script that takes displays the size of the body of the response
curl -sI "$1" | grep -i content-length
