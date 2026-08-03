
# Set Tax Electronic Delivery Consent Request

*This model accepts additional fields of type Any.*

## Structure

`SetTaxElectronicDeliveryConsentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `us_1099_k` | `bool` | Optional | Consent to electronically deliver tax form US1099-K. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.set_tax_electronic_delivery_consent_request import SetTaxElectronicDeliveryConsentRequest

set_tax_electronic_delivery_consent_request = SetTaxElectronicDeliveryConsentRequest(
    us_1099_k=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

