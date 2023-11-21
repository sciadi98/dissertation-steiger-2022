# Sharp Force Trauma (SFT) models

This document is a guide to use the the machine algorithms to predict serration and blade bevel using the following traits:
- **General morhology of the kerf shape:** Ellipse, D shape or Indeterminate
- **Shape of the cross-profile (entrance and exit):** V shape or Y shape
- **Location of the rising profile (entrance and exit):** single, bilateral or absent
- **Presence or absence of feathering:** present or absent
- **Presence or absence of shards:** present or absent
- **Location (entrance, center and exit):** single, bilateral or absent
- **General morphology of the mounding:** marked, not marked or absent


## Supported versions:

- Python 3 
- JupyterLab (Jupyter Notebook not tested)

## Before starting please download the .zip file at https://github.com/sciadi98/dissertation-steiger-2022/archive/refs/heads/main.zip and unzip it


## Windows 10/11
### Installation
Download Python at https://www.python.org/downloads/ 

*How to install Python*
1. Run the installer

![Alt text](figures/image-1.png)

3. Click "Install Now"
4. Disable "Path length limit" > close

![Alt text](figures/image-2.png)

*How to install the dependencies*

1. Double click on "install.bat file"
2. The install of the dependecies could require several seconds, wait until the terminal closes itself

**The installation steps must be executed only one time. If you move the main directory after the installation of the dependencies the app will stop working and it must be unistalled (delete main directory) and re install it**

### App

*How to prepare the data*
1. Use the template provided in the main directory (dissertation_steiger_2022)
2. The template can be filled with the following variables (see example in the template spreadsheet): E, D or I (shape);  V or I/ (profile shape); single, bilateral or absent (rising); present or absent (shards); present or absent (feathering); single, bilateral or absent (mounding location); marked, not marked or absent (mounding general)

> [!WARNING]  
> It's imperative to have the file excel in the main directory "dissertation_steiger_2022" otherwise it won't be loaded correctly.

*How to run the app*
1. Go in the unzipped dissertation-steiger-2022-main directory
2. Double click on "SFT_analysis.bat" file
3. Follow the instructions on the terminal



## MacOS
Download Python at https://www.python.org/downloads/
### Installation 
*How to install Python* 
1. After accepting user agreement > Install > close

![Alt text](figures/image-3.png)

2. Double click on install.certificates.cmd 

![Alt text](figures/image-4.png)

3. execute > close the terminal 

![Alt text](figures/image-5.png)

*How to install dependencies*

1. Right click "install.command" file > click open > click open > Open app
2. Wait until the session is finished, then close the terminal (the process could take several seconds)

**The installation steps must be executed only the first time. If you move the main directory after the installation of the dependencies the app will stop working and it must be unistalled (delete main directory) and re install it**

### App

*How to prepare the dataset*
1. Use the template provided in the main directory
2. The template can be fill with the following variables: E, D or I (shape);  V or I/ (profile shape); single, bilateral or absent (rising); present or absent (shards); present or absent (feathering); single, bilateral or absent (mounding location); marked, not marked or absent (mounding general morphology)

> [!WARNING]  
> It is imperative to have the file excel in the main directory "dissertation_steiger_2022" otherwise it won't be loaded correctly

*How to run the app*
1. Go in the unzipped dissertation-steiger-2022-main directory
2. Right click "SFT_analysis.command" file > open > open
3. Follow the instructions on the terminal

![Alt text](figures/image-8.png)
![Alt text](figures/image-7.png)


## Linux

### Installation
#### Ubuntu or Debian derivatives

```
$ sudo apt install python3
````
#### openSUSE
Python is already pre-installed on openSUSE, if not execute:
```
$ sudo zypper install python3
```
#### Fedora or RedHat derivatives
Python is already pre-installed on Fedora, if not execute :
```
$ sudo dnf install python3
```
#### Arch derivatives
```
$ sudo pacman -S python3
```
*How to install the dependencies"
1. Open a terminal and execute "install.sh"


### App

*How to prepare the dataset*

1. Use the template provided in the main directory
2. The template can be fill with the following variables: E, D or I (shape);  V or I/ (profile shape); single, bilateral or absent (rising); present or absent (shards); present or absent (feathering); single, bilateral or absent (mounding location); marked, not marked or absent (mounding general morphology)

> [!WARNING]  
> It is imperative to have the file excel in the main directory "dissertation_steiger_2022" otherwise it won't be loaded correctly


*How to open app* 
1. Open a terminal > execute "SFT_analysis"




