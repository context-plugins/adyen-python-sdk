
# Platform Payment

*This model accepts additional fields of type Any.*

## Structure

`PlatformPayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `modification_merchant_reference` | `str` | Optional | The capture's merchant reference included in the transfer. |
| `modification_psp_reference` | `str` | Optional | The capture reference included in the transfer. |
| `payment_merchant_reference` | `str` | Optional | The payment's merchant reference included in the transfer. |
| `platform_payment_type` | [`PlatformPaymentType`](../../doc/models/platform-payment-type.md) | Optional | - |
| `psp_payment_reference` | `str` | Optional | The payment reference included in the transfer. |
| `mtype` | [`Type63`](../../doc/models/type-63.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.platform_payment import PlatformPayment
from adyen.models.platform_payment_type import PlatformPaymentType

platform_payment = PlatformPayment(
    modification_merchant_reference='modificationMerchantReference8',
    modification_psp_reference='modificationPspReference0',
    payment_merchant_reference='paymentMerchantReference2',
    platform_payment_type=PlatformPaymentType.INTERCHANGE,
    psp_payment_reference='pspPaymentReference8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

