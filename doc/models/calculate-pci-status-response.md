
# Calculate Pci Status Response

## Structure

`CalculatePciStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `signing_required` | `bool` | Optional | Indicates if the user is required to sign PCI questionnaires. If **false**, they do not need to sign any questionnaires. |

## Example

```python
from adyen.models.calculate_pci_status_response import CalculatePciStatusResponse

calculate_pci_status_response = CalculatePciStatusResponse(
    signing_required=False
)
```

