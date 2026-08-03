
# Test Card Range Creation Result

*This model accepts additional fields of type Any.*

## Structure

`TestCardRangeCreationResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_number_range_end` | `str` | Required | The last test card number in the generated test card range.<br><br>Example: 5432 1234 1234 4321 |
| `card_number_range_start` | `str` | Required | The first test card number in the generated test card range.<br><br>Example: 5432 1234 1234 1234 |
| `creation_result_code` | [`CreationResultCode`](../../doc/models/creation-result-code.md) | Required | - |
| `message` | `str` | Optional | An optional information message about the result. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.creation_result_code import CreationResultCode
from adyen.models.test_card_range_creation_result import TestCardRangeCreationResult

test_card_range_creation_result = TestCardRangeCreationResult(
    card_number_range_end='cardNumberRangeEnd0',
    card_number_range_start='cardNumberRangeStart2',
    creation_result_code=CreationResultCode.ALREADY_EXISTS,
    message='message4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

