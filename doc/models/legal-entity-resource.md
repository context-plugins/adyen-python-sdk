
# Legal Entity Resource

## Structure

`LegalEntityResource`

## Inherits From

[`Resource`](../../doc/models/resource.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `legal_entity_id` | `str` | Required | The unique identifier of the resource connected to the component.<br>For [Onboarding components](https://docs.adyen.com/platforms/onboard-users/components), this is the legal entity that has a contractual relationship with your platform and owns the [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments). For sole proprietorships, this is the legal entity of the individual owner.<br><br>**Constraints**: *Minimum Length*: `1` |

## Example

```python
from adyen.models.resource import LegalEntityResource

legal_entity_resource = LegalEntityResource(
    legal_entity_id='legalEntityId4',
    mtype='legalEntity'
)
```

