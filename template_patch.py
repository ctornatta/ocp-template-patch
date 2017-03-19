#!/usr/bin/env python
import json
from pprint import pprint

claim_label = {
                "selector": {
                     "matchLabels": {
                        "environment": "internal"
                    }
                }
              }

with open('ocp_mysql_template.json') as json_file:
    data = json.load(json_file)
    for index, kind_dict in enumerate(data['objects']):
         #Loop through and get index value
         #print('INDEX: {}'.format(index))

         if 'PersistentVolumeClaim' in kind_dict['kind']:
             print('Found you: {}'.format(index))
             data['objects'][index]['spec'].update(claim_label)

    #pprint(data)

with open('out.txt', 'w') as outfile:
    json.dump(data, outfile,indent=4)

# vim: ai et ts=4 sts=4 sw=4 nu
