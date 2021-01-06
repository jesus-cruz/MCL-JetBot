# Jetbot environment installation in Ubuntu
## WLS or VirtualBox
The Windows Subsystem for Linux is a little more complicated (more steps). Installing a virtual machine using Virtual Box is easier, because it already comes with an X-server
### WSL Installation
If you want to use WSL then follow the next two tutorials
1. [WSL installation](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
2. [Using WSL 2 with X-Server — Linux on Windows](https://medium.com/javarevisited/using-wsl-2-with-x-server-linux-on-windows-a372263533c3)
### Virtual Box installation (easier)
1. Download and install Virtual Box from [virtualbox.org](https://www.virtualbox.org/)
2. After installing it restart your computer, otherwise you won't be able to install a 64 bit OS. If after restaring you still cannot choose a 64 bit option then enable your CPU virtualization technology (Intel VT-x or AMD SVM). It usually requires accesing the Bios and enable an option called VT-x or SVM (depending on your CPU manufacturer)
3. Download ubuntu from [ubuntu.com/download](https://ubuntu.com/download/desktop)
4. Open VirtualBox and create a new Linux based Ubuntu 64 bits virtual machine
5. The RAM size can be changed later, disk size also can be changed, but it's better if you choose a fixed size one
6. Once the virtual machine has been created, boot it. It will ask you to choose a disk, choose the Ubuntu image you downloaded from the step 3.
7. Proceed with the installation. At the end you should have a working Ubuntu VM.
8. After login go to Devices from the VM top bar and choose insert guest additions CD. Proceed wit the installation. At the end a restart (of the VM) will be required.

### Jetbot environment installation
Follow the next steps

Update Ubuntu to the last version

  ``` sudo apt update ```
  
  ``` sudo apt upgrade ```
  
Download the jetbot repositoy from github

``` wget https://github.com/NVIDIA-AI-IOT/jetbot/archive/master.zip ```

Extract it

Install the next python packages

```pip sudo apt install python3```

```pip sudo apt install python3-pip```

```pip3 install trailets```

```pip3 install opencv-python```

```pip3 install ipywidgets```

```pip3 install --upgrade setuptools```

```pip3 install RPI.GPIO```

```pip3 install adafruit-circuitpython-motorkit```

```pip3 install Adafruit-MotorHAT```

Open and edit the file ``` jetbot-master/projects/jetbot/__init__.py ```:  comment lines 5 and 6

Create a file helloWorld.py at jetbot-master with the given contents 

```
from jetbot import Robot

print("Hello World")
```
Then do

```python3 helloWorld.py```

You should see a Hello World message in the terminal

## ROS Tutorial
* [Script-based tutorial](https://www.jetsonhacks.com/2019/10/23/install-ros-on-jetson-nano/)
* [jetbot_ros repo](https://github.com/dusty-nv/jetbot_ros)

### TO-DO
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es
https://ngc.nvidia.com/catalog/containers/nvidia:pytorch

