# ocp-template-patch

## Overview

This python script applies a label selector to a persistent volume claim object within an OpenShift template. It simply reads in a template JSON file and writes the modified template to the file.


## Usage

Help:

```
template_patch.py -h
usage: template_patch.py [-h] [--debug] infile outfile label

Appends a selector to the persistent volume claim in the template

positional arguments:
  infile      Template file to read in. Must be a JSON file
  outfile     The modified template file to write to. Will be a JSON file
  label       The selector label that you want to apply

optional arguments:
  -h, --help  show this help message and exit
  --debug     Enable debugging output
```


Example Use:

```
$ template_patch.py ocp_mysql_template.json ocp_mysql_template_mod.json internal --debug
--------------------
INPUT FILE: ocp_mysql_template.json
OUTPUT FILE: ocp_mysql_template_mod.json
LABEL TO APPLY: internal
CLAIM LABEL STRING: {"selector":{"matchLabels": {"environment": "internal"}}}
--------------------
$
```
