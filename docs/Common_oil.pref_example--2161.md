# Common oil.pref example

Here is an example of common\_oil.pref.
By default, RT-Druid searches it at *rtdruid\_base\_path/configuration/common\_oil.pref*

```
# This is an example of RT-Druid configuration file.
# By default, RT-Druid searches this file at RT-Druid_base_path/configuration/common_oil.pref

################
#
#  Erika Enterprise Files
#
################

# Set erika enterprise path to ErikaEnterpriseFiles directory relative to RT-Druid base directory
# this works with both windows and linux
#erika_enterprise_location = ${eclipse_home}/../ErikaEnterpriseFiles

# Use of absolute path (windows)
#erika_enterprise_location = C:/Evidence/ErikaEnterpriseFiles
#erika_enterprise_location = C:\\Evidence\\ErikaEnterpriseFiles

# Use of absolute path (linux)
#erika_enterprise_location = /opt/Evidence/ErikaEnterpriseFiles

################
#
#  Erika Enterprise Templates
#
################

# Some examples of windows template paths
#templates_path = C:/Evidence/ErikaEnterpriseTemplates
#templates_path = C:/Evidence/ErikaEnterpriseTemplates/path1;C:/Evidence/ErikaEnterpriseTemplates/path2
#templates_path = C:\\Evidence\\ErikaEnterpriseTemplates\\path1;C:\\Evidence\\ErikaEnterpriseTemplates\\path2

# An example of linux template paths
#templates_path = /opt/Evidence/ErikaEnterpriseTemplates/path1:/opt/Evidence/ErikaEnterpriseTemplates/path2


################
#
#  dsPic
#
################

# Path to the ASM30 Assembler
#   Please put the path to the MPLABIDE Assembler
#   NOT the assembler distributed with the C30 Compiler!
#preference_pic30__path_for_asm_compiler = C:\\Programmi\\Microchip\\MPLAB ASM30 Suite

# Path to the C30 Compiler
#   Please put the path to the MPLABIDE Assembler
#   NOT the assembler distributed with the C30 Compiler!
#preference_pic30__path_for_gcc_compiler = C:\\Programmi\\Microchip\\MPLAB C30

################
#
#  pic32
#
################

# Path to the ASM32 Assembler
#   Please put the path to the MPLABIDE Assembler
#   NOT the assembler distributed with the C30 Compiler!
#preference_pic32__path_for_asm_compiler = C:\\Programmi\\Microchip\\MPLAB ASM30 Suite

# Path to the C32 Compiler
#   Please put the path to the MPLABIDE Assembler
#   NOT the assembler distributed with the C30 Compiler!
#preference_pic32__path_for_gcc_compiler = C:\\Programmi\\Microchip\\MPLAB C30


################
#
#  arm7
#
################

#preference_arm7__path_for_cc_compiler=/opt/arm7/compiler/path

################
#
#  avr8
#
################

#preference_avr8__path_for_gcc_compiler = C:/programs/avr8/compiler/path
#preference_avr8__path_for_arduino_sdk  = C:/programs/arduino/sdk/path

################
#
#  cortex
#
################

#preference_cortex_mx__path_for_iar_compiler = /opt/cortex/compiler/path
#preference_cortex_mx__path_for_ccs_compiler = /opt/cortex/compiler/path
#preference_cortex_mx__path_for_keil_compiler = /opt/cortex/compiler/path


################
#
#  renesas
#
################

#preference_renesas_rx200__path_for_ccrx_compiler = C:/programs/Renesas/Hew/Tools/Renesas/RX/1_2_0
#preference_renesas_rl78__path_for_ccrl_compiler = C:/programs/ccrl
#preference_renesas_rl78__path_for_e2studio = C:/programs/e2studio
#preference_renesas_rl78__path_for_ca78k0r_compiler = C:/programs/ca78k0r
#preference_renesas_rl78__path_for_csplus = C:/programs/csplus


################
#
#  s12
#
################

#preference_S12__path_for_codewarrior_compiler = c:/programs/s12/codewarrior/compiler/path
#preference_S12__path_for_cosmic_compiler  = c:/programs/s12/cosmic/compiler/path

################
#
#  powerpc
#
################

#preference_ppc_e200zx__path_for_codewarrior_compiler = c:/programs/codewarrior/ppc/compiler/path
#preference_ppc_e200zx__path_for_codewarrior_compiler = /opt/codewarrior/ppc/compiler/path

#preference_ppc_e200zx__path_for_diab_compiler = c:/programs/diab/ppc/compiler/path
#preference_ppc_e200zx__path_for_diab_compiler = /opt/diab/ppc/compiler/path

################
#
#  tricore AURIX
#
################

#preference_tricore__path_for_diab_compiler    = /diab/tricore/path/compiler
#preference_tricore__path_for_gnu_compiler     = /gnu/tricore/path/compiler
#preference_tricore__path_for_tasking_compiler = /tasking/tricore/path/compiler
```

<a id="See_also"></a>

## See also

[RT-Druid configuration](RT-Druid_configuration--2158.md "RT-Druid configuration")

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Common_oil.pref_example) · [Archived source revision 6098](http://erika.tuxfamily.org/wiki/index.php?oldid=6098)
- Last source edit: 2017-07-11T14:19:45Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: WikiSysop, Nicola.
- [Original MediaWiki source](../source/wikitext/2161.mediawiki) · [Original editing history](../source/history/batch-003.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
