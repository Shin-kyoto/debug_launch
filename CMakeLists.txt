cmake_minimum_required(VERSION 3.5)
project(debug_launch)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

install(
  PROGRAMS
  scripts/unzstd.py
  scripts/reindex.py
  scripts/play_reeval_planning.sh
  DESTINATION lib/${PROJECT_NAME}
)

ament_auto_package(
  INSTALL_TO_SHARE
  launch
  config
)
