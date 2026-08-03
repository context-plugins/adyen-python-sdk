
# Create Test Card Ranges Result

*This model accepts additional fields of type Any.*

## Structure

`CreateTestCardRangesResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `range_creation_results` | [`List[TestCardRangeCreationResult]`](../../doc/models/test-card-range-creation-result.md) | Required | The results of the test card creation. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.create_test_card_ranges_result import CreateTestCardRangesResult
from adyen.models.creation_result_code import CreationResultCode
from adyen.models.test_card_range_creation_result import TestCardRangeCreationResult

create_test_card_ranges_result = CreateTestCardRangesResult(
    range_creation_results=[
        TestCardRangeCreationResult(
            card_number_range_end='cardNumberRangeEnd6',
            card_number_range_start='cardNumberRangeStart8',
            creation_result_code=CreationResultCode.ALREADY_EXISTS,
            message='message0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

