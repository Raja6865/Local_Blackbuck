#!/bin/bash

input_file="/Users/thotarajasekhar/Downloads/sample.csv"
cat $input_file | while read line;
do
	local_doc=`echo $line | awk -F ',' '{print $1}'`
	S3_doc=`echo $line | awk -F ',' '{print $2}' | sed 's/^.\{37\}//'`
	echo "$local_doc"
	echo "$S3_doc"
	path=$(pwd)
 `cp $path/$local_doc $ecom_path/$S3_doc`	
	echo "cp $path/$local_doc $ecom_path/$S3_doc"	
done
