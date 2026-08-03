
# Svs Info

*This model accepts additional fields of type Any.*

## Structure

`SvsInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorisation_mid` | `str` | Required | The merchant ID (MID) that the acquirer recognizes you by. |
| `currency_code` | `str` | Required | The three-character ISO currency code, example **USD** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.svs_info import SvsInfo

svs_info = SvsInfo(
    authorisation_mid='authorisationMid6',
    currency_code='currencyCode0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

