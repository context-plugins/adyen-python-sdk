
# Terminal

*This model accepts additional fields of type Any.*

## Structure

`Terminal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assignment` | [`TerminalAssignment`](../../doc/models/terminal-assignment.md) | Optional | - |
| `cloud_device_api_endpoint` | `str` | Optional | The [regional base URL](https://docs.adyen.com/api-explorer/terminal-api/1/overview#endpoints-for-cloud-communications) to use for sending Terminal API requests when using cloud communications. |
| `connectivity` | [`TerminalConnectivity`](../../doc/models/terminal-connectivity.md) | Optional | - |
| `country_code` | `str` | Optional | The country code of the country where the terminal is located. |
| `firmware_version` | `str` | Optional | The software release currently in use on the terminal. |
| `id` | `str` | Optional | The unique identifier of the terminal. |
| `installed_ap_ks` | [`List[InstalledApKs]`](../../doc/models/installed-ap-ks.md) | Optional | A list of Android apps installed on the terminal. |
| `last_activity_at` | `datetime` | Optional | Date and time of the last activity on the terminal. Not included when the last activity was more than 14 days ago. |
| `last_transaction_at` | `datetime` | Optional | Date and time of the last transaction on the terminal. Not included when the last transaction was more than 14 days ago. |
| `model` | `str` | Optional | The model name of the terminal. |
| `restart_local_time` | `str` | Optional | The exact time of the terminal reboot, in the timezone of the terminal in **HH:mm** format. |
| `serial_number` | `str` | Optional | The serial number of the terminal. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

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

terminal = Terminal(
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
    cloud_device_api_endpoint='cloudDeviceApiEndpoint4',
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
    country_code='countryCode2',
    firmware_version='firmwareVersion4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

