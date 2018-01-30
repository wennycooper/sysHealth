#!/usr/bin/env python
# File name: sysHealth 
# Copyright (c) 2017,
# Latest Editor: ChienLiang, CHU (2017/06/19)
# Original Author: CLC
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Willow Garage, Inc. nor the names of its
#      contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import rospy
import sys
import time
import math
import tf
import os
import subprocess
import xmlrpclib

from std_msgs.msg import Bool

def check_health_status():
    
    m = xmlrpclib.ServerProxy(os.environ['ROS_MASTER_URI'])
    try:
        code, msg, val = m.getSystemState('/script')
        if code == 1:
            pubs, subs, srvs = val
            #print "call success"
        else:
            print "ROS_MASTER is down"
            #child.kill()
            child.terminate()
            sys.exit()
            
    except:
        print "call failed"
        #child.kill()
        child.terminate()
        sys.exit()

    pub_health_status()
    time.sleep(1)

def pub_health_status():
    health_status_pub = rospy.Publisher('/sysHealth', Bool, queue_size = 10)
    health_status_pub.publish(True)

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node("sysHealth",anonymous = False)
    rospy.loginfo("===== sysHealth node =====")
    rospy.loginfo(" o_0 hope everything goes well. o_0")
    #child = subprocess.Popen(["python","-m","SimpleHTTPServer","8080"])
    child = subprocess.Popen(["python","/home/kkuei/catkin_ws/src/sysHealth/script/wsSysHealth.py"])
    #os.system("cd catkin_ws/src/Rugby_Alpha/rugby/src/web/;python -m SimpleHTTPServer 8080")
    rospy.loginfo("===== SimpleHTTPServer Start =====")
    
    # Go to class functions that do all the heavy lifting. Do error checking.
    while not rospy.is_shutdown():
        check_health_status()
    if rospy.is_shutdown:
        rospy.loginfo("--Crash--//(ToT)//--Crash--")
         
    rospy.spin()
