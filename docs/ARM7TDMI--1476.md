# ARM7TDMI

<a id="ARM7TDMI_support"></a>

## ARM7TDMI support

ERIKA Enterprise supports ARM7TDMI machines since 2002. The support for RT-Druid has been made public only in 2009 on release 1.5.0.

The ARM7TDMI support includes:

- support for GCC and ADS compilers (earlier version have run also on Diab DCC)
- support for interworking between ARM and THUMB mode
- support for single and multi stack configurations
- support for Lauterbach Trace32 (automatic generation of scripts and ORTI files)
- FIQ and ISR interrupt supported

<a id="MCUs"></a>

## MCUs

The MCUs supported are currently the following:

- Samsung ks32c50100 (an ARM7 @ 50Mhz, with a simple interrupt controller)
- ST sta2051 Vespucci (including the code to handle the interrupt controller; support to this architecture thanks to [Cobra AT](http://www.cobra-at.com))
- [UNIBO MPARM](http://www-micrel.deis.unibo.it/sitonew/research/mparm.html) (a cycle-accurate simulator of ARM7TDMI; support to this architecture thanks to the [PREDATOR FP7 Project](http://www.predator-project.eu/))

In the past, ERIKA supported also the following architectures (which are not supported by RT-Druid)

- Triscend A7 (an ARM7TDMI plus FPGA. triscend has been acquired by Xilinx a few years ago)
- ST Janus (a dual core on a single chip for automotive. The interrupt controller was similar to the ST sta2051 Vespucci. The porting was done in collaboration with [Magneti Marelli](http://www.magnetimarelli.com)

<a id="Boards"></a>

## Boards

The boards supported are:

- ARM Evaluator7T - a low cost ARM evaluation board hosting Samsung ks32c50100
- Triscend A7 (see above)
- UNIBO MPARM (see above)

<a id="Available_examples"></a>

## Available examples

There are a few examples available for ARM and Evaluator7T available on the SVN, but they have not been inserted into the 1.5.0 examples because the board is no more in production :-(

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=ARM7TDMI) · [Archived source revision 2975](http://erika.tuxfamily.org/wiki/index.php?oldid=2975)
- Last source edit: 2011-04-07T09:00:40Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Paolo.gai, WikiSysop.
- [Original MediaWiki source](../source/wikitext/1476.mediawiki) · [Original editing history](../source/history/batch-001.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
