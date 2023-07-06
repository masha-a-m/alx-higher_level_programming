#!/bin/bash
#pn;y status code
curl -s -o /dev/null -w "%{http_code}" "$1"
