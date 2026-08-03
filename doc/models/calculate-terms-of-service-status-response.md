
# Calculate Terms of Service Status Response

*This model accepts additional fields of type Any.*

## Structure

`CalculateTermsOfServiceStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terms_of_service_types` | [`List[TermsOfServiceType]`](../../doc/models/terms-of-service-type.md) | Optional | The type of Terms of Service that the legal entity needs to accept. If empty, no Terms of Service needs to be accepted. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.calculate_terms_of_service_status_response import CalculateTermsOfServiceStatusResponse
from adyen.models.terms_of_service_type import TermsOfServiceType

calculate_terms_of_service_status_response = CalculateTermsOfServiceStatusResponse(
    terms_of_service_types=[
        TermsOfServiceType.ADYENPCCR
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

