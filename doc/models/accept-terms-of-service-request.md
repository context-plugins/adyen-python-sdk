
# Accept Terms of Service Request

*This model accepts additional fields of type Any.*

## Structure

`AcceptTermsOfServiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accepted_by` | `str` | Required | The legal entity ID of the user accepting the Terms of Service.<br><br>For organizations, this must be the individual legal entity ID of an authorized signatory for the organization.<br><br>For sole proprietorships, this must be the individual legal entity ID of the owner.<br><br>For individuals, this must be the individual legal entity id of either the individual, parent, or guardian. |
| `ip_address` | `str` | Optional | The IP address of the user accepting the Terms of Service. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.accept_terms_of_service_request import AcceptTermsOfServiceRequest

accept_terms_of_service_request = AcceptTermsOfServiceRequest(
    accepted_by='acceptedBy0',
    ip_address='ipAddress2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

