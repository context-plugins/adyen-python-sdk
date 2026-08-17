
# RIX Account Identifier

## Structure

`RIXAccountIdentifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `clearing_number` | `str` | Required | The 4- to 5-digit clearing number, without separators or whitespace. |

## Example

```python
from adyen.models.rix_account_identifier import RIXAccountIdentifier

rix_account_identifier = RIXAccountIdentifier(
    account_number='accountNumber4',
    clearing_number='clearingNumber8'
)
```

