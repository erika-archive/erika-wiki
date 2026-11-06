# Tutorial: RT-Druid Command Line

<a id="Introduction"></a>

### Introduction

It is possible to execute few RT-Druid's tasks without using a GUI. These tasks are invoked through ant scripts or using directly RT-Druid scripts.

```
 Please, note that RT-Druid is based on eclipse framework even in the CLI form. This means that 
 - ant scripts with RT-Druid tasks should be run using ant embedded in eclipse
 - direct invocation of RT-Druid scripts result in execution of an eclipse environment
```

<a id="Packaging"></a>

### Packaging

RT-Druid is distributed in several packagings:

- Update site: it contains only RT-Druid and Erika Enterprise plugins and can be used to update an existing installation of RT-Druid, or to add RT-Druid functionalities to a generic (and standard) installation of eclipse
- GUI: it contains RT-Druid and Erika Enterprise plugins, eclipse framework and c/c++ support. There are several versions, depending on Os (es. Windows, Linux). It contains also RT-Druid scripts.
- CLI: it contains RT-Druid and Erika Enterprise plugins and the minimum set of eclipse plugins required by RT-Druid. It contains also RT-Druid scripts. There are three versions
  - RT-Druid: contains only RT-Druid and can be invoked only with RT-Druid scripts
  - EE\_RT-Druid: contains Erika Enterprise (sources and examples) and RT-Druid. Can be invoked only with RT-Druid scripts
  - EE\_RT-Druid\_ant: contains Erika Enterprise (sources and examples) and RT-Druid. Can be invoked both with RT-Druid scripts and ant scripts

<a id="Advantages"></a>

### Advantages

Both GUI and CLI packages can be used without a graphical interface but the CLI ones are smaller, than you can save space:

- GUI packages requires around 180MByte
- CLI with Erika Enterprise, RT-Druid and ant support requires around 71MByte
- CLI with Erika Enterprise, RT-Druid requires around 55MByte
- CLI with RT-Druid requires around 7MByte

moreover the package with only RT-Druid is the best one if you are using Erika Enterprise from svn and compiling everything in an automated system.

<a id="Disadvantages"></a>

### Disadvantages

On the other side, all CLI versions cannot be automatically updated and the only way to "update" them is to download a new one.

<a id="Configuration"></a>

### Configuration

Usually, it is useful to configure one or more parameter before run RT-Druid from command line, like compiler and Erika Enterprise path. [[Here](RT-Druid_configuration--2158.md)] is some details about how do it.

<a id="Ant_Tasks"></a>

### Ant Tasks

Here is the list of available RT-Druid ant tasks:

| Task Name | Description |
| [rtdruid.Convert](RT-Druid_ant_tasks--2303.md#rtdruid.Convert "RT-Druid ant tasks") | If needed, converts and merges one or more input files into a single new RT-Druid file |
| [rtdruid.Oil.Configurator](RT-Druid_ant_tasks--2303.md#rtdruid.Oil.Configurator "RT-Druid ant tasks") | Generates the Erika Enterprise configuration files |
| [rtdruid.Oil.Example](RT-Druid_ant_tasks--2303.md#rtdruid.Oil.Example "RT-Druid ant tasks") | Instantiates a single example |
| [rtdruid.Oil.Examples](RT-Druid_ant_tasks--2303.md#rtdruid.Oil.Examples "RT-Druid ant tasks") | Instantiates all examples managed by RT-Druid |
| [rtdruid.templates.path.add](RT-Druid_ant_tasks--2303.md#rtdruid.templates.path.add "RT-Druid ant tasks") | Add additional paths where search templates |

[Here](http://ant.apache.org/) you can find info about ant.

<a id="RT-Druid_scripts"></a>

### RT-Druid scripts

Here is the list of available scripts:

| Task Name | Description |
| [generate\_code](RT-Druid_scripts--2302.md#Generate_Code "RT-Druid scripts") | Generates all configuration files for Erika Enterprise |
| [instantiate\_template](RT-Druid_scripts--2302.md#Instantiate_template "RT-Druid scripts") | Instantiates a template |
| [start\_ant](RT-Druid_scripts--2302.md#Start_Ant "RT-Druid scripts") | Executes an ant script using ant libraries provided with eclipse |

Each script is available in for windows (with .bat suffix) and for cygwin/linux (with .sh suffix).

```
 Please note that current version of generate_code.sh requires bash to work
```

<a id="Makefile_examples"></a>

### Makefile examples

Here there are two examples about how use RT-Druid command line versions. In both makefile, main targets are:

- download or just update RT-Druid and Erika Enterprise
- configure the system
- build

The first  [makefile](Makefile_RT-Druid_CLI_with_EE_svn--2305.md "Makefile: RT-Druid CLI with EE svn") gets Erika Enterprise directly from svn and the package with RT-Druid only. In this way it easier to read and modify Erika Enterprise files.

The second  [makefile](Makefile_EE_RT-Druid_CLI--2306.md "Makefile: EE RT-Druid CLI") gets the package with both Erika Enterprise and RT-Druid. The benefit is that this couple passed all tests we do before release RT-Druid packages.

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Tutorial%3A_RT-Druid_Command_Line) · [Archived source revision 4731](http://erika.tuxfamily.org/wiki/index.php?oldid=4731)
- Last source edit: 2012-04-02T11:41:07Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Nicola.
- [Original MediaWiki source](../source/wikitext/2301.mediawiki) · [Original editing history](../source/history/batch-011.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
