# Writing a mono-stack with interrupt not nested

<a id="Reference_test"></a>

#### Reference test

examples/s12xs/porting\_examples/EEtest2

examples/s12xs/porting\_examples/EEtest3

examples/s12xs/porting\_examples/EEtest4

<a id="Description"></a>

#### Description

The three tests below tests the behavior which may happen at the end of an interrupt:

1. from the main() function, return to the main() function
2. from the main() function, return to a ready task activated in the interrupt
3. from the running task, return to a ready task activated in the interrupt
4. from the running task, return to the same task (eventually another task has been activated and is queued in the ready queue)

examples/s12xs/porting\_examples/EEtest2:

- tests behavior 1 and 2
- The goal is to test a task activation made within an interrupt. The execution behavior is that when the main is running, an interrupt arrives calling ActivateTask. At the end of the interrupt, the task is activated.
- To configure the task set we must change the files eecfg.h and eecfg.c located inside the Debug folder.
- The isr configuration is architecture dependent. In this case we modified the vector\_s12x.c file.

- Finally, we created inside the EEtest2 a C file with a main() function. That function explicitly calls the function for periodic interrupt timer configuration and finishing with a for(;;). Please note that this small application can be executed to test the behaviour of the interrupt stub. The compilation must finish with an executable fully linked.

examples/s12xs/porting\_examples/EEtest3:

- tests behavior 3
- The goal is to activate two tasks with different priorities to test the preemption behavior. The main function activates the low priority task. The high priority task is activated within the interrupt and is executed at the end of the interrupt. Then the low priority task can continue until the end.

examples/s12xs/porting\_examples/EEtest4:

- tests behavior 4
- The goal is to activate two tasks with different priorities to test again the preemption behaviour. The main function activates the high priority task. The low priority task is activated within the interrupt and is not executed at the end of the interrupt. The rtos continues the execution of the first task and then the low priority task is scheduled.

- Note1: for correct interrupt execution we should take care of the interrupt stub and the following functions EE\_ISR2\_prestub, EE\_ISR2\_poststub (see the header file ee\_irqstub.h at the path ee\pkg\cpu\cosmic\_hs12xs\inc).

<a id="Expected_output"></a>

#### Expected output

When everything is done in the right way, with the following commands we can have the executable file:

- open a Cygwin shell
- cd into the Debug directory
- the commands make clean and make all should work correctly producing an executable inside the Debug directory.

To simulate the application we can use directly the hardware or a "good" software debugger.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Writing_a_mono-stack_with_interrupt_not_nested) · [Archived source revision 1641](http://erika.tuxfamily.org/wiki/index.php?oldid=1641)
- Last source edit: 2009-11-18T15:29:38Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds, Paolo.gai.
- [Original MediaWiki source](../source/wikitext/1461.mediawiki) · [Original editing history](../source/history/batch-013.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
