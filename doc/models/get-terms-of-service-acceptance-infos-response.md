
# Get Terms of Service Acceptance Infos Response

## Structure

`GetTermsOfServiceAcceptanceInfosResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[TermsOfServiceAcceptanceInfo]`](../../doc/models/terms-of-service-acceptance-info.md) | Optional | The Terms of Service acceptance information. |

## Example

```python
import dateutil.parser

from adyen.models.get_terms_of_service_acceptance_infos_response import GetTermsOfServiceAcceptanceInfosResponse
from adyen.models.terms_of_service_acceptance_info import TermsOfServiceAcceptanceInfo
from adyen.models.type_64_enum import Type64Enum

get_terms_of_service_acceptance_infos_response = GetTermsOfServiceAcceptanceInfosResponse(
    data=[
        TermsOfServiceAcceptanceInfo(
            accepted_by='acceptedBy8',
            accepted_for='acceptedFor0',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id0',
            mtype=Type64Enum.ADYENACCOUNT
        ),
        TermsOfServiceAcceptanceInfo(
            accepted_by='acceptedBy8',
            accepted_for='acceptedFor0',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id0',
            mtype=Type64Enum.ADYENACCOUNT
        )
    ]
)
```

