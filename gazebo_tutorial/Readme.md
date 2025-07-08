# Gazebo tutorial
Available at https://gazebosim.org/docs/latest/building_robot/

# Steps
- Created a 3 wheeled object with basic links and joints.
- Move the robot.
    - Set the plugin in world that enables and controls movement with respect to wheels. This exposes an input topic for commands. Messages can be sent to this - `gz topic -t "/cmd_vel" -m gz.msgs.Twist -p "linear: {x: -35.5, y: 54.9}, angular: {z: 0.125}"`
    - Set a UI plugin (`Key Publisher`) that captures keypresses.
    - Set the plugin in world that forwards key press topic messages to motion controller input topic. For monitoring any topic - `gz topic -e -t <topic>`.
