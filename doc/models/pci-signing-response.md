
# Pci Signing Response

## Structure

`PciSigningResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pci_questionnaire_ids` | `List[str]` | Optional | The unique identifiers of the signed PCI documents. |
| `signed_by` | `str` | Optional | The [legal entity ID](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id) of the individual who signed the PCI questionnaire. |

## Example

```python
from adyen.models.pci_signing_response import PciSigningResponse

pci_signing_response = PciSigningResponse(
    pci_questionnaire_ids=[
        'pciQuestionnaireIds5'
    ],
    signed_by='signedBy6'
)
```

