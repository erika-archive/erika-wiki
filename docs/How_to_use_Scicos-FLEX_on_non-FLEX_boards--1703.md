# How to use Scicos-FLEX on non-FLEX boards

It is possible to use Scicos-FLEX with non-FLEX boards.
These steps should make it possible to compile an EE application based on a custom board.

Here is what you need to do:

- You need to write your own blocks. see the following link
  - [How to add a new Scicos block to ERIKA Enterprise](How_to_add_a_new_Scicos_block_to_ERIKA_Enterprise--1283.md "How to add a new Scicos block to ERIKA Enterprise")
- You need to create a template for your board.
  - First, start from an existing template. The reference template is stored into the example eclipse plugin. under my PC, it is currently C:\Evidence\eclipse\plugins\com.eu.evidence.ee.templates.dspic\_1.5.1.201011221106\examples\pic30\pic30\_scicos
  - Then, copy the template in another directory under the examples directory (for example, ".../examples/pic30/myboard")
  - change, in the template.xml, the board ID from "board\_flex" to "myboard"
  - change the code to reflect your board configuration by editing the 'oil' and the source files.
- Now you need to add the template in the Scicos target settings, by editing the file SCI+'/contrib/scicos\_ee/scicos\_flex/dsPIC/macros /codegen/SetTarget\_.sci', changing the templates list as follows: lab\_template = ['board\_flex', 'board\_easylab', 'myboard'];
- At this point you need to recompile all the files by running "builder.sce".

Finally, when generating the code, use "myboard" instead of "board\_flex" in the Target board parameter in the code generator dialog box.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=How_to_use_Scicos-FLEX_on_non-FLEX_boards) · [Archived source revision 4741](http://erika.tuxfamily.org/wiki/index.php?oldid=4741)
- Last source edit: 2012-04-10T09:28:43Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Paolo.gai, Erikadds.
- [Original MediaWiki source](../source/wikitext/1703.mediawiki) · [Original editing history](../source/history/batch-006.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
