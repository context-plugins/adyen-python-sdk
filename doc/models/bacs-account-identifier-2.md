
# BACS Account Identifier 2

Identifiers relevant for Bankers' Automated Clearing Services (BACS) payments, primarily used in the United Kingdom.

## Structure

`BACSAccountIdentifier2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `sort_code` | `str` | Required | A number that identifies the specific bank and branch where a UK bank account is held. |

## Example

```python
from adyen.models.bacs_account_identifier_2 import BACSAccountIdentifier2

bacs_account_identifier_2 = BACSAccountIdentifier2(
    account_number='accountNumber4',
    sort_code='sortCode6'
)
```

