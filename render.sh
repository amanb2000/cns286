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
	--mathml \
    --standalone \
    --css style.css \
	--metadata link_prefix="http://lancelot.languagegame.io/cns286/" \
    --metadata image_prefix="http://lancelot.languagegame.io/cns286/" \
	--metadata title=""
done

if [ "$1" == "publish" ]; then 
	cp -r /home/odysseus/cns286/figs/ /mnt/arc/cns286
	cp /home/odysseus/cns286/style.css /mnt/arc/cns286/
	cp /home/odysseus/cns286/html/* /mnt/arc/cns286/
fi
