#!/bin/bash

# This file must be used with launch/reeval_planning.launch.xml
BAG_NAME=$1

COMMAND_OPTION='--remap '

# remap all except for perception/object_recognition/detection/centerpoint/objects
PERCEPTION_TOPIC=$(ros2 bag info $BAG_NAME | awk '{print $2}' | grep perception | grep -v '/perception/object_recognition/detection/centerpoint/objects')
for i in ${PERCEPTION_TOPIC[@]}; do
    TARGET_PERCEPTION_TOPIC=$i
    RENAMED_TARGET_PERCEPTION_TOPIC=$(echo $TARGET_PERCEPTION_TOPIC | sed 's/\/perception/\/tmp\/perception/g')
    COMMAND_OPTION=$COMMAND_OPTION' '$TARGET_PERCEPTION_TOPIC':='$RENAMED_TARGET_PERCEPTION_TOPIC
done

ros2 bag play $BAG_NAME $COMMAND_OPTION --clock -r 0.6 -s sqlite3
