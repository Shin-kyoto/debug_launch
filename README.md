# debug_launchのブランチ切り替え

- workspaceがv0.41ならブランチもv0.41に
- workspaceがmainでrosbagがv0.41ならlocalization:=trueにする

# For replaying

```
ros2 launch debug_launch replay.launch.xml \
vehicle_model:=lexus sensor_model:=aip_xx1 \
map_path:=$HOME/workspace/maps/experiment
```

# For running planning locally

```
ros2 launch debug_launch reeval_planning.launch.xml \
vehicle_model:=lexus sensor_model:=aip_xx1 \
map_path:=$HOME/workspace/maps/experiment
```

```
ros2 run debug_launch play_reeval_planning.sh <path to bag>
```

# For comparing perception of rosbag/reeval

```
ros2 launch debug_launch reeval_perception.launch.xml \
vehicle_model:=lexus sensor_model:=aip_xx1 \
map_path:=$HOME/workspace/maps/experiment
```

```
ros2 run debug_launch play_reeval_perception.sh <path to bag>
```

# For reevaluating occupancy grid map

```
ros2 launch debug_launch reeval_occupancy_grid_map.launch.xml \
vehicle_model:=lexus sensor_model:=aip_xx1 \
map_path:=$HOME/workspace/maps/experiment
```

```
ros2 run debug_launch play_reeval_perception.sh <path to bag>
```

# For reevaluating behavior_velocity from recorded `path_with_lane_id`

```
ros2 launch debug_launch reeval_behavior_velocity.launch.xml \
vehicle_model:=lexus sensor_model:=aip_xx1 \
map_path:=$HOME/workspace/maps/experiment
```

```
ros2 run debug_launch play_reeval_behavior_velocity.sh <path to bag>
```
