
# BACS Account Identifier

## Structure

`BACSAccountIdentifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `sort_code` | `str` | Required | A number that identifies the specific bank and branch where a UK bank account is held. |

## Example

```python
from adyen.models.bacs_account_identifier import BACSAccountIdentifier

bacs_account_identifier = BACSAccountIdentifier(
    account_number='accountNumber2',
    sort_code='sortCode2'
)
```

