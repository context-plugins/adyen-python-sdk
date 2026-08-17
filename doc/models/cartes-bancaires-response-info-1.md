
# Cartes Bancaires Response Info 1

**cartesbancaire** details

## Structure

`CartesBancairesResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `siret` | `str` | Optional | Cartes Bancaires SIRET. Format: 14 digits. |
| `transaction_description` | [`TransactionDescriptionResponseInfo1`](../../doc/models/transaction-description-response-info-1.md) | Optional | Information regarding the transaction description. |

## Example

```python
from adyen.models.cartes_bancaires_response_info_1 import CartesBancairesResponseInfo1
from adyen.models.transaction_description_response_info_1 import TransactionDescriptionResponseInfo1
from adyen.models.type_8_enum import Type8Enum

cartes_bancaires_response_info_1 = CartesBancairesResponseInfo1(
    siret='siret6',
    transaction_description=TransactionDescriptionResponseInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

