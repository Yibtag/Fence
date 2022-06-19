# Fence
## What is fence?
Fence is a simple program for encrypting files.
## How to use it?
## Installation
This software only supports windows. It does not have an installer yet so you will have to install it manually.

### 1.Downloading the program


Download the [exe](https://github.com/Yibtag/Fence/blob/main/bin/fence.exe) from the bin folder in this repo.

Then go to your program files folder in windows and create a new folder called fence. Then drag and drop the [exe](https://github.com/Yibtag/Fence/blob/main/bin/fence.exe) into the folder.

![How to install](./assets/README%20assets/how_to_install_1.gif)


### 2.Setting up environment  variables

Go to the folder where you put your exe and copy the path.

Then navigate to the environment variables
by right clicking on the windows icon scrolling down clicking advanced system options.Then click environment  variables. Go under system variables and double chick the variable called path then click on new and paste the path you have copied from before.

![How to env](./assets/README%20assets/how_to_create_env.gif)


## Using the tool

Chose a file you want to encrypt then copy the path and open up the command prompted. And use the following commands:

### fence -e \<file\>: For encrypting a file.

### fence -d \<file\>: For decrypting a file.