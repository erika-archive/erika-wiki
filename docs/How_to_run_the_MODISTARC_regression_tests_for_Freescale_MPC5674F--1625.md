# How to run the MODISTARC regression tests for Freescale MPC5674F

1. Checkout the svn repository to work with the last version of the test cases. Note that you can use subversion in anonymous mode without logging in (in this case you won't be allowed to write on the repository for adding, editing or removing files).
   - To checkout the source, type:  svn co <svn://svn.tuxfamily.org/svnroot/erika/erikae/repos/ee/trunk/ee>
   - To update the sources type:  svn update
2. Change the working directory to:  repos/ee/trunk/ee/testcase
3. Start the compilation by typing make ARCH=e200zx (see below for other targets) and by specifying MCU target, e.g: make ARCH=e200zx\_diab\_5\_5\_1\_vle MCU\_TARGET=mamba where mamba represents MPC5674F. The build system will compile all the projects through the following steps:
   1. Creating all the temporary directories;
   2. Processing the OIL configuration files using RT\_DRUID;
   3. Compiling the sources to generate the .elf files;
   4. Creating the Lauterbach scripts to run the regression tests on the processor.DIRS="modistarc\_task\_1" </tt>
4. Launch the tests: cd tmp; t32mppc
5. After the test, open the file tmp/report.log. You should find a line saying Test OK for every test; if a test is marked with Test Failed then you have found something broken.

The e200zx target uses the Diab compiler and the FLE instruction set. It is possible to choose the CodeWarrior compiler and/or the VLE instruction set using one of these other targets: e200zx\_diab\_vle, e200zx\_codewarrior\_vle, or e200zx\_codewarrior\_fle.

See also: [Freescale PPC e200 (MPC 56xx)](Freescale_PPC_e200_MPC_56xx--1612.md "Freescale PPC e200 (MPC 56xx)")

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=How_to_run_the_MODISTARC_regression_tests_for_Freescale_MPC5674F) · [Archived source revision 5663](http://erika.tuxfamily.org/wiki/index.php?oldid=5663)
- Last source edit: 2014-07-29T06:24:32Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Fchecconi, Dibbe, Francesco.
- [Original MediaWiki source](../source/wikitext/1625.mediawiki) · [Original editing history](../source/history/batch-006.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
