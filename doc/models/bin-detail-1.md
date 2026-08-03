
# Bin Detail 1

Bin Group Details

*This model accepts additional fields of type Any.*

## Structure

`BinDetail1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `issuer_country` | `str` | Optional | The country where the card was issued. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bin_detail_1 import BinDetail1

bin_detail_1 = BinDetail1(
    issuer_country='issuerCountry2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

