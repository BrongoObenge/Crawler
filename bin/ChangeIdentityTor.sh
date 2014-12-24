#!/bin/bash
i=0
while true;
do
    ((i++));
	echo "$i    >>Changing Identity";
	echo -e 'AUTHENTICATE "hello"\r\nsignal NEWNYM\r\nQUIT' | nc 127.0.0.1 9051
	killall -HUP tor;
	sleep 1;
done
