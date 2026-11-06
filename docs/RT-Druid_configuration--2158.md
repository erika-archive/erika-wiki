# RT-Druid configuration

<a id="Ways_to_configure_RT-Druid"></a>

## Ways to configure RT-Druid

It is possible to configure some aspects of RT-Druid using three different approaches

- environment variables: usually used for both command line and graphical execution of RT-Druid

- configuration file: usually used only during batch (command line) execution of RT-Druid. It is a plain text file that uses the *java properties* format: each line is composed by a pair **keyword = value**, while lines starting with **#** are considered comments. The default name of configuration file is **common\_oil.pref** and it is placed in *rtdruid\_base\_path/configuration/common\_oil.pref* (see also [Common\_oil.pref\_example](Common_oil.pref_example--2161.md "Common oil.pref example"))

- eclipse preferences: usually used only during graphical execution of RT-Druid

<a id="Erika_Enterprise_Files_path"></a>

## Erika Enterprise Files path

The path of Erika Enterprise files inside your system should be wrote using the native format of your system. This means that under windows, it is a windows path even if everything is compiled using cygwin.

- **User value**: Using the graphical interface, it is possible to override this default value, both for the whole workspace and for each single project.

- **environment** : **ERIKA\_FILES** is the environment variable where RT-Druid looks for Erika Enterprise path. Note that the old variable EE\_BASE is deprecated, is not considered by RT-Druid and should be used only inside makefiles.

- **configuration files**: the keyword **erika\_enterprise\_location** is used in the RT-Druid configuration file to set the path to Erika Enterprise files. Note that this path can be written using eclipse variables. The most useful is ${eclipse\_home} because it allow to write a path relative to the eclipse installation directory.

```
Please note that, under windows, you can use both / and \ to separate paths but if you choose to use \ you have to protect them with another \. Here is an example:
erika_enterprise_location = C:\\Evidence\\ErikaEnterpriseFiles
```

- **plugins**: By default, RT-Druid is configured to use Erika Enterprise files in *com.eu.evidence.ee* plugin (a component of RT-Druid distribution).

<a id="Priority_and_validity"></a>

### Priority and validity

Here is a table that compare priority and application of each method used to set Erika Enterprise files path. Elements with higher priority override those elements with lower priority.

| What | Priority | GUI  support | Batch  support | Where | When | Description |
| --- | --- | --- | --- | --- | --- | --- |
| User Value | Highest | X |  | Project/workspace property | hardcoded in the project,  than always valid even if the project   is shared among different instances of RT-Druid | Value set by the user in the project/workspace properties. |
| ERIKA\_FILES | High | X | X | Environment | is valid only in the current instance of RT-Druid | Environment variable set before run RT-Druid. |
| erika\_enterprise\_location | Middle | X | X | defined in the configuration file es. configuration/common\_oil.pref (see also [Common\_oil.pref\_example](Common_oil.pref_example--2161.md "Common oil.pref example")) | this value is a property of the installation   and then is available for all instances of this installation | Configuration of a particular installation of RT-Druid. |
| plugins | Low | X | X | set inside RT-Druid/Erika plugins | RT-Druid distributions | it is a feature of a specific RT-Druid distribution version |

<a id="Examples"></a>

### Examples

Environment

```
Windows (set environment variable)
set ERIKA_FILES=C:\Evidence\ErikaEnterpriseFiles
```

```
Linux (set environment variable)
ERIKA_FILES=/opt/Evidence/ErikaEnterpriseFiles
export ERIKA_FILES
```

Configuration file

```
Configuation file with eclipse variables (by default rtdruid_base_path/configuration/common_oil.pref)
# pointing to ErikaEnterpriseFiles directory relative to RT-Druid base directory
# this works with both windows and linux
erika_enterprise_location = ${eclipse_home}/../ErikaEnterpriseFiles
```

```
Configuation file with windows path (by default rtdruid_base_path/configuration/common_oil.pref)
# pointing to ErikaEnterpriseFiles directory using an absolute path (example 1)
erika_enterprise_location = C:/Evidence/ErikaEnterpriseFiles
```

```
Configuation file with windows path (by default rtdruid_base_path/configuration/common_oil.pref)
# pointing to ErikaEnterpriseFiles directory using an absolute path (example 2)
erika_enterprise_location = C:\\Evidence\\ErikaEnterpriseFiles
```

```
Configuation file with linux path (by default rtdruid_base_path/configuration/common_oil.pref)
# pointing to ErikaEnterpriseFiles directory using an absolute path
erika_enterprise_location = /opt/Evidence/ErikaEnterpriseFiles
```

<a id="Erika_Enterprise_Templates_path"></a>

## Erika Enterprise Templates path

In additions to Erika Enterprise Templates, it is possible to specify additional directories. Where not specified, paths are expressed using the native formalism of your system. If you want to define more than one path, you can write each path separated by the default character for your system. Examples:

```
Windows example 1:   C:/Evidence/template_1;C:/Evidence/template_2
Windows example 2:   C:\\Evidence\\template_1;C:\\Evidence\\template_2
Linux example:   /opt/Evidence/template_1:/opt/Evidence/template_2
```

Please note that currently is only possible to add templates those provided by RT-Druid plugins, i.e. it is not possible to disable one or more template. It is possible to add templates providing path through:

- **environment** : **RTDRUID\_TEMPLATES\_PATH** is the environment variable where RT-Druid looks for paths of additional Erika Enterprise Templates.

- **ant task**: if you are using ant scripts, **rtdruid.templates.path.add path** is a RT-Druid task that allows to add one or more paths where RT-Druid will look for Erika Enterprise Templates. All paths

```
Please note that effects of this task are valid within a running instance of ant.
This means that an added path is available until the instance of ant is running.
```

- **configuration files**: the keyword **templates\_path** is used in the RT-Druid configuration file to set the path of additional Erika Enterprise templates.

```
Please note that, under windows, you can use both / and \ to separate paths 
but if you choose to use \ you have to protect them with another \. Here is an example:
templates_path = C:\\Evidence\\ErikaEnterpriseFiles
```

```
If more than one template uses the same ID, the first one is used.
To reduce indeterminism RT-Druid will search inside paths provided by environment variable,
then the ones provided by ant_task, then ones in configuration files and
as last resource the ones provided by RT-Druid plugins.
```

<a id="Examples_2"></a>

### Examples

Environment

```
Windows (set environment variable)
set RTDRUID_TEMPLATES_PATH=C:\Evidence\ErikaEnterpriseTemplates
```

```
Windows (set environment variable)
set RTDRUID_TEMPLATES_PATH=C:\Evidence\ErikaEnterpriseTemplates\path1;C:\Evidence\ErikaEnterpriseTemplates\path2
```

```
Linux (set environment variable)
RTDRUID_TEMPLATES_PATH=/opt/Evidence/ErikaEnterpriseTemplates
export RTDRUID_TEMPLATES_PATH
```

```
Linux (set environment variable)
RTDRUID_TEMPLATES_PATH=/opt/Evidence/ErikaEnterpriseTemplates/path1:/opt/Evidence/ErikaEnterpriseTemplates/path2
export RTDRUID_TEMPLATES_PATH
```

Configuration file

```
Configuation file with windows path (by default rtdruid_base_path/configuration/common_oil.pref)
# Single path (example 1)
templates_path = C:/Evidence/ErikaEnterpriseTemplates
```

```
Configuation file with windows path (by default rtdruid_base_path/configuration/common_oil.pref)
# Multiple path (example 2)
templates_path = C:/Evidence/ErikaEnterpriseTemplates/path1;C:/Evidence/ErikaEnterpriseTemplates/path2
```

```
Configuation file with windows path (by default rtdruid_base_path/configuration/common_oil.pref)
# Multiple path (example 3)
templates_path = C:\\Evidence\\ErikaEnterpriseTemplates\\path1;C:\\Evidence\\ErikaEnterpriseTemplates\\path2
```

```
Configuation file with linux path (by default rtdruid_base_path/configuration/common_oil.pref)
# Single path (example 1)
templates_path = /opt/Evidence/ErikaEnterpriseTemplates
```

```
Configuation file with linux path (by default rtdruid_base_path/configuration/common_oil.pref)
# Multiple path (example 2)
templates_path = /opt/Evidence/ErikaEnterpriseTemplates/path1:/opt/Evidence/ErikaEnterpriseTemplates/path2
```

Ant task

```
Using a Windows absolute path

<?xml version="1.0" encoding="UTF-8"?>
<project name="rtdruid" default="an_examples" basedir=".">
	
	<!-- Instantiates a single template -->
	<target name="an_example">
		<rtdruid.add.template.path path="c:/Evidence/Erika/ee/examples"/>

		<!-- default values -->
		<property name="example_output_dir" value="output"/>
		
		<!-- exec -->
		<rtdruid.Oil.Example ExampleID="${example_id}" OutputDirectory="${examples_output_dir}" />
	</target>
</project>
```

```
Using a linux absolute path

<?xml version="1.0" encoding="UTF-8"?>
<project name="rtdruid" default="an_examples" basedir=".">
	
	<!-- Instantiates a single template -->
	<target name="an_example">
		<rtdruid.add.template.path path="/opt/Evidence/Erika/ee/examples"/>

		<!-- default values -->
		<property name="example_output_dir" value="output"/>
		
		<!-- exec -->
		<rtdruid.Oil.Example ExampleID="${example_id}" OutputDirectory="${examples_output_dir}" />
	</target>
</project>
```

```
Using an ant variable

<?xml version="1.0" encoding="UTF-8"?>
<project name="rtdruid" default="an_examples" basedir=".">
	
	<!-- Instantiates a single template -->
	<target name="an_example">
		<rtdruid.add.template.path path="${erika_templates_path}"/>

		<!-- default values -->
		<property name="example_output_dir" value="output"/>
		
		<!-- exec -->
		<rtdruid.Oil.Example ExampleID="${example_id}" OutputDirectory="${examples_output_dir}" />
	</target>
</project>
```

<a id="Compiler_paths"></a>

## Compiler paths

Each architecture requires a different compiler. Usually it is possible to set it through GUI (workspace preferences) and in few cases it is set using environment variables.
Slowly we are increasing the number of compiler that can be set using RT-Druid configuration file.
Here is a list of available keywords:

- **preference\_arm7\_\_path\_for\_cc\_compiler** set the compiler path for arm7
- **preference\_avr8\_\_path\_for\_gcc\_compiler** set the compiler path for avr8
- **preference\_avr8\_\_path\_for\_arduino\_sdk** set the arduino SDK path (used by avr8)
- **preference\_pic30\_\_path\_for\_gcc\_compiler** and **preference\_pic30\_\_path\_for\_asm\_compiler** set c and asm compiler paths for dspic
- **preference\_pic32\_\_path\_for\_gcc\_compiler** and **preference\_pic32\_\_path\_for\_asm\_compiler** set c and asm compiler paths for pic32
- **preference\_cortex\_mx\_\_path\_for\_iar\_compiler** set the IAR compiler path for cortex mX
- **preference\_cortex\_mx\_\_path\_for\_ccs\_compiler** set the Texas Instruments TMS470 compiler path for cortex mX
- **preference\_cortex\_mx\_\_path\_for\_keil\_compiler** set the Keil uVision compiler path for cortex mX
- **preference\_renesas\_rl78\_\_path\_for\_ca78k0r\_compiler** set the Renesas compiler path for Renesas Rl78 CA78K0R
- **preference\_renesas\_rl78\_\_path\_for\_ccrl\_compiler** set the Renesas compiler path for Renesas Rl78 ccrl
- **preference\_renesas\_rl78\_\_path\_for\_csplus** set the CS+ path for Renesas Rl78
- **preference\_renesas\_rl78\_\_path\_for\_e2studio** set the E2Studio path for Renesas Rl78
- **preference\_renesas\_rx200\_\_path\_for\_ccrx\_compiler** set the Renesas compiler path for Renesas Rx200
- **preference\_S12\_\_path\_for\_codewarrior\_compiler** and **preference\_S12\_\_path\_for\_cosmic\_compiler** set the codewarrior and cosmic compiler paths for s12
- **preference\_ppc\_e200zx\_\_path\_for\_codewarrior\_compiler** set codewarrior compiler paths for powerpc
- **preference\_ppc\_e200zx\_\_path\_for\_diab\_compiler** set diab compiler paths for powerpc
- **preference\_tricore\_\_path\_for\_diab\_compiler** set Wind River Diab compiler path for Tricore AURIX
- **preference\_tricore\_\_path\_for\_gnu\_compiler** set HIGHTEC gcc compiler path for Tricore AURIX
- **preference\_tricore\_\_path\_for\_tasking\_compiler** set Altium TASKING compiler path for Tricore AURIX

<a id="Common_oil.pref"></a>

## Common\_oil.pref

Here is an [example of RT-Druid configuration file](Common_oil.pref_example--2161.md "Common oil.pref example").

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=RT-Druid_configuration) · [Archived source revision 6097](http://erika.tuxfamily.org/wiki/index.php?oldid=6097)
- Last source edit: 2017-07-11T14:17:41Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: WikiSysop, Outlawch, Nicola, Pj, Eguidieri.
- [Original MediaWiki source](../source/wikitext/2158.mediawiki) · [Original editing history](../source/history/batch-009.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
