#!/bin/sh

# Check if a file argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

# Execute SQL commands from the file, prompting for password
mysql -u hasan -p < $1
