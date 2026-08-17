
# Get Pci Questionnaire Response

## Structure

`GetPciQuestionnaireResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | `str` | Optional | The generated questionnaire in a base64 encoded format. |
| `created_at` | `datetime` | Optional | The date the questionnaire was created, in ISO 8601 extended format. For example, 2022-12-18T10:15:30+01:00 |
| `id` | `str` | Optional | The unique identifier of the signed questionnaire. |
| `valid_until` | `datetime` | Optional | The expiration date of the questionnaire, in ISO 8601 extended format. For example, 2022-12-18T10:15:30+01:00 |

## Example

```python
import dateutil.parser

from adyen.models.get_pci_questionnaire_response import GetPciQuestionnaireResponse

get_pci_questionnaire_response = GetPciQuestionnaireResponse(
    content='content0',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id6',
    valid_until=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

