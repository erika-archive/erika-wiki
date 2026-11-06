# Running the MODISTARC regression tests

<a id="Description"></a>

#### Description

MODISTARC regression tests: Objectives and results

The main goal of the MODISTARC project is to support the effort of the European car industry towards the development and standardisation of networking architectures. Through the OSEK/VDX consortium activities, the European industry has issued three new standards defining respectively the OSEK/VDX Operating System, Communication and Network Management. These specifications describe the applicable services and protocols and define the associated APIs. They intend to fulfil the two major goals of the OSEK/VDX initiative:

- enable portability of applications to ECUs coming from different suppliers
- enable interoperability of interconnected ECUs in a distributed automotive system
- enable interoperability of interconnected ECUs in a distributed automotive system

The MODISTARC project aims to help the European car industry to keep its leading position in the network based car architectures by providing the relevant test methods and tools to assess the conformance of OSEK/VDX implementations.

For other info go to web site: [OSEK portal](http://portal.osek-vdx.org/index.php?option=com_content&task=view&id=14&Itemid=17)

- The following steps explain how to test the compilation procedure and kernel performances using the MODISTARC regression tests.

<a id="How_to_set_up_the_MODISTARC_regression_procedure"></a>

#### How to set up the MODISTARC regression procedure

- Create in the path testcase a script to set the following environment variables:
  - RTDRUID\_ECLIPSE\_HOME (the path of the eclipse directory: e.g. C:/Evidence/Evidence/eclipse)
  - CLASSPATH (the class path: e.g. "$CLASSPATH;$ECLIPSE\_HOME\\plugins\\$LAUNCHER\_JAR"; this is for **Nios II** only)

- Create in the path testcase\common a folder for the desired architecture. The folder should contain:
  - Files necessary to compile each test.
  - Files for configuring the debugger.
  - The file test.mk containing the main rules of the makefiles chain.
  - The main script for the debugger to run the regression tests;

- Within each test folder to modify the following files:
  - code.c, the application file.
  - conf.in, the file containing the list of architectures supported by the test.
  - appl.oil, the OIL configuration file of the test (this file includes header files from the folder testcase\common\rtdruid\_common, you have to create a new header file for the desired architecture).

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Running_the_MODISTARC_regression_tests) · [Archived source revision 4869](http://erika.tuxfamily.org/wiki/index.php?oldid=4869)
- Last source edit: 2012-07-23T08:37:59Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds, Dibbe, Pj, Nicola.
- [Original MediaWiki source](../source/wikitext/1529.mediawiki) · [Original editing history](../source/history/batch-010.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
