# Writing a mono-stack with nested interrupts

<a id="Reference_test"></a>

#### Reference test

examples/s12xs/porting\_examples/EEtest5

<a id="Description"></a>

#### Description

- The test below tests the behavior which may happen with nested interrupts.
- The goal is to test the execution of the interrupts with different priorities. A low priority ISR is interrupted by a high priority interrupt repeatedly. The goal is to obtain that all ISR routines execute with the proper status registers.
- The isr configuration is architecture dependent. In this case we modified the vector\_s12x.c file.

- Finally, we created inside the EEtest5 a C file with a main() function. That function explicitly calls the function for periodic interrupt timer configuration and finishing with a for(;;). Please note that this small application can be executed to test again the behaviour of the interrupt stub. The compilation must finish with an executable fully linked.

- Note1: As the previous test for correct interrupt execution we should take care of the interrupt stub and the following functions EE\_ISR2\_prestub, EE\_ISR2\_poststub (see the header file ee\_irqstub.h at the path ee\pkg\cpu\cosmic\_hs12xs\inc).

<a id="Expected_output"></a>

#### Expected output

When everything is done in the right way, with the following commands we can have the executable file:

- open a Cygwin shell
- cd into the Debug directory
- the commands make clean and make all should work correctly producing an executable inside the Debug directory.

To simulate the application we can use directly the hardware or a "good" software debugger.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Writing_a_mono-stack_with_nested_interrupts) · [Archived source revision 1650](http://erika.tuxfamily.org/wiki/index.php?oldid=1650)
- Last source edit: 2009-11-25T14:52:44Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds.
- [Original MediaWiki source](../source/wikitext/1470.mediawiki) · [Original editing history](../source/history/batch-013.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
