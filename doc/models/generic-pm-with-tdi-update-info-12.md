
# Generic Pm with Tdi Update Info 12

Details to provide if `type` is **maestro_usa**.
Only for Maestro USA, otherwise use `maestro`.

## Structure

`GenericPmWithTdiUpdateInfo12`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.generic_pm_with_tdi_update_info_12 import GenericPmWithTdiUpdateInfo12
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

generic_pm_with_tdi_update_info_12 = GenericPmWithTdiUpdateInfo12(
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

