
# List Terminals Response

*This model accepts additional fields of type Any.*

## Structure

`ListTerminalsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks`](../../doc/models/pagination-links.md) | Optional | - |
| `data` | [`List[Terminal]`](../../doc/models/terminal.md) | Optional | The list of terminals and their details. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.first import First
from adyen.models.last import Last
from adyen.models.list_terminals_response import ListTerminalsResponse
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.pagination_links import PaginationLinks
from adyen.models.prev import Prev
from adyen.models.status_24 import Status24
from adyen.models.status_32 import Status32
from adyen.models.terminal import Terminal
from adyen.models.terminal_assignment import TerminalAssignment
from adyen.models.terminal_connectivity import TerminalConnectivity
from adyen.models.terminal_connectivity_bluetooth import TerminalConnectivityBluetooth
from adyen.models.terminal_connectivity_cellular import TerminalConnectivityCellular
from adyen.models.terminal_connectivity_ethernet import TerminalConnectivityEthernet
from adyen.models.terminal_connectivity_wifi import TerminalConnectivityWifi
from adyen.models.terminal_reassignment_target import TerminalReassignmentTarget

list_terminals_response = ListTerminalsResponse(
    items_total=224,
    pages_total=186,
    links=PaginationLinks(
        first=First(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        last=Last(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mself=Self(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        next=Next(
            href='href4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        prev=Prev(
            href='href8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    data=[
        Terminal(
            assignment=TerminalAssignment(
                company_id='companyId6',
                status=Status24.INVENTORY,
                merchant_id='merchantId2',
                reassignment_target=TerminalReassignmentTarget(
                    inventory=False,
                    company_id='companyId4',
                    merchant_id='merchantId0',
                    store_id='storeId8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                store_id='storeId0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            cloud_device_api_endpoint='cloudDeviceApiEndpoint2',
            connectivity=TerminalConnectivity(
                bluetooth=TerminalConnectivityBluetooth(
                    ip_address='ipAddress2',
                    mac_address='macAddress2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                cellular=TerminalConnectivityCellular(
                    iccid='iccid6',
                    iccid_2='iccid24',
                    status=Status32.DEPRECATED,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ethernet=TerminalConnectivityEthernet(
                    ip_address='ipAddress2',
                    link_negotiation='linkNegotiation6',
                    mac_address='macAddress2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                wifi=TerminalConnectivityWifi(
                    ip_address='ipAddress8',
                    mac_address='macAddress6',
                    ssid='ssid4',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            country_code='countryCode6',
            firmware_version='firmwareVersion2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Terminal(
            assignment=TerminalAssignment(
                company_id='companyId6',
                status=Status24.INVENTORY,
                merchant_id='merchantId2',
                reassignment_target=TerminalReassignmentTarget(
                    inventory=False,
                    company_id='companyId4',
                    merchant_id='merchantId0',
                    store_id='storeId8',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                store_id='storeId0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            cloud_device_api_endpoint='cloudDeviceApiEndpoint2',
            connectivity=TerminalConnectivity(
                bluetooth=TerminalConnectivityBluetooth(
                    ip_address='ipAddress2',
                    mac_address='macAddress2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                cellular=TerminalConnectivityCellular(
                    iccid='iccid6',
                    iccid_2='iccid24',
                    status=Status32.DEPRECATED,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ethernet=TerminalConnectivityEthernet(
                    ip_address='ipAddress2',
                    link_negotiation='linkNegotiation6',
                    mac_address='macAddress2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                wifi=TerminalConnectivityWifi(
                    ip_address='ipAddress8',
                    mac_address='macAddress6',
                    ssid='ssid4',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            country_code='countryCode6',
            firmware_version='firmwareVersion2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

