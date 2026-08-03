
# Donation 1

The object that contains the details of the donation.

*This model accepts additional fields of type Any.*

## Structure

`Donation1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes/). |
| `donation_type` | `str` | Optional | The [type of donation](https://docs.adyen.com/online-payments/donations/#donation-types).<br><br>Possible values:<br><br>* **roundup**: a donation where the original transaction amount is rounded up as a donation.<br>* **fixedAmounts**: a donation where you show fixed donations amounts that the shopper can select from. |
| `max_roundup_amount` | `int` | Optional | The maximum amount a transaction can be rounded up to make a donation. This field is only present when `donationType` is **roundup**. |
| `mtype` | `str` | Required | The [type of donation](https://docs.adyen.com/online-payments/donations/#donation-types).<br><br>Possible values:<br><br>* **roundup**: a donation where the original transaction amount is rounded up as a donation.<br>* **fixedAmounts**: a donation where you show fixed donation amounts that the shopper can select from. |
| `values` | `List[int]` | Optional | The fixed donation amounts in [minor units](https://docs.adyen.com/development-resources/currency-codes//#minor-units). This field is only present when `donationType` is **fixedAmounts**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.donation_1 import Donation1

donation_1 = Donation1(
    currency='currency4',
    mtype='type4',
    donation_type='donationType8',
    max_roundup_amount=104,
    values=[
        36,
        37,
        38
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

