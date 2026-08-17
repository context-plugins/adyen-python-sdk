
# Pay by Bank Plaid Update Info

## Structure

`PayByBankPlaidUpdateInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.pay_by_bank_plaid_update_info import PayByBankPlaidUpdateInfo
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

pay_by_bank_plaid_update_info = PayByBankPlaidUpdateInfo(
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

