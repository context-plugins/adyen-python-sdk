
# Diners Response Info

## Structure

`DinersResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mid_number` | `str` | Optional | MID (Merchant ID) number. |
| `reuse_mid_number` | `bool` | Optional | Indicates whether the JCB Merchant ID is reused from a previously configured JCB payment method. |
| `service_level` | `str` | Optional | The service level (settlement type) of this payment method. Possible values:<br><br>* **noContract**: Adyen holds the contract with JCB.<br>* **gatewayContract**: JCB receives the settlement and handles disputes, then pays out to you or your sub-merchant directly. |
| `transaction_description` | [`TransactionDescriptionResponseInfo1`](../../doc/models/transaction-description-response-info-1.md) | Optional | Information regarding the transaction description. |

## Example

```python
from adyen.models.diners_response_info import DinersResponseInfo
from adyen.models.transaction_description_response_info_1 import TransactionDescriptionResponseInfo1
from adyen.models.type_8_enum import Type8Enum

diners_response_info = DinersResponseInfo(
    mid_number='midNumber2',
    reuse_mid_number=False,
    service_level='serviceLevel4',
    transaction_description=TransactionDescriptionResponseInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

