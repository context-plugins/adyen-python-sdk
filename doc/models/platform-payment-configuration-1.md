
# Platform Payment Configuration 1

Contains key-value pairs to configure the sales day closing time and settlement delay for a balance account.

*This model accepts additional fields of type Any.*

## Structure

`PlatformPaymentConfiguration1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sales_day_closing_time` | `datetime` | Optional | Specifies at what time a sales day ends for this account.<br><br>Possible values: Time in **"HH:MM"** format. **HH** ranges from **00** to **07**. **MM** must be **00**.<br><br>Default value: **"00:00"**. |
| `settlement_delay_days` | `int` | Optional | Specifies after how many business days the funds in a settlement batch are made available in this balance account. Requires Custom Sales Day Payout to be enabled for your balance account. Contact your account manager or implementation manager to enable this.<br><br>Possible values: **1** to **20**, or **null**.<br><br>Default value: **null**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.platform_payment_configuration_1 import PlatformPaymentConfiguration1

platform_payment_configuration_1 = PlatformPaymentConfiguration1(
    sales_day_closing_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    settlement_delay_days=48,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

