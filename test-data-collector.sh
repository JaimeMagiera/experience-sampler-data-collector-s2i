#!/bin/sh
# This shell script simulates a survey submission to your data collector script. Use the -u flag to provide the complete URL to the data collector script. The Study ID value is "TEST123". The "Participant ID" and "Pause Time" are randomly generated.

study_id="TEST123"

# Get command line options
while getopts ":u:h" opt; do
  case $opt in
	u) data_collector_script_url="$OPTARG"
	;;
	h) print_help=true
	;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

# Check if the -h flag was used. If so, print help
if  [ "$print_help" = true ]; then
	echo 'This shell script simulates a survey submission to your data collector script. Use the -u flag to provide the complete URL to the data collector script. The Study ID value is "TEST123". The "Participant ID" and "Pause Time" are randomly generated.' 
	exit 0;
fi

# Generate random participant_id and pause_time
participant_id=$RANDOM
pause_time=$RANDOM

echo "URL: " ${data_collector_script_url}
echo "Study ID: " ${study_id}
echo "Participant ID: " ${participant_id}
echo "Pause Time: " ${pause_time}

# Post to the server
curl -d "participant_id=${participant_id}&study_id=${study_id}&pause_time=${pause_time}" -X POST ${data_collector_script_url}
