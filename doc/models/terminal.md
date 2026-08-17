
# Terminal

## Structure

`Terminal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assignment` | [`TerminalAssignment2`](../../doc/models/terminal-assignment-2.md) | Optional | Indicates the account level to which the terminal is assigned, the [assignment status](https://docs.adyen.com/point-of-sale/automating-terminal-management/assign-terminals-api), and where the terminals is in the process of being reassigned to. |
| `cloud_device_api_endpoint` | `str` | Optional | The [regional base URL](https://docs.adyen.com/api-explorer/terminal-api/1/overview#endpoints-for-cloud-communications) to use for sending Terminal API requests when using cloud communications. |
| `connectivity` | [`TerminalConnectivity2`](../../doc/models/terminal-connectivity-2.md) | Optional | Information about bluetooth, cellular, ethernet and wifi connectivity for the terminal. |
| `country_code` | `str` | Optional | The country code of the country where the terminal is located. |
| `firmware_version` | `str` | Optional | The software release currently in use on the terminal. |
| `id` | `str` | Optional | The unique identifier of the terminal. |
| `installed_ap_ks` | [`List[InstalledAPKs]`](../../doc/models/installed-ap-ks.md) | Optional | A list of Android apps installed on the terminal. |
| `last_activity_at` | `datetime` | Optional | Date and time of the last activity on the terminal. Not included when the last activity was more than 14 days ago. |
| `last_transaction_at` | `datetime` | Optional | Date and time of the last transaction on the terminal. Not included when the last transaction was more than 14 days ago. |
| `model` | `str` | Optional | The model name of the terminal. |
| `restart_local_time` | `str` | Optional | The exact time of the terminal reboot, in the timezone of the terminal in **HH:mm** format. |
| `serial_number` | `str` | Optional | The serial number of the terminal. |

## Example

```python
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

terminal = Terminal(
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
    cloud_device_api_endpoint='cloudDeviceApiEndpoint4',
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
    country_code='countryCode2',
    firmware_version='firmwareVersion4'
)
```

