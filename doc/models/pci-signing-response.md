
# Pci Signing Response

*This model accepts additional fields of type Any.*

## Structure

`PciSigningResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pci_questionnaire_ids` | `List[str]` | Optional | The unique identifiers of the signed PCI documents. |
| `signed_by` | `str` | Optional | The [legal entity ID](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id) of the individual who signed the PCI questionnaire. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pci_signing_response import PciSigningResponse

pci_signing_response = PciSigningResponse(
    pci_questionnaire_ids=[
        'pciQuestionnaireIds5'
    ],
    signed_by='signedBy6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

