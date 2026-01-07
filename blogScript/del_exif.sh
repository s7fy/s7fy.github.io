#!/bin/zsh
set -e

if [ -z "$1" ]; then
    echo "usage: $0 image_name"
    exit 1
fi

IMG_PATH="/Users/s7fy/blog/blogScript/$1"

if [[ ! -f "$IMG_PATH" ]]; then
    echo "Error: File not found - $IMG_PATH"
    exit 1
fi
exiftool -all= $IMG_PATH

base="image"
ext="png"
i=1

while [[ -e "${base}-${i}.${ext}" ]]; do
  ((i++))
done

new_name="${base}-${i}.${ext}"
bak_name="${base}-${i}.${ext}.bak"

exiftool -all= -o "$new_name" "$IMG_PATH"

mv "$IMG_PATH" "$bak_name"

echo "changed name    : $1 → $new_name"
echo "created backup  : $bak_name"
