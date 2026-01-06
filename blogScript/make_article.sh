#!/bin/zsh
set -e

cd ~/blog

if [ -z "$1" ]; then
  echo "usage: $0 article_name"
  exit 1
fi

POST="/Users/s7fy/blog/content/posts/$1.md"

DATE=$(date "+%Y-%m-%dT%H:%M:%S+09:00")
TAG_Y=$(date "+%Y")
TAG_YM=$(date "+%Y-%m")

if [ -e "$POST" ]; then
  echo "already exists: $POST"
  exit 1
fi

cat <<EOF > "$POST"
+++
date = '$DATE'
title = '$1'
tags = ['$TAG_Y', '$TAG_YM']
draft = true
+++

EOF

echo "made it : $POST"

vim $POST
