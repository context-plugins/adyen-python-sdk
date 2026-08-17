
# Split Configuration Rule

## Structure

`SplitConfigurationRule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_region` | [`CardRegionEnum`](../../doc/models/card-region-enum.md) | Optional | The card region condition that determines whether the [split logic](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/splitConfigurations#request-rules-splitLogic) applies to the transaction.<br><br>> This condition is in pilot phase, and not yet available for all platforms.<br><br>Possible values:<br><br>* **domestic**: The card issuer and the store where the transaction is processed are registered in the same country.<br>* **international**: The card issuer and the store where the transaction is processed are registered in different countries or regions. Includes all **interRegional** and **intraRegional** transactions.<br>* **interRegional**: The card issuer and the store where the transaction is processed are registered in different regions.<br>* **intraRegional**: The card issuer and the store where the transaction is processed are registered in different countries, but in the same region.<br>* **intraEEA**: The card issuer and the store where the transaction is processed are registered in different countries, but in the European Economic Area (EEA).<br>* **ANY**: Applies to all transactions, regardless of the processing and issuing country/region. |
| `currency` | `str` | Required | The currency condition that defines whether the split logic applies.<br>Its value must be a three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217). |
| `funding_source` | [`FundingSource1Enum`](../../doc/models/funding-source-1-enum.md) | Required | The funding source of the payment method.<br><br>Possible values:<br><br>* **credit**<br>* **debit**<br>* **prepaid**<br>* **deferred_debit**<br>* **charged**<br>* **ANY** |
| `payment_method` | `str` | Required | The payment method condition that defines whether the split logic applies.<br><br>Possible values:<br><br>* [Payment method variant](https://docs.adyen.com/development-resources/paymentmethodvariant): Apply the split logic for a specific payment method.<br>* **ANY**: Apply the split logic for all available payment methods. |
| `rule_id` | `str` | Optional, Read-only | The unique identifier of the split configuration rule. |
| `shopper_interaction` | [`ShopperInteraction11Enum`](../../doc/models/shopper-interaction-11-enum.md) | Required | The sales channel condition that defines whether the split logic applies.<br><br>Possible values:<br><br>* **Ecommerce**: Online transactions where the cardholder is present.<br>* **ContAuth**: Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer).<br>* **Moto**: Mail-order and telephone-order transactions where the customer is in contact with the merchant via email or telephone.<br>* **POS**: Point-of-sale transactions where the customer is physically present to make a payment using a secure payment terminal.<br>* **ANY**: All sales channels. |
| `split_logic` | [`SplitConfigurationLogic2`](../../doc/models/split-configuration-logic-2.md) | Required | Contains the split logic that is applied if the rule conditions are met. |

## Example

```python
from adyen.models.acquiring_fees_enum import AcquiringFeesEnum
from adyen.models.additional_commission_1 import AdditionalCommission1
from adyen.models.adyen_commission_enum import AdyenCommissionEnum
from adyen.models.adyen_fees_enum import AdyenFeesEnum
from adyen.models.adyen_markup_enum import AdyenMarkupEnum
from adyen.models.card_region_enum import CardRegionEnum
from adyen.models.commission_1 import Commission1
from adyen.models.funding_source_1_enum import FundingSource1Enum
from adyen.models.shopper_interaction_11_enum import ShopperInteraction11Enum
from adyen.models.split_configuration_logic_2 import SplitConfigurationLogic2
from adyen.models.split_configuration_rule import SplitConfigurationRule

split_configuration_rule = SplitConfigurationRule(
    currency='currency0',
    funding_source=FundingSource1Enum.CHARGED,
    payment_method='paymentMethod8',
    shopper_interaction=ShopperInteraction11Enum.CONTAUTH,
    split_logic=SplitConfigurationLogic2(
        commission=Commission1(
            fixed_amount=112,
            variable_percentage=52
        ),
        acquiring_fees=AcquiringFeesEnum.DEDUCTFROMLIABLEACCOUNT,
        additional_commission=AdditionalCommission1(
            balance_account_id='balanceAccountId0',
            fixed_amount=100,
            variable_percentage=64
        ),
        adyen_commission=AdyenCommissionEnum.DEDUCTFROMLIABLEACCOUNT,
        adyen_fees=AdyenFeesEnum.DEDUCTFROMLIABLEACCOUNT,
        adyen_markup=AdyenMarkupEnum.DEDUCTFROMLIABLEACCOUNT
    ),
    card_region=CardRegionEnum.DOMESTIC
)
```

