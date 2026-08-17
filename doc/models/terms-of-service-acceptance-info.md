
# Terms of Service Acceptance Info

## Structure

`TermsOfServiceAcceptanceInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accepted_by` | `str` | Optional | The unique identifier of the user that accepted the Terms of Service. |
| `accepted_for` | `str` | Optional | The unique identifier of the legal entity for which the Terms of Service are accepted. |
| `created_at` | `datetime` | Optional | The date when the Terms of Service were accepted, in ISO 8601 extended format. For example, 2022-12-18T10:15:30+01:00. |
| `id` | `str` | Optional | An Adyen-generated reference for the accepted Terms of Service. |
| `mtype` | [`Type64Enum`](../../doc/models/type-64-enum.md) | Optional | The type of Terms of Service.<br><br>Possible values:<br><br>* **adyenForPlatformsManage**<br>* **adyenIssuing**<br>* **adyenForPlatformsAdvanced**<br>* **adyenCapital**<br>* **adyenAccount**<br>* **adyenCard**<br>* **adyenFranchisee**<br>* **adyenPccr**<br>* **adyenChargeCard**<br>* **kycOnInvite** |
| `valid_to` | `datetime` | Optional | The expiration date for the Terms of Service acceptance, in ISO 8601 extended format. For example, 2022-12-18T00:00:00+01:00. |

## Example

```python
import dateutil.parser

from adyen.models.terms_of_service_acceptance_info import TermsOfServiceAcceptanceInfo
from adyen.models.type_64_enum import Type64Enum

terms_of_service_acceptance_info = TermsOfServiceAcceptanceInfo(
    accepted_by='acceptedBy4',
    accepted_for='acceptedFor4',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id6',
    mtype=Type64Enum.ADYENFORPLATFORMSADVANCED
)
```

