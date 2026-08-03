
# Klarna

*This model accepts additional fields of type Any.*

## Structure

`Klarna`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_address` | `str` | Optional | The address where to send the invoice. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `delivery_address` | `str` | Optional | The address where the goods should be delivered. |
| `merchant_data` | `str` | Optional | Base64-encoded merchant metadata (Extra Merchant Data) forwarded to Klarna at authorization.<br><br>**Constraints**: *Maximum Length*: `10240` |
| `personal_details` | `str` | Optional | Shopper name, date of birth, phone number, and email address. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `subtype` | `str` | Optional | The type of flow to initiate. |
| `mtype` | [`Type34`](../../doc/models/type-34.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.klarna import Klarna
from adyen.models.type_34 import Type34

klarna = Klarna(
    mtype=Type34.KLARNA_B2B,
    billing_address='billingAddress8',
    checkout_attempt_id='checkoutAttemptId6',
    delivery_address='deliveryAddress6',
    merchant_data='merchantData4',
    personal_details='personalDetails8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

