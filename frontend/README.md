# turtlebot3_blockly
This is a modified version of the official [dabit-industries/turtlebot3_blockly](https://github.com/dabit-industries/turtlebot3_blockly) repository, which again is a fork of the private [aravindk2604/turtlebot3_blockly](https://github.com/aravindk2604/turtlebot3_blockly) repo, which was based on the 
[erlerobot/robot_blockly](https://github.com/erlerobot/robot_blockly.git) repo. 
There are two changes. Some modifications in the frontend/blockly submodule, so that the 'seconds' parameters (how long a block should run) is correctly used.

The code above points to the tag of the latest commit of aravindk2604 on this submodule, but this commit is actual performed in his branch [testChanges](https://github.com/aravindk2604/blockly/tree/testChanges/generators/python). The main branch has no turtlebot-specific blocks, and the branch [testTurtlebot](https://github.com/aravindk2604/blockly/tree/testTurtlebot/generators/python) actually contains the code to communicate with the older TurtleBot2.

###

See for the rest of the documentation the [README](../README.md) in the directory above.
