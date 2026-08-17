
# Diners Info 1

Details to provide if `type` is **diners**.
For merchants operating in Japan, Diners payments are processed through the JCB network. This means that you must include [JCB-specific fields](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/paymentMethodSettings/(paymentMethodId)#request-jcb) in this object.

## Structure

`DinersInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mid_number` | `str` | Optional | MID (Merchant ID) number. Required for merchants operating in Japan.<br>Format: 14 numeric characters.<br><br>**Constraints**: *Maximum Length*: `14` |
| `reuse_mid_number` | `bool` | Required | Indicates whether the JCB Merchant ID is reused from a previously configured JCB payment method.<br>The default value is **false**.<br>For merchants operating in Japan, this field is required and must be set to **true**.<br><br>**Default**: `False` |
| `service_level` | [`ServiceLevel1Enum`](../../doc/models/service-level-1-enum.md) | Optional | Specifies the service level (settlement type) of this payment method. Required for merchants operating in Japan. Possible values:<br><br>* **noContract**: Adyen holds the contract with JCB.<br>* **gatewayContract**: JCB receives the settlement and handles disputes, then pays out to you or your sub-merchant directly. |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.diners_info_1 import DinersInfo1
from adyen.models.service_level_1_enum import ServiceLevel1Enum
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

diners_info_1 = DinersInfo1(
    reuse_mid_number=False,
    mid_number='midNumber6',
    service_level=ServiceLevel1Enum.NOCONTRACT,
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

