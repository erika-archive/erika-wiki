# TODO List

This is is a list of things to doin the short term:

<a id="Misc"></a>

### Misc

- remove things that are currently not updated since a longtime and put them into an "old" directory. In particular, COM, hard\_alarms

<a id="CPU"></a>

### CPU

- remove the support for a user-defined types.h
- Separate EE\_ADDR in EE\_ADDR and EE\_FADDR (pointers to data and to code in some architectures have different sizes). This is being superseded by further development for MISRA compliance, as EE\_ADDR remains a generic data pointer and pointers to functions are being replaced with ad-hoc new types.
- Insertion of function in the HAL to disable/enable IRQs by saving and restoring previous states. To be used in the next point.
- Turning on and off IRQs associated to type-2 ISRs, needed to support OSEK `SuspendOSInterrupts()`. A possible solution:
  1. ISR sections in OIL list the associated IRQ
  2. A suitable data structure is filled in eecfg.c (a bitmap should be enough on many architectures)
  3. New APIs (e.g., `EE_hal_enableIRQ2()`, `EE_hal_disableIRQ2()`) should be added to HAL to disable and restore the state of IRQs associated to type-2 ISR. Existing `EE_hal_enableIRQ()`, `EE_hal_disableIRQ()` could be used as a fall-back (though they don't provide a way to restore the previous state).
     1. we could use the functions at the previous point to save/restore the previous state while disabling the IRQs

<a id="PIC30"></a>

#### PIC30

- use extern inline for PIC inline functions to avoid code bloating when the student license ends
- support for large model
- commit fix to the bug of DISI when nested interrupts
- add a traps file to the dsPIC using an OIL option or using an EEOPT variable

<a id="S12XS"></a>

#### S12XS

- allow the possibility to mask only a specific priority when in kernel mode (that is, using CCR instead of SEI/CLI)
- implement a stack test at the task or interrupt end (to be done in the endcycle\_stacked or endcycle\_ready; in this way the kernel is not modified)
- how to implement timers which are resistant to a timer overrun? Should we use hard\_alarms?

<a id="e200zX"></a>

#### e200zX

- Add an EEOPT to remove stmw and lmw (store/load multiple word) instructions. These instructions are good for performance, but they seem to fill Nexus FIFOs, which is bad if you want a full data trace (e.g., using [Lauterbach Trace32](Freescale_PPC_e200_MPC_56xx--1612.md#Lauterbach_Trace32_and_ORTI_support "Freescale PPC e200 (MPC 56xx)")). Such an EEOPT should be used to change the compiler options (there should be a switch to inhibit generation of stmw and lmw), and enable alternative code (using a sequence of store or load) in assembly files.

<a id="Examples"></a>

### Examples

- provide a compilation script to compile all exampes in bulk to always ensure that they always all compile fine
- Modify main() inside OO examples (which call `StartOS()`). `StartOS()` could not return, and should not according to Autosar. Also, its behavior has been recently changed to also enable interrupts. The body of `main()` in OO examples should be changed accordingly into something like the following (which does not depend on `StartOS()` returning). Please note that tasks can be started by `StartOS()` if they have the `AUTOSTART` property set in the OIL file.

```
int main(void)
{
	/* HW initialization goes here */
	/* Do anything, but do not enable interrupts */

	/* Call StartOS, but don't expect it to return */
	StartOS(OSDEFAULTAPPMODE);
	while (1) {
		/* Wait forever */
	}
}
```

<a id="DIST"></a>

### DIST

- rethink the DIST scripts for the creation of the distribution

<a id="Scilab_and_FLEX"></a>

### Scilab and FLEX

- remove the code and the block for the OLD LCD driver (there are no boards currently working with that code).
- Add scicos blocks for the Mini Flex
- [look at this post on the forum](http://erika.tuxfamily.org/forum/viewtopic.php?f=3&t=777#p1165):
  1. the "success" message should not be there
  2. the error on the "find" command "No such file or directory" is not masked 8if it is an error the compilation should stop there...)
  3. we should probably check that all the folders used for the compilation are at their correct place (if not, link to a FAQ).

<a id="Regression_tests"></a>

### Regression tests

- launch them twice to check wethere there are problems with dependencies (dependencies are created at the first compilation round)

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=TODO_List) · [Archived source revision 4134](http://erika.tuxfamily.org/wiki/index.php?oldid=4134)
- Last source edit: 2011-11-14T13:32:16Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Paolo.gai, WikiSysop, Rischiav, Dibbe.
- [Original MediaWiki source](../source/wikitext/1528.mediawiki) · [Original editing history](../source/history/batch-010.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
