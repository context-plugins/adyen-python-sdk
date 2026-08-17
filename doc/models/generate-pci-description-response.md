
# Generate Pci Description Response

## Structure

`GeneratePciDescriptionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | `str` | Optional | The generated questionnaires in a base64 encoded format. |
| `language` | `str` | Optional | The two-letter [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code for the questionnaire. For example, **en**. |
| `pci_template_references` | `List[str]` | Optional | The array of Adyen-generated unique identifiers for the questionnaires. If empty, the user is not required to sign questionnaires. |

## Example

```python
from adyen.models.generate_pci_description_response import GeneratePciDescriptionResponse

generate_pci_description_response = GeneratePciDescriptionResponse(
    content='content8',
    language='language6',
    pci_template_references=[
        'pciTemplateReferences4',
        'pciTemplateReferences5'
    ]
)
```

