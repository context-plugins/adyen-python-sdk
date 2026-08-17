
# Name 6

## Structure

`Name6`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Required | Set to **requested** to request a [name validation](https://docs.adyen.com/payment-methods/cards/name-validation) to verify if the cardholder name provided by the shopper matches the cardholder name on file at the issuing bank. |

## Example

```python
from adyen.models.name_6 import Name6

name_6 = Name6(
    status='status0'
)
```

