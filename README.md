# ROS_TP_NOTER

### (1) Open a terminal and use the following commands:

```
source catkin_ws/devel/setup.bash
```
#### Then run roscore
```roscore```

### (2) Open another terminal and repeat the source command in (1)
### Then run the node 
```rosrun maeker_visualization publish_marker.py```

### (3) Repeat step (2) for the other node and run them

### (4) run the rostopic command in another terminal, to verify if all the topics are running correctly
##### (1)
```source catkin_ws/devel/setup.bash```
##### (2)
```rostopic list```
### Then run the command rviz 
```rviz```

### (5) In the rviz desktop, click the add button and go to topic and select the topic that you want to add
