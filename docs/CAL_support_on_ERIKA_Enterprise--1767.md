# CAL support on ERIKA Enterprise

<a id="Introduction"></a>

### Introduction

In this tutorial we will explain all the solutions adopted to integrate the CAL language and the ACTORS source code inside Erika Enterprise.
First of all we will give a quick overview of the directories where all the source code related to the CAL language can be found along with demos specifically created for a Lattice Mico32 platform.
In the following we will explain the choices we made to integrate the ACTORS code in Erika and what has been done to compile projects in Erika Enterprise.
A preliminary knowledge of the ACTORS project and the CAL language, even if not mandatory, could be useful to the reader so it is suggested to have a look at [Brief introduction to the CAL language](Brief_introduction_to_the_CAL_language--1768.md "Brief introduction to the CAL language").

<a id="Directories_created_in_the_ERIKA.27s_repository_to_support_the_CAL_language"></a>

### Directories created in the ERIKA's repository to support the CAL language

The source code for the CAL language can be found inside the ERIKA's repository in the cal directory, under: ee/contrib.
The files have been stored using the following criteria:

- cfg: here you will find the cfg.mk file, needed by the ERIKA's Enterprise toolchain to compile CAL projects along with makefiles coming from the ACTORS project and opportunely modified to integrate them in ERIKA.
- inc: here we placed the library prototypes coming from the ACTORS project and cal\_redefinitions.h where we redefined some methods and types not usable in ERIKA's Enterprise.
- src: here we stored the modified version of ACTORS' library actors-rts.c along with source code (in C and CAL languages) for system actors art\_led and art\_switch.

In addition we've created two CAL project demos for our FPG-EYE using both CAL actors and system actors. All the related code can be found in cal\_demo and cal\_demo\_cal\_actors directories under ee/examples/mico32/demo/sw\_projects/.

<a id="Integration_of_the_CAL_language_in_ERIKA"></a>

### Integration of the CAL language in ERIKA

From the actorsproject directory in the OpenDF's repository we've extrapolated libraries and makefiles needed for our integration. Our main goal was to realize working CAL projects into a specific environment, the ERIKA Enterprise, so that some adjustments to the ACTORS' libraries were to be undertaken.
All the code that can't be employed in ERIKA, as you can see for instance in actors-rts.c library, has been placed under #ifndef \_\_ERIKA\_\_ so that the library results untouched if the build process is taken outside the ERIKA'S Enterprise.
In addition we'we created the file cal\_redefinitions.h where we've redefined all the methods and types present in the ACTORS' libraries which can't be used into ERIKA Enterprise.

Our main efforts were focused on adjusting the ACTORS' makefiles so that it is possible, as you can see in [Tutorial: Compiling a CAL application with ERIKA Enterprise](Tutorial_Compiling_a_CAL_application_with_ERIKA_Enterprise--1757.md "Tutorial: Compiling a CAL application with ERIKA Enterprise"), to smoothly build a CAL project inside ERIKA. This has been accomplished by integrating in the makefiles chain:

- cfg.mk: this file is included by ERIKA Enterprise when building CAL projects. Here are listed the source code libraries to include when building projects (mainly actors-rts.c). In addition you find a variable, called SYS\_ACTORS where all the system actors (in C language) we've created are listed. These actors will be used to create at build time the library libactors.a. Notice that if you want to add a newly created system actor it has to be placed in the same directory where the others already reside (so in cal/src) and append its source name to the SYS\_ACTORS variable in order to build your project.
- actors.mk: this file was called makefile in the ACTORS' repository. This is the starting point for the elaboration of CAL and netlist files into C files.
- makemodel.mk: this is the main ACTORS makefile where the elaboration of the actors is accomplished in order to create C source code.
- definitions.mk: here you can basically find the definition of all the paths where the ACTORS' tools can be found.

<a id="Creation_of_a_CAL_project_in_ERIKA"></a>

### Creation of a CAL project in ERIKA

In order to better understand the basics about projects in ERIKA please have a look at [Tutorial: RT-Druid and OIL basics](Tutorial_RT-Druid_and_OIL_basics--1658.md "Tutorial: RT-Druid and OIL basics").

One of the main points we had to face in our job was how to integrate the CAL main application into ERIKA. The ACTORS makefiles create as a default a main method in the C file elaborated from the netlist. As an example, if you have a netlist file called switchled.nl the ACTORS makefiles will create the switchled.c with a main method defined inside. This is not desired in ERIKA since the main method is defined elsewhere, in main.c for example (which is one of the mandatory files to create projects in ERIKA Enterprise). To overcome this problem we edit at compile time the switchled.c file in order to have a main\_cal method which is then encapsulated into an ERIKA's task. This task is defined in main.c, it's named calTask in our examples as you can see at [Tutorial: Compiling a CAL application with ERIKA Enterprise](Tutorial_Compiling_a_CAL_application_with_ERIKA_Enterprise--1757.md "Tutorial: Compiling a CAL application with ERIKA Enterprise") and calls the main\_cal function using the most suited argv variable to launch the CAL runtime process. Please notice that there is a check on the definition of CAL\_STATISTICS which is one of of the ERIKA Enterprise options that has been added to the conf.oil file.

In the main function there are moreover the calls at EE\_cal\_init and EE\_cal\_start methods that are declared and defined in cal/inc/ee\_cal.h and cal/src/ee\_cal.c and whose tasks are to initialize some FPG-EYE components and activate the calTask.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=CAL_support_on_ERIKA_Enterprise) · [Archived source revision 2636](http://erika.tuxfamily.org/wiki/index.php?oldid=2636)
- Last source edit: 2011-02-15T16:59:33Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Ryosab81, Paolo.gai.
- [Original MediaWiki source](../source/wikitext/1767.mediawiki) · [Original editing history](../source/history/batch-002.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
