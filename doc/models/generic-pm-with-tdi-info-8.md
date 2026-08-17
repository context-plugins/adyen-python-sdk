
# Generic Pm with Tdi Info 8

Details to provide if `type` is **maestro**.
In the US, `maestro` is not supported; use `maestro_usa` instead.

## Structure

`GenericPmWithTdiInfo8`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.generic_pm_with_tdi_info_8 import GenericPmWithTdiInfo8
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

generic_pm_with_tdi_info_8 = GenericPmWithTdiInfo8(
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

