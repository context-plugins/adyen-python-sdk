
# Mandate Account Identification 2

Contains the bank account details of the counterparty. The fields required in this object depend on the country of the bank account and the currency of the transfer.

## Structure

`MandateAccountIdentification2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |

## Example

```python
from adyen.models.mandate_account_identification_2 import MandateAccountIdentification2

mandate_account_identification_2 = MandateAccountIdentification2(
    mtype='MandateAccountIdentification2'
)
```

