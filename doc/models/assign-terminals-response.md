
# Assign Terminals Response

*This model accepts additional fields of type Any.*

## Structure

`AssignTerminalsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `results` | `Dict[str, str]` | Required | Array that returns a list of the terminals, and for each terminal the result of assigning it to an account or store.<br><br>The results can be:<br><br>- `Done`: The terminal has been assigned.<br><br>- `AssignmentScheduled`: The terminal will be assigned asynschronously.<br><br>- `RemoveConfigScheduled`: The terminal was previously assigned and boarded. Wait for the terminal to synchronize with the Adyen platform. For more information, refer to [Reassigning boarded terminals](https://docs.adyen.com/point-of-sale/managing-terminals/assign-terminals#reassign-boarded-terminals).<br><br>- `Error`: There was an error when assigning the terminal. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.assign_terminals_response import AssignTerminalsResponse

assign_terminals_response = AssignTerminalsResponse(
    results={
        'key0': 'results9'
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

