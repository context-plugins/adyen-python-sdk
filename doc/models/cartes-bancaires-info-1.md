
# Cartes Bancaires Info 1

Details to provide if `type` is **cartebancaire**.

## Structure

`CartesBancairesInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `siret` | `str` | Required | Cartes Bancaires SIRET. Format: 14 digits. |
| `transaction_description` | [`TransactionDescriptionInfo1`](../../doc/models/transaction-description-info-1.md) | Optional | Information regarding the transaction description.<br><br>> You cannot configure the transaction description in the test environment. |

## Example

```python
from adyen.models.cartes_bancaires_info_1 import CartesBancairesInfo1
from adyen.models.transaction_description_info_1 import TransactionDescriptionInfo1
from adyen.models.type_8_enum import Type8Enum

cartes_bancaires_info_1 = CartesBancairesInfo1(
    siret='siret4',
    transaction_description=TransactionDescriptionInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

