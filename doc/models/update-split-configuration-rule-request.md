
# Update Split Configuration Rule Request

*This model accepts additional fields of type Any.*

## Structure

`UpdateSplitConfigurationRuleRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The currency condition that defines whether the split logic applies.<br>Its value must be a three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217). |
| `funding_source` | `str` | Required | The funding source of the payment method.<br><br>Possible values:<br><br>* **credit**<br>* **debit**<br>* **prepaid**<br>* **deferred_debit**<br>* **charged**<br>* **ANY** |
| `payment_method` | `str` | Required | The payment method condition that defines whether the split logic applies.<br><br>Possible values:<br><br>* [Payment method variant](https://docs.adyen.com/development-resources/paymentmethodvariant): Apply the split logic for a specific payment method.<br>* **ANY**: Apply the split logic for all available payment methods. |
| `shopper_interaction` | `str` | Required | The sales channel condition that defines whether the split logic applies.<br><br>Possible values:<br><br>* **Ecommerce**: Online transactions where the cardholder is present.<br>* **ContAuth**: Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer).<br>* **Moto**: Mail-order and telephone-order transactions where the customer is in contact with the merchant via email or telephone.<br>* **POS**: Point-of-sale transactions where the customer is physically present to make a payment using a secure payment terminal.<br>* **ANY**: All sales channels. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.update_split_configuration_rule_request import UpdateSplitConfigurationRuleRequest

update_split_configuration_rule_request = UpdateSplitConfigurationRuleRequest(
    currency='currency0',
    funding_source='fundingSource6',
    payment_method='paymentMethod8',
    shopper_interaction='shopperInteraction6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

