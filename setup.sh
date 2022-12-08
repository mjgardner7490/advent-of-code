#!/usr/bin/env bash

YEAR=$(date +%Y)
DAY=$(date +%d)
DIR="$YEAR/d${DAY}"

if [ "$1" != "-o" ] && [ -d $DIR ]; then
  echo "$DIR already setup. Use -o to overwrite."
  exit 1
fi

SESSION_COOKIE=$(cat .session)

echo "----- $YEAR Day $DAY -----"
echo "📂 Creating directory $DIR"
mkdir -p $DIR

echo "🗒️  Fetching input file"
curl --silent \
  --output $DIR/$DAY_in.txt \
  --cookie "$SESSION_COOKIE" \
  https://adventofcode.com/$YEAR/day/$(date +%-d)/input
