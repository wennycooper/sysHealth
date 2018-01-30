# sysHealth

This package provides sysHealth services for both web service on 8080 port and ros topic on /sysHealth

# Installation

    $ git clone this package to your catkin_ws/src
    $ rospack profile

# Dependancy
* You may need to install python web module with following command:

    $ sudo pip install lpthw.web
* You may need to modify the script pathname of Popen line in sysHealth.py 
    $ vi sysHealth

# Run

    $ rosrun sysHealth sysHealth.py

# Check
* HTTP browse http://ServerIP:8080/sysHealth   // You should see a 200 OK with "good"
* rostopic echo /sysHealth                     // You should see a "good" string


