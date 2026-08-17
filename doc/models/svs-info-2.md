
# Svs Info 2

Details to provide if `type` is **svs**.

## Structure

`SvsInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_mid` | `str` | Required | The merchant ID (MID) that the acquirer recognizes you by. |
| `currency_code` | `str` | Required | The three-character ISO currency code, example **USD** |

## Example

```python
from adyen.models.svs_info_2 import SvsInfo2

svs_info_2 = SvsInfo2(
    authorisation_mid='authorisationMid2',
    currency_code='currencyCode6'
)
```

