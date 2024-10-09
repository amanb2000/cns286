#!/bin/bash

# Iterate over all markdown files in the md/ directory
for file in ~/cns286/md/*.md; do
    # Get the filename without the extension
    filename=$(basename -- "$file" .md)
	echo "filename: $filename"
	echo "file: $file"
    
    # Convert the markdown file to HTML using pandoc
    pandoc -s "$file" \
    -o "html/$filename.html" \
    --mathjax \
	 --toc-depth=2 \
    --standalone \
    --css ~/cns286/style.css \
	--metadata title=""
done
