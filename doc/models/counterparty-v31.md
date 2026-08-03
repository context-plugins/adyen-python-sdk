
# Counterparty V31

The other party in the transfer.

*This model accepts additional fields of type Any.*

## Structure

`CounterpartyV31`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | The unique identifier of the counterparty [balance account](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id). |
| `bank_account` | [`BankAccountV3`](../../doc/models/bank-account-v3.md) | Optional | - |
| `card` | [`Card4`](../../doc/models/card-4.md) | Optional | - |
| `merchant` | [`MerchantData`](../../doc/models/merchant-data.md) | Optional | - |
| `transfer_instrument_id` | `str` | Optional | The unique identifier of the counterparty [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.address_8 import Address8
from adyen.models.au_local_account_identification import AuLocalAccountIdentification
from adyen.models.bank_account_v_3 import BankAccountV3
from adyen.models.card_4 import Card4
from adyen.models.card_identification import CardIdentification
from adyen.models.counterparty_v_31 import CounterpartyV31
from adyen.models.merchant_data import MerchantData
from adyen.models.name_location import NameLocation
from adyen.models.party_identification import PartyIdentification
from adyen.models.type_413 import Type413

counterparty_v_31 = CounterpartyV31(
    balance_account_id='balanceAccountId2',
    bank_account=BankAccountV3(
        account_holder=PartyIdentification(
            address=Address8(
                country='country0',
                city='city6',
                line_1='line18',
                line_2='line20',
                postal_code='postalCode8',
                state_or_province='stateOrProvince4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            date_of_birth=dateutil.parser.parse('2016-03-13').date(),
            email='email6',
            first_name='firstName4',
            full_name='fullName0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        account_identification=AuLocalAccountIdentification(
            account_number='accountNumber4',
            bsb_code='bsbCode8',
            mtype=Type413.AULOCAL,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        stored_payment_method_id='storedPaymentMethodId2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    card=Card4(
        card_holder=PartyIdentification(
            address=Address8(
                country='country0',
                city='city6',
                line_1='line18',
                line_2='line20',
                postal_code='postalCode8',
                state_or_province='stateOrProvince4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            date_of_birth=dateutil.parser.parse('2016-03-13').date(),
            email='email0',
            first_name='firstName8',
            full_name='fullName6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        card_identification=CardIdentification(
            expiry_month='expiryMonth2',
            expiry_year='expiryYear2',
            issue_number='issueNumber0',
            number='number6',
            start_month='startMonth8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant=MerchantData(
        acquirer_id='acquirerId6',
        mcc='mcc4',
        merchant_id='merchantId0',
        name_location=NameLocation(
            city='city6',
            country='country8',
            country_of_origin='countryOfOrigin0',
            name='name4',
            raw_data='rawData0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        postal_code='postalCode6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    transfer_instrument_id='transferInstrumentId6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

