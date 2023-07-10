#!/bin/bash

# Check if the text argument is provided
if [ -z "$1" ]; then
  echo "No text provided."
  exit 1
fi

# Store the text argument in a variable
input_text="$1"

# Call the Python script and pass the input text as an argument
hashed_text=$(python3 hasher.py "$input_text")

# Extract the first 5 characters of the hashed text
file_name=${hashed_text:0:5}

result=$(find "datasets/hashes/hashes" -name "$file_name.txt")

# Check if the file was found
if [ -n "$result" ]; then
  # Assign to rest of the hashed text to a variable
  hash_to_search=${hashed_text:5}

  # Pass the $file_name to an Java program as an argument
  hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -files mapper_prog2.py,reducer_prog2.py -mapper "python3 mapper_prog2.py $hash_to_search $input_text" -reducer reducer_prog2.py -input input_prog2/"$file_name.txt" -output output_prog2/hashout

else
  echo "Hash does not exist."
fi

