#!/bin/sh

if (( $# < 1 ))
then
	echo "Not enough argument"
	exit
elif (( $# > 1 ))
then
	echo "Too many argument"
	exit
fi

RESULT=$(curl -s $1 | grep "moved here" | cut -d'"' -f2)

if (( ${#RESULT} == 0 ))
then
	echo "No moved url found"
else
	echo $RESULT
fi
