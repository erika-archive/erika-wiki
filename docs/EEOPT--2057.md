# EEOPT

EEOPT is a way to specify configuration flags to the Erika build environment.

EEOPTs can be specified as strings in the OS section of the OIL file. Examples:

```
 EE_OPT = "DEBUG";
 EE_OPT = "USE_UART";
```

Please notice that spelling inside the OIL file includes an underscore: `EE_OPT`.

The only supported format for EEOPTs is a single name, which should be a valid C identifier (i.e., only Latin letters, digits, and underscore are allowed; the first character cannot be a digit). And any other format is not supported, and even if it works now, it may break in the future.

<a id="Common_EEOPTs"></a>

### Common EEOPTs

The following list shows EEOPTs supported by all architectures (except when stated otherwise)

**DEBUG**

**\_\_MULTI\_\_**

**\_\_IRQ\_STACK\_NEEDED\_\_**

<a id="See_Also"></a>

### See Also

- [Erika Makefiles](Erika_Makefiles--1601.md "Erika Makefiles")
- [Tutorial: RT-Druid and OIL basics](Tutorial_RT-Druid_and_OIL_basics--1658.md "Tutorial: RT-Druid and OIL basics")

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=EEOPT) · [Archived source revision 3157](http://erika.tuxfamily.org/wiki/index.php?oldid=3157)
- Last source edit: 2011-07-18T10:39:24Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Dibbe.
- [Original MediaWiki source](../source/wikitext/2057.mediawiki) · [Original editing history](../source/history/batch-003.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
