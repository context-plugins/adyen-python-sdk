
# Interac Card Response Info 1

**interac_card** details

## Structure

`InteracCardResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_description` | [`TransactionDescriptionResponseInfo1`](../../doc/models/transaction-description-response-info-1.md) | Optional | Information regarding the transaction description. |

## Example

```python
from adyen.models.interac_card_response_info_1 import InteracCardResponseInfo1
from adyen.models.transaction_description_response_info_1 import TransactionDescriptionResponseInfo1
from adyen.models.type_8_enum import Type8Enum

interac_card_response_info_1 = InteracCardResponseInfo1(
    transaction_description=TransactionDescriptionResponseInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

