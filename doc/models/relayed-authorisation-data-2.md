
# Relayed Authorisation Data 2

If you are using relayed authorisation, this object contains information from the relayed authorisation response from your server.

## Structure

`RelayedAuthorisationData2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | `Dict[str, str]` | Optional | Contains key-value pairs of your references and descriptions, for example, `customId`:`your-own-custom-field-12345`. |
| `reference` | `str` | Optional | Your reference for the relayed authorisation data. |

## Example

```python
from adyen.models.relayed_authorisation_data_2 import RelayedAuthorisationData2

relayed_authorisation_data_2 = RelayedAuthorisationData2(
    metadata={
        'key0': 'metadata5',
        'key1': 'metadata4',
        'key2': 'metadata3'
    },
    reference='reference4'
)
```

