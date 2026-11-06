# PPC GNU Toolchain Integration

<a id="Background"></a>

## Background

In the freeware software distribution there is no GNU compiler toolchain that natively supports PPC e200zx cores. However, it is possible to generate compatible code for PPC e200zx cores acting on compiler and linker switches of any GNU Compiler Toolchian for PPC.

NOTE: All freeware GNU compiler toolchains generate PPC code in FLE mode ONLY!!!

The choose of [Macraigor System GNU Tools](http://www.macraigor.com/full_gnu.htm) PowerPC GNU Toolkit V:4.7.0-0 as GNU Toolchain for PPC was made basing on suggestion of [Lauterbach](http://www.lauterbach.com/frames.html?home.html) support team.

The integration was based on [PowerPC cross development with GNU Toolchain and Eclipse](http://download.ronetix.info/toolchains/powerpc/ppc_cross_development_guide.pdf) guide released by [Ronetix](http://www.ronetix.at/).

<a id="Freescale_MPC5554_build_example"></a>

## Freescale MPC5554 build example

The PowerPC cross development with GNU Toolchain and Eclipse guide released by Ronetix provides a [build example](http://download.ronetix.info/examples/mpc5554_example.tar.gz) for [Freescale MPC5554](http://www.freescale.com/webapp/sps/site/prod_summary.jsp?code=MPC5554) MCU.

Inside the build example package there is a Makefile with the followings compiler/linker build configuration switches:

```
 PROJECT = mpc_ram
 LDSCRIPT= ./prj/MPC5554_SRAM.ld
 OPT = -O0
 MCU = 8540
 MCFLAGS = -mcpu=$(MCU)
 ASFLAGS = $(MCFLAGS)  -g -mno-eabi -mregnames -Wa,-mregnames -Wa,-mbooke32 -Wa,-me500 -misel=yes -mspe=yes -mfloat-gprs=no -msoft-float -mno-string -msdata=none -Wa,-I./inc -gdwarf-2
 CPFLAGS = $(MCFLAGS) $(OPT) -g -mno-eabi -mregnames -Wa,-mregnames -Wa,-mbooke32 -Wa,-me500 -misel=yes -mspe=yes -mfloat-gprs=no -msoft-float -mno-string -msdata=none -gdwarf-2
 LDFLAGS = $(MCFLAGS) -Wl,-g -Wl,-T$(LDSCRIPT) -Wl,-Map=$(PROJECT).map,--cref,--no-warn-mismatch $(LIBDIR)
```

<a id="Compiler_Switches"></a>

## Compiler Switches

- -mcpu=8540: Use features of and schedule code for given CPU (8540)
- -me500: Generate code for Motorola e500 core complex
- -mbooke32: Generate code for 32-bit PowerPC BookE
- -no-eabi: Don't use EABI.

With these switches the compiler generates PPC machine code in FLE mode compatible with PPC e200zx cores.

<a id="Linker_Switches"></a>

## Linker Switches

- -nostdlib: Only use library directories specified on the command line.
- -nostartfiles: Do not use the standard system startup files when linking. The standard system libraries are used normally, unless -nostdlib or -nodefaultlibs is used.

With these switches the linker DO NOT includes startup-code and standard libraries.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=PPC_GNU_Toolchain_Integration) · [Archived source revision 5853](http://erika.tuxfamily.org/wiki/index.php?oldid=5853)
- Last source edit: 2014-09-24T16:04:55Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Giuseppe Serano.
- [Original MediaWiki source](../source/wikitext/2482.mediawiki) · [Original editing history](../source/history/batch-008.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
