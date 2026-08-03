
# Relayed Authorisation Data

*This model accepts additional fields of type Any.*

## Structure

`RelayedAuthorisationData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | `Dict[str, str]` | Optional | Contains key-value pairs of your references and descriptions, for example, `customId`:`your-own-custom-field-12345`. |
| `reference` | `str` | Optional | Your reference for the relayed authorisation data. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.relayed_authorisation_data import RelayedAuthorisationData

relayed_authorisation_data = RelayedAuthorisationData(
    metadata={
        'key0': 'metadata3',
        'key1': 'metadata2'
    },
    reference='reference2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

