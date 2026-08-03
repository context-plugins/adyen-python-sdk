
# Legal Entity Association

*This model accepts additional fields of type Any.*

## Structure

`LegalEntityAssociation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `associator_id` | `str` | Optional, Read-only | The unique identifier of another legal entity with which the `legalEntityId` is associated. When the `legalEntityId` is associated to legal entities other than the current one, the response returns all the associations. |
| `entity_type` | `str` | Optional, Read-only | The legal entity type of associated legal entity.<br><br>For example, **organization**, **soleProprietorship** or **individual**. |
| `job_title` | `str` | Optional | The individual's job title if the `type` is **uboThroughControl** or **signatory**. |
| `legal_entity_id` | `str` | Required | The unique identifier of the associated [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id). |
| `name` | `str` | Optional, Read-only | The name of the associated [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id).<br><br>- For **individual**, `name.firstName` and `name.lastName`.<br>- For **organization**, `legalName`.<br>- For **soleProprietorship**, `name`. |
| `nominee` | `bool` | Optional | Default value: **false**<br>Set to **true** if the entity association `type` **director**, **secondaryPartner** or **shareholder** is also a nominee. Only applicable to New Zealand. |
| `relationship` | `str` | Optional | The individual's relationship to a legal representative if the `type` is **legalRepresentative**. Possible values: **parent**, **guardian**. |
| `settlor_exemption_reason` | `List[str]` | Optional | Defines the KYC exemption reason for a settlor associated with a trust. Only applicable to trusts in Australia.<br><br>For example, **professionalServiceProvider**, **deceased**, or **contributionBelowThreshold**. |
| `mtype` | [`Type142`](../../doc/models/type-142.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.legal_entity_association import LegalEntityAssociation
from adyen.models.type_142 import Type142

legal_entity_association = LegalEntityAssociation(
    legal_entity_id='legalEntityId6',
    mtype=Type142.IMMEDIATEPARENTCOMPANY,
    associator_id='associatorId2',
    entity_type='entityType2',
    job_title='jobTitle4',
    name='name0',
    nominee=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

