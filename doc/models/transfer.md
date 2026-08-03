
# Transfer

*This model accepts additional fields of type Any.*

## Structure

`Transfer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`ResourceReference`](../../doc/models/resource-reference.md) | Optional | - |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Required | - |
| `balance_account` | [`ResourceReference`](../../doc/models/resource-reference.md) | Optional | - |
| `category` | [`Category3`](../../doc/models/category-3.md) | Required | - |
| `category_data` | [BankCategoryData](../../doc/models/bank-category-data.md) \| [InternalCategoryData](../../doc/models/internal-category-data.md) \| [IssuedCard](../../doc/models/issued-card.md) \| [PlatformPayment](../../doc/models/platform-payment.md) \| None | Optional | This is a container for one-of cases. |
| `counterparty` | [`CounterpartyV3`](../../doc/models/counterparty-v3.md) | Required | - |
| `created_at` | `datetime` | Optional | The date and time when the transfer was created, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |
| `creation_date` | `datetime` | Optional | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |
| `description` | `str` | Optional | Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.<br><br>Supported characters: **[a-z] [A-Z] [0-9] / - ?** **: ( ) . , ' + Space**<br><br>Supported characters for **regular** and **fast** transfers to a US counterparty: **[a-z] [A-Z] [0-9] & $ % # @** **~ = + - _ ' " ! ?** |
| `direct_debit_information` | [`DirectDebitInformation`](../../doc/models/direct-debit-information.md) | Optional | - |
| `direction` | [`Direction`](../../doc/models/direction.md) | Optional | - |
| `execution_date` | [`ExecutionDate`](../../doc/models/execution-date.md) | Optional | - |
| `id` | `str` | Optional | The ID of the resource. |
| `payment_instrument` | [`PaymentInstrument2`](../../doc/models/payment-instrument-2.md) | Optional | - |
| `reason` | [`Reason21`](../../doc/models/reason-21.md) | Optional | - |
| `reference` | `str` | Optional | Your reference for the transfer, used internally within your platform. If you don't provide this in the request, Adyen generates a unique reference.<br><br>**Constraints**: *Maximum Length*: `80` |
| `reference_for_beneficiary` | `str` | Optional | A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds.<br><br>Supported characters: **a-z**, **A-Z**, **0-9**.The maximum length depends on the `category`.<br><br>- **internal**: 80 characters<br><br>- **bank**: 35 characters when transferring to an IBAN, 15 characters for others. |
| `review` | [`TransferReview`](../../doc/models/transfer-review.md) | Optional | - |
| `status` | [`Status53`](../../doc/models/status-53.md) | Required | - |
| `mtype` | [`Type83`](../../doc/models/type-83.md) | Optional | - |
| `ultimate_party` | [`UltimatePartyIdentification`](../../doc/models/ultimate-party-identification.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.address_8 import Address8
from adyen.models.amount_5 import Amount5
from adyen.models.au_local_account_identification import AuLocalAccountIdentification
from adyen.models.bank_account_v_3 import BankAccountV3
from adyen.models.bank_category_data import BankCategoryData
from adyen.models.card_4 import Card4
from adyen.models.card_identification import CardIdentification
from adyen.models.category_3 import Category3
from adyen.models.counterparty_v_3 import CounterpartyV3
from adyen.models.merchant_data import MerchantData
from adyen.models.name_location import NameLocation
from adyen.models.party_identification import PartyIdentification
from adyen.models.priority import Priority
from adyen.models.resource_reference import ResourceReference
from adyen.models.status_53 import Status53
from adyen.models.transfer import Transfer
from adyen.models.type_312 import Type312
from adyen.models.type_413 import Type413

transfer = Transfer(
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    category=Category3.PLATFORMPAYMENT,
    counterparty=CounterpartyV3(
        balance_account_id='balanceAccountId0',
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
        transfer_instrument_id='transferInstrumentId4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    status=Status53.BOOKED,
    account_holder=ResourceReference(
        description='description0',
        id='id0',
        reference='reference4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    balance_account=ResourceReference(
        description='description2',
        id='id2',
        reference='reference2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    category_data=BankCategoryData(
        priority=Priority.INSTANT,
        mtype=Type312.BANK,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

