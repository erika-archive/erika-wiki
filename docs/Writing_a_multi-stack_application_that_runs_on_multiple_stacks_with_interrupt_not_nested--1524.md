# Writing a multi-stack application that runs on multiple stacks with interrupt not nested

<a id="Reference_test"></a>

#### Reference test

examples/s12xs/porting\_examples/multistack/EEtest2

<a id="Description"></a>

#### Description

- The goal of this test is to activate two tasks that runs on multiple stacks with interrupt not nested.

- We changed inside the EEtest2 the C file with the main() function. The program configures a periodic timer to enable an interrupt. The ISR function explicitly calls ActivateTask for both the tasks. Please note that this small application can be executed to test, in a particualar case, the behavior of the kernel internal function ready2stacked, and of the ISRs in the MULTISTACK case. The kernel functions must be linked and used without problems resulting in an fully linked executable file.

<a id="Expected_output"></a>

#### Expected output

When everything is done in the right way, with the following commands we can have the executable file:

- open a Cygwin shell
- cd into the Debug directory
- the commands make clean and make all should work correctly producing an executable inside the Debug directory.

To simulate the application we can use directly the hardware or a "good" software debugger.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Writing_a_multi-stack_application_that_runs_on_multiple_stacks_with_interrupt_not_nested) · [Archived source revision 1764](http://erika.tuxfamily.org/wiki/index.php?oldid=1764)
- Last source edit: 2009-12-10T09:12:11Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds.
- [Original MediaWiki source](../source/wikitext/1524.mediawiki) · [Original editing history](../source/history/batch-013.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
