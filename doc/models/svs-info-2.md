
# Svs Info 2

Details to provide if `type` is **svs**.

*This model accepts additional fields of type Any.*

## Structure

`SvsInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_mid` | `str` | Required | The merchant ID (MID) that the acquirer recognizes you by. |
| `currency_code` | `str` | Required | The three-character ISO currency code, example **USD** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.svs_info_2 import SvsInfo2

svs_info_2 = SvsInfo2(
    authorisation_mid='authorisationMid2',
    currency_code='currencyCode6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

