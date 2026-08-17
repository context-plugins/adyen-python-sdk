
# Amex Info

## Structure

`AmexInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mid_number` | `str` | Optional | Merchant ID (MID) number. Format: 10 numeric characters.<br>You must provide this field when you request `gatewayContract` or `paymentDesignatorContract` service levels.<br><br>**Constraints**: *Maximum Length*: `10` |
| `reuse_mid_number` | `bool` | Optional | Indicates whether the Amex Merchant ID is reused from a previously setup Amex payment method.<br>This is only applicable for `gatewayContract` and `paymentDesignatorContract` service levels.<br>The default value is **false**.<br><br>**Default**: `False` |
| `service_level` | [`ServiceLevelEnum`](../../doc/models/service-level-enum.md) | Required | Specifies the service level (settlement type) of this payment method. Possible values:<br><br>* **noContract**: Adyen holds the contract with American Express.<br>* **gatewayContract**: American Express receives the settlement and handles disputes, then pays out to you or your sub-merchant directly.<br>* **paymentDesignatorContract**: Adyen receives the settlement, and handles disputes and payouts. |

## Example

```python
from adyen.models.amex_info import AmexInfo
from adyen.models.service_level_enum import ServiceLevelEnum

amex_info = AmexInfo(
    service_level=ServiceLevelEnum.NOCONTRACT,
    mid_number='midNumber4',
    reuse_mid_number=False
)
```

