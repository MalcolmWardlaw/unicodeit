import json
import sys
import os

from unicodeit import replace

# Extract the query string from the command-line arguments passed by Alfred
query = sys.argv[1]

# Construct the command to call the command-line tool with the modified query string

output = replace(query)

# Remove trailing whitespace, including newlines, from the output
output = output.strip()

# Format the output as JSON
result = {
    "items": [
        {
            "title": output,  # Assuming output is in UTF-8 encoding
            "arg": output,  # This is the value that Alfred will pass on if this item is selected
        }
    ]
}

# Print the JSON to stdout
print(json.dumps(result))
