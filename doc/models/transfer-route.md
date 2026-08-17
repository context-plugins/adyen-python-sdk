
# Transfer Route

## Structure

`TransferRoute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category` | [`Category2Enum`](../../doc/models/category-2-enum.md) | Optional | The type of transfer.<br><br>Possible values:<br><br>- **bank**: Transfer to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id) or a bank account. |
| `country` | `str` | Optional | The two-character ISO-3166-1 alpha-2 country code of the counterparty. For example, **US** or **NL**. |
| `currency` | `str` | Optional | The three-character ISO currency code of transfer. For example, **USD** or **EUR**. |
| `priority` | [`Priority2Enum`](../../doc/models/priority-2-enum.md) | Optional | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Possible values:<br><br>* **regular**: For normal, low-value transactions.<br><br>* **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.<br><br>* **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.<br><br>* **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).<br><br>* **crossBorder**: For high-value transfers to a recipient in a different country.<br><br>* **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN). |
| `requirements` | List[[AdditionalBankIdentificationRequirement](../../doc/models/additional-bank-identification-requirement.md) \| [AddressRequirement](../../doc/models/address-requirement.md) \| [AmountMinMaxRequirement](../../doc/models/amount-min-max-requirement.md) \| [AmountNonZeroDecimalsRequirement](../../doc/models/amount-non-zero-decimals-requirement.md) \| [BankAccountIdentificationTypeRequirement](../../doc/models/bank-account-identification-type-requirement.md) \| [IbanAccountIdentificationRequirement](../../doc/models/iban-account-identification-requirement.md) \| [PaymentInstrumentRequirement](../../doc/models/payment-instrument-requirement.md) \| [USInstantPayoutAddressRequirement](../../doc/models/us-instant-payout-address-requirement.md) \| [USInternationalAchAddressRequirement](../../doc/models/us-international-ach-address-requirement.md) \| [USInternationalAchPriorityRequirement](../../doc/models/us-international-ach-priority-requirement.md)] \| None | Optional | This is List of a container for one-of cases. |

## Example

```python
from adyen.models.additional_bank_identification_requirement import AdditionalBankIdentificationRequirement
from adyen.models.additional_bank_identification_type_enum import AdditionalBankIdentificationTypeEnum
from adyen.models.category_2_enum import Category2Enum
from adyen.models.priority_2_enum import Priority2Enum
from adyen.models.transfer_route import TransferRoute

transfer_route = TransferRoute(
    category=Category2Enum.INTERNAL,
    country='country2',
    currency='currency2',
    priority=Priority2Enum.INSTANT,
    requirements=[
        AdditionalBankIdentificationRequirement(
            additional_bank_identification_type=AdditionalBankIdentificationTypeEnum.GBSORTCODE,
            description='description8'
        )
    ]
)
```

