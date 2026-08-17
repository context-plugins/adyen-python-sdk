
# Owner Entity 2

Contains information about the resource that owns the document.

## Structure

`OwnerEntity2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Unique identifier of the resource that owns the document. For `type` **legalEntity**, this value is the unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id). For `type` **bankAccount**, this value is the unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id). |
| `mtype` | `str` | Required | Type of resource that owns the document.<br><br>Possible values: **legalEntity**, **bankAccount**. |

## Example

```python
from adyen.models.owner_entity_2 import OwnerEntity2

owner_entity_2 = OwnerEntity2(
    id='id8',
    mtype='type2'
)
```

