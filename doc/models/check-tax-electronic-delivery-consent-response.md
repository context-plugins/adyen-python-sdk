
# Check Tax Electronic Delivery Consent Response

## Structure

`CheckTaxElectronicDeliveryConsentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `us_1099_k` | `bool` | Optional | Consent to electronically deliver tax form US1099-K. |

## Example

```python
from adyen.models.check_tax_electronic_delivery_consent_response import CheckTaxElectronicDeliveryConsentResponse

check_tax_electronic_delivery_consent_response = CheckTaxElectronicDeliveryConsentResponse(
    us_1099_k=False
)
```

