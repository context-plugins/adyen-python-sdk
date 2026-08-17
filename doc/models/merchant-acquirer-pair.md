
# Merchant Acquirer Pair

## Structure

`MerchantAcquirerPair`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acquirer_id` | `str` | Optional | The acquirer ID. |
| `merchant_id` | `str` | Optional | The merchant identification number (MID). |

## Example

```python
from adyen.models.merchant_acquirer_pair import MerchantAcquirerPair

merchant_acquirer_pair = MerchantAcquirerPair(
    acquirer_id='acquirerId4',
    merchant_id='merchantId8'
)
```

