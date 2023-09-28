#!/bin/bash
# A script that takes displays the size of the body of the response
curl -s "$1" | wc -c
