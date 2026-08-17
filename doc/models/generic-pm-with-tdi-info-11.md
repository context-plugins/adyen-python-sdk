
# Generic Pm with Tdi Info 11

Details to provide if `type` is **visa**.

## Structure

`GenericPmWithTdiInfo11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.generic_pm_with_tdi_info_11 import GenericPmWithTdiInfo11
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

generic_pm_with_tdi_info_11 = GenericPmWithTdiInfo11(
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

