
# Pay by Bank Plaid Info 1

Details to provide if `type` is **paybybank_plaid**.

## Structure

`PayByBankPlaidInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo` | `str` | Optional | Merchant logo (max. size 150kB). Format: Base64-encoded string. |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.pay_by_bank_plaid_info_1 import PayByBankPlaidInfo1
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

pay_by_bank_plaid_info_1 = PayByBankPlaidInfo1(
    logo='logo0',
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

