#!/bin/zsh
set -e

cd ~/blog &&

hugo &&
git add ./content &&
cd ~/blog &&
git commit -m "post $(date '+%Y-%m-%d %H:%M')" &&
git push
