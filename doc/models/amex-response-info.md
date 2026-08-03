
# Amex Response Info

*This model accepts additional fields of type Any.*

## Structure

`AmexResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mid_number` | `str` | Optional | Merchant ID (MID) number. |
| `reuse_mid_number` | `bool` | Optional | Indicates whether the Amex Merchant ID is reused from a previously setup Amex payment method. |
| `service_level` | `str` | Optional | The service level (settlement type) of this payment method. Possible values:<br><br>* **noContract**: Adyen holds the contract with American Express.<br>* **gatewayContract**: American Express receives the settlement and handles disputes, then pays out to you or your sub-merchant directly.<br>* **paymentDesignatorContract**: Adyen receives the settlement, and handles disputes and payouts. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amex_response_info import AmexResponseInfo

amex_response_info = AmexResponseInfo(
    mid_number='midNumber4',
    reuse_mid_number=False,
    service_level='serviceLevel8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

