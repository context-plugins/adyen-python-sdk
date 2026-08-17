
# Svs Response Info 2

**svs** details

## Structure

`SvsResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_mid` | `str` | Optional | The merchant ID (MID) that the acquirer recognizes you by. |
| `currency_code` | `str` | Optional | The three-character ISO currency code, example **USD** |

## Example

```python
from adyen.models.svs_response_info_2 import SvsResponseInfo2

svs_response_info_2 = SvsResponseInfo2(
    authorisation_mid='authorisationMid0',
    currency_code='currencyCode4'
)
```

