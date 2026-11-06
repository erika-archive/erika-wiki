# Black Box Regression tests

This page documents about the Black Box regression tests implemented for ERIKA Enterprise.

<a id="Main_idea"></a>

## Main idea

The main idea is expressed by the following points:

- the system allows the specification of a set of tests
  - each test is a black box test
    - each test contains a set of assertions
    - each assertion checks both the execution order as well as return values of functions
    - the test is successful when the test executed in the proper order

- the tests are compiled for a target platform
  - for each test is possible to specify for which architecture it works (variable worksfor in conf.in)
  - for each test it is possible to specify a set of values for the testing
    - typical example: a test must work for BCC1, BCC2, ECC1, ECC2, both standard and extended error checking
    - the system will test all the possible combination of all the variables (in the case above, they will be 8 combinations)
    - please refer the variable conf in conf.in

- the test generates a debugger configuration (e.g. for Lauterbach)
  - the debugger configuration is responsible to run all tests
  - each run does the following:
    - loads the application
    - sets a breakpoint in a specific position (typically EE\_assert\_last
    - runs the application
    - if the application does not stop, then it is a failure :-)
    - if the application stops, then a variable is tested. If it is ok, it means that all the execution of all the assertions are correct
  - all the debugger output is returned and stored in a log file.

- the tests currently implement the [MODISTARC tests](http://portal.osek-vdx.org/index.php?option=com_content&task=view&id=13&Itemid=16), plus some other tests to check the behavior of the main context change and interrupt functions.

<a id="Important_files"></a>

## Important files

- all files are stored inside the testcase directory
- the testcase/makefile if run without parameters gives an idea of the possible commands
- each test is stored in a separate directory
  - conf.in which contains the settings that explains how to run the test
    - note that the conf.in settings are handled as #defines in the OIL and.c file
  - code.c is the test source code
  - appl.oil is the OIL configuration file
- common
  - contains all the scritps
  - important things to look at are the subdirectories, one for each architecture, and in particular the test.mk which contains information of the commands run at each phase.

<a id="More_info"></a>

## More info

Some more information can be found at [Running the MODISTARC regression tests](Running_the_MODISTARC_regression_tests--1529.md "Running the MODISTARC regression tests").

For MPC5674F please refere to  [http://erika.tuxfamily.org/wiki/index.php?title=How\_to\_run\_the\_MODISTARC\_regression\_tests\_for\_Freescale\_MPC5674F](How_to_run_the_MODISTARC_regression_tests_for_Freescale_MPC5674F--1625.md)

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Black_Box_Regression_tests) · [Archived source revision 5665](http://erika.tuxfamily.org/wiki/index.php?oldid=5665)
- Last source edit: 2014-07-29T06:35:39Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Paolo.gai, Francesco.
- [Original MediaWiki source](../source/wikitext/2156.mediawiki) · [Original editing history](../source/history/batch-002.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
