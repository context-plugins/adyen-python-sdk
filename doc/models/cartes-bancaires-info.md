
# Cartes Bancaires Info

*This model accepts additional fields of type Any.*

## Structure

`CartesBancairesInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `siret` | `str` | Required | Cartes Bancaires SIRET. Format: 14 digits. |
| `transaction_description` | [`TransactionDescriptionInfo`](../../doc/models/transaction-description-info.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.cartes_bancaires_info import CartesBancairesInfo
from adyen.models.transaction_description_info import TransactionDescriptionInfo
from adyen.models.type_33 import Type33

cartes_bancaires_info = CartesBancairesInfo(
    siret='siret2',
    transaction_description=TransactionDescriptionInfo(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type33.FIXED,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

