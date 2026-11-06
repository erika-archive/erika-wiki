# Tutorial: RT-Druid and OIL basics

OIL (OSEK Implementation Language) is a part of the OSEK/VDX standard, that isused for OS and application configuration.
The specification of the OIL file structure and syntax is provided in the OSEK/VDX web site at <http://www.osek-vdx.org>.
In the RT-Druid and in the Erika Enterprise RTOS the configuration of the system is defined inside an OIL file.
In this web page we only provide a quick introduction of the OIL Language (for a complete description see the documentation
at <http://erika.tuxfamily.org/documentation.html>), together with a specification of the specific OIL attributes implemented by RT-Druid.
In Erika Enterprise all the RTOS objects like tasks, alarms, resources, are static and predefined at application compile time.
To specify which objects exists in a particular application, Erika Enterprise uses the OIL Language, which is a simple text description language.
Here is an example of the OIL File for the dsPIC (R) DSC device:

CPU mySystem {

OS myOs {  

EE\_OPT = " DEBUG ";

CPU\_DATA = PIC30 {  

APP\_SRC = " code1.c";

APP\_SRC = " code2.c";

MULTI\_STACK = FALSE ;

ICD2 = TRUE;

};

MCU\_DATA = PIC30 {  

MODEL = 33 FFJ256GP710;

};

BOARD\_DATA = EE\_FLEX {  

USELEDS = TRUE;

}

};

TASK myTask {  

PRIORITY = 1;

STACK = SHARED ;

SCHEDULE = FULL;

};

TASK myTask {  

PRIORITY = 1;

STACK = SHARED ;

SCHEDULE = FULL;

};

};

The example contains a single object called CPU, which contains all the specifications and the values used by the system.
Inside the CPU, are described the objects which are present in the application:
an OS, which specifies the global attributes for the system, and, in the example, two TASKs.

The OIL File is parsed by the RT-Druid code generator and, as a result, part of the RTOS source code is generated and compiled
together with the application. An OIL file consists of two parts: a set of definitions and a set of declarations.
Definitions are used to define data types, constants and kernel objects that need to be provided in the declaration part for
configuring a specific kernel. In other words, the definition part tells the configurator that there exists different objects
like tasks, resources, and so on, describing their attributes and types, like in a C struct declaration. Then, the declaration part
is used to specify which objects are really present in a particular application.
In RT-Druid, the definition part of the OIL file is fixed and is contained inside the RT-Druid Eclipse Plugins.
The user has only to provide the declaration part, specifying for a particular application the objects to be created.

The OIL file basically contains the description of a set of objects. A CPU is a container of these objects.
Other objects include the following:

- OS is the Operating System which runs on the CPU. This object contains all the global settings which influence the compilation

process and the customization of the Erika Enterprise RTOS.

- APPMODE defines the different application mode. These modes are then used to control the autostart feature for tasks and alarms in the OIL file.
- TASK is an application task handled by the OS.
- RESOURCE is a resource (basically a binary mutex) used for mutual exclusion.
- EVENT is a synchronization flag used by extended tasks.
- COUNTER is a software source for periodic / one shot alarms.
- ALARM is a notification mechanism attached to a counter which can be used to activate a task, set an event, or call a function.

All the attributes in the OIL file can be:

- numbers, i.e. the PRIORITY attribute;
- strings, i.e. the APP\_SRC attribute;
- enumerations, i.e. the KERNEL\_TYPE attribute.

The OIL file includes a set of fields for controlling the command line parameters which are passed to the compiler tools.
The meaning of those elements is the following:

- EE\_OPT contains a list of additional compilation flags passed to the Erika Enterprise makefile.

In practice, the EE\_OPT makefile variable controls which files has to be compiled and with which options.
The EE\_OPT attributes are translated in #defines in the C code.

- CFLAGS contains the list of additional C compiler options.
- ASFLAGS contains the list of additional assembly options.
- LDFLAGS Contains the list of additional linker parameters.
- LDDEPS Contains the list of additional library dependencies which have to be added to the makefile rules.
- LIBS Contains the list of additional libraries that needs to be linked.

Example of declaration:

CPU mySystem {

OS myOs {  

EEOPT = " MYFLAG1 ";

EEOPT = " MYFLAG2 ";

CFLAGS = "-G0 ";

CFLAGS = "-O0 -g";

CFLAGS = "- Wall -Wl ,-Map -Wl , project .map ";

ASFLAGS = "-g";

LIBS = "-lm ";

...

};

...  
}

The CPU\_DATA section of the OS object is used to specify the configuration of a core in a single or in a multiple core device.
The MCU\_DATA section of the OS object is used to specify the configuration of peripherals which are present in a specific microcontroller.
The BOARD\_DATA section of the OS object is used to specify the configuration of the board where the microcontroller is placed.
For example, the board configuration includes the configuration of the external devices like leds, buttons, displays, and other peripherals.
The OIL file can specify a set of libraries which are distributed with or are supported by Erika Enterprise and that have to be linked
together with the application. The specification is done by using the LIB attribute.
The list of supported libraries depends on the target and can be found in the Erika Enterprise Manual for the specific target.
Libraries which are not directly supported by Erika Enterprise can be added directly by specifying the appropriate linker parameters in
the LDFLAGS attribute of the OS object.

<a id="Examples"></a>

### Examples

- [OIL file for Lattice Mico32](OIL_file_for_Lattice_Mico32--1659.md "OIL file for Lattice Mico32")
- [OIL file for Freescale S12](OIL_example_for_Freescale_S12--2224.md)

<a id="See_also"></a>

### See also

- [Tutorial: Installing ERIKA and RT-Druid, and compile your first application](Tutorial_PIC30_-_Installing_ERIKA_and_RT-Druid_and_compile_your_first_application--1637.md "Tutorial: Installing ERIKA and RT-Druid, and compile your first application")
- [EEOPT](EEOPT--2057.md "EEOPT")

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Tutorial%3A_RT-Druid_and_OIL_basics) · [Archived source revision 4716](http://erika.tuxfamily.org/wiki/index.php?oldid=4716)
- Last source edit: 2012-03-29T09:33:09Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds, Dibbe, Nicola.
- [Original MediaWiki source](../source/wikitext/1658.mediawiki) · [Original editing history](../source/history/batch-011.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
