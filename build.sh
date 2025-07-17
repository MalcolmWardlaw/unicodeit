#!/bin/bash
set -e

WF_NAME="unicodeit"
OUTPUT_FILE="${WF_NAME}.alfredworkflow"

echo "Packaging Alfred workflow..."

(cd src && zip -r "../$OUTPUT_FILE" . -x "*.DS_Store" "*.git*")

echo "Packaged: $OUTPUT_FILE"
