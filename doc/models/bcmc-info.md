
# Bcmc Info

## Structure

`BcmcInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_bcmc_mobile` | `bool` | Optional | Indicates if [Bancontact mobile](https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile) is enabled. |

## Example

```python
from adyen.models.bcmc_info import BcmcInfo

bcmc_info = BcmcInfo(
    enable_bcmc_mobile=False
)
```

