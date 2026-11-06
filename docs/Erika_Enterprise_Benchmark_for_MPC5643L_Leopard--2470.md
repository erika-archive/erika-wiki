# Erika Enterprise Benchmark for MPC5643L Leopard

A preliminary test on Freescale MPC5643L (Leopard) under the following conditions:

- Single core;
- I-Cache disabled;
- CPU running at 120 Mhz;
- Flash prefetch enabled;
- 3 wait state while reading from Flash.

Gave the following result:

| Test Name | value (usec) |
| --- | --- |
| New task from an ISR2 (Time between the first instruction of the Erika ISR-handler and the Task body defined by the user) | 5.700 |
| ISR2 latency (Time between the first instruction of the Erika ISR-handler and the ISR2 body defined by the user) | 0.800 |

Note: these results have been collected by using the Lauterbach-Tracer funcionalities. More details available at <http://www.lauterbach.com>

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Erika_Enterprise_Benchmark_for_MPC5643L_Leopard) · [Archived source revision 5586](http://erika.tuxfamily.org/wiki/index.php?oldid=5586)
- Last source edit: 2014-04-30T07:13:48Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Rischiav, Francesco.
- [Original MediaWiki source](../source/wikitext/2470.mediawiki) · [Original editing history](../source/history/batch-004.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
