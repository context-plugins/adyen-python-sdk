
# Merchants Restriction

## Structure

`MerchantsRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[MerchantAcquirerPair]`](../../doc/models/merchant-acquirer-pair.md) | Optional | List of merchant ID and acquirer ID pairs. |

## Example

```python
from adyen.models.merchant_acquirer_pair import MerchantAcquirerPair
from adyen.models.merchants_restriction import MerchantsRestriction

merchants_restriction = MerchantsRestriction(
    operation='operation4',
    value=[
        MerchantAcquirerPair(
            acquirer_id='acquirerId4',
            merchant_id='merchantId8'
        )
    ]
)
```

