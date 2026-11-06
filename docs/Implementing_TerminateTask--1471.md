# Implementing TerminateTask

<a id="Reference_test"></a>

#### Reference test

examples/s12xs/porting\_examples/EEtest6

examples/s12xs/porting\_examples/EEtest7

examples/s12xs/porting\_examples/EEtest8

<a id="Description"></a>

#### Description

The three tests below tests the following features:

1. StartOs(...) function and TerminateTask() function;
2. BCC1 mode;
3. BCC2 mode;
4. BCC1 mode with a shared resource;

examples/s12xs/porting\_examples/EEtest6:

- tests behavior 1 and 2
- The goal is to test the start phase of the kernel (StartOs(...)), the activation of a task and its termination procedure.
- To configure the task set we must change the files eecfg.h and eecfg.c located inside the Debug folder.
- Finally, we created inside the EEtest6 a C file with a main() function. That function explicitly calls the StartOs(...) function and finishing with a for(;;). Please note that the TerminateTask() function is called inside a function called by the task. The compilation must finish with an executable fully linked.

examples/s12xs/porting\_examples/EEtest7:

- tests behavior 3
- The goal is to create a task with pending activations to test the kernel behaviour in the BCC2 mode. Task2 is executed six times at the beginning.

examples/s12xs/porting\_examples/EEtest8:

- tests behavior 4
- The goal is to activate two tasks that share a resource to test the scheduler and the blocking mechanism. The main function activates the low priority task. The high priority task is activated within the first task and is executed at the end of the low priority task. The rtos continues the execution of the high priority task.

<a id="Expected_output"></a>

#### Expected output

When everything is done in the right way, with the following commands we can have the executable file:

- open a Cygwin shell
- cd into the Debug directory
- the commands make clean and make all should work correctly producing an executable inside the Debug directory.

To simulate the application we can use directly the hardware or a "good" software debugger.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Implementing_TerminateTask) · [Archived source revision 1652](http://erika.tuxfamily.org/wiki/index.php?oldid=1652)
- Last source edit: 2009-11-25T16:40:06Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds.
- [Original MediaWiki source](../source/wikitext/1471.mediawiki) · [Original editing history](../source/history/batch-006.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
