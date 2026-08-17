
# Sepa Direct Debit Update Info 1

Details to provide if `type` is **sepadirectdebit**.

## Structure

`SepaDirectDebitUpdateInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.sepa_direct_debit_update_info_1 import SepaDirectDebitUpdateInfo1
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

sepa_direct_debit_update_info_1 = SepaDirectDebitUpdateInfo1(
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

