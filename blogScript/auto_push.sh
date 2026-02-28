#!/bin/zsh
set -e

cd ~/blog &&

hugo &&
git add . &&
git commit -m "post $(date '+%Y-%m-%d %H:%M')" &&
git push &&
