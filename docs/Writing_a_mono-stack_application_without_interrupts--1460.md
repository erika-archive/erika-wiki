# Writing a mono-stack application without interrupts

<a id="Reference_test"></a>

#### Reference test

examples/s12xs/porting\_examples/EEtest1

<a id="Description"></a>

#### Description

- The goal of this test is to activate a task to test the internal function ready2stacked. To configure the task set we change the files eecfg.h and eecfg.c located inside the Debug folder (the basic structure is inspired to the Microchip PIC30 port). At the end of the porting the task set configuration will be deducted from the .oil file.

- Finally, we created inside the EEtest1 a C file with a main() function. That function explicitly calls ActivateTask finishing with a for(;;). Please note that this small application can be executed to test the behavior of the kernel during a task activation. The function must be linked and used without problems resulting in an executable fully linked.

- Note1: At this point we have to write two functions: EE\_hal\_begin\_nested\_primitive and EE\_hal\_end\_nested\_primitive in the header file "ee\_internal.h" at the path ee\pkg\cpu\cosmic\_hs12xs\inc.
  - the two functions are used to:
    - begin: save the current status of the interrupt and disable them
    - end: restore the status saved before with the begin function

- Note2: Another header file to change is ee\_cpu.h that contains some useful macros and the types definitions.

- Note3: The TerminateTask () primitive is not part of this test and will be tested apart with a specific test.

<a id="Expected_output"></a>

#### Expected output

When everything is done in the right way, with the following commands we can have the executable file:

- open a Cygwin shell
- cd into the Debug directory
- the commands make clean and make all should work correctly producing an executable inside the Debug directory.

To simulate the application we can use directly the hardware or a "good" software debugger.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Writing_a_mono-stack_application_without_interrupts) · [Archived source revision 1648](http://erika.tuxfamily.org/wiki/index.php?oldid=1648)
- Last source edit: 2009-11-25T14:33:38Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds, Paolo.gai.
- [Original MediaWiki source](../source/wikitext/1460.mediawiki) · [Original editing history](../source/history/batch-013.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
