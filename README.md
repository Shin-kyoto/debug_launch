# For replaying

```
ros2 launch debug_launch replay.launch.xml \
vehicle_model:=lexus sensor_model:=aip_xx1 \
map_path:=$HOME/workspace/maps/experiment
```

# For running planning

```
ros2 launch debug_launch planning.launch.xml \
vehicle_model:=lexus sensor_model:=aip_xx1 \
map_path:=$HOME/workspace/maps/experiment
```

```
scripts/without_planning.sh <bag_dir>
```
