# Overview
This follows the Ros2 turtlesim tutorial for CLI and rqt, given here - https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools.html

# Installation
- Followed Ubuntu installation given here, was done within few minutes. https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
- This does not work for Ubuntu 22.04 and ROS Jazzy distro. I am using Ubuntu 22.04 with ROS Humble distro.
- I am using Windows WSL to do all development on Ubuntu. Running nodes (even with simulators) and RQT works perfectly fine without any graphical issue.  

# How to Run

## 1. Using launch file
- `ros2 launch launch.yaml`

## 2. Individual nodes
- Run turtlesim node - `ros2 run turtlesim turtlesim_node --ros-args --params-file turtlesim_node.yaml`
- Run turtlesim teleop node - `ros2 run turtlesim turtle_teleop_key`


# Record
- Record events - `ros2 bag record -o subset /turtle1/pose /turtle1/cmd_vel`
- Replay events on sim - `ros2 bag play subset`
