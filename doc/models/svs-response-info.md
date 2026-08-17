
# Svs Response Info

## Structure

`SvsResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_mid` | `str` | Optional | The merchant ID (MID) that the acquirer recognizes you by. |
| `currency_code` | `str` | Optional | The three-character ISO currency code, example **USD** |

## Example

```python
from adyen.models.svs_response_info import SvsResponseInfo

svs_response_info = SvsResponseInfo(
    authorisation_mid='authorisationMid6',
    currency_code='currencyCode0'
)
```

