#!/bin/bash
echo "connecting to database"
#`mysql -uroot -D Blackbuck -e "show processlist" | grep "Query" > "/Users/thotarajasekhar/Desktop/dump.csv"`
cat /Users/thotarajasekhar/Desktop/dump.csv| while read line;
do
	process_id=`echo $line | awk  '{print $1}'`
	echo "$process_id"
	# echo "mysql -uroot -D Blackbuck -e Call mysql.rds_kill($process_id)"
	`mysql -uroot -D Blackbuck -e "Call mysql.rds_kill($process_id)"`	
done
