
# Check Tax Electronic Delivery Consent Response

*This model accepts additional fields of type Any.*

## Structure

`CheckTaxElectronicDeliveryConsentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `us_1099_k` | `bool` | Optional | Consent to electronically deliver tax form US1099-K. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.check_tax_electronic_delivery_consent_response import CheckTaxElectronicDeliveryConsentResponse

check_tax_electronic_delivery_consent_response = CheckTaxElectronicDeliveryConsentResponse(
    us_1099_k=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

