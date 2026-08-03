
# Google Pay Info 1

Details to provide if `type` is **googlepay**.

*This model accepts additional fields of type Any.*

## Structure

`GooglePayInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Required | Google Pay [Merchant ID](https://support.google.com/paymentscenter/answer/7163092?hl=en). Character length and limitations: 16 alphanumeric characters or 20 numeric characters.<br><br>**Constraints**: *Minimum Length*: `16`, *Maximum Length*: `20` |
| `reuse_merchant_id` | `bool` | Optional | Indicates whether the Google Pay Merchant ID is used for several merchant accounts. Default value: **false**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.google_pay_info_1 import GooglePayInfo1

google_pay_info_1 = GooglePayInfo1(
    merchant_id='merchantId2',
    reuse_merchant_id=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

