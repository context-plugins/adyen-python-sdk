
# Calculate Terms of Service Status Response

## Structure

`CalculateTermsOfServiceStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terms_of_service_types` | [`List[TermsOfServiceTypeEnum]`](../../doc/models/terms-of-service-type-enum.md) | Optional | The type of Terms of Service that the legal entity needs to accept. If empty, no Terms of Service needs to be accepted. |

## Example

```python
from adyen.models.calculate_terms_of_service_status_response import CalculateTermsOfServiceStatusResponse
from adyen.models.terms_of_service_type_enum import TermsOfServiceTypeEnum

calculate_terms_of_service_status_response = CalculateTermsOfServiceStatusResponse(
    terms_of_service_types=[
        TermsOfServiceTypeEnum.ADYENPCCR
    ]
)
```

