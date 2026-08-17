
# Svs Info

## Structure

`SvsInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_mid` | `str` | Required | The merchant ID (MID) that the acquirer recognizes you by. |
| `currency_code` | `str` | Required | The three-character ISO currency code, example **USD** |

## Example

```python
from adyen.models.svs_info import SvsInfo

svs_info = SvsInfo(
    authorisation_mid='authorisationMid6',
    currency_code='currencyCode0'
)
```

