

# ansible-module-vcloud-director

## Overview
ansible-module-vcloud-director is a set of ansible modules that manage a VMware vCloud Director instance.

## Try it out

### Prerequisites

* The [pyvcloud](https://github.com/vmware/pyvcloud) module is required. 
* vCD Ansible modules require Python 3.6 or above.

### Build & Run

1. pip install --user pyvcloud
2. git clone https://github.com/vmware/ansible-module-vcloud-director
3. cd ansible-module-vcloud-director

## Documentation

Refer [docs](https://github.com/vmware/ansible-module-vcloud-director/tree/master/docs) to know more about available modules's usage.

1. vcd_catalog
2. vcd_catalog_item
3. vcd_disk
4. vcd_external_network
5. vcd_gateway_info
6. vcd_gateway_services
7. vcd_org
8. vcd_org_vdc
9. vcd_roles
10. vcd_user
11. vcd_vapp
12. vcd_vapp_network
13. vcd_vapp_vm
14. vcd_vapp_vm_disk
15. vcd_vapp_vm_nic
16. vcd_vapp_vm_snapshot
17. vcd_vdc_gateway
18. vcd_vdc_network
19. vcd_vdc_vm

## Releases & Major Branches

Following is the version matrix tested and supported through vCD ansible modules,

| vCD Version   | Pyvcloud Version | API Versions       |
| ------------- | :-------------:  | -----:             |
| vCD 9.1       | 20.1             | 28.0 / 29.0 / 30.0 |

Note - Testing is still in progress for new releases of vCD and Pyvcloud.

## Contributing

The ansible-module-vcloud-director project team welcomes contributions from the community. Before you start working with ansible-module-vcloud-director, please read our [Developer Certificate of Origin](https://cla.vmware.com/dco). All contributions to this repository must be signed as described on that page. Your signature certifies that you wrote the patch or have the right to pass it on as an open-source patch. For more detailed information, refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## License
[BSD-2 License or GPLv3](LICENSE.txt)
