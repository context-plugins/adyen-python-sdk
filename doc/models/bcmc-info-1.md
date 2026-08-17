
# Bcmc Info 1

Details to provide if `type` is **bcmc** (Bancontact).

## Structure

`BcmcInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_bcmc_mobile` | `bool` | Optional | Indicates if [Bancontact mobile](https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile) is enabled. |

## Example

```python
from adyen.models.bcmc_info_1 import BcmcInfo1

bcmc_info_1 = BcmcInfo1(
    enable_bcmc_mobile=False
)
```

