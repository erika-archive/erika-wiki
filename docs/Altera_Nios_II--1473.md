# Altera Nios II

<a id="Nios_II_and_the_support_for_multicore_applications"></a>

## Nios II and the support for multicore applications

The development trends for next generation embedded devices clearly states that the future lies to multicore devices on the same chip.

The Altera Nios II platform is an example of these multicore platforms.

Thanks to the configurability of FPGAs, developers can design multiprocessors in minutes. Although on one side hardware design is simplified by tools like Altera SOPCBuilder, on the other side application development is made more complex by the fact that the application code have to be spread out among different processors.

<a id="Features_of_ERIKA_Enterprise_and_RT-Druid_for_Altera_Nios_II"></a>

## Features of ERIKA Enterprise and RT-Druid for Altera Nios II

<a id="Altera_integration_features:"></a>

### Altera integration features:

- Integrated as a component in the Altera
- Compatible with the Altera HAL peripheral drivers and system libraries;
- Support for nested interrupts;
- Support for a RTOS configuration code generator compliant with the OSEK OIL specifications.

<a id="ERIKA_Enterprise_features_specific_for_Nios_II:"></a>

### ERIKA Enterprise features specific for Nios II:

- Support for OSEK OS conformance classes (BCC1, BCC2, ECC1, ECC2), and for the FP conformance class;
- Multicore support specific for Nios II (see later);
- All the other features of ERIKA Enterprise are supported.

<a id="Multicore_support:"></a>

### Multicore support:

- Advanced software partitioning support:
  - developers can decide which task goes on which processor;
  - developers can move tasks between processors without changing the source code;
  - Transparent handling of shared resource locks behavior depending on the partitioning of the application;
- Interprocessor interrupt support;
- Shared resource support using queuing spin locks on top of the Altera Mutex Peripheral;
- Automatic cache disabling technique without changes to the user source code (only changes to data definitions);
- Support for multiprocessor scheduling algorithms with bounded blocking times on multiprocessors.

<a id="Requirements"></a>

## Requirements

The following table lists the requirements upon external programs for the Altera Nios II port.

There is no guarantee our software will work if you install a different version from what is listed in the table below.

- ERIKA Enterprise for Nios II 1.4.2.1 works with Altera Nios II 8.0, 8.1
- ERIKA Enterprise for Nios II 1.4.2.2 works with Altera Nios II 8.1

<a id="Download"></a>

## Download

The latest version available of ERIKA Enterprise for the Nios II is ERIKA 1.4.2.2 working on Altera Nios II 8.1.

- INSTALL INSTRUCTIONS:
  - [INSTALL\_nios2\_1\_4\_2\_2 INSTALL\_nios2\_1\_4\_2\_2](http://download.tuxfamily.org/erika/webdownload/nios2/1422/INSTALL_nios2_1_4_2_2.txt)
- This version includes support for Altera Nios II 8.1, and full source code distributed under the GPL+Linking exception license.
  - [EMF 2.0.3](../assets/linked/emf-sdo-xsd-SDK-2.0.3--be66e6ff6fd391c3.zip)
  - [GEF SDK 3.0.1](../assets/linked/GEF-SDK-3.0.1--7f16d4ed515e48bf.zip)
  - [090504\_evidence\_ee.zip](../assets/linked/090504_evidence_ee--e6134edb3667a79f.zip)
  - [rtd\_gpl\_nios2\_\_142\_\_\_20090511\_1832.zip](../assets/linked/rtd_gpl_nios2__142___20090511_1832--af67fbb2ecbf55a1.zip)
- Hardware designs for Altera Stratix 2s60:
  - [Single CPU design for ERIKA Enterprise FRSH Kernel](http://download.tuxfamily.org/erika/webdownload/nios2/1422/1cpu.qar)
  - [4 CPU design for ERIKA Enterprise FRSH Kernel](http://download.tuxfamily.org/erika/webdownload/nios2/1422/4cpu.qar)
- Additional documentation produced in the IST FRESCOR FP6 Project related on Nios II
  - [FRESCOR\_WP4\_D-EP7v2.pdf - describing the implementation of the FRSH kernel over Multicore Nios II Projects](../assets/linked/FRESCOR_WP4_D-EP7v2--18e99682e85f83be.pdf)

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Altera_Nios_II) · [Archived source revision 5004](http://erika.tuxfamily.org/wiki/index.php?oldid=5004)
- Last source edit: 2013-03-28T09:29:39Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Paolo.gai, WikiSysop, Pj.
- [Original MediaWiki source](../source/wikitext/1473.mediawiki) · [Original editing history](../source/history/batch-002.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
