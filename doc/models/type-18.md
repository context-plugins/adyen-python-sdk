
# Type 18

The resource for which you want to receive notifications. Possible values:

* **balancePlatform**: receive notifications about balance changes in your entire balance platform.

* **accountHolder**: receive notifications about balance changes of a specific user.

* **balanceAccount**: receive notifications about balance changes in a specific balance account.

## Enumeration

`Type18`

## Fields

| Name |
|  --- |
| `BALANCEACCOUNT` |
| `ACCOUNTHOLDER` |
| `BALANCEPLATFORM` |

## Example

```python
from adyen.models.type_18 import Type18

type_18 = Type18.ACCOUNTHOLDER
```

