
# Third Party Token Redundancy Info

## Structure

`ThirdPartyTokenRedundancyInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_parameters` | `Dict[str, str]` | Optional | Request-specific parameter values to populate the template placeholders. Each key must match a placeholder defined in the template referenced by `requestTemplateCode`. |
| `request_template_code` | `str` | Required | Identifier for the third-party token request template configured in your Adyen account. This template defines the structure and endpoint for token requests. |

## Example

```python
from adyen.models.third_party_token_redundancy_info import ThirdPartyTokenRedundancyInfo

third_party_token_redundancy_info = ThirdPartyTokenRedundancyInfo(
    request_template_code='requestTemplateCode6',
    request_parameters={
        'key0': 'requestParameters5'
    }
)
```

