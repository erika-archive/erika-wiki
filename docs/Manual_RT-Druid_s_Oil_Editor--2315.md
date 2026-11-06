# Manual: RT-Druid's Oil Editor

RT-Druid 2.0 comes with a new textual editor for oil files.

<a id="New_features"></a>

## New features

New features are:

- Content assist
- On-line documantation
- Resolution of cross reference
- On-line validation
- Quick fixes
- Fully customizable syntax coloring
- Support for templates

Oil files may or may not contain the oil Implementation section. If this section is missing, the default one is used.

<a id="Content_assist"></a>

### Content assist

It is always possible to ask the list of valid values at the current cursor position.
The default key sequence is **crtl-space**.

Depending on what is written before current cursor position, the content assist may propose

- a key word, like TASK
- one or more attributes for the current element
- the value of an attribute. Usually this is available for boolean, enumerators and reference to objects (like tasks)

The set of proposed attributes may be reduced after typing few characters.

<a id="On-line_documantation"></a>

### On-line documantation

In many conditions, will try to show the description and documentation (if available) of elements.
This usually happens during the content assist selection and moving the mouse over an element.

It is possible to document an element directly through the oil editor, adding a multi line comment **/\* ... \*/** just before the element or using oil description sintax (i.e. adding **: "..."** just after the element).
If an element has an oil description, the multi line comment is ignored even if available.

<a id="Resolution_of_cross_reference"></a>

### Resolution of cross reference

Inside oil CPU sections, there are a lot of references and these references are navigable with **crtl+mouse left click** if the referred object is in the same file. Examples of references are:

- the name of an attribute
- the value of a Boolean
- the value of an Enum
- the value of a reference to an Oil Object (like a task)

<a id="On-line_validation"></a>

### On-line validation

While typing, the editor will try to check if the oil is valid or not.
Some examples of validation checks are

- the syntax is correct
- attributes are defined
- values of an attribute are valid for that attribute type, considering also restriction if present

"Heavy" checks are not done in this phase, in order to achieve a quicker response.

<a id="Quick_fixes"></a>

### Quick fixes

For some kins of problem, the editor is able to propose quick fixes, i.e. suggest one or more way to solve the problem and perform the select one.

A simple example is to propose the list of valid values (if there are a limited set).

<a id="Fully_customizable_syntax_coloring"></a>

### Fully customizable syntax coloring

The editor comes with a preference page that allow the user to change the color and the font for each type of element in the editor.

<a id="Support_for_templates"></a>

### Support for templates

Using a preference page, it is possible to write your own template and specify where it is available.

<a id="Limitations"></a>

## Limitations

Current editor works only within a single file. This means

1. it is not possible to follow cross references to object outside the edited file. This usually happens for oil attributes described RT-Druid oil file library.
2. the editor does not handle inclusion, i.e. **#include ".."** may cause unexpected errors and references to objects in the included file are not resolved.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Manual%3A_RT-Druid%27s_Oil_Editor) · [Archived source revision 4800](http://erika.tuxfamily.org/wiki/index.php?oldid=4800)
- Last source edit: 2012-07-12T13:17:11Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Nicola.
- [Original MediaWiki source](../source/wikitext/2315.mediawiki) · [Original editing history](../source/history/batch-008.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
