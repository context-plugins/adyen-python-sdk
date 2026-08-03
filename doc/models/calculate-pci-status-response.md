
# Calculate Pci Status Response

*This model accepts additional fields of type Any.*

## Structure

`CalculatePciStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `signing_required` | `bool` | Optional | Indicates if the user is required to sign PCI questionnaires. If **false**, they do not need to sign any questionnaires. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.calculate_pci_status_response import CalculatePciStatusResponse

calculate_pci_status_response = CalculatePciStatusResponse(
    signing_required=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

