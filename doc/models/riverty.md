
# Riverty

*This model accepts additional fields of type Any.*

## Structure

`Riverty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_address` | `str` | Optional | The address where to send the invoice. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `delivery_address` | `str` | Optional | The address where the goods should be delivered. |
| `device_fingerprint` | `str` | Optional | A string containing the shopper's device fingerprint. For more information, refer to [Device fingerprinting](https://docs.adyen.com/risk-management/device-fingerprinting).<br><br>**Constraints**: *Maximum Length*: `5000` |
| `iban` | `str` | Optional | The iban number of the customer<br><br>**Constraints**: *Maximum Length*: `34` |
| `merchant_data` | `str` | Optional | Base64-encoded merchant metadata (Extra Merchant Data) forwarded to Riverty at authorization.<br><br>**Constraints**: *Maximum Length*: `10240` |
| `personal_details` | `str` | Optional | Shopper name, date of birth, phone number, and email address. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `subtype` | `str` | Optional | The payment method subtype. |
| `mtype` | [`Type49`](../../doc/models/type-49.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.riverty import Riverty
from adyen.models.type_49 import Type49

riverty = Riverty(
    mtype=Type49.RIVERTY,
    billing_address='billingAddress8',
    checkout_attempt_id='checkoutAttemptId0',
    delivery_address='deliveryAddress0',
    device_fingerprint='deviceFingerprint0',
    iban='iban8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

