# Tutorial: Installing CAL with ERIKA Enterprise

<a id="Introduction"></a>

### Introduction

This tutorial describes all the steps to follow in order to install the tools needed to compile and run projects in CAL language on a [Lattice Mico32 platform](http://www.latticesemi.com/products/intellectualproperty/ipcores/mico32/index.cfm).

For a brief introduction on the CAL language have a look at [Brief introduction to the CAL language](Brief_introduction_to_the_CAL_language--1768.md "Brief introduction to the CAL language")

The tutorial has been tested on the FPG-EYE board produced by Evidence in which we've integrated an FPGA using a Mico32 processor.
The operating system chosen is an Ubuntu 10.10 maverick running on a virtual machine, anyway the installation process could be adapted to almost all other Linux releases on virtual or physical machines.

<a id="Note_for_Linux_Users"></a>

### Note for Linux Users

Since it has to be used a Linux distribution please look carefully at the following warnings:

1. The Evidence package installation path should NOT contain directory name with spaces. e.g. use ~/Evidence.
2. The actorsproject package installation path should NOT contain directory name with spaces: e.g. use ~/opendf/trunk/contrib/actorsproject.
3. It is strongly encouraged to adopt real paths instead of using symbolic links and aliases.
4. Please install all the ACTORS project compilers into their default directory. For instance, given the ACTORS project repository is installed in ~/opendf/trunk/contrib/actorsproject the compilers will have to be located in ~/opendf/trunk/contrib/actorsproject/bin

<a id="Prerequisites"></a>

### Prerequisites

As a first step you have to download the ERIKA's Enterprise repository where you will find, among other things, the CAL language libraries (specifically adapted to work in Erika Enterprise), system actors created in C language and a couple of demos that can be compiled and run.
Secondly install ERIKA Enterprise and RT-Druid on Linux. Both steps can be accomplished just following [Tutorial: Installing ERIKA and RT-Druid on a Linux host](Tutorial_Installing_ERIKA_and_RT-Druid_on_a_Linux_host--1721.md "Tutorial: Installing ERIKA and RT-Druid on a Linux host").

In the follow-up of this tutorial we will assume that you've correctly stored the ERIKA's repository in ~/Evidence/Erika and installed the eclipse\_3\_6\_ready\_to\_use\_LINUX\_201101111314 version of ERIKA'S Enterprise under the ~/Evidence folder, in order to find the eclipse directory under ~/Evidence/eclipse

Create then a virtual machine with Ubuntu 10.10 maverick as guest operating system. In our example we've used VMware Player 3.1.3 and installed WMware tools for linux version 8.4.5 version. Anyway all the tests can be smoothly deployed on a Linux physical machine.

After creating the virtual machine, before proceeding with the installation process, it would be useful to completely update the packages installed in your system to the latest version. To update all the packages open a Terminal window and execute the following commands:

```
sudo apt-get update
sudo apt-get upgrade
```

Now install all the packages that will be needed to compile our projects. Type:

```
sudo apt-get install java-common sun-java6-bin sun-java6-jre sun-java6-jdk sun-java6-source
sudo apt-get install ant subversion csh gawk libxml2-dev libsdl1.2-dev libgtk2.0-dev
```

<a id="Downloading_the_OpenDF_repository_and_the_ACTORS_project_source_code"></a>

### Downloading the OpenDF repository and the ACTORS project source code

You are now ready to download the OpenDF repository on your system (i.e. in ~/opendf):

```
mkdir opendf
cd opendf
svn co https://opendf.svn.sourceforge.net/svnroot/opendf/trunk
```

Under the OpenDF's project repository you will find all the ACTORS project source code needed for our purpose in: ~/opendf/trunk/contrib/actorsproject. Move to this directory and install the tools provided for the compilation of CAL projects by writing in a Terminal window:

```
make
make install
```

Now you have all the tools needed to convert CAL files into C language (xlim2c compiler and others) under the directory:~/opendf/trunk/contrib/actorsproject/bin

<a id="Installing_LatticeMico32_System_and_ispVM_System_on_Linux"></a>

### Installing LatticeMico32 System and ispVM System on Linux

The LatticeMico32 System is used to implement the LatticeMico32 soft microprocessor and attached peripheral components in a Lattice FPGA. It contains integrated tools that combine with ispLEVER software (which includes ispVM System) to coordinate the building of an embedded processor system on an FPGA device and write the software to drive it. All the software we will use can be downloaded from the [Lattice Semiconductor site](http://www.latticesemi.com); for our tutorial we've chosen the 8.0.00.63 version for Linux of the LatticeMico32 System and the 17.6 version for Linux of the ispVM System. Lattice Diamond doesn't work (yet) with Erika.

Download the RL8.0.00.63.43.09\_linux\_lm32.tar file and put it on your hard disk, for instance in ~/temp\_lattice. After having created in your home the ~/Lattice folder follow the steps reported below:

```
cd ~/temp_lattice
tar xf RL8.0.00.63.43.09_linux_lm32.tar
cd ../Lattice/
../temp_lattice/RL8.0.00.63.43.09_lm32/mico32_install.csh /home/user/temp_lattice/RL8.0.00.63.43.09_lm32
rm -R ~/temp_lattice
```

Accept all the terms and agreements you will be prompted. When asked, tell the setup to install both gtool and Lattice Mico32 System Tools and point out you are not installing neither from a dvd drive, nor from a cd one.

Next install ispVM System on your virtual machine; put the ispvm\_v17\_6\_linux.tar.gz file on a newly created ~/temp\_ispvm directory, create the ~/Lattice/ispvm folder and follow the steps reported below:

```
cd ~/temp_ispvm
tar -xvzf ispvm_v17_6_linux.tar.gz 
mv isptools/ ../Lattice/ispvm/
cd ~ && rm -R ~/temp_ispvm
```

<a id="Exporting_environment_variables"></a>

### Exporting environment variables

Before launching for the first time the LatticeMico32 System we have to create and export some environment variables needed to compile projects into LatticeMico32 System.
Open the ~/.profile file with a text editor (i.e. Gedit) and append the following lines:

```
export ISPVM_DIR=/home/user/Lattice/ispvm/isptools/ispvmsystem/
export RTDRUID_ECLIPSE_HOME=/home/user/Evidence/eclipse
export ERIKA_FILES=/home/user/Evidence/Erika/ee
export CAL_BASE=/home/user/opendf/trunk/contrib/actorsproject
export ACTORS_JAVA=/usr/bin/java
```

Open a new Terminal window and export the newly created environment variables by copying the very same lines you've just added. Or, if you prefer, relog into your system.

<a id="Launch_LatticeMico32_System_and_compile_a_CAL_application_with_ERIKA_Enterprise"></a>

### Launch LatticeMico32 System and compile a CAL application with ERIKA Enterprise

Employing the same Terminal window used previously to export the environment variables move to the directory where LatticeMico32 System resides and launch the executable file:

```
cd ~/Lattice/micosystem
./LatticeMico32Launcher
```

Finally compile and run a CAL application with ERIKA Enterprise following the [Tutorial: Compiling a CAL application with ERIKA Enterprise](Tutorial_Compiling_a_CAL_application_with_ERIKA_Enterprise--1757.md "Tutorial: Compiling a CAL application with ERIKA Enterprise").

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Tutorial%3A_Installing_CAL_with_ERIKA_Enterprise) · [Archived source revision 3932](http://erika.tuxfamily.org/wiki/index.php?oldid=3932)
- Last source edit: 2011-10-18T15:26:12Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Ryosab81, Paolo.gai, Dibbe, Nicola.
- [Original MediaWiki source](../source/wikitext/1755.mediawiki) · [Original editing history](../source/history/batch-011.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
