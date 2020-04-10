#!/bin/bash
# cURL a JSON file
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
