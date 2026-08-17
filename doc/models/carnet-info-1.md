
# Carnet Info 1

Details to provide if `type` is **carnet**.

## Structure

`CarnetInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `add_mcc_acronym` | `bool` | Optional | Indicates whether to add the MCC acronym to the merchant name for Prosa acquirer in Mexico.<br>When set to **true**, the MCC acronym is automatically appended to the merchant name.<br>Default: **false**. |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.carnet_info_1 import CarnetInfo1
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

carnet_info_1 = CarnetInfo1(
    add_mcc_acronym=False,
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

