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
    #print(type(data))
    #pprint(data)
    #print(data['objects'])

    #Just prints out all the objects out of the template
    #print_data = json.dumps(data['objects'],indent=4)
    #print(print_data)
    for template_obj in data['objects']:
        if 'kind' in template_obj:
            #print the value of kind
            print(template_obj['kind'])
            #print(template_obj['kind']['spec'])

#with open('out.txt', 'w') as outfile:
#    json.dump(data, outfile,indent=4)

# vim: ai et ts=4 sts=4 sw=4 nu
