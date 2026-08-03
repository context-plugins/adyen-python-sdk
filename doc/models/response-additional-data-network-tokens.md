
# Response Additional Data Network Tokens

*This model accepts additional fields of type Any.*

## Structure

`ResponseAdditionalDataNetworkTokens`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `network_token_available` | `str` | Optional | Indicates whether a network token is available for the specified card. |
| `network_token_bin` | `str` | Optional | The Bank Identification Number of a tokenized card, which is the first six digits of a card number. |
| `network_token_token_summary` | `str` | Optional | The last four digits of a network token. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.response_additional_data_network_tokens import ResponseAdditionalDataNetworkTokens

response_additional_data_network_tokens = ResponseAdditionalDataNetworkTokens(
    network_token_available='networkToken.available6',
    network_token_bin='networkToken.bin2',
    network_token_token_summary='networkToken.tokenSummary6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

