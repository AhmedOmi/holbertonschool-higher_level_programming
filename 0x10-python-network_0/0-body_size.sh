#!/bin/bash
# display received
curl -so /dev/null -w '%{size_download}\n' "$1"
