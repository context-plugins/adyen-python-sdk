
# Pay Pal Info

*This model accepts additional fields of type Any.*

## Structure

`PayPalInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `direct_capture` | `bool` | Optional | Indicates if direct (immediate) capture for PayPal is enabled. If set to **true**, this setting overrides the [capture](https://docs.adyen.com/online-payments/capture) settings of your merchant account. Default value: **true**. |
| `payer_id` | `str` | Required | PayPal Merchant ID. Character length and limitations: 13 single-byte alphanumeric characters.<br><br>**Constraints**: *Minimum Length*: `13`, *Maximum Length*: `13` |
| `subject` | `str` | Required | Your business email address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pay_pal_info import PayPalInfo

pay_pal_info = PayPalInfo(
    payer_id='payerId8',
    subject='subject6',
    direct_capture=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

