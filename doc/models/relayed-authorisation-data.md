
# Relayed Authorisation Data

## Structure

`RelayedAuthorisationData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | `Dict[str, str]` | Optional | Contains key-value pairs of your references and descriptions, for example, `customId`:`your-own-custom-field-12345`. |
| `reference` | `str` | Optional | Your reference for the relayed authorisation data. |

## Example

```python
from adyen.models.relayed_authorisation_data import RelayedAuthorisationData

relayed_authorisation_data = RelayedAuthorisationData(
    metadata={
        'key0': 'metadata3',
        'key1': 'metadata2'
    },
    reference='reference2'
)
```

