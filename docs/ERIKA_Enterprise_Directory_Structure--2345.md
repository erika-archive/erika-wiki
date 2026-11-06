# ERIKA Enterprise Directory Structure

The following paragraphs give an idea of the internal directory structure of the kernel:

- pkg

  all the code of ERIKA Enterprise

  - cpu

    core CPU (int. disabling, context change, types, ...)
  - mcu

    specific microcontroller (how many serial lines?)
  - board

    connection of a MCU in the board (functions to light a LED that is connected on pin 35 of the MCU on board XYZ)
  - kernel

    scheduling algorithms

    - as

      AUTOSAR extensions for the OO kernel
    - edf

      minimal EDF implementation, useful for research purposes
    - fp

      minimal Fixed Point implementation, useful for research purposes
    - frsh

      minimal implementation of a scheduler with resource reservations, useful for research purposes, result of the FRESCOR FP6 Project
    - oo

      OSEK/VDX OSEK OS kernel API
    - rn

      remote notifications, for implementing interprocessor interrupts on multicores
    - sem

      semaphore implementation used by FP, EDF, FRSH
- contrib

  third party libraries, with licenses other than GPL2+linking exception
- examples

  demo application done with ERIKA Enterprise
- testcase

  regression tests, see [Black Box Regression tests](Black_Box_Regression_tests--2156.md "Black Box Regression tests")

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=ERIKA_Enterprise_Directory_Structure) · [Archived source revision 4961](http://erika.tuxfamily.org/wiki/index.php?oldid=4961)
- Last source edit: 2012-12-29T13:35:43Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Pj.
- [Original MediaWiki source](../source/wikitext/2345.mediawiki) · [Original editing history](../source/history/batch-003.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
