
# Association Initiate Request

## Structure

`AssociationInitiateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `List[str]` | Required | The list of unique identifiers of the resources that you are associating with the SCA device.<br><br>Maximum: 5 strings. |
| `mtype` | `str` | Required, Constant | The type of resource that you are associating with the SCA device.<br><br>Possible value: **PaymentInstrument**<br><br>**Value**: `"PaymentInstrument"` |

## Example

```python
from adyen.models.association_initiate_request import AssociationInitiateRequest

association_initiate_request = AssociationInitiateRequest(
    ids=[
        'ids3'
    ]
)
```

