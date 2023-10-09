"""
duplicate_mongo_chunks.py

Description:
    This script duplicates the chunks within a MongoDB-style JSON document.
    The purpose is to expand the size of the JSON document by creating duplicate values under new indices.
    The original chunks are maintained, and new chunks are added with incremented indices.

Usage:
    Ensure the JSON file you want to modify is named 'test.json' in the same directory as this script.
    Run this script, and it will update 'test.json' with the duplicated chunks.
"""

import json

# Load the JSON document
with open('test.json', 'r') as file:
    data = json.load(file)

# Get the current number of chunks
num_chunks = len(data['chunks'])

# Duplicate each chunk
for i in range(num_chunks):
    chunk_key = str(i)
    new_chunk_key = str(i + num_chunks)
    data['chunks'][new_chunk_key] = data['chunks'][chunk_key].copy()

# Update the JSON file with the duplicated chunks
with open('test.json', 'w') as file:
    json.dump(data, file, indent=4)

print("JSON updated successfully!")
