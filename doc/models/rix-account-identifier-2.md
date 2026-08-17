
# RIX Account Identifier 2

Identifiers relevant for the Rix (Russian Interbank eXchange) system, used for interbank payments within Russia.

## Structure

`RIXAccountIdentifier2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The account number of the bank account. |
| `clearing_number` | `str` | Required | The 4- to 5-digit clearing number, without separators or whitespace. |

## Example

```python
from adyen.models.rix_account_identifier_2 import RIXAccountIdentifier2

rix_account_identifier_2 = RIXAccountIdentifier2(
    account_number='accountNumber6',
    clearing_number='clearingNumber6'
)
```

