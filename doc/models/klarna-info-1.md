
# Klarna Info 1

Details to provide if `type` is **klarna** or its variant.

You can use the following payment method `type` values for Klarna:

* **klarna**: Klarna Pay Later
* **klarna_account**: Klarna Pay over time
* **klarna_paynow**: Klarna Pay now
* **klarna_b2b**: [Billie via Klarna](https://docs.adyen.com/payment-methods/klarna/billie)

## Structure

`KlarnaInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_capture` | `bool` | Optional | Indicates the status of [Automatic capture](https://docs.adyen.com/online-payments/capture#automatic-capture). Default value: **false**. |
| `dispute_email` | `str` | Required | The email address for disputes. |
| `region` | [`RegionEnum`](../../doc/models/region-enum.md) | Required | The region of operation. For example, **NA**, **EU**, **CH**, **AU**.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `support_email` | `str` | Required | The email address of merchant support. |

## Example

```python
from adyen.models.klarna_info_1 import KlarnaInfo1
from adyen.models.region_enum import RegionEnum

klarna_info_1 = KlarnaInfo1(
    dispute_email='disputeEmail0',
    region=RegionEnum.CH,
    support_email='supportEmail4',
    auto_capture=False
)
```

