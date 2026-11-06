# Makefile: EE RT-Druid CLI

This makefile has these main targets:

- download the last release of EE\_RT-Druid CLI package (i.e. RT-Druid with Erika Enterprise source files)
- use RT-Druid to configure the system
- build the system using Erika Enterprise files

The suggestion is to set TOOLS\_BASE in the environment before run the makefile. Examples:

- TOOLS\_BASE=C:/Evidence/
- TOOLS\_BASE=$HOME/Evidence

```
Important: This makefile does not handle correctly names and paths with white-spaces.
```

```
#############################################################
#
# CONVERT_PATH macro is used to get an absolute path that can
#              be used by host programs, like JAVA 
#
#############################################################

ifeq ($(strip $(HOST_OS)),)
HOST_OS :=$(shell uname -a)
endif

# CYGWIN Specific
ifeq ($(findstring CYGWIN, ${HOST_OS}), CYGWIN)
# CYGWIN
CONVERT_PATH_TO_OS = $(shell cygpath -m $(1))
CONVERT_PATH_TO_MK = $(shell cygpath $(1))
else
# DEFAULT (unix like)
CONVERT_PATH_TO_OS = $(1)
CONVERT_PATH_TO_MK = $(1)
endif 


#############################################################
#
# Tools paths. By defaylt all paths are related to TOOLS_BASE
#
#############################################################
TOOLS_BASE   ?= tools
RTDRUID_HOME ?= $(TOOLS_BASE)/RT-Druid
EE_TEMP      ?= $(TOOLS_BASE)/temp

# ERIKA_FILES should be an absolute path in the OS format, while EEBASE is in the 
# Makefile form and should be used only inside the makefile
ifdef ERIKA_FILES
export ERIKA_FILES
endif

# Output folder
BUILD_DIR ?= output

#############################################################
#
# HTTP URL of RT-Druid package.
#
#############################################################

# Example: tuxfamily standard path
RTDRUID_FILE_NAME ?=EE_RT-Druid_1.6.1.zip
RTDRUID_WEB_SITE ?= http://software.evidence.eu.com/ee_161/CLI/$(RTDRUID_FILE_NAME)

# Example: custom path with password
#   RTDRUID_FILE_NAME ?=MY_RT-Druid_1.6.1.zip
#   RTDRUID_WEB_SITE ?= --user=MyUser --ask-password http://software.evidence.eu.com/special_edition/$(RTDRUID_FILE_NAME)
#   RTDRUID_WEB_SITE ?= --user=MyUser --password=123456 http://software.evidence.eu.com/special_edition/$(RTDRUID_FILE_NAME)


#############################################################
#
# RT-Druid input files
#
#############################################################

# The list of input files.
# Current version of makefile does not support paths and file names with whitespace
# By default the input file is just "conf.oil". If the user set INPUTS_PATH, INPUTS
# will contain all files with suffix .oil, .arxml and .ertd
ifndef INPUTS
INPUTS := conf.oil
ifdef INPUTS_PATH
	INPUTS := $(shell find $(INPUTS_PATH) -iname "*.oil" -or -iname "*.ertd")
endif
else
ifdef INPUTS_PATH
	$(error INPUTS_PATH can be specified only if INPUTS is empty or unset)
endif
endif

ifneq ($(notdir $(RTDRUID_HOME)),RT-Druid)
$(warning RT-Druid update target works better if RTDRUID_HOME ends with RT-Druid)
endif

#############################################################
#
# HELP
#
#############################################################
.PHONY: help
help:
	@echo -e "\n\
	This makefile tries to setup the environment needed  to build  a system  based on\n\
	RT-Druid and Erika Enterprise.  The environment is downloaded and updated through\n\
	the web, using\n\
	- svn for Erikae Enterprise sources and\n\
	- wget for RT-Druid packages (here it is used the smallest Command Line package).\n\
	\n\
	Please note that this makefile cannot handle paths and filenames with whitespaces\n\
	\n\
	Targets:\n\
	update_ee_rtduid - updates RT-Druid packages and Erika Enterprise.\n\
	configure     - using RT-Druid, configure an Erika Enterprise system.\n\
	                Depends on RTDRUID_HOME and may call update_ee_rtduid.\n\
	build         - build the configurated system.\n\
	                Depends on RTDRUID_HOME and may call update_ee_rtduid.\n\
	build_clean   - clean the results of a build process, without touch the generated\n\
	                configuration.\n\
	all           - calls build_clean and build targets.\n\
	                Considering all dependecies, the result is:\n\
	                * tries to clean an existing build (all errors are ignored);\n\
	                * check if RT-Druid is available; if not, download a new one;\n\
	                * check if configuration folder exist and is newer than RT-Druid\n\
	                  folder; if not, runs RT-Druid to generate the new configuration\n\
	                * build the system\n\
	\n\
	Variables:\n\
	TOOLS_BASE   - path used to build  default values of  RT-Druid,  Erika Enterprise\n\
	               and temp folders.\n\
	               (current value = $(TOOLS_BASE) )\n\
	RTDRUID_HOME - path of RT-Druid package. It should end with RT-Druid.\n\
	               Default TOOL_BASE/RT-Druid\n\
	               (current value = $(RTDRUID_HOME) )\n\
	ERIKA_FILES  - even if discouraged,  it can be used to select a different path of\n\
	               Erika Enterprise sources. This path has to be in the host  format,\n\
	               i.e.  all  absolute  path are like  C:\\ee under windows, and like\n\
	               /opt/ee otherwise  ( usually relative paths  are the  same in both\n\
	               windows and linux).\n\
	               By default is unset and RT-Druid points  to erika enterprise files\n\
	               inside RT-Druid plugins\n\
	               (current value = $(ERIKA_FILES) )\n\
	EE_TEMP      - path of a folder  used to save bakups  and temporary files used to\n\
	               correctly do RT-Druid updates. Default TOOL_BASE/temp\n\
	               (current value = $(EE_TEMP) )\n\
	BUILD_DIR    - the path where  RT-Druid will place the folder with  all generated\n\
	               configuration files.\n\
	               (current value = $(BUILD_DIR) )\n\
	INPUTS       - list of files  (spaced by a whitespace) used by  RT-Druid as input\n\
	               for configuration generation process.\n\
	               Default conf.oil\n\
	               (current value = $(INPUTS) )\n\
	INPUTS_PATH  - identifies one or more folders (spaced by a whitespace) where look\n\
	               for RT-Druid input files. This variable cannnot be used if INPUTS\n\
	               is set.\n\
	               (current value = $(INPUTS_PATH) )\n\
	\n\
	Examples:\n\
	   make all\n\
	   TOOLS_BASE=/opt/evidence make all\n\
	   TOOLS_BASE=/opt/evidence INPUTS_PATH=conf make build\n\
	   INPUTS=\`ls --format=horizontal conf/*\` make build\n\
	   INPUTS=\`find conf -type f -printf \"%p \"\` make build"

#############################################################
#
# Update RT-Druid
#
#############################################################
.PHONY: update_rtdruid
update_rtdruid: download_rtdruid $(RTDRUID_HOME)

download_rtdruid $(EE_TEMP)/$(RTDRUID_FILE_NAME): 
	@echo -e "\
		=================================\n\
		          Update RT-Druid\n\
		================================="
	@mkdir -p $(EE_TEMP) ; \
	cd $(EE_TEMP) ; wget -N $(RTDRUID_WEB_SITE)

$(RTDRUID_HOME): $(EE_TEMP)/$(RTDRUID_FILE_NAME)
	@if [ -d "$(RTDRUID_HOME)" ]; then (\
		cp "$(RTDRUID_HOME)/configuration/common_oil.pref" $(EE_TEMP) 2>/dev/null ;\
		rm -rf "$(EE_TEMP)/RT-Druid_backup"; \
		mv "$(RTDRUID_HOME)" "$(EE_TEMP)/RT-Druid_backup" && \
		rm -rf $(RTDRUID_HOME) \
	) fi && \
	unzip $(EE_TEMP)/$(RTDRUID_FILE_NAME) -d $(TOOLS_BASE) && \
	(cp "$(EE_TEMP)/common_oil.pref" "$(RTDRUID_HOME)/configuration/"  2>/dev/null || exit 0); \
	if [ -d "$(RTDRUID_HOME)" ]; then (\
		touch $(RTDRUID_HOME) \
	) else ( \
		echo "RT-Druid HOME does not exist. Check zip file and RTDRUID_HOME"; exit 1 \
	) fi



#############################################################
#
# Use RT-Druid to configure Erika Enterprise
#
#############################################################
.PHONY: configure
configure $(BUILD_DIR): $(RTDRUID_HOME) $(INPUTS)
	@echo -e "\
		=================================\n\
		          Configure\n\
		================================="
	@bash $(RTDRUID_HOME)/evidence/generate_code.sh \
			$(RTDRUID_HOME) \
			$(call CONVERT_PATH_TO_OS, $(INPUTS)) \
			$(call CONVERT_PATH_TO_OS,$(BUILD_DIR)) && \
	(if [ -d "$(BUILD_DIR)" ]; then \
			touch $(BUILD_DIR) ; \
		else \
			echo "System configured but $(BUILD_DIR) does not exist" ; exit 1 ; \
	fi)

#############################################################
#
# Compile the system
#
#############################################################
.PHONY: build
build: $(BUILD_DIR) $(RTDRUID_HOME)
	@echo -e "\
		=================================\n\
		          Build\n\
		================================="
	@cd $(BUILD_DIR) ; \
	make

#############################################################
#
# Clean compile results
#
#############################################################
.PHONY: build_clean
build_clean: $(RTDRUID_HOME)
	@echo -e "\
		=================================\n\
		          Build Clean\n\
		================================="
	@rm -f $(BUILD_DIR)/build.log
	@if [ -d "$(BUILD_DIR)" ]; then cd $(BUILD_DIR) && make clean ; fi

#############################################################
#
# Clean Erika Enterprise configuration files generated by
# RT-Druid
#
#############################################################
.PHONY: conf_clean
conf_clean:
	@echo -e "\
		=================================\n\
		      Configuration clean\n\
		================================="
	@rm -rf $(BUILD_DIR)


#############################################################
#
# Clean prervious compile results and do a new build
#
#############################################################
.PHONY: all
all: build_clean build
```

---

## Archive provenance

- [Original page](http://erika.tuxfamily.org/wiki/index.php?title=Makefile%3A_EE_RT-Druid_CLI) · [Archived source revision 4738](http://erika.tuxfamily.org/wiki/index.php?oldid=4738)
- Last source edit: 2012-04-03T13:14:04Z. Source retrieved on 2026-11-06; Markdown conversion completed on 2026-11-07.
- Original contributors recorded in exported history: Nicola.
- [Original MediaWiki source](../source/wikitext/2306.mediawiki) · [Original editing history](../source/history/batch-007.xml)
- [Attribution and licensing notice](../NOTICE.md). Original file-specific notices, where present, remain applicable.
