
# JCB Info 1

Details to provide if `type` is **jcb**.
For merchants operating in Japan, `midNumber`, `reuseMidNumber`, and `serviceLevel` fields are required.
For merchants operating outside of Japan, these fields are not required.
For merchants operating in Australia, New Zealand & Canada, JCB and American Express are automatically requested together.

## Structure

`JCBInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mid_number` | `str` | Optional | MID (Merchant ID) number. Required for merchants operating in Japan or merchants operating in Canada, Australia and New Zealand when requesting `gatewayContract` or `paymentDesignatorContract` service levels.Format: 14 numeric characters for Japan, 10 numeric characters for Canada, Australia and New Zealand.<br><br>**Constraints**: *Maximum Length*: `14` |
| `reuse_mid_number` | `bool` | Optional | Indicates whether the JCB Merchant ID is reused from a previously setup JCB payment method.<br>The default value is **false**.For merchants operating in Japan, this field is required and must be set to **true**.<br><br>**Default**: `False` |
| `service_level` | [`ServiceLevel2Enum`](../../doc/models/service-level-2-enum.md) | Optional | Specifies the service level (settlement type) of this payment method. Required for merchants operating in Japan.<br>Possible values:<br><br>* **noContract**: Adyen holds the contract with JCB for merchants operating in Japan or American Express for merchants operating in Canada, Australia and New Zealand.<br>* **gatewayContract**: JCB or American Express receives the settlement and handles disputes, then pays out to you or your sub-merchant directly.<br>* **paymentDesignatorContract**: Available only for merchants operating in Canada, Australia and New Zealand. Adyen receives the settlement, and handles disputes and payouts. |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.jcb_info_1 import JCBInfo1
from adyen.models.service_level_2_enum import ServiceLevel2Enum
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

jcb_info_1 = JCBInfo1(
    mid_number='midNumber6',
    reuse_mid_number=False,
    service_level=ServiceLevel2Enum.PAYMENTDESIGNATORCONTRACT,
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

