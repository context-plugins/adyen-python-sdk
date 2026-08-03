
# Third Party Token Redundancy Info 1

Configuration for creating redundant payment tokens with third-party token vaults using the Adyen Forward API. This feature requires Forward API webhook integration and pre-configured templates in your Adyen account. Contact your Adyen account manager for setup and availability.

*This model accepts additional fields of type Any.*

## Structure

`ThirdPartyTokenRedundancyInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_parameters` | `Dict[str, str]` | Optional | Request-specific parameter values to populate the template placeholders. Each key must match a placeholder defined in the template referenced by `requestTemplateCode`. |
| `request_template_code` | `str` | Required | Identifier for the third-party token request template configured in your Adyen account. This template defines the structure and endpoint for token requests. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.third_party_token_redundancy_info_1 import ThirdPartyTokenRedundancyInfo1

third_party_token_redundancy_info_1 = ThirdPartyTokenRedundancyInfo1(
    request_template_code='requestTemplateCode8',
    request_parameters={
        'key0': 'requestParameters7',
        'key1': 'requestParameters8',
        'key2': 'requestParameters9'
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

