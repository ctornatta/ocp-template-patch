#!/usr/bin/env python
import json
from collections import OrderedDict

claim_label = {
                "selector": {
                     "matchLabels": {
                        "environment": "internal"
                    }
                }
              }

with open('ocp_mysql_template.json') as json_file:

    # load json file and keep the order
    data = json.load(json_file, object_pairs_hook=OrderedDict)

    # Since 'objects' is a list we need to get the index
    for index, kind_dict in enumerate(data['objects']):
         if 'PersistentVolumeClaim' in kind_dict['kind']:

            # Update the 'spec' dictionary with the claim label
            data['objects'][index]['spec'].update(claim_label)


with open('out.txt', 'w') as outfile:
    json.dump(data, outfile,indent=4)

# vim: ai et ts=4 sts=4 sw=4 nu
