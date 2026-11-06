# Interface between ERIKA and RT-Druid

[RT-Druid](ERIKA_Enterprise_and_RT-Druid_Design_Flow--2067.md "ERIKA Enterprise and RT-Druid Design Flow") is the tool used to configure the ERIKA Enterprise OS.

<a id="Files"></a>

### Files

RT-Druid produces at least three files in the project output directory (normally called Debug):

**makefile**

The main makefile that defines some [EEOPTs](EEOPT--2057.md "EEOPT") and starts the compilation process (see also [Erika Makefiles](Erika_Makefiles--1601.md "Erika Makefiles"))

**eecfg.h**

A C header containing the definitions of macros for several constant parameters (such as task IDs, the number of tasks...). This header is included also in some assembly files, so it must contain only defines.

**eecfg.c**

A C file containing the definition of all the kernel data structures that depend on the configuration (e.g., an OIL file)

Other files may be produced, depending on the configuration or the target architecture.

<a id="Upgrading_the_interface"></a>

### Upgrading the interface

RT-Druid and ERIKA Enterprise must be kept in sync, because the structures produced inside eecfg.c by RT-Druid must reflect those in ERIKA source code. During the development, sometimes those structures must be changed (though it happens rarely, and care should be taken to minimize such changes). This may cause problems to developers working on the latest version of ERIKA on the repository, or people living on the [Bleeding edge](Tutorial_PIC30_-_Installing_ERIKA_and_RT-Druid_and_compile_your_first_application--1637.md#Bleeding_edge "Tutorial: Installing ERIKA and RT-Druid, and compile your first application"). A mechanism has been introduced to address this problem:

1. RT-Druid writes the version of its current interface inside the macro `RTDRUID_CONFIGURATOR_NUMBER`, defined in eecfg.h. A variable with the same name is produced inside the generated makefile.
2. The file [pkg/ee\_rtdruid\_versions.h](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/pkg/ee_rtdruid_versions.h) contains a set of defines that record the values of the interface version when the interface has changed.
3. When ERIKA needs to be modified in a way not compatible with the current RT-Druid interface, a new define is added to pkg/ee\_rtdruid\_versions.h, and the new ERIKA code uses #if directives to remain compatible with the old versions of RT-Druid. Please note that #if directives must first check for the definition of `RTDRUID_CONFIGURATOR_NUMBER`, as old RT-Druid versions do not support such a feature.
4. When the RT-Druid interface is updated, also its `RTDRUID_CONFIGURATOR_NUMBER` is updated according to the values in pkg/ee\_rtdruid\_versions.h. If pkg/ee\_rtdruid\_versions.h contains more than one pending modification, the version numbers inside pkg/ee\_rtdruid\_versions.h may be reordered to reflect the true history of RT-Druid.

RT-Druid is distributed with an up-to-date snapshot of ERIKA source files. A setup composed by an old ERIKA together with a more recent RT-Druid is not supported, as it would be too complicated.

<a id="See_also"></a>

### See also

[ERIKA Enterprise and RT-Druid SVN Access](ERIKA_Enterprise_and_RT-Druid_SVN_Access--1464.md "ERIKA Enterprise and RT-Druid SVN Access")

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Interface_between_ERIKA_and_RT-Druid) · [Archived source revision 3772](http://erika.tuxfamily.org/wiki/index.php?oldid=3772)
- Last source edit: 2011-10-11T17:07:06Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Dibbe.
- [Original MediaWiki source](../source/wikitext/2128.mediawiki) · [Original editing history](../source/history/batch-006.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
