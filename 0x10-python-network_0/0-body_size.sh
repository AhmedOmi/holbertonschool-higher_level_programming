#!/bin/bash
curl -o /dev/null -w '%{size_download}\n' "$1"
