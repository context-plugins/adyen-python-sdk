
# Disable Permit Result

## Structure

`DisablePermitResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `psp_reference` | `str` | Optional | A unique reference associated with the request. This value is globally unique; quote it when communicating with us about this request. |
| `status` | `str` | Optional | Status of the disable request. |

## Example

```python
from adyen.models.disable_permit_result import DisablePermitResult

disable_permit_result = DisablePermitResult(
    psp_reference='pspReference2',
    status='status2'
)
```

