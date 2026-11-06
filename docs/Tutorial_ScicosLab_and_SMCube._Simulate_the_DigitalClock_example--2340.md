# Tutorial: ScicosLab and SMCube. Simulate the DigitalClock example.

If you want to quickly try SMCube in simulation mode, you can do as follows, using the Digital Clock example. To do that, follow these steps:

- open Scicoslab
- give the command

  ```
   cd "C:\Evidence\scicoslab-4.4.1\contrib\scicos_ee\examples\scicos_flex\SMCube\DigitalClock" 
  ```

  (please put the correct directory)
- then the command

  ```
  scicos();
  ```
- open DigitalClock.cos
- open the superblock
- double click on the block names "SMCube mode\_selector.xml"
- choose "Properties", and set "Mode" to 1 (to say interactive simulation), press ok
- close the superblock window
- Menu Simulate, Run
- two windows will appear: the Demo board simulator and the SMCube simulation window.
- Press the play button on the SMCube simulation window to start the SMCube simulation
- Then, press the first button on the left of the simulated Demo board. The selector state machine which is graphically simulated will change its status.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Tutorial%3A_ScicosLab_and_SMCube._Simulate_the_DigitalClock_example.) · [Archived source revision 4880](http://erika.tuxfamily.org/wiki/index.php?oldid=4880)
- Last source edit: 2012-08-21T08:06:24Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Pj.
- [Original MediaWiki source](../source/wikitext/2340.mediawiki) · [Original editing history](../source/history/batch-012.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
