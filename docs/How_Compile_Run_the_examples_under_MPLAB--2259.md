# How Compile & Run the examples under MPLAB

<a id="Compile_.26_Run_example_under_MPLAB_IDE"></a>

## Compile & Run example under MPLAB IDE

To compile and run the example you should use [MPLAB IDE](http://www.microchip.com/stellent/idcplg?IdcService=SS_GET_PAGE&nodeId=1406&dDocName=en019469&part=SW007002) v8.66 or later and follow these steps:

1. Create a project directory and put all Easylab Library files inside (easylab.h, easylab.c, main.c).
2. Open MPLAB IDE and start a new Project Wizard ([MAIN MENU] Project-> [ITEM] Project Wizard...). Following steps are made inside wizard procedure.
3. Connect your Easylab with supply-communication cable and connect you microstick board with programmer cable to your computer
4. select dsPIC33FJ64MC802 as target device ([Main Menu] Configure -> Select Device...)
5. Choose your Toolsuite (Microchip C30 Toolsuite), eventually give the path to the tools if MPLAB IDE is not able to found them by it self.
6. Create a new Project file browsing for the previously created project directory and giving a name to project file in "Save Project As" dialog.
7. Add all Easylab Library files at your project.
8. After click next until the end of wizard you could uncomment all needed compile defines at begin of easylab.h file or add them to your project build options ([Project CONTEXT MENU] (right click on the project) -> [ITEM] Build Options... -> [TAB] MPLAB C30 ->[GROUP] Preprocessr Macros -> [BUTTON] Add) .
9. Build your project ([Project CONTEXT MENU] -> [ITEM] Build All).
10. Select Starter Kits programmer ([MAIN MENU] Programmer -> [SUB MENU] Select Programmer -> [ITEM] Starter Kits)
11. Open a Serial Terminal (e.g. Putty.exe, HTerm.exe). Configure the port, baud rate (115200),data bits(8 bit), stop bits (1 bit) and parity bits (none). DON'T enable CTS. Connet to the channel.
12. Program your board ([MAIN TOLLBAR] ->[BUTTON] Program (It should have been appeared after you selected the programmer))
13. Enjoy the kitt effect and a nice stadium choir. :)
14. Look at your serial teminal, you should get the example instruction on the console.
15. Have fun with it. :D

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=How_Compile_%26_Run_the_examples_under_MPLAB) · [Archived source revision 4504](http://erika.tuxfamily.org/wiki/index.php?oldid=4504)
- Last source edit: 2012-01-30T15:48:19Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Salva.
- [Original MediaWiki source](../source/wikitext/2259.mediawiki) · [Original editing history](../source/history/batch-005.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
