# RT-Druid ant tasks

<a id="rtdruid.Convert"></a>

### rtdruid.Convert

This task takes one or more input files, merge them and produces a new single RT-Druid file.
If the output file does not support all informations contained in input files, they are discard (and lost).

Input files are provided by nested elements.

| Parameter | Description | Required |
| Store | The output file name | Yes |

| Nested Element | Description | Required |
| [FileList](http://ant.apache.org/manual/Types/filelist.html) | One or more input files. | No |
| [FileSet](http://ant.apache.org/manual/Types/fileset.html) | One or more input files. | No |

It is possible to specify a many FileList and FileSet elements as needed and the resulting collection of input files is
the union of all input files specified by each nested element.
The only requirement here is that resulting collection contains at least one input file.

```
<?xml version="1.0" encoding="UTF-8"?>
<project name="rtdruid" default="convert" basedir=".">
	<target name="convert">
		<!-- default values -->
		<property name="output_file" value="conf.oil"/>
		<rtdruid.Convert store="${output_file}">
			<fileset dir="conf_1">
				<include name="*.oil"/>
				<include name="*.ertd"/>
			</filset>
			<fileset dir="conf_2">
				<include name="*.rtd"/>
			</filset>
			<filelist dir="${conf.src}">
				<file name="base.oil"/>
				<file name="system.ertd"/>
			</filelist>
		</rtdruid.Convert>
	</target>
</project>
```

<a id="rtdruid.Oil.Configurator"></a>

### rtdruid.Oil.Configurator

This task takes one or more input files, merge them and produces the Erika Enterprise configuration files.
All generated files are saved in the specified output folder.

| Parameter | Description | Required |
| Preferencefile | The path of RT-Druid preferences file. | No |
| Inputfile | The input file. This parameter is useful if you need to specify a single input file. Additional input files can be specify using one or more nested elements to specify. | No |
| Outputdir | The output folder. If not specified, results are saved in the current folder. | No |

| Nested Element | Description | Required |
| [FileSet](http://ant.apache.org/manual/Types/fileset.html) | One or more input files. | No |

It is possible to specify a many FileSet elements as needed and the resulting collection of input files is
the union of all input files specified by each nested element and the .
The only requirement here is that resulting collection contains at least one input file.

```
<?xml version="1.0" encoding="UTF-8"?>
<project name="rtdruid" default="compile" basedir=".">
	<target name="compile">
		<!-- default values -->
		<property name="in_conf_file" value="conf.oil"/>
		<property name="pref_file" value=""/>
		<property name="conf_output_dir" value="debug"/>
	
	
		<rtdruid.Oil.Configurator Inputfile="${in_conf_file}" Preferencefile="${pref_file}" Outputdir="${conf_output_dir}"/>

		<rtdruid.Oil.Configurator Preferencefile="${pref_file}" Outputdir="${conf_output_dir}"/>
			<fileset dir="conf_1">
				<include name="*.oil"/>
				<include name="*.ertd"/>
			</filset>
			<fileset dir="conf_2">
				<include name="*.rtd"/>
			</filset>
		</rtdruid.Oil.Configurator>
	</target>

</project>
```

<a id="rtdruid.Oil.Example"></a>

### rtdruid.Oil.Example

This task Instantiates a single example.

| Parameter | Description | Required |
| ExampleID | Identifies the selected example. | Yes |
| OutputDirectory | The output folder. If not specified, results are saved in the current folder. | No |

```
<?xml version="1.0" encoding="UTF-8"?>
<project name="rtdruid" default="an_examples" basedir=".">
	
	<!-- Instantiates a single template -->
	<target name="an_example">
<!-- .....-->
		<rtdruid.Oil.Example ExampleID="${example_id}" OutputDirectory="${examples_output_dir}" />
	</target>
</project>
```

<a id="rtdruid.Oil.Examples"></a>

### rtdruid.Oil.Examples

This task instantiates all examples inside the specified folder.

| Parameter | Description | Required |
| AlsoConfigure | If set to `true`, RT-Druid will configure all instantiated templates. | Yes |
| OutputDirectory | The output folder. If not specified, results are saved in the current folder. | No |

```
<?xml version="1.0" encoding="UTF-8"?>
<project name="rtdruid" default="examples" basedir=".">
	<target name="examples">
<!-- .....-->
		<rtdruid.Oil.Examples AlsoConfigure="true" OutputDirectory="${examples_output_dir}" />
	</target>
</project>
```

<a id="rtdruid.templates.path.add"></a>

### rtdruid.templates.path.add

This task can be used to specify more paths where RT-Druid will look for new examples.

| Parameter | Description | Required |
| Path | A path of a folder in the filesystem. | Yes |

```
<?xml version="1.0" encoding="UTF-8"?>
<project name="rtdruid" default="an_example" basedir=".">
	
	<!-- Instantiates a single template -->
	<target name="an_example">
		<rtdruid.add.template.path path="c:/Evidence/Erika/ee/examples"/>
		<rtdruid.add.template.path path="${basedir}/../ee/examples"/>

		<!-- default values -->
		<property name="example_output_dir" value="output"/>
		
		<!-- exec -->
		<rtdruid.Oil.Example ExampleID="${example_id}" OutputDirectory="${examples_output_dir}" />
	</target>
</project>
```

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=RT-Druid_ant_tasks) · [Archived source revision 4703](http://erika.tuxfamily.org/wiki/index.php?oldid=4703)
- Last source edit: 2012-03-29T09:27:03Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Nicola.
- [Original MediaWiki source](../source/wikitext/2303.mediawiki) · [Original editing history](../source/history/batch-009.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
