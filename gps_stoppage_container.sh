#!/bin/bash

set -x

truck=$1

>output.csv
exec < input.csv || exit 1
read header # read (and ignore) the first line
while IFS=, read from to; do
python stoppage_data.py $1 $from $to $2
cat output.csv >>final.csv
done
awk -F, '{ print $2","$6","$4","$5}' final.csv| tail -n+2 | sed -e "s///" -e 's/entry_time_GMT,//g' -e 's/exit_time_GMT,//g' -e 's/lat,//g' -e 's/lng//g' | grep -v '^$'  >a.csv
#pandoc a.csv --to=pdf -t latex -o stoppage_$1.pdf --pdf-engine=/Library/TeX/texbin/pdflatex
echo "entry_time_GMT,exit_time_GMT,lat,lng" > ${truck}_data.csv

grep -v '^$' a.csv >> ${truck}_data.csv
rm a.csv final.csv output.csv data_file.csv data.json
