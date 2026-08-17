
# Sepa Direct Debit Info 2

Details to provide if `type` is **sepadirectdebit**.

## Structure

`SepaDirectDebitInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `creditor_id` | `str` | Optional | Creditor id |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.sepa_direct_debit_info_2 import SepaDirectDebitInfo2
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

sepa_direct_debit_info_2 = SepaDirectDebitInfo2(
    creditor_id='creditorId6',
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

