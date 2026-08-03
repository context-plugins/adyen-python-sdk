
# Relayed Authorisation Data 2

If you are using relayed authorisation, this object contains information from the relayed authorisation response from your server.

*This model accepts additional fields of type Any.*

## Structure

`RelayedAuthorisationData2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | `Dict[str, str]` | Optional | Contains key-value pairs of your references and descriptions, for example, `customId`:`your-own-custom-field-12345`. |
| `reference` | `str` | Optional | Your reference for the relayed authorisation data. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.relayed_authorisation_data_2 import RelayedAuthorisationData2

relayed_authorisation_data_2 = RelayedAuthorisationData2(
    metadata={
        'key0': 'metadata5',
        'key1': 'metadata4',
        'key2': 'metadata3'
    },
    reference='reference4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

