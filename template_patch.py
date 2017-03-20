#!/usr/bin/env python
import json
import argparse
from collections import OrderedDict


claim_label = {
                    "selector": {
                        "matchLabels": {
                            "environment": "internal"
                        }
                    }
                }

def get_args():

    parser = argparse.ArgumentParser(description='Appends a selector to the persistent volume claim in the template')
    parser.add_argument("infile", type=str, help='Template file to read in. Must be a JSON file')
    parser.add_argument("outfile", type=str, help='The modified template file to write to. Will be a JSON file')
    parser.add_argument('--debug', action='store_true', help='Enable debugging output')

    args = parser.parse_args()

    return args

if __name__ == '__main__':

    args = get_args()

    with open(args.infile) as json_file:
        # load json file and keep the order
        data = json.load(json_file, object_pairs_hook=OrderedDict)

        # Since 'objects' is a list we need to get the index
        for index, kind_dict in enumerate(data['objects']):
             if 'PersistentVolumeClaim' in kind_dict['kind']:

                # Update the 'spec' dictionary with the claim label
                data['objects'][index]['spec'].update(claim_label)


    with open(args.outfile, 'w') as outfile:
        json.dump(data, outfile,indent=4)

# vim: ai et ts=4 sts=4 sw=4 nu
