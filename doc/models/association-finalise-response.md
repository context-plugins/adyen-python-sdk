
# Association Finalise Response

## Structure

`AssociationFinaliseResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Optional | The unique identifier of the SCA device you associated with a resource. |
| `ids` | `List[str]` | Optional | The list of unique identifiers of the resources that you associated with the SCA device. |
| `mtype` | `str` | Required, Constant | The type of resource that you associated with the SCA device.<br><br>**Value**: `"PAYMENT_INSTRUMENT"` |

## Example

```python
from adyen.models.association_finalise_response import AssociationFinaliseResponse

association_finalise_response = AssociationFinaliseResponse(
    device_id='deviceId2',
    ids=[
        'ids3'
    ]
)
```

