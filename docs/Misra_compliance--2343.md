# Misra compliance

<a id="MISRA_C_compliance_of_Erika_RTOS"></a>

### MISRA C compliance of Erika RTOS

Erika MISRA-C compliance has been certified in collaboration with the Tool & Methodologies team of Magneti Marelli Power Train. In this context, the Erika code has been verified through the use of Flexelint (ver. 9.00h) and Lin (ver. 7.10), furthermore the compliance has been pursued using the Windriver Diab compiler (ver. 5.5.1). Lin is a tool developed by Magneti Marelli Power Train that use Flexlint as MISRA-C checker engine. The outcome of these tools in terms of MISRA-C deviations can be considered composed by two sets. The first set of deviations represents an internal concern of Magneti Marelli, it collects all the deviations accepted by Magneti Marelli in its software life-cycle process. The second one represents the set of deviations introduced by Erika RTOS as additions with respect to the first set. Therefore, for confidential reasons, only the second group of deviations has been reported.

According with the OSEK standard, the MISRA compliance of Erika RTOS has been achieved in the following OSEK conformance classes: BCC1, BCC2, ECC1, ECC2. Erika RTOS is also available in multicore configuration and in a configuration that guarantees the functionalities to ensure memory protection capability. MISRA C compliance has been certified even in these two non-OSEK configurations, with the limitations pointed out so far.

<a id="Compliance_Matrix"></a>

### Compliance Matrix

Compliance Matrix:

| Rule No. | Checking tool (error message) | Manual Review |
| MISRA 3.1 | FlexeLint 793 (1) | No manual review |
| MISRA 10.6 | FlexeLint 960 (2) | No manual review |
| MISRA 11.3 | FlexeLint 923 (2) | No manual review |
| MISRA 14.2 | FlexeLint 522 (4) | No manual review |
| MISRA 16.7 | FlexeLint 818 (5) | No manual review |
| MISRA 18.4 | FlexeLint 960 (6) | No manual review |
| MISRA 20.2 | FlexeLint 960 (7) | No manual review |

<a id="Notes_concerning_MISRA-C_compliance_matrix:"></a>

### Notes concerning MISRA-C compliance matrix:

Note 1) MISRA 3.1 (FlexeLint 793): ANSI/ISO limit of 8 'conditional inclusion levels'. The Erika tree exceedes the maximum conditional inclusion level required by MISRA that is 8. Currently, the maximum inclusion level of Erika is 14. This value is constantly monitored by Erika maintenance team;

Note 2) MISRA 11.3, MISRA 10.6 (FlexeLint 923, FlexeLint 960): 2 occurrences. These deviations are caused by two macros used to access hardware registers;

Note 3) MISRA 11.4 (FlexeLint 929): 1 data structure occurrence. In the Erika memory protection paradigm there is an automatically generated data structure. This structure is an array containing system calls, such a system calls are casted pointers. Cast from pointer to pointer is not allowed in MISRA but mandatory in this context to make this feature reliable and easy to be managed;

Note 4) MISRA 14.2 (FlexeLint 522): 7 occurrences. Lacks side-effects. There are a set of functions that lack of side-effect. They are assembly inline functions;

Note 5) MISRA 16.7 (FlexeLint 818): 2 occurrences. Pointer parameters could be declared as pointing to const. The Autosar declaration of GetElapsedValue() and GetApplicationState() do not require const input parameters. In order to be fully-compliant with the Autosar standard, these parameters have not been declared as const although Misra requires the opposite;

Note 6) MISRA 18.4 (FlexeLint 960): 2 occurrences. Declaration of union type or object of union type. Use of 2 unions to speed-up performances: EE\_oo\_ErrorHook\_parameters, EE\_TYPERN\_PARAM;

Note 7) MISRA 20.2 (FlexeLint 960): Re-use of C90 identifier pattern. 1 occurrence. Definition of NULL pointer; MISRA 20.2 (FlexeLint 960): Re-use of C90 identifier pattern. 50 occurrences. Header guards defined with double underscore heading.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Misra_compliance) · [Archived source revision 4908](http://erika.tuxfamily.org/wiki/index.php?oldid=4908)
- Last source edit: 2012-10-29T11:35:30Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Francesco.
- [Original MediaWiki source](../source/wikitext/2343.mediawiki) · [Original editing history](../source/history/batch-008.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
