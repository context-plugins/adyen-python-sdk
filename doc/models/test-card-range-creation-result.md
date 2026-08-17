
# Test Card Range Creation Result

## Structure

`TestCardRangeCreationResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_number_range_end` | `str` | Required | The last test card number in the generated test card range.<br><br>Example: 5432 1234 1234 4321 |
| `card_number_range_start` | `str` | Required | The first test card number in the generated test card range.<br><br>Example: 5432 1234 1234 1234 |
| `creation_result_code` | [`CreationResultCodeEnum`](../../doc/models/creation-result-code-enum.md) | Required | Notification message. It informs about the outcome of the operation. Possible values:<br><br>* CREATED<br>* ALREADY_EXISTS<br>* ERROR |
| `message` | `str` | Optional | An optional information message about the result. |

## Example

```python
from adyen.models.creation_result_code_enum import CreationResultCodeEnum
from adyen.models.test_card_range_creation_result import TestCardRangeCreationResult

test_card_range_creation_result = TestCardRangeCreationResult(
    card_number_range_end='cardNumberRangeEnd0',
    card_number_range_start='cardNumberRangeStart2',
    creation_result_code=CreationResultCodeEnum.ALREADY_EXISTS,
    message='message4'
)
```

