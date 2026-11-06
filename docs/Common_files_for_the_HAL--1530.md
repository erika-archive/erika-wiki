# Common files for the HAL

<a id="Intro"></a>

### Intro

During the porting of Mico32 someone thought that it could be possible to reuse a substantial part of the code of the HAL among many architectures. The files contained in [ee/pkg/cpu/common](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common) can be used both as a part of a new porting, by including them, or as a base to derive code specific to a particular architecture.

All the files in cpu/common are written in standard C; they should work as they are on almost any platform or compiler. The should be decoupled enough so that if a porting requires a custom implementation of some parts, the rest could be used with no modification. A new porting should use the common implementation when possible, or an ad-hoc implementation under cpu/XXX otherwise.

Please do not modify these files to accommodate some quirks of your architecture. Instead, make a copy of them and create a branch under your cpu/XXX directory or whatever. Implementations that can potentially be useful on many platforms are welcome; e.g., [ee/pkg/cpu/common/inc/ee\_compiler\_gcc.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_compiler_gcc.h) works only for Gcc, but it should work across all platforms where Gcc is available.

The common layer is used by following portings:

- [EnSilica eSi-RISC](EnSilica_eSi-RISC--1664.md "EnSilica eSi-RISC")
- [Lattice Mico32](Lattice_Mico32--1632.md "Lattice Mico32")
- [Freescale PPC e200 (MPC 56xx)](Freescale_PPC_e200_MPC_56xx--1612.md "Freescale PPC e200 (MPC 56xx)")
- [TI MSP430](TI_MSP430--1719.md "TI MSP430")
- [Microchip dsPIC](Microchip_dsPIC--1474.md "Microchip dsPIC")
- [Renesas RX200](Renesas_RX200_and_RX130--2307.md "Renesas RX200")
- [ARM Cortex MX](ARM_Cortex_MX--2226.md "ARM Cortex MX")
- [Atmel AVR8](Atmel_AVR8--2466.md "Atmel AVR8")

<a id="Content"></a>

### Content

cpu/common contains a practically complete monostack version of Erika without interrupts, with support for the multistack version and interrupts. There is one context-changing function (instead of the two of previous portings). Where possible, all parts have been written so that there is one implementation in C for all versions (mono or multistack); this is accomplished through the use of macros or small inline functions that are defined differently depending on the version. See the inline definition of EE\_hal\_ready2stacked() in [ee/pkg/cpu/common/inc/ee\_context.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_context.h?view=markup) for an example.

- [README.txt](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/README.txt?view=markup)
- [cfg/cfg.mk](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/cfg/cfg.mk?view=markup)
- [inc/README.txt](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/README.txt?view=markup)
- [inc/ee\_compiler\_gcc.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_compiler_gcc.h?view=markup) Definitions for the Gnu C compiler
- [inc/ee\_compiler\_ccrx.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_compiler_ccrx.h?view=markup) Definitions for the Renesas RX C compiler
- [inc/ee\_compiler\_ccs.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_compiler_ccs.h?view=markup) Definitions for the Texas Instruments CCSv4 tms470 C compiler
- [inc/ee\_compiler\_codewarrior.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_compiler_codewarrior.h?view=markup) Definitions for the Freescale Codewarrior C compiler
- [inc/ee\_compiler\_diab.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_compiler_diab.h?view=markup) Definitions for the Wind River Diab C compiler
- [inc/ee\_compiler\_iar.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_compiler_iar.h?view=markup) Definitions for the IAR C compiler
- [inc/ee\_compiler\_keil.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_compiler_keil.h?view=markup) Definitions for the ARM Keil C compiler
- [inc/ee\_compiler\_tasking.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_compiler_tasking.h?view=markup) Definitions for the TASKING C compiler
- [inc/ee\_context.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_context.h?view=markup) Definitions related to stack- and context-changing functions
- [inc/ee\_hal\_structs.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_hal_structs.h?view=markup) Common structure declarations
- [inc/ee\_irqstub.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_irqstub.h?view=markup) Functions possibly useful for IRQ post-stub
- [inc/ee\_primitives.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_primitives.h?view=markup) Inline functions used in kernel primitives
- [inc/ee\_stdint.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_stdint.h?view=markup) Definitions of (some) ISO types
- [inc/ee\_types.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/inc/ee_types.h?view=markup) Definition of Erika types based on limits.h
- [src/ee\_context.c](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/src/ee_context.c?view=markup) Stack- and context-changing functions
- [src/ee\_hal\_structs.c](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/cpu/common/src/ee_hal_structs.c?view=markup) Definitions of common structures

<a id="Porting_to_a_new_architecture"></a>

### Porting to a new architecture

See [Porting ERIKA Enterprise and RT-Druid to a new microcontroller](Porting_ERIKA_Enterprise_and_RT-Druid_to_a_new_microcontroller--1458.md "Porting ERIKA Enterprise and RT-Druid to a new microcontroller") for the general instructions.

1. Create the architecture-specific directory ee/pkg/cpu/XXX
2. Create the files inc/ee\_cpu.h and inc/ee\_internal.h in the above directory. They should include all the files cpu/common/inc/ee\_\*.h suitable for your architecture. Write any architecture-specific definition or declaration in them.
3. Modify the files ee/pkg/ee.h and ee/pkg/ee\_internal.h to include your newly create files.
4. Modify the file cpu/common/cfg/cfg.mk to compile the common C source files suitable for your architecture.
5. Create or modify any additional file you need.
6. Run make and enjoy.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Common_files_for_the_HAL) · [Archived source revision 5652](http://erika.tuxfamily.org/wiki/index.php?oldid=5652)
- Last source edit: 2014-07-15T12:32:58Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Dibbe, Giuseppe Serano.
- [Original MediaWiki source](../source/wikitext/1530.mediawiki) · [Original editing history](../source/history/batch-003.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
