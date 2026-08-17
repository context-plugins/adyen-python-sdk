
# Merchants Restriction 1

List of merchant ID and acquirer ID pairs, and the operation.

Supported operations: **anyMatch**, **noneMatch**.

## Structure

`MerchantsRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[MerchantAcquirerPair]`](../../doc/models/merchant-acquirer-pair.md) | Optional | List of merchant ID and acquirer ID pairs. |

## Example

```python
from adyen.models.merchant_acquirer_pair import MerchantAcquirerPair
from adyen.models.merchants_restriction_1 import MerchantsRestriction1

merchants_restriction_1 = MerchantsRestriction1(
    operation='operation8',
    value=[
        MerchantAcquirerPair(
            acquirer_id='acquirerId4',
            merchant_id='merchantId8'
        )
    ]
)
```

