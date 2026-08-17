
# Amex Response Info 1

**amex** details

## Structure

`AmexResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mid_number` | `str` | Optional | Merchant ID (MID) number. |
| `reuse_mid_number` | `bool` | Optional | Indicates whether the Amex Merchant ID is reused from a previously setup Amex payment method. |
| `service_level` | `str` | Optional | The service level (settlement type) of this payment method. Possible values:<br><br>* **noContract**: Adyen holds the contract with American Express.<br>* **gatewayContract**: American Express receives the settlement and handles disputes, then pays out to you or your sub-merchant directly.<br>* **paymentDesignatorContract**: Adyen receives the settlement, and handles disputes and payouts. |

## Example

```python
from adyen.models.amex_response_info_1 import AmexResponseInfo1

amex_response_info_1 = AmexResponseInfo1(
    mid_number='midNumber6',
    reuse_mid_number=False,
    service_level='serviceLevel0'
)
```

