# Writing a multi-stack application that runs on multiple stacks with semaphores

<a id="Reference_test"></a>

#### Reference test

examples/s12xs/porting\_examples/multistack/EEtest5

examples/s12xs/porting\_examples/multistack/EEtest6

<a id="Description"></a>

#### Description

- The goal of the two tests is to activate two tasks that run on different stacks and use semaphores. To configure the task set we change the files eecfg.h and eecfg.c located inside the Debug folder (the basic structure is inspired to the Microchip PIC30 port) and the makefile.

examples/s12xs/porting\_examples/multistack/EEtest5

- The demo is a classical producer/consumer problem implemented with two semaphores P and V. The demo is used to test the following features of ERIKA Enterprise OS:
  - Multistack configuration: The Producer and the Consumer task need a separate stack because they block calling the WaitSem primitive.
  - Semaphores: ERIKA Enterprise supports counting semaphores. The demo show how to initialize the semaphores, and how to use the main semaphore primitives (PostSem and WaitSem).

examples/s12xs/porting\_examples/multistack/EEtest6

- The demo can be used to test the internal function: EE\_s12xs\_hal\_stkchange. The low priority task Task1 is activated in the main function. Task1 then activates the high priority task Task2. At this point Task1 is preempted (and the stack change inside the EE\_s12xs\_hal\_ready2stacked) and Task2 begins to execute. Task2 then is blocked on a semaphore and Task1 is resumed with a call to the internal funtion EE\_s12xs\_hal\_stkchange.
- Please note that this small application shows a particular case where a stack is saved inside the EE\_s12xs\_hal\_ready2stacked function and resumed inside the EE\_s12xs\_hal\_stkchange function. This can help to better understand the stack change mechanism.

<a id="Expected_output"></a>

#### Expected output

When everything is done in the right way, with the following commands we can have the executable file:

- open a Cygwin shell
- cd into the Debug directory
- the commands make clean and make all should work correctly producing an executable inside the Debug directory.

To simulate the application we can use directly the hardware or a "good" software debugger.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Writing_a_multi-stack_application_that_runs_on_multiple_stacks_with_semaphores) · [Archived source revision 1773](http://erika.tuxfamily.org/wiki/index.php?oldid=1773)
- Last source edit: 2009-12-10T09:44:54Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds.
- [Original MediaWiki source](../source/wikitext/1527.mediawiki) · [Original editing history](../source/history/batch-013.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
