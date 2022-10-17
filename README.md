# turtlebot3_blockly
This is a modified version of the official [dabit-industries/turtlebot3_blockly](https://github.com/dabit-industries/turtlebot3_blockly) repository, which again is a fork of the private [aravindk2604/turtlebot3_blockly](https://github.com/aravindk2604/turtlebot3_blockly) repo, which was based on the 
[erlerobot/robot_blockly](https://github.com/erlerobot/robot_blockly.git) repo. 
There are two changes. Some modifications in the frontend/blockly submodule, so that the 'seconds' parameters (how long a block should run) is correctly used. Another modification is that this code is tested on a ROS Melodic system -  Ubuntu 18.04, with improved documentation.

You can now control TurtleBot3 using Blockly - drag and drop software developed by Google.

![](img/launchCode.png)

### GIF showing drag-drop of blocks

![](img/simpCode.gif)

### Prerequisites

```
python2.7 -m pip install --upgrade pip
python2.7 -m pip install autobahn
python2.7 -m pip install MAVProxy

python3.6 -m pip install cryptography==36.0.2 autobahn

sudo apt-get install curl gnupg2 lsb-release
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

sudo apt-get install ros-melodic-catkin
sudo apt-get install ros-melodic-mavros ros-melodic-mavros-extras
sudo apt-get install ros-melodic-turtlebot3-teleop
```

### Installation

```
mkdir -p ~/blockly_ws/src
cd ~/blockly_ws/src
git clone https://github.com/physar/turtlebot3_blockly.git
cd ~/blockly_ws/
source /opt/ros/melodic/setup.bash
catkin_make_isolated -j2 --pkg turtlebot3_blockly --install
```

### Launch

```
cd ~/blockly_ws
source install_isolated/setup.bash
roslaunch turtlebot3_blockly turtlebot3_blockly.launch
```

### Webinterface

Open your browser to access the now locally running blockly-webserver: [http://127.0.0.1:1036/](http://127.0.0.1:1036/)

If the webserver is up and running, the top-left item under 'Builder' should read 'Launch'. Don't forget to switch the Python radio-button to Python2, because that is the version still used by ROS Melodic.

![](img/launchCode.png)

### Documentation
- [TurtleBot3 Blockly Getting Started](http://turtlebot-3-blockly-wiki.rtfd.io/)
- [TurtleBot3 setup](http://turtlebot3.robotis.com/en/latest/hardware.html)
- [ROS Wiki](http://www.ros.org) 
