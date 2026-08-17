
# Sepa Direct Debit Info

## Structure

`SepaDirectDebitInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `creditor_id` | `str` | Optional | Creditor id |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.sepa_direct_debit_info import SepaDirectDebitInfo
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

sepa_direct_debit_info = SepaDirectDebitInfo(
    creditor_id='creditorId8',
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

