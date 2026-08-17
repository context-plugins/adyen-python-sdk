
# List Terminals Response

## Structure

`ListTerminalsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks1`](../../doc/models/pagination-links-1.md) | Optional | Pagination references. |
| `data` | [`List[Terminal]`](../../doc/models/terminal.md) | Optional | The list of terminals and their details. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |

## Example

```python
from adyen.models.links_element_10 import LinksElement10
from adyen.models.links_element_11 import LinksElement11
from adyen.models.links_element_12 import LinksElement12
from adyen.models.links_element_13 import LinksElement13
from adyen.models.links_element_9 import LinksElement9
from adyen.models.list_terminals_response import ListTerminalsResponse
from adyen.models.pagination_links_1 import PaginationLinks1
from adyen.models.status_21_enum import Status21Enum
from adyen.models.status_31_enum import Status31Enum
from adyen.models.terminal import Terminal
from adyen.models.terminal_assignment_2 import TerminalAssignment2
from adyen.models.terminal_connectivity_2 import TerminalConnectivity2
from adyen.models.terminal_connectivity_bluetooth import TerminalConnectivityBluetooth
from adyen.models.terminal_connectivity_cellular import TerminalConnectivityCellular
from adyen.models.terminal_connectivity_ethernet import TerminalConnectivityEthernet
from adyen.models.terminal_connectivity_wifi import TerminalConnectivityWifi
from adyen.models.terminal_reassignment_target_2 import TerminalReassignmentTarget2

list_terminals_response = ListTerminalsResponse(
    items_total=224,
    pages_total=186,
    links=PaginationLinks1(
        first=LinksElement9(
            href='href2'
        ),
        last=LinksElement10(
            href='href2'
        ),
        mself=LinksElement13(
            href='href0'
        ),
        next=LinksElement11(
            href='href4'
        ),
        prev=LinksElement12(
            href='href8'
        )
    ),
    data=[
        Terminal(
            assignment=TerminalAssignment2(
                company_id='companyId6',
                status=Status21Enum.INVENTORY,
                merchant_id='merchantId2',
                reassignment_target=TerminalReassignmentTarget2(
                    inventory=False,
                    company_id='companyId4',
                    merchant_id='merchantId0',
                    store_id='storeId8'
                ),
                store_id='storeId0'
            ),
            cloud_device_api_endpoint='cloudDeviceApiEndpoint2',
            connectivity=TerminalConnectivity2(
                bluetooth=TerminalConnectivityBluetooth(
                    ip_address='ipAddress2',
                    mac_address='macAddress2'
                ),
                cellular=TerminalConnectivityCellular(
                    iccid='iccid6',
                    iccid_2='iccid24',
                    status=Status31Enum.DEPRECATED
                ),
                ethernet=TerminalConnectivityEthernet(
                    ip_address='ipAddress2',
                    link_negotiation='linkNegotiation6',
                    mac_address='macAddress2'
                ),
                wifi=TerminalConnectivityWifi(
                    ip_address='ipAddress8',
                    mac_address='macAddress6',
                    ssid='ssid4'
                )
            ),
            country_code='countryCode6',
            firmware_version='firmwareVersion2'
        ),
        Terminal(
            assignment=TerminalAssignment2(
                company_id='companyId6',
                status=Status21Enum.INVENTORY,
                merchant_id='merchantId2',
                reassignment_target=TerminalReassignmentTarget2(
                    inventory=False,
                    company_id='companyId4',
                    merchant_id='merchantId0',
                    store_id='storeId8'
                ),
                store_id='storeId0'
            ),
            cloud_device_api_endpoint='cloudDeviceApiEndpoint2',
            connectivity=TerminalConnectivity2(
                bluetooth=TerminalConnectivityBluetooth(
                    ip_address='ipAddress2',
                    mac_address='macAddress2'
                ),
                cellular=TerminalConnectivityCellular(
                    iccid='iccid6',
                    iccid_2='iccid24',
                    status=Status31Enum.DEPRECATED
                ),
                ethernet=TerminalConnectivityEthernet(
                    ip_address='ipAddress2',
                    link_negotiation='linkNegotiation6',
                    mac_address='macAddress2'
                ),
                wifi=TerminalConnectivityWifi(
                    ip_address='ipAddress8',
                    mac_address='macAddress6',
                    ssid='ssid4'
                )
            ),
            country_code='countryCode6',
            firmware_version='firmwareVersion2'
        )
    ]
)
```

