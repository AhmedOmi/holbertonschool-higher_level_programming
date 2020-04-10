#!/bin/bash
# cURL only methods
curl -s "$1" -I | grep Allow | cut -d' ' -f2-
