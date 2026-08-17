
# Visa Response Info 2

**visa** details

## Structure

`VisaResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_description` | [`TransactionDescriptionResponseInfo1`](../../doc/models/transaction-description-response-info-1.md) | Optional | Information regarding the transaction description. |

## Example

```python
from adyen.models.transaction_description_response_info_1 import TransactionDescriptionResponseInfo1
from adyen.models.type_8_enum import Type8Enum
from adyen.models.visa_response_info_2 import VisaResponseInfo2

visa_response_info_2 = VisaResponseInfo2(
    transaction_description=TransactionDescriptionResponseInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

