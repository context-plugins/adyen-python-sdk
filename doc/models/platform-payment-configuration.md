
# Platform Payment Configuration

## Structure

`PlatformPaymentConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sales_day_closing_time` | `datetime` | Optional | Specifies at what time a sales day ends for this account.<br><br>Possible values: Time in **"HH:MM"** format. **HH** ranges from **00** to **07**. **MM** must be **00**.<br><br>Default value: **"00:00"**. |
| `settlement_delay_days` | `int` | Optional | Specifies after how many business days the funds in a settlement batch are made available in this balance account. Requires Custom Sales Day Payout to be enabled for your balance account. Contact your account manager or implementation manager to enable this.<br><br>Possible values: **1** to **20**, or **null**.<br><br>Default value: **null**. |

## Example

```python
import dateutil.parser

from adyen.models.platform_payment_configuration import PlatformPaymentConfiguration

platform_payment_configuration = PlatformPaymentConfiguration(
    sales_day_closing_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    settlement_delay_days=74
)
```

