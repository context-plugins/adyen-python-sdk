
# Create Permit Result

## Structure

`CreatePermitResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `permit_result_list` | [`List[PermitResult]`](../../doc/models/permit-result.md) | Optional | List of new permits. |
| `psp_reference` | `str` | Optional | A unique reference associated with the request. This value is globally unique; quote it when communicating with us about this request. |

## Example

```python
from adyen.models.create_permit_result import CreatePermitResult
from adyen.models.permit_result import PermitResult

create_permit_result = CreatePermitResult(
    permit_result_list=[
        PermitResult(
            result_key='resultKey4',
            token='token6'
        ),
        PermitResult(
            result_key='resultKey4',
            token='token6'
        )
    ],
    psp_reference='pspReference0'
)
```

