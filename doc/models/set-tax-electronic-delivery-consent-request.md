
# Set Tax Electronic Delivery Consent Request

## Structure

`SetTaxElectronicDeliveryConsentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `us_1099_k` | `bool` | Optional | Consent to electronically deliver tax form US1099-K. |

## Example

```python
from adyen.models.set_tax_electronic_delivery_consent_request import SetTaxElectronicDeliveryConsentRequest

set_tax_electronic_delivery_consent_request = SetTaxElectronicDeliveryConsentRequest(
    us_1099_k=False
)
```

