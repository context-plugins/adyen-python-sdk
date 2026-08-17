
# Device 11 Enum

Logical device located on a Sale Terminal or a POI Terminal, in terms of class of information to output (display, print, or store), or input (keyboard) for the Cashier or the Customer.
Possible values:

* **CashierDisplay**
* **CashierInput**
* **CustomerDisplay**
* **CustomerInput**

## Enumeration

`Device11Enum`

## Fields

| Name |
|  --- |
| `CASHIERDISPLAY` |
| `CUSTOMERDISPLAY` |
| `CASHIERINPUT` |
| `CUSTOMERINPUT` |

## Example

```python
from adyen.models.device_11_enum import Device11Enum

device_11 = Device11Enum.CASHIERDISPLAY
```

