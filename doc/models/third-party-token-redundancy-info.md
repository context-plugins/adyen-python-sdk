
# Third Party Token Redundancy Info

*This model accepts additional fields of type Any.*

## Structure

`ThirdPartyTokenRedundancyInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_parameters` | `Dict[str, str]` | Optional | Request-specific parameter values to populate the template placeholders. Each key must match a placeholder defined in the template referenced by `requestTemplateCode`. |
| `request_template_code` | `str` | Required | Identifier for the third-party token request template configured in your Adyen account. This template defines the structure and endpoint for token requests. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.third_party_token_redundancy_info import ThirdPartyTokenRedundancyInfo

third_party_token_redundancy_info = ThirdPartyTokenRedundancyInfo(
    request_template_code='requestTemplateCode6',
    request_parameters={
        'key0': 'requestParameters5'
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

