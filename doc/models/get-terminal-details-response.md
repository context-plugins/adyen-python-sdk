
# Get Terminal Details Response

*This model accepts additional fields of type Any.*

## Structure

`GetTerminalDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bluetooth_ip` | `str` | Optional | The Bluetooth IP address of the terminal. |
| `bluetooth_mac` | `str` | Optional | The Bluetooth MAC address of the terminal. |
| `company_account` | `str` | Required | The company account that the terminal is associated with. If this is the only account level shown in the response, the terminal is assigned to the inventory of the company account. |
| `country` | `str` | Optional | The country where the terminal is used. |
| `device_model` | `str` | Optional | The model name of the terminal. |
| `dhcp_enabled` | `bool` | Optional | Indicates whether assigning IP addresses through a DHCP server is enabled on the terminal. |
| `display_label` | `str` | Optional | The label shown on the status bar of the display. This label (if any) is specified in your Customer Area. |
| `ethernet_ip` | `str` | Optional | The terminal's IP address in your Ethernet network. |
| `ethernet_mac` | `str` | Optional | The terminal's MAC address in your Ethernet network. |
| `firmware_version` | `str` | Optional | The software release currently in use on the terminal. |
| `iccid` | `str` | Optional | The integrated circuit card identifier (ICCID) of the SIM card in the terminal. |
| `last_activity_date_time` | `datetime` | Optional | Date and time of the last activity on the terminal. Not included when the last activity was more than 14 days ago. |
| `last_transaction_date_time` | `datetime` | Optional | Date and time of the last transaction on the terminal. Not included when the last transaction was more than 14 days ago. |
| `link_negotiation` | `str` | Optional | The Ethernet link negotiation that the terminal uses:<br><br>- `auto`: Auto-negotiation<br><br>- `100full`: 100 Mbps full duplex |
| `merchant_account` | `str` | Optional | The merchant account that the terminal is associated with. If the response doesn't contain a `store` the terminal is assigned to this merchant account. |
| `merchant_inventory` | `bool` | Optional | Boolean that indicates if the terminal is assigned to the merchant inventory. This is returned when the terminal is assigned to a merchant account.<br><br>- If **true**, this indicates that the terminal is in the merchant inventory. This also means that the terminal cannot be boarded.<br><br>- If **false**, this indicates that the terminal is assigned to the merchant account as an in-store terminal. This means that the terminal is ready to be boarded, or is already boarded. |
| `permanent_terminal_id` | `str` | Optional | The permanent terminal ID. |
| `serial_number` | `str` | Optional | The serial number of the terminal. |
| `sim_status` | `str` | Optional | On a terminal that supports 3G or 4G connectivity, indicates the status of the SIM card in the terminal: ACTIVE or INVENTORY. |
| `store` | `str` | Optional | The store code of the store that the terminal is assigned to. |
| `store_details` | [`Store1`](../../doc/models/store-1.md) | Optional | - |
| `terminal` | `str` | Required | The unique terminal ID. |
| `terminal_status` | [`TerminalStatus`](../../doc/models/terminal-status.md) | Optional | - |
| `wifi_ip` | `str` | Optional | The terminal's IP address in your Wi-Fi network. |
| `wifi_mac` | `str` | Optional | The terminal's MAC address in your Wi-Fi network. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.get_terminal_details_response import GetTerminalDetailsResponse

get_terminal_details_response = GetTerminalDetailsResponse(
    company_account='companyAccount8',
    terminal='terminal2',
    bluetooth_ip='bluetoothIp0',
    bluetooth_mac='bluetoothMac4',
    country='country8',
    device_model='deviceModel2',
    dhcp_enabled=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

