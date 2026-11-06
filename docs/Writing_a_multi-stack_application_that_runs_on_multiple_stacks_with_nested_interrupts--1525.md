# Writing a multi-stack application that runs on multiple stacks with nested interrupts

<a id="Reference_test"></a>

#### Reference test

examples/s12xs/porting\_examples/multistack/EEtest3

<a id="Description"></a>

#### Description

- The goal of this test is to activate two tasks that runs on multiple stacks with nested interrupts.

- We changed inside the EEtest3 the C file with the main() function. The program configures two periodic timers to enable the corresponding interrupt. The ISRs functions explicitly calls ActivateTask for the two tasks. Please note that this small application can be executed to test the behavior of the kernel internal function ready2stacked, the ISRs nesting mechanism in the MULTISTACK case. The kernel functions must be linked and used without problems resulting in an fully linked executable file.

<a id="Expected_output"></a>

#### Expected output

When everything is done in the right way, with the following commands we can have the executable file:

- open a Cygwin shell
- cd into the Debug directory
- the commands make clean and make all should work correctly producing an executable inside the Debug directory.

To simulate the application we can use directly the hardware or a "good" software debugger.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Writing_a_multi-stack_application_that_runs_on_multiple_stacks_with_nested_interrupts) · [Archived source revision 1765](http://erika.tuxfamily.org/wiki/index.php?oldid=1765)
- Last source edit: 2009-12-10T09:15:21Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds.
- [Original MediaWiki source](../source/wikitext/1525.mediawiki) · [Original editing history](../source/history/batch-013.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
