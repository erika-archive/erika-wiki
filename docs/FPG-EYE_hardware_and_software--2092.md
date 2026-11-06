# FPG-EYE hardware and software

The FPG-EYE is a development board produced by [Evidence S.r.l.](http://www.evidence.eu.com/).
The board is based on Lattice core [Lattice XP2-17 fpga](http://www.latticesemi.com/products/fpga/xp2/index.cfm). This board can either be used as a standard fpga development board or as a [mico32](http://www.latticesemi.com/products/intellectualproperty/ipcores/mico32/index.cfm) soft-core platform.

<a id="FPG-EYE_Hardware"></a>

### FPG-EYE Hardware

The FPG-EYE is equipped with following onboard devices:

- Fpga LFXP2-17
- 25Mhz crystal oscillator
- SRAM: 512 kB
- SDRAM: 32 MB
- Serial Flash: 4 MB
- Leds and switches

and additional external standard modules:

- RS232 Transceiver
- Ethernet module

Following external modules are also available optionally:

- CMOS Camera (Color)
- RF Transceiver Module

For more details, refer [Evidence FPG-EYE page](http://www.evidence.eu.com/content/view/377/436/). In the [FPG-EYE software packet](../assets/linked/FPG-EYE_software_packet--117012d0f3aa1162.zip) you can find a [Test hardware](Test_hardware--2152.md "Test hardware") file. This [Test hardware](Test_hardware--2152.md "Test hardware") file tests all component device present on the FPG-EYE.

<a id="FPG-EYE_Software"></a>

### FPG-EYE Software

In the [Erika repository](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/) there are two [platform project](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/mico32/demo/platforms). If you use the [Lattice ispLever](http://www.latticesemi.com/products/designsoftware/isplever/isplever/index.cfm?source=sidebar) as development tool, you have to choose the [fpg\_eye\_isplever](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/mico32/demo/platforms/fpg_eye_isplever), while if you use more recent [Diamond](http://www.latticesemi.com/products/designsoftware/diamond/index.cfm) as development tool the right platform is the [fpg\_eye\_diamond](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/mico32/demo/platforms/fpg_eye_diamond). Please remember, if you are using the ispLever software, you have to apply the patches at the sram and serial flash components. The patches are placed in the [FPG-EYE software packet](../assets/linked/FPG-EYE_software_packet--117012d0f3aa1162.zip).
The FPG-EYE board comes with a pre-loaded demo application, the Web-server Camera demo, which is hosted by a [Mico32 platform](http://www.latticesemi.com/products/intellectualproperty/ipcores/mico32/index.cfm).
The [demo source files](http://svn.tuxfamily.org/viewvc.cgi/erika_erikae/repos/ee/trunk/ee/examples/mico32/demo/sw_projects/webserver_camera/) can be found in the Erika examples.
The Web-server Camera demo is an Erika-based application and uses Evidence custom components and platforms.
The FPG-EYE custom components and the bootloader are contained in the [FPG-EYE software packet](../assets/linked/FPG-EYE_software_packet--117012d0f3aa1162.zip) and can be freely downloaded.

The [FPG-EYE software packet](../assets/linked/FPG-EYE_software_packet--117012d0f3aa1162.zip) includes:

- Evidence custom **mico32\_camera** component (MSB component with binary netlist).
- Evidence custom **serpar\_io** component (MSB source component).
- Binary external flash bootloader.
- Python bootloader interface script.
- Mico32 standard Async SRAM Controller and SPI Flash Controller components patched (only for Lattice ispLever, not required for Lattice Diamond).

<a id="Brief_description_of_software_components"></a>

### Brief description of software components

<a id="Evidence_custom_camera_component"></a>

#### Evidence custom camera component

The **mico32\_camera** is a [wishbone](http://www.google.it/url?sa=t&rct=j&q=wishobone%20bus&source=web&cd=2&ved=0CDAQFjAB&url=http%3A%2F%2Fsen.enst.fr%2Ffilemanager%2Factive%3Ffid%3D662&ei=w9GFTpHzLOqs0QW8wdH7Dw&usg=AFQjCNExXH_Cr7tBXmN2Gc9Kj9BDxAw8Bw&cad=rj) component developed by [Evidence S.r.l.](http://www.evidence.eu.com/). It must be  [imported in MSB's](Installation_of_Mico32_FPG-EYE_development_environment--2093.md#Import_custom_Mico32_components_in_LatticeMico_System_Development_Tools "Installation of Mico32/FPG-EYE development environment") *Available Components*, before using in platform designs.
**Mico32\_camera** comes with an [Erika](http://www.evidence.eu.com/content/view/27/254/) driver which is needed for developing your applications.

Example of *mico32\_camera* can be found under the section [Camera API](Camera_API--2137.md "Camera API").
To write your customised driver, refer [Mico32\_camera: Writing drivers based on mico32\_camera](Mico32_camera_Writing_drivers_based_on_mico32_camera--2069.md "Mico32 camera: Writing drivers based on mico32 camera") page.

<a id="Evidence_custom_serpar_io_component"></a>

#### Evidence custom serpar\_io component

This is a component developed by [Evidence S.r.l.](http://www.evidence.eu.com/). Like any custom component, it must be  [imported in MSB's](Installation_of_Mico32_FPG-EYE_development_environment--2093.md#Import_custom_Mico32_components_in_LatticeMico_System_Development_Tools "Installation of Mico32/FPG-EYE development environment") before hand.

It is basically a parallel to serial converter. The processor writes a datum on serpar\_io component out register, that serializes it out to a [74hc595](http://www.nxp.com/documents/data_sheet/74HC_HCT595.pdf) (serial to parallel shift register) device.
Similarly, serpar\_io can get a serialized datum from [74hc165](http://www.nxp.com/documents/data_sheet/74HC_HCT165.pdf) (parallel to serial shift register) and puts it on the register so that the cpu can read it. The serial to parallel shift register enables/disables board peripherals power supply and LEDs, while the parallel to serial shift register reads switches the states.

The [sample code for serialpar\_io](Sample_code_for_serialpar_io--2148.md "Sample code for serialpar io") shows a simple use of this component.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=FPG-EYE_hardware_and_software) · [Archived source revision 4305](http://erika.tuxfamily.org/wiki/index.php?oldid=4305)
- Last source edit: 2012-01-16T09:24:35Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Salva, Eguidieri, Dibbe, Erikadds.
- [Original MediaWiki source](../source/wikitext/2092.mediawiki) · [Original editing history](../source/history/batch-005.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
