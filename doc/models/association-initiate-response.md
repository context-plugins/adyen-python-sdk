
# Association Initiate Response

## Structure

`AssociationInitiateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sdk_input` | `str` | Optional | A string that you must pass to the authentication SDK to continue with the association process.<br><br>**Constraints**: *Maximum Length*: `20000` |

## Example

```python
from adyen.models.association_initiate_response import AssociationInitiateResponse

association_initiate_response = AssociationInitiateResponse(
    sdk_input='sdkInput2'
)
```

