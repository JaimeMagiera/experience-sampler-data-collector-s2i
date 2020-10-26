#!/bin/bash

# Get command line options
while getopts ":s:h" opt; do
  case $opt in
	s) SERVER_URL="$OPTARG"
	;;
	h) PRINT_HELP=true
	;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done


if  [ "$PRINT_HELP" = true ]; then
	echo "Use the -s flag to denote the target server"
	exit 0;
fi

participant_id=$RANDOM
pause_time=$RANDOM

echo "Server: " ${SERVER_URL}
echo "Participant ID: " ${participant_id}
echo "Pause Time: " ${pause_time}

curl -d "participant_id=${participant_id}&pause_time=${pause_time}" -X POST ${SERVER_URL}/cgi-bin/data_collector.cgi
