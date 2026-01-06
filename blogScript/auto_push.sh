#!/bin/zsh
set -e

hugo
cd docs
git add .
git commit -m "update $(date '+%Y-%m-%d %H:%M')"
git push
