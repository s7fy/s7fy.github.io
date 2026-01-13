#!/bin/zsh
set -e

if [[ $# -ne 3 ]]; then
    echo "usage: $0 image_name image_path article_path"
    exit 1
fi

IMG_PATH="$2/$1"
ARTICLE_PATH="/Users/s7fy/blog/content/posts/$3"

if [[ ! -f "$IMG_PATH" ]]; then
    echo "Error: File not found - $IMG_PATH"
    exit 1
fi

base="image"
exts=(png jpg gif)
i=1

while :; do
    for ext in "${exts[@]}"; do
        if [[ -e "${base}-${i}.${ext}" ]]; then
            ((i++))
            continue 2   # while に戻る
        fi
    done
    break
done

# 元ファイルの拡張子を取得
orig_ext="${1##*.}"

new_name="${base}-${i}.${orig_ext}"
bak_name="${base}-${i}.${orig_ext}.bak"

exiftool -all= -o "$new_name" "$IMG_PATH"
mv "$IMG_PATH" "$bak_name"

cp -a "$new_name" "$ARTICLE_PATH" 
echo "changed name    : $1 → $new_name"
echo "created backup  : $bak_name"

