
# JCB Response Info 1

**jcb** details

## Structure

`JCBResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mid_number` | `str` | Optional | MID (Merchant ID) number. |
| `reuse_mid_number` | `bool` | Optional | Indicates whether the JCB Merchant ID is reused from a previously setup JCB payment method. |
| `service_level` | `str` | Optional | Specifies the service level (settlement type) of this payment method. |
| `transaction_description` | [`TransactionDescriptionResponseInfo1`](../../doc/models/transaction-description-response-info-1.md) | Optional | Information regarding the transaction description. |

## Example

```python
from adyen.models.jcb_response_info_1 import JCBResponseInfo1
from adyen.models.transaction_description_response_info_1 import TransactionDescriptionResponseInfo1
from adyen.models.type_8_enum import Type8Enum

jcb_response_info_1 = JCBResponseInfo1(
    mid_number='midNumber8',
    reuse_mid_number=False,
    service_level='serviceLevel8',
    transaction_description=TransactionDescriptionResponseInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

