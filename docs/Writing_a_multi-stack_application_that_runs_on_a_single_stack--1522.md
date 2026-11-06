# Writing a multi-stack application that runs on a single stack

<a id="Reference_test"></a>

#### Reference test

examples/s12xs/porting\_examples/multistack/EEtest0

<a id="Description"></a>

#### Description

- The goal of this test is to activate two tasks that share the same stack to test the internal function ready2stacked in MULTISTACK case. To configure the task set we change the files eecfg.h and eecfg.c located inside the Debug folder (the basic structure is inspired to the Microchip PIC30 port) and the makefile. At the end of the porting the task set configuration will be deducted from the .oil file.

- Finally, we created inside the EEtest0 a C file with a main() function. That function explicitly calls ActivateTask inside an infinite cycle. Please note that this small application can be executed to test, in a particualar case, the behavior of the kernel internal function ready2stacked and also the compilation chain. The kernel functions must be linked and used without problems resulting in an fully linked executable file.

- Note1: At this point we have to write the internal function: EE\_s12xs\_hal\_ready2stacked located in the source file "ee\_hal.S" at the path ee\pkg\cpu\cosmic\_hs12xs\src.
  - the function EE\_s12xs\_hal\_ready2stacked is used to:
    - call the threads and change the stacks properly.

- In the reference test examples/s12xs/porting\_examples/multistack/EEtest6 we'll test the internal function EE\_s12xs\_hal\_stkchange.
  - This function can be found in the same file "ee\_hal.S" and is used to:
    - change the stack to resume a stacked thread.

<a id="Expected_output"></a>

#### Expected output

When everything is done in the right way, with the following commands we can have the executable file:

- open a Cygwin shell
- cd into the Debug directory
- the commands make clean and make all should work correctly producing an executable inside the Debug directory.

To simulate the application we can use directly the hardware or a "good" software debugger.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Writing_a_multi-stack_application_that_runs_on_a_single_stack) · [Archived source revision 1774](http://erika.tuxfamily.org/wiki/index.php?oldid=1774)
- Last source edit: 2009-12-10T09:45:38Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds.
- [Original MediaWiki source](../source/wikitext/1522.mediawiki) · [Original editing history](../source/history/batch-013.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
