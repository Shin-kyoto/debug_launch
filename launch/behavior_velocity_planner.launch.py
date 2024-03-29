import launch
from launch.actions import DeclareLaunchArgument
from launch.actions import GroupAction
from launch.actions import IncludeLaunchDescription
from launch.actions import OpaqueFunction
from launch.actions import SetLaunchConfiguration
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from launch_ros.substitutions import FindPackageShare
import yaml


def launch_setup(context, *args, **kwargs):
    # vehicle information parameter
    vehicle_param_path = LaunchConfiguration("vehicle_param_file").perform(
        context
    )
    with open(vehicle_param_path, "r") as f:
        vehicle_param = yaml.safe_load(f)["/**"]["ros__parameters"]

    # common parameter
    with open(
        LaunchConfiguration("common_param_path").perform(context), "r"
    ) as f:
        common_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    # nearest search parameter
    with open(
        LaunchConfiguration("nearest_search_param_path").perform(context), "r"
    ) as f:
        nearest_search_param = yaml.safe_load(f)["/**"]["ros__parameters"]

    # smoother param
    with open(
        LaunchConfiguration("motion_velocity_smoother_param_path").perform(
            context
        ),
        "r",
    ) as f:
        motion_velocity_smoother_param = yaml.safe_load(f)["/**"][
            "ros__parameters"
        ]
    with open(
        LaunchConfiguration(
            "behavior_velocity_smoother_type_param_path"
        ).perform(context),
        "r",
    ) as f:
        behavior_velocity_smoother_type_param = yaml.safe_load(f)["/**"][
            "ros__parameters"
        ]

    # behavior velocity planner
    with open(
        LaunchConfiguration("blind_spot_param_path").perform(context), "r"
    ) as f:
        blind_spot_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    with open(
        LaunchConfiguration("crosswalk_param_path").perform(context), "r"
    ) as f:
        crosswalk_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    with open(
        LaunchConfiguration("walkway_param_path").perform(context), "r"
    ) as f:
        walkway_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    with open(
        LaunchConfiguration("detection_area_param_path").perform(context), "r"
    ) as f:
        detection_area_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    with open(
        LaunchConfiguration("intersection_param_path").perform(context), "r"
    ) as f:
        intersection_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    with open(
        LaunchConfiguration("stop_line_param_path").perform(context), "r"
    ) as f:
        stop_line_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    with open(
        LaunchConfiguration("traffic_light_param_path").perform(context), "r"
    ) as f:
        traffic_light_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    with open(
        LaunchConfiguration("virtual_traffic_light_param_path").perform(
            context
        ),
        "r",
    ) as f:
        virtual_traffic_light_param = yaml.safe_load(f)["/**"][
            "ros__parameters"
        ]
    with open(
        LaunchConfiguration("occlusion_spot_param_path").perform(context), "r"
    ) as f:
        occlusion_spot_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    with open(
        LaunchConfiguration("no_stopping_area_param_path").perform(context),
        "r",
    ) as f:
        no_stopping_area_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    with open(
        LaunchConfiguration("run_out_param_path").perform(context), "r"
    ) as f:
        run_out_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    with open(
        LaunchConfiguration("speed_bump_param_path").perform(context), "r"
    ) as f:
        speed_bump_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    with open(
        LaunchConfiguration("out_of_lane_param_path").perform(context), "r"
    ) as f:
        out_of_lane_param = yaml.safe_load(f)["/**"]["ros__parameters"]
    with open(
        LaunchConfiguration("behavior_velocity_planner_param_path").perform(
            context
        ),
        "r",
    ) as f:
        behavior_velocity_planner_param = yaml.safe_load(f)["/**"][
            "ros__parameters"
        ]

    behavior_velocity_planner_component = ComposableNode(
        package="behavior_velocity_planner",
        plugin="behavior_velocity_planner::BehaviorVelocityPlannerNode",
        name="behavior_velocity_planner",
        namespace="",
        remappings=[
            ("~/input/path_with_lane_id", "path_with_lane_id"),
            ("~/input/vector_map", "/map/vector_map"),
            ("~/input/vehicle_odometry", "/localization/kinematic_state"),
            ("~/input/accel", "/localization/acceleration"),
            (
                "~/input/dynamic_objects",
                "/perception/object_recognition/objects",
            ),
            (
                "~/input/no_ground_pointcloud",
                "/perception/obstacle_segmentation/pointcloud",
            ),
            (
                "~/input/compare_map_filtered_pointcloud",
                "compare_map_filtered/pointcloud",
            ),
            (
                "~/input/vector_map_inside_area_filtered_pointcloud",
                "vector_map_inside_area_filtered/pointcloud",
            ),
            (
                "~/input/traffic_signals",
                "/perception/traffic_light_recognition/traffic_signals",
            ),
            (
                "~/input/external_traffic_signals",
                "/external/traffic_light_recognition/traffic_signals",
            ),
            (
                "~/input/external_velocity_limit_mps",
                "/planning/scenario_planning/max_velocity_default",
            ),
            (
                "~/input/virtual_traffic_light_states",
                "/awapi/tmp/virtual_traffic_light_states",
            ),
            (
                "~/input/occupancy_grid",
                "/perception/occupancy_grid_map/map",
            ),
            ("~/output/path", "path"),
            (
                "~/output/stop_reasons",
                "/planning/scenario_planning/status/stop_reasons",
            ),
            (
                "~/output/infrastructure_commands",
                "/planning/scenario_planning/status/infrastructure_commands",
            ),
            ("~/output/traffic_signal", "debug/traffic_signal"),
        ],
        parameters=[
            nearest_search_param,
            behavior_velocity_planner_param,
            blind_spot_param,
            crosswalk_param,
            walkway_param,
            detection_area_param,
            intersection_param,
            stop_line_param,
            traffic_light_param,
            virtual_traffic_light_param,
            occlusion_spot_param,
            no_stopping_area_param,
            vehicle_param,
            run_out_param,
            speed_bump_param,
            out_of_lane_param,
            common_param,
            motion_velocity_smoother_param,
            behavior_velocity_smoother_type_param,
        ],
        extra_arguments=[
            {
                "use_intra_process_comms": LaunchConfiguration(
                    "use_intra_process"
                )
            }
        ],
    )

    container = ComposableNodeContainer(
        name="behavior_planning_container",
        namespace="",
        package="rclcpp_components",
        executable=LaunchConfiguration("container_executable"),
        composable_node_descriptions=[
            behavior_velocity_planner_component,
        ],
        output="screen",
    )

    group = GroupAction(
        [
            container,
        ]
    )

    return [group]


def generate_launch_description():
    launch_arguments = []

    def add_launch_arg(name: str, default_value=None, description=None):
        launch_arguments.append(
            DeclareLaunchArgument(
                name, default_value=default_value, description=description
            )
        )

    # vehicle parameter
    add_launch_arg("vehicle_param_file")

    # interface parameter
    add_launch_arg("map_topic_name", "/map/vector_map", "input topic of map")

    # package parameter

    # component
    add_launch_arg(
        "use_intra_process",
        "false",
        "use ROS 2 component container communication",
    )
    add_launch_arg("use_multithread", "false", "use multithread")

    # for points filter of run out module
    add_launch_arg("use_pointcloud_container", "true")
    add_launch_arg("container_name", "pointcloud_container")

    set_container_executable = SetLaunchConfiguration(
        "container_executable",
        "component_container",
        condition=UnlessCondition(LaunchConfiguration("use_multithread")),
    )
    set_container_mt_executable = SetLaunchConfiguration(
        "container_executable",
        "component_container_mt",
        condition=IfCondition(LaunchConfiguration("use_multithread")),
    )

    return launch.LaunchDescription(
        launch_arguments
        + [
            set_container_executable,
            set_container_mt_executable,
        ]
        + [OpaqueFunction(function=launch_setup)]
    )
