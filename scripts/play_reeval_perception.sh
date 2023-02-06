#!/bin/bash

# This file must be used with launch/reeval_planning.launch.xml
BAG_NAME=$1

# until acceleration becomes available
COMMAND_OPTION='--remap '

# mission_planning is necessary for behavior_planner
PLANNING_TOPIC=$(ros2 bag info $BAG_NAME | awk '{print $2}' | grep perception | grep -v rois)
for i in ${PLANNING_TOPIC[@]}; do
    TARGET_PLANNING_TOPIC=$i
    RENAMED_TARGET_PLANNING_TOPIC=$(echo $TARGET_PLANNING_TOPIC | sed 's/\/perception/\/tmp\/perception/g')
    COMMAND_OPTION=$COMMAND_OPTION' '$TARGET_PLANNING_TOPIC':='$RENAMED_TARGET_PLANNING_TOPIC
done

ros2 bag play $BAG_NAME $COMMAND_OPTION --clock 100 -r 0.3 -s sqlite3
