# Copyright © 2018 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause OR GPL-3.0-only

# !/usr/bin/python


# from __future__ import (absolute_import, division, print_function)
# __metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
module: vdc_gateway_info
short_description: Ansible module to get info from edge gateway in vCloud Director.
version_added: "2.7"
description:
    - "Ansible module to get info from edge gateway in vCloud Director."
author:
    - Sergey Kuzakov <s.kuzakov@arenadata.io>
options:
    user:
        description:
            - vCloud Director user name
        type: str
        required: false
    password:
        description:
            - vCloud Director user password
        type: str
        required: false
    host:
        description:
            - vCloud Director host address
        type: str
        required: false
    org:
        description:
            - Organization name on vCloud Director to access i.e. System.
        type: str
        required: false
    vdc_name:
        description:
            - The name of the vdc where Gateway is going to be created.
        required: false
        type: str
    org_name:
        description:
            - Name of the organization the Gateway belongs to.
        type: str
        required: false
    state:
        description:
            - State of the Gateway.
        type: string
        required: true
        choices: ['get_info']
'''


EXAMPLES = '''
- name: Get first edge gateway's ip addresses mapping  
  vcd_gateway_info:
    user: "{{vcd_user}}"
    password: "{{vcd_password}}"
    host: "{{host}}"
    org_name: "{{customer_org}}"
    vdc_name: "{{vdc_name}}"
    state: get_info
  register: gw_info
'''


RETURN = '''
msg: success/failure message corresponding first edge gateway's ip addresses mapping
'''


from pyvcloud.vcd.org import Org
from pyvcloud.vcd.vdc import VDC
from pyvcloud.vcd.gateway import Gateway
from ansible.module_utils.vcd import VcdAnsibleModule


EDGE_NETWORK_STATES = ['get_info']


def vdc_gw_argument_spec():
    return dict(
        org_name=dict(type='str', required=True),
        vdc_name=dict(type='str', required=True),
        state=dict(choices=EDGE_NETWORK_STATES, required=True)
    )


class VdcGW_info(VcdAnsibleModule):
    def __init__(self, **kwargs):
        super(VdcGW_info, self).__init__(**kwargs)
        self.vdc_name = self.params.get('vdc_name')
        self.org_name = self.params.get('org_name')
        org_resource = self.client.get_org_by_name(self.org_name)
        self.org = Org(self.client, resource=org_resource)
        vdc_resource = self.org.get_vdc(self.vdc_name)
        self.vdc = VDC(self.client, name=self.vdc_name, resource=vdc_resource)

    def manage_states(self):
        state = self.params.get('state')
        if state == "get_info":
            return self.get_gw_info()

    def get_gw_info(self):
        response = dict()
        response['changed'] = False
        edge_gateways = self.vdc.list_edge_gateways()
        gateway_name = edge_gateways[0].get('name')
        href = edge_gateways[0].get('href')
        gateway = Gateway(self.client, gateway_name, href)
        try:
            response['edge_gateway'] = gateway.list_configure_ip_settings()
            response['edge_name'] = gateway_name
        except Warning:
            response['warnings'] = "Edge Gateway {0} is not present"

        return response


def main():
    argument_spec = vdc_gw_argument_spec()
    response = dict(msg=dict(type='str'))
    module = VdcGW_info(argument_spec=argument_spec, supports_check_mode=True)
    try:
        if not module.params.get('state'):
            raise Exception('Please provide the state for the resource.')

        response = module.manage_states()
        module.exit_json(**response)

    except Exception as error:
        response['msg'] = error.__str__()
        module.fail_json(**response)


if __name__ == '__main__':
    main()
