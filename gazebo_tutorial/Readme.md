# Gazebo tutorial
Available at https://gazebosim.org/docs/harmonic/building_robot/ (Use https://gazebosim.org/docs/latest/building_robot/ for latest)
- Specification is available at http://sdformat.org/spec?ver=1.8&elem=sdf

# Steps
- Created a 3 wheeled object with basic links and joints. Run with `gz sim robot.sdf`
- Move the robot.
    - Set the plugin in world that enables and controls movement with respect to wheels. This exposes an input topic for commands. Messages can be sent to this - `gz topic -t "/cmd_vel" -m gz.msgs.Twist -p "linear: {x: -35.5, y: 54.9}, angular: {z: 0.125}"`
    - Set a UI plugin (`Key Publisher`) that captures keypresses.
    - Set the plugin in world that forwards key press topic messages to motion controller input topic. For monitoring any topic - `gz topic -e -t <topic>`.
- Add custom world with custom GUI config and including models from local and URL.
    - Use `gz topic -e -t /world/custom_world/stats` for listening to world stats.
    - Use https://app.gazebosim.org/dashboard for pre built models and worlds.
- Sensors, Controller node, Launch file -
    - Add contact sensor to wall. Add IMU and Lidar to car. Lidar requires dedicated frame because it's position is dynamic and the information it generates is relative to objects other than the car.
    - Add custom controller logic in a lidar_node.cc code to listen to one topic (/lidar) and depending on data send movement directions to another topic(/cmd_vel).
    - Launch file is for composing multiple nodes.
- Lots of information about GUI - https://gazebosim.org/docs/harmonic/gui/
- Dynamically loading models into world -
    - World exposes a Create service for entity -
    ```
    % gz sim empty.sdf

    % gz service -l | grep create

    /world/empty/create
    /world/empty/create_multiple

    % gz service -is /world/empty/create
    
    Service providers [Address, Request Message Type, Response Message Type]:
    tcp://172.17.0.1:32833, gz.msgs.EntityFactory, gz.msgs.Boolean
    ```
    - Call this to inject model 
    ```
    % gz service -s /world/empty/create --reqtype gz.msgs.EntityFactory --reptype gz.msgs.Boolean --timeout 1000 --req 'sdf_filename: "./gazebo_tutorial/models/rrbot.urdf", name: "urdf_model"'

    data: true
    ```

# References
- Tutorial code available at https://github.com/gazebosim/docs/tree/master/harmonic/tutorials
- Example scripts, plugins and worlds for GZ SIM are available at https://github.com/gazebosim/gz-sim/tree/gz-sim8/examples
- Full list of sensors supported by GZ SIM are available at https://github.com/gazebosim/gz-sensors
