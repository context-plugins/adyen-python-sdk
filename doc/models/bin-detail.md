
# Bin Detail

## Structure

`BinDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `issuer_country` | `str` | Optional | The country where the card was issued. |

## Example

```python
from adyen.models.bin_detail import BinDetail

bin_detail = BinDetail(
    issuer_country='issuerCountry2'
)
```

