
# Pci Signing Request

*This model accepts additional fields of type Any.*

## Structure

`PciSigningRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pci_template_references` | `List[str]` | Required | The array of Adyen-generated unique identifiers for the questionnaires. |
| `signed_by` | `str` | Required | The [legal entity ID](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id) of the individual who signs the PCI questionnaire. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pci_signing_request import PciSigningRequest

pci_signing_request = PciSigningRequest(
    pci_template_references=[
        'pciTemplateReferences0',
        'pciTemplateReferences1'
    ],
    signed_by='signedBy6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

