
# Get Terms of Service Acceptance Infos Response

*This model accepts additional fields of type Any.*

## Structure

`GetTermsOfServiceAcceptanceInfosResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[TermsOfServiceAcceptanceInfo]`](../../doc/models/terms-of-service-acceptance-info.md) | Optional | The Terms of Service acceptance information. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.get_terms_of_service_acceptance_infos_response import GetTermsOfServiceAcceptanceInfosResponse
from adyen.models.terms_of_service_acceptance_info import TermsOfServiceAcceptanceInfo
from adyen.models.type_25 import Type25

get_terms_of_service_acceptance_infos_response = GetTermsOfServiceAcceptanceInfosResponse(
    data=[
        TermsOfServiceAcceptanceInfo(
            accepted_by='acceptedBy8',
            accepted_for='acceptedFor0',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id0',
            mtype=Type25.ADYENACCOUNT,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        TermsOfServiceAcceptanceInfo(
            accepted_by='acceptedBy8',
            accepted_for='acceptedFor0',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id0',
            mtype=Type25.ADYENACCOUNT,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

