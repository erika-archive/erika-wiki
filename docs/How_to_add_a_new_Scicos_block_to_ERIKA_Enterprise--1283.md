# How to add a new Scicos block to ERIKA Enterprise

These are a few notes useful if you want to create a new block in Scicos and the corresponding implementation function in ERIKA Enterprise.

<a id="Scicoslab_4.4.1"></a>

## Scicoslab 4.4.1

This section describes how to create a new block for Erika Enterprise, and applies the Scicoslab 4.4.1 version of the toolbox.

Installation steps:

1. Install Scicoslab 4.4.1
2. Install the last ScicosLab-Pack for FLEX boards
3. Install Microsoft Visual Studio Express 2010 (free version is available!)

Block creation tutorial:

Preface: directory names are the directory names of my laptop...

1. In the folder of interest (e.g. C:\Programmi\scilab\scicoslab\_441\contrib\dspic\macros\flex\_blocks\FLEX-MTB) write the sci code of your block. Please note the name of your C function must be specified in the scicos\_model.sim field.
2. If you want to put your new block in a **new palette**, you need to create a new child folder of flex\_blocks, put the block file (.sci file) into and edit **builder.sce** and **loader.sce** scripts to take this new folder in account.
3. To compile block code change the working directory from the scilab console in this way "cd c:/Programmi/scilab/scicoslab\_441/contrib/dspic" and then digit the following command "exec builder.sce". You obtain a .bin file.
4. To create the new palette file digit the following command "create\_palette(folder\_path)" (e.g. create\_palette("C:\Programmi\scilab\scicoslab\_44b7\contrib\dspic\macros\flex\_blocks\FLEX-MTB")). You obtain a .cosf file.
5. Move the .cosf file in the palettes folder (e.g. C:\Programmi\scilab\scicoslab\_441\contrib\dspic\macros\palettes) replacing older file.
6. Modify the .scilab configuration file in your $(HOME)/ScicosLab/{version}, to add the new palette to scicos' palettes sub-menu.
7. Modify the file named "symbols" inserting the name of your block and the symbols you want to be associated.
8. Write your C files and place them in the scicos folders inside Erika Enterprise tree. (e.g. C:\Evidence\eclipse\plugins\com.eu.evidence.ee\_1.5.1.201005181137\ee\_base\contrib\scicos\inc\pic30\mycode.h C:\Evidence\eclipse\plugins\com.eu.evidence.ee\_1.5.1.201005181137\ee\_base\contrib\scicos\src\pic30\mycode.c). Please check if you must modify the contrib\scicos\cfg\cfg.mk to tell the compiler that your file must be compiled!
9. Create a DLL with the computational function of your block to be used for simulation, and link the DLL library in ScicosLab (type "help link" for further info).
10. Create a scicos diagram and try to genereate the code.

If your application works fine you have successfully completed this tutorial. Congratulations!!! ;-)

<a id="Scilab_4.1.2"></a>

## Scilab 4.1.2

This information derives from a post in the ERIKA Forum, and applies the Scilab 4.1.2 version of the toolbox.

1. Preface
   1. Directory names are the directory names of my laptop...
   2. Use the zip file attached. for each step, there are a few files to look at
   3. I had to edit the post to substitute backslash with slashes
2. Install Scilab 4.1.2
3. Install the Scicos Pack for the FLEX boards
4. Install Microsoft Visual Studio Express 2008
5. [Install these patches](http://www.evidence.eu.com/download/scicos/MSVC2008_Patch.zip) in Scilab 4.1.2. They are needed to let Scilab discover the Visual studio compiler
6. NMake
   1. install NMake from <http://support.microsoft.com/default.aspx?scid=kb;en-us;Q132084>
   2. rename the executable file in nmake.exe and copy it into C:/Windows
7. Update the files
   1. You need to create the block file. You can use Roberto's block editor <http://web.dti.supsi.ch/~bucher/> . Or check out the block example at <http://www.evidence.eu.com/component/option,com_fireboard/Itemid,262/func,view/id,6/catid,3/>
   2. add into the C:/Programmi/scilab-4.1.2/contrib/dspic/macros/name one line with the file name
   3. in C:/Programmi/scilab-4.1.2/contrib/dspic/bulder.sce , we have to comment a few lines, because we are not going to compile the .c files distributed with the package. in particular, comment from the line "cd(ROUTINES)" to the one but last line (leave only the "cd('..')"
8. Compile
   1. open scilab 4.1.2
   2. from the scilab console, "cd c:/Programmi/scilab-4.1.2/contrib/dspic"
   3. from the scilab console, "exec builder.sce"
9. you get an output similar to the following one

   --------------------------------------------------------------------

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   scilab-4.1.1



   Copyright (c) 1989-2007

   Consortium Scilab (INRIA, ENPC)

   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_







   Startup execution:

   loading initial environment

   shared archive loaded

   \_link\_ done



   Scicos-FLEX Ready



   -->cd c:/Programmi/scilab-4.1.1/contrib/dspic

   ans =



   c:/Programmi/scilab-4.1.1/contrib/dspic



   -->exec builder.sce



   -->mode(-1);



   -->



   --------------------------------------------------------------------
10. Add the block to the scicos Palette
    1. "cd macros"
    2. open scicos by typing "scicos();"
    3. Menu "Diagram/Load", load the file "dspic.cosf"
    4. Menu "Edit/Add New block", specify the file name "dspic\_getfreq", press ok and place the block inside the palette where you want
    5. menu "Diagram/Save As", and give the name "dspic.cosf" - with the final "f"!!!
    6. close Scicos and Scilab
    7. now if you open again scicos, the dspic palette should have the dspic\_getfreq block.
11. Configuring Erika Enterprise
    1. copy the getfreq.c file inside "C:/Programmi/Evidence/ee/contrib/scicos/src/pic30"
    2. add getfreq.c inside "C:/Programmi/Evidence/ee/contrib/scicos/cfg/cfg.mk" (see file attached for an example)
12. Create a scicos example
    1. Follow the Scicos tutorial, but use the getfreq instead of the Sine (see files in the zip)
    2. compile and enjoy!

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=How_to_add_a_new_Scicos_block_to_ERIKA_Enterprise) · [Archived source revision 5476](http://erika.tuxfamily.org/wiki/index.php?oldid=5476)
- Last source edit: 2013-09-25T14:19:49Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Paolo.gai, Erikadds, Eguidieri.
- [Original MediaWiki source](../source/wikitext/1283.mediawiki) · [Original editing history](../source/history/batch-005.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
