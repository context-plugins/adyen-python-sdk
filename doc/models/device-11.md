
# Device 11

Logical device located on a Sale Terminal or a POI Terminal, in terms of class of information to output (display, print, or store), or input (keyboard) for the Cashier or the Customer.
Possible values:

* **CashierDisplay**
* **CashierInput**
* **CustomerDisplay**
* **CustomerInput**

## Enumeration

`Device11`

## Fields

| Name |
|  --- |
| `CASHIERDISPLAY` |
| `CUSTOMERDISPLAY` |
| `CASHIERINPUT` |
| `CUSTOMERINPUT` |

## Example

```python
from adyen.models.device_11 import Device11

device_11 = Device11.CASHIERDISPLAY
```

