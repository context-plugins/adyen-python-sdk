
# Transfer Route

*This model accepts additional fields of type Any.*

## Structure

`TransferRoute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category` | [`Category2`](../../doc/models/category-2.md) | Optional | - |
| `country` | `str` | Optional | The two-character ISO-3166-1 alpha-2 country code of the counterparty. For example, **US** or **NL**. |
| `currency` | `str` | Optional | The three-character ISO currency code of transfer. For example, **USD** or **EUR**. |
| `priority` | [`Priority2`](../../doc/models/priority-2.md) | Optional | - |
| `requirements` | List[[AdditionalBankIdentificationRequirement](../../doc/models/additional-bank-identification-requirement.md) \| [AddressRequirement](../../doc/models/address-requirement.md) \| [AmountMinMaxRequirement](../../doc/models/amount-min-max-requirement.md) \| [AmountNonZeroDecimalsRequirement](../../doc/models/amount-non-zero-decimals-requirement.md) \| [BankAccountIdentificationTypeRequirement](../../doc/models/bank-account-identification-type-requirement.md) \| [IbanAccountIdentificationRequirement](../../doc/models/iban-account-identification-requirement.md) \| [PaymentInstrumentRequirement](../../doc/models/payment-instrument-requirement.md) \| [USInstantPayoutAddressRequirement](../../doc/models/us-instant-payout-address-requirement.md) \| [USInternationalAchAddressRequirement](../../doc/models/us-international-ach-address-requirement.md) \| [USInternationalAchPriorityRequirement](../../doc/models/us-international-ach-priority-requirement.md)] \| None | Optional | This is List of a container for one-of cases. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_bank_identification_requirement import AdditionalBankIdentificationRequirement
from adyen.models.additional_bank_identification_type import AdditionalBankIdentificationType
from adyen.models.category_2 import Category2
from adyen.models.priority_2 import Priority2
from adyen.models.transfer_route import TransferRoute
from adyen.models.type_610 import Type610

transfer_route = TransferRoute(
    category=Category2.INTERNAL,
    country='country2',
    currency='currency2',
    priority=Priority2.INSTANT,
    requirements=[
        AdditionalBankIdentificationRequirement(
            mtype=Type610.ADDITIONALBANKIDENTIFICATIONREQUIREMENT,
            additional_bank_identification_type=AdditionalBankIdentificationType.GBSORTCODE,
            description='description8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

