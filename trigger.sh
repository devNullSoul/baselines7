#!/bin/bash

BASE=$(cat base64-data.txt)

#curl -X POST -vv4 http://localhost:5678/webhook-test/api/generate \
#  -d '{ "data"="@kurzepdf.pdf" }' \
#  -H "Content-Type: application/json"

curl -X POST  http://localhost:5678/webhook-test/api/generate \
  -H "Content-Type: multipart/form-data" \
  -F "data=@kurzepdf.pdf"

#curl -X POST http://localhost:5678/webhook-test/api/generate \
#  -H "Content-Type: application/json" \
#  -d "$(jq -n --arg data "$(base64 -w 0 kurzepdf.pdf)" '{ data: $data }')"
