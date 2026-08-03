
# Svs Response Info 2

**svs** details

*This model accepts additional fields of type Any.*

## Structure

`SvsResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_mid` | `str` | Optional | The merchant ID (MID) that the acquirer recognizes you by. |
| `currency_code` | `str` | Optional | The three-character ISO currency code, example **USD** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.svs_response_info_2 import SvsResponseInfo2

svs_response_info_2 = SvsResponseInfo2(
    authorisation_mid='authorisationMid0',
    currency_code='currencyCode4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

