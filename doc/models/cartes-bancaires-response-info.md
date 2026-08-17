
# Cartes Bancaires Response Info

## Structure

`CartesBancairesResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `siret` | `str` | Optional | Cartes Bancaires SIRET. Format: 14 digits. |
| `transaction_description` | [`TransactionDescriptionResponseInfo1`](../../doc/models/transaction-description-response-info-1.md) | Optional | Information regarding the transaction description. |

## Example

```python
from adyen.models.cartes_bancaires_response_info import CartesBancairesResponseInfo
from adyen.models.transaction_description_response_info_1 import TransactionDescriptionResponseInfo1
from adyen.models.type_8_enum import Type8Enum

cartes_bancaires_response_info = CartesBancairesResponseInfo(
    siret='siret2',
    transaction_description=TransactionDescriptionResponseInfo1(
        doing_business_as_name='doingBusinessAsName0',
        mtype=Type8Enum.FIXED
    )
)
```

