#!/bin/bash
#Get every manpages from system
os=`uname -s`
ver=`uname -r`
dir=$os"/"$ver
mkdir -p $dir
LIST=`man -k . | awk '{print $1}'  | sort -u `
for e in $LIST;  do 
	newfile=$dir"/"$e
	trimede=`echo $e | awk 'BEGIN{FS="("}{ print $1}'`
	echo "Working on $newfile"
	man $trimede | col -bx >$newfile
done

`tar cvf  $os".tar" $os`
`gzip $os".tar"`

