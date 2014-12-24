#!/bin/bash
i=0
while true;
do
    ((i++));
	echo "$i    >>Changing Identity";
	killall -HUP tor;
	sleep 1;
done
