
# Bin Detail

*This model accepts additional fields of type Any.*

## Structure

`BinDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `issuer_country` | `str` | Optional | The country where the card was issued. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bin_detail import BinDetail

bin_detail = BinDetail(
    issuer_country='issuerCountry2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

