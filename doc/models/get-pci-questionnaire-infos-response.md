
# Get Pci Questionnaire Infos Response

## Structure

`GetPciQuestionnaireInfosResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[PciDocumentInfo]`](../../doc/models/pci-document-info.md) | Optional | Information about the signed PCI questionnaires. |

## Example

```python
import dateutil.parser

from adyen.models.get_pci_questionnaire_infos_response import GetPciQuestionnaireInfosResponse
from adyen.models.pci_document_info import PciDocumentInfo

get_pci_questionnaire_infos_response = GetPciQuestionnaireInfosResponse(
    data=[
        PciDocumentInfo(
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id0',
            valid_until=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ]
)
```

