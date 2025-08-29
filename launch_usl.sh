#!/bin/bash
echo "--- USL System Master Launch Script ---"
echo "This will open several new terminal windows."

# Define the workspace directory
WORKSPACE_DIR=~/usl_drone_project

# The command to source the environment in each new terminal
SOURCE_CMD="source /opt/ros/jazzy/setup.bash && source $WORKSPACE_DIR/install/setup.bash"

# Launch Gazebo in its own terminal
gnome-terminal --title="GAZEBO" --working-directory=$WORKSPACE_DIR -- bash -c "$SOURCE_CMD; echo '--- Launching Gazebo ---'; ros2 launch usl_drone_project usl_gazebo.launch.py; exec bash"

# Wait for Gazebo to initialize
echo "Waiting 10 seconds for Gazebo to start..."
sleep 10

# Launch the core USL nodes, each in its own terminal
gnome-terminal --title="USL Orchestrator" --working-directory=$WORKSPACE_DIR -- bash -c "$SOURCE_CMD; echo '--- Launching USL Main ---'; ros2 run usl_drone_project usl_main; exec bash"
gnome-terminal --title="Command Gate" --working-directory=$WORKSPACE_DIR -- bash -c "$SOURCE_CMD; echo '--- Launching Command Gate ---'; ros2 run usl_drone_project usl_command_gate; exec bash"
gnome-terminal --title="Adaptive Controller" --working-directory=$WORKSPACE_DIR -- bash -c "$SOURCE_CMD; echo '--- Launching Adaptive Controller ---'; ros2 run usl_drone_project usl_adaptive_controller; exec bash"
gnome-terminal --title="Intent Translator" --working-directory=$WORKSPACE_DIR -- bash -c "$SOURCE_CMD; echo '--- Launching Intent Translator ---'; ros2 run usl_drone_project usl_intent_translator; exec bash"

echo ""
echo "--- All Core Systems Launched ---"
echo "The Gazebo simulation and all USL nodes are now running in new windows."
echo "You can now run the mover test in a new terminal."
