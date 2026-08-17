
# Type 181 Enum

The resource for which you want to receive notifications. Possible values:

* **balancePlatform**: receive notifications about balance changes in your entire balance platform.

* **accountHolder**: receive notifications about balance changes of a specific user.

* **balanceAccount**: receive notifications about balance changes in a specific balance account.

## Enumeration

`Type181Enum`

## Fields

| Name |
|  --- |
| `BALANCEACCOUNT` |
| `ACCOUNTHOLDER` |
| `BALANCEPLATFORM` |

## Example

```python
from adyen.models.type_181_enum import Type181Enum

type_181 = Type181Enum.BALANCEACCOUNT
```

