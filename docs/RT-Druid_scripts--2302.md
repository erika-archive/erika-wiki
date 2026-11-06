# RT-Druid scripts

<a id="Generate_Code"></a>

### Generate Code

**generate\_code.bat** and **generate\_code.sh** can be used to generate Erika Enterprise Configuration files from one or more input files. Usually the input is a single oil file, but it is possible to specify multiple files of different types. The available types for input files depends on the specific set of RT-Druid plugins that you have installed.

The usage is:

```
  code_generation.XXX "RT-Druid_dir" "input_file" ["additional_input_file1"..."additional_input_fileN"] "output_dir" 
```

where XXX is .bat or .sh depending on your shell.

| Field | Description | Required |
| RT-Druid\_dir | The home directory of RT-Druid | Yes |
| input\_file | The first input file | Yes |
| additional\_input\_file | Additional input files. They can be zero, one or more | No |
| output\_dir | The directory where store generated Erika Enterprise Configuration file. If the directory does not exist, RT-Druid will try to create it. | Yes |

<a id="Instantiate_template"></a>

### Instantiate template

**instantiate\_template.bat** and **instantiate\_template.sh** can be used to instantiate one of all examples managed by RT-Druid.

The usage is:

```
  instantiate_template.XXX "RT-Druid_dir" "template_id" "output_dir" 
```

where XXX is .bat or .sh depending on your shell.

| Field | Description | Required |
| RT-Druid\_dir | The home directory of RT-Druid | Yes |
| template\_id | The id of the template that should be instantiate | Yes |
| output\_dir | The directory where store all files related to the choosed template. If the directory does not exist, RT-Druid will try to create it. | Yes |

```
 Note that you can use environment variable or RT-Druid configuration parameter to provide
 to RT-Druid your own templates, as described in  RT-Druid configuration page.
 In this way, you can instantiate one of your template.
```

<a id="Start_Ant"></a>

### Start Ant

**start\_ant.bat** and **start\_ant.sh** can be used to run a generic build.xml file using ant library provided with eclipse. The advantage is that all eclipse plugins are available, including RT-Druid ones.

The usage is:

```
  start_ant.XXX "RT-Druid_dir" [ant options]
```

where XXX is .bat or .sh depending on your shell.

| Field | Description | Required |
| RT-Druid\_dir | The home directory of RT-Druid | Yes |
| ant options | Zero or more ant options that are provided as them are to ant library. An example is -buildfile to select a build file or -Dparam=value to set a specific value | No |

With RT-Druid is provided a simple build.xml file. The description of RT-Druid ant tasks is [here](RT-Druid_ant_tasks--2303.md "RT-Druid ant tasks"). Useful links are
[the ant manual](http://ant.apache.org/manual/index.html) and the section with
[details on writhing buildfiles](http://ant.apache.org/manual/using.html#buildfile).

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=RT-Druid_scripts) · [Archived source revision 4707](http://erika.tuxfamily.org/wiki/index.php?oldid=4707)
- Last source edit: 2012-03-29T09:29:04Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Nicola.
- [Original MediaWiki source](../source/wikitext/2302.mediawiki) · [Original editing history](../source/history/batch-009.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
