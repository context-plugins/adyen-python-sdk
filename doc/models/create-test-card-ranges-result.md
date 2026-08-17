
# Create Test Card Ranges Result

## Structure

`CreateTestCardRangesResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `range_creation_results` | [`List[TestCardRangeCreationResult]`](../../doc/models/test-card-range-creation-result.md) | Required | The results of the test card creation. |

## Example

```python
from adyen.models.create_test_card_ranges_result import CreateTestCardRangesResult
from adyen.models.creation_result_code_enum import CreationResultCodeEnum
from adyen.models.test_card_range_creation_result import TestCardRangeCreationResult

create_test_card_ranges_result = CreateTestCardRangesResult(
    range_creation_results=[
        TestCardRangeCreationResult(
            card_number_range_end='cardNumberRangeEnd6',
            card_number_range_start='cardNumberRangeStart8',
            creation_result_code=CreationResultCodeEnum.ALREADY_EXISTS,
            message='message0'
        )
    ]
)
```

