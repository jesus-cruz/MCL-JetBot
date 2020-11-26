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

### Jetbot environment installation
1. Update Ubuntu to the last version

  ``` sudo apt update ```
  ``` sudo apt upgrade ```
  
2. Download the jetbot repositoy from github



