
# Passcodes

## Structure

`Passcodes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `admin_menu_pin` | `str` | Optional | The passcode for the Admin menu and the Settings menu.<br><br>**Constraints**: *Maximum Length*: `6` |
| `refund_pin` | `str` | Optional | The passcode for referenced and unreferenced refunds on standalone terminals.<br><br>**Constraints**: *Maximum Length*: `6` |
| `screen_lock_pin` | `str` | Optional | The passcode to unlock the terminal screen after a timeout.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `6` |
| `tx_menu_pin` | `str` | Optional | The passcode for the Transactions menu.<br><br>**Constraints**: *Maximum Length*: `6` |

## Example

```python
from adyen.models.passcodes import Passcodes

passcodes = Passcodes(
    admin_menu_pin='adminMenuPin0',
    refund_pin='refundPin4',
    screen_lock_pin='screenLockPin4',
    tx_menu_pin='txMenuPin4'
)
```

