
# Mandate Bank Account

## Structure

`MandateBankAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`MandatePartyIdentification2`](../../doc/models/mandate-party-identification-2.md) | Required | Contains information about the owner of the counterparty bank account. |
| `account_identification` | [`MandateAccountIdentification2`](../../doc/models/mandate-account-identification-2.md) | Required | Contains the bank account details of the counterparty. The fields required in this object depend on the country of the bank account and the currency of the transfer. |

## Example

```python
from adyen.models.mandate_account_identification_2 import MandateAccountIdentification2
from adyen.models.mandate_bank_account import MandateBankAccount
from adyen.models.mandate_party_identification_2 import MandatePartyIdentification2

mandate_bank_account = MandateBankAccount(
    account_holder=MandatePartyIdentification2(
        full_name='fullName0'
    ),
    account_identification=MandateAccountIdentification2(
        mtype='MandateAccountIdentification2'
    )
)
```

