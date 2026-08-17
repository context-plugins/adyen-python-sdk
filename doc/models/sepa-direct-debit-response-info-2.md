
# Sepa Direct Debit Response Info 2

**sepadirectdebit** details

## Structure

`SepaDirectDebitResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `creditor_id` | `str` | Optional | Creditor id |
| `transaction_description` | [`TransactionDescriptionResponseInfo1`](../../doc/models/transaction-description-response-info-1.md) | Optional | Information regarding the transaction description. |

## Example

```python
from adyen.models.sepa_direct_debit_response_info_2 import SepaDirectDebitResponseInfo2
from adyen.models.transaction_description_response_info_1 import TransactionDescriptionResponseInfo1
from adyen.models.type_8_enum import Type8Enum

sepa_direct_debit_response_info_2 = SepaDirectDebitResponseInfo2(
    creditor_id='creditorId8',
    transaction_description=TransactionDescriptionResponseInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

