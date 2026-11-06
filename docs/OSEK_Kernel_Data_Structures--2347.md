# OSEK Kernel Data Structures

This page gives some short information about the data structures used in the OSEK/VDX implementation.

It is not meant as a complete list; This page is filled up as a reference as the questions come on the Forum.

- EE\_th\_rnact

  contains the remaining activations for a task
- EE\_th\_nact

  (for FP, EDF, FRSH, not for OO) contains the number of pending activations still to be executed
- EE\_th\_status

  contains the execution status of the thread (SUSPENDED, RUNNING, WAITING, READY)
- EE\_th\_next

  next pointer, used to create the ready or stacked queue at runtime
- EE\_th\_ready\_prio

  Priority of the task as specified in the OIL file, implemented as a bitmask
- EE\_th\_dispatch\_prio

  Run-time priority of the task. Can be higher than the ready task due to the implementation of Internal Resources or if the task is non-preemptive

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=OSEK_Kernel_Data_Structures) · [Archived source revision 5000](http://erika.tuxfamily.org/wiki/index.php?oldid=5000)
- Last source edit: 2013-01-17T08:24:02Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Pj.
- [Original MediaWiki source](../source/wikitext/2347.mediawiki) · [Original editing history](../source/history/batch-008.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
