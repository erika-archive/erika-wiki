# A brief description on how to run MODISTARC regression tests for Freescale S12XS

<a id="How_to_run_MODISTARC_regression_tests_for_Freescale_S12_Family"></a>

## How to run MODISTARC regression tests for Freescale S12 Family

Requirements: The "procmail" package should be installed in Cygwin using the Cygwin 'Setup.exe' (the setup program is downloadable form this site: <http://www.cygwin.com/>).

The makefiles chain will compile all the projects through the following steps:

- Directories creation;
- OIL elaboration by RT\_DRUID;
- Compilation to generate the .elf file;
- Debugger script creation to run the regression tests on the processor;

The procedure to run MODISTARC regression tests is the following:

<a id="Earliest_version_.28before_Erika_revision_1531.29"></a>

## Earliest version (before Erika revision 1531)

1. Perfom a repository checkout to work with the last version of the testcases. Note that you can use Subversion only in anonymous mode without logging in. Hence, you won't be allowed to write on the repository (adding, editing or removing files).
   - To perform a checkout, type:  svn co <svn://svn.tuxfamily.org/svnroot/erika/erikae/repos/ee/trunk/ee>
   - To perform an update type:  svn update
2. Change the working directory in:  repos\ee\trunk\ee\testcase  and type:  . ./s12xs\_startup\_scripts  to configure the environment.
3. Start the compilation typing:  make ARCH=s12xs  The makefiles chain will compile all the projects through the following steps:
   1. Directories creation;
   2. OIL elaboration by RT\_DRUID;
   3. Compilation to generate the .elf file;
   4. Debugger script creation to run the regression tests on the processor;

NOTE1: To compile only one test type:  make ARCH=s12xs DIRS="modistarc\_task\_1" 
NOTE2: To compile the tests you can use the batch file located in common/s12xs. To run the batch file type:

- common\s12xs\modistarc\_regression\_test.bat  to compile all the tests or
- common\s12xs\modistarc\_regression\_test.bat modistarc\_task\_1  to compile only one test;
  - In these cases the batch file will call the HIWAVE debugger at the end of the compilation to load the executables files on the processor using the generated script file.
- common\s12xs\modistarc\_regression\_test.bat clean  to clean all the tests;
- common\s12xs\modistarc\_regression\_test.bat hiwave  to call HIWAVE debugger directly.

<a id="Latest_version:_.28since_Erika_revision_1531.29"></a>

## Latest version: (since Erika revision 1531)

1. Perfom a repository checkout to work with the last version of the testcases. Note that you can use Subversion only in anonymous mode without logging in. Hence, you won't be allowed to write on the repository (adding, editing or removing files).
   - To perform a checkout, type:  svn co <svn://svn.tuxfamily.org/svnroot/erika/erikae/repos/ee/trunk/ee>
   - To perform an update type:  svn update
2. Change the working directory in:  repos\ee\trunk\ee\testcase  Then edit and execute:  . ./s12\_startup\_scripts  to configure the environment. The environment variables to be set are: ERIKA\_FILES pointing to the Erika main folder (the folder downloaded with the svn checkout, it contains the testcase folder).
3. Start the compilation with:
   - make ARCH=s12xs\_cosmic  if you are working with MC9S12XS128 and the Cosmic Compiler.
   - make ARCH=s12g\_cw  if you are working with MC9S12G128 and the CodeWarrior Compiler.

NOTE1: To compile only one test type:  make ARCH=s12xs\_cosmic DIRS="modistarc\_task\_1" 
NOTE2: To compile the tests you can use the batch file located in common/s12. To run the batch file type:

- common\s12\s12xs\_cosmic\modistarc\_regression\_test.bat  to compile all the tests or
- common\s12\s12xs\_cosmic\modistarc\_regression\_test.bat modistarc\_task\_1  to compile only one test;
  - In these cases the batch file will call the HIWAVE debugger at the end of the compilation to load the executables files on the processor using the generated script file.
- common\s12xs\s12xs\_cosmic\modistarc\_regression\_test.bat clean  to clean all the tests;
- common\s12xs\s12xs\_cosmic\modistarc\_regression\_test.bat hiwave  to call HIWAVE debugger directly.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=A_brief_description_on_how_to_run_MODISTARC_regression_tests_for_Freescale_S12XS) · [Archived source revision 4182](http://erika.tuxfamily.org/wiki/index.php?oldid=4182)
- Last source edit: 2011-12-09T10:21:12Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Erikadds.
- [Original MediaWiki source](../source/wikitext/1597.mediawiki) · [Original editing history](../source/history/batch-001.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
