
# Response Additional Data Network Tokens

## Structure

`ResponseAdditionalDataNetworkTokens`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `network_token_available` | `str` | Optional | Indicates whether a network token is available for the specified card. |
| `network_token_bin` | `str` | Optional | The Bank Identification Number of a tokenized card, which is the first six digits of a card number. |
| `network_token_token_summary` | `str` | Optional | The last four digits of a network token. |

## Example

```python
from adyen.models.response_additional_data_network_tokens import ResponseAdditionalDataNetworkTokens

response_additional_data_network_tokens = ResponseAdditionalDataNetworkTokens(
    network_token_available='networkToken.available6',
    network_token_bin='networkToken.bin2',
    network_token_token_summary='networkToken.tokenSummary6'
)
```

