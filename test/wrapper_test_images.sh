#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
GPUID="${1:-0}"

for n in $(ls $SCRIPT_DIR/../build/) ; do
	echo "$n"
	
	CMD="$SCRIPT_DIR/test_image.sh $GPUID $n"
	echo "$CMD"
	pids[${i}]=$!

        GPUID=$(( GPUID+1 ))

	if (( GPUID > 7 )); then
		for pid in ${pids[*]}; do
    			wait $pid
		done
		GPUID=0
	fi
done
