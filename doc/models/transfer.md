
# Transfer

## Structure

`Transfer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder` | [`ResourceReference5`](../../doc/models/resource-reference-5.md) | Optional | The account holder associated with the balance account involved in the transfer. |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The amount of the transfer. |
| `balance_account` | [`ResourceReference1`](../../doc/models/resource-reference-1.md) | Optional | Contains information about the balance account involved in the transfer. |
| `category` | [`Category3Enum`](../../doc/models/category-3-enum.md) | Required | The category of the transfer.<br><br>Possible values:<br><br>- **bank**: A transfer involving a [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id) or a bank account.<br><br>- **card**: A transfer involving a third-party card.<br><br>- **internal**: A transfer between [balance accounts](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id) within your platform.<br><br>- **issuedCard**: A transfer initiated by an Adyen-issued card.<br><br>- **platformPayment**: Funds movements related to payments that are acquired for your users.<br><br>- **topUp**: An incoming transfer initiated by your user to top up their balance account. |
| `category_data` | [BankCategoryData](../../doc/models/bank-category-data.md) \| [InternalCategoryData](../../doc/models/internal-category-data.md) \| [IssuedCard](../../doc/models/issued-card.md) \| [PlatformPayment](../../doc/models/platform-payment.md) \| None | Optional | This is a container for one-of cases. |
| `counterparty` | [`CounterpartyV31`](../../doc/models/counterparty-v31.md) | Required | The other party in the transfer. |
| `created_at` | `datetime` | Optional | The date and time when the transfer was created, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |
| `creation_date` | `datetime` | Optional | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |
| `description` | `str` | Optional | Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.<br><br>Supported characters: **[a-z] [A-Z] [0-9] / - ?** **: ( ) . , ' + Space**<br><br>Supported characters for **regular** and **fast** transfers to a US counterparty: **[a-z] [A-Z] [0-9] & $ % # @** **~ = + - _ ' " ! ?** |
| `direct_debit_information` | [`DirectDebitInformation1`](../../doc/models/direct-debit-information-1.md) | Optional | The details of the direct debit. |
| `direction` | [`DirectionEnum`](../../doc/models/direction-enum.md) | Optional | The direction of the transfer.<br><br>Possible values: **incoming**, **outgoing**. |
| `execution_date` | [`ExecutionDate1`](../../doc/models/execution-date-1.md) | Optional | Contains information about the date when the transfer will be processed. The execution date must be within 30 days of the current date.<br><br>Until the execution date:<br><br>- The `status` of the transfer remains as **received**.<br>- The `reason` of the transfer remains as **pending**. |
| `id` | `str` | Optional | The ID of the resource. |
| `payment_instrument` | [`PaymentInstrument3`](../../doc/models/payment-instrument-3.md) | Optional | Contains information about the payment instrument used in the transfer. |
| `reason` | [`Reason2Enum`](../../doc/models/reason-2-enum.md) | Optional | Additional information about the status of the transfer. |
| `reference` | `str` | Optional | Your reference for the transfer, used internally within your platform. If you don't provide this in the request, Adyen generates a unique reference.<br><br>**Constraints**: *Maximum Length*: `80` |
| `reference_for_beneficiary` | `str` | Optional | A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds.<br><br>Supported characters: **a-z**, **A-Z**, **0-9**.The maximum length depends on the `category`.<br><br>- **internal**: 80 characters<br><br>- **bank**: 35 characters when transferring to an IBAN, 15 characters for others. |
| `review` | [`TransferReview1`](../../doc/models/transfer-review-1.md) | Optional | Contains status updates related to additional reviews. |
| `status` | [`Status51Enum`](../../doc/models/status-51-enum.md) | Required | The result of the transfer.<br><br>For example:<br><br>- **received**: an outgoing transfer request is created.<br>- **refused**: the transfer request is rejected by Adyen for one of the following reasons:<br>  - Transfer limit exceeded.<br>  - Transaction rule requirements violated.<br>- **authorised**: the transfer request is authorized and the funds are reserved.<br>- **booked**: the funds are deducted from your user's balance account.<br>- **failed**: the transfer is rejected by the counterparty's bank.<br>- **returned**: the transfer is returned by the counterparty's bank. |
| `mtype` | [`Type83Enum`](../../doc/models/type-83-enum.md) | Optional | The type of transfer or transaction. For example, **refund**, **payment**, **internalTransfer**, **bankTransfer**. |
| `ultimate_party` | [`UltimatePartyIdentification1`](../../doc/models/ultimate-party-identification-1.md) | Optional | The ultimate sender of the funds of the transfer (ultimate debtor). |

## Example

```python
import dateutil.parser

from adyen.models.address_12 import Address12
from adyen.models.amount_17 import Amount17
from adyen.models.au_local_account_identification import AULocalAccountIdentification
from adyen.models.bank_account_v_31 import BankAccountV31
from adyen.models.bank_category_data import BankCategoryData
from adyen.models.card_12 import Card12
from adyen.models.card_identification_3 import CardIdentification3
from adyen.models.category_3_enum import Category3Enum
from adyen.models.counterparty_v_31 import CounterpartyV31
from adyen.models.merchant_data_2 import MerchantData2
from adyen.models.name_location_2 import NameLocation2
from adyen.models.party_identification_1 import PartyIdentification1
from adyen.models.party_identification_3 import PartyIdentification3
from adyen.models.priority_1_enum import Priority1Enum
from adyen.models.resource_reference_1 import ResourceReference1
from adyen.models.resource_reference_5 import ResourceReference5
from adyen.models.status_51_enum import Status51Enum
from adyen.models.transfer import Transfer
from adyen.models.type_310_enum import Type310Enum

transfer = Transfer(
    amount=Amount17(
        currency='currency2',
        value=110
    ),
    category=Category3Enum.PLATFORMPAYMENT,
    counterparty=CounterpartyV31(
        balance_account_id='balanceAccountId0',
        bank_account=BankAccountV31(
            account_holder=PartyIdentification3(
                address=Address12(
                    country='country0',
                    city='city6',
                    line_1='line18',
                    line_2='line20',
                    postal_code='postalCode8',
                    state_or_province='stateOrProvince4'
                ),
                date_of_birth=dateutil.parser.parse('2016-03-13').date(),
                email='email6',
                first_name='firstName4',
                full_name='fullName0'
            ),
            account_identification=AULocalAccountIdentification(
                account_number='accountNumber4',
                bsb_code='bsbCode8'
            ),
            stored_payment_method_id='storedPaymentMethodId2'
        ),
        card=Card12(
            card_holder=PartyIdentification1(
                address=Address12(
                    country='country0',
                    city='city6',
                    line_1='line18',
                    line_2='line20',
                    postal_code='postalCode8',
                    state_or_province='stateOrProvince4'
                ),
                date_of_birth=dateutil.parser.parse('2016-03-13').date(),
                email='email0',
                first_name='firstName8',
                full_name='fullName6'
            ),
            card_identification=CardIdentification3(
                expiry_month='expiryMonth2',
                expiry_year='expiryYear2',
                issue_number='issueNumber0',
                number='number6',
                start_month='startMonth8'
            )
        ),
        merchant=MerchantData2(
            acquirer_id='acquirerId6',
            mcc='mcc4',
            merchant_id='merchantId0',
            name_location=NameLocation2(
                city='city6',
                country='country8',
                country_of_origin='countryOfOrigin0',
                name='name4',
                raw_data='rawData0'
            ),
            postal_code='postalCode6'
        ),
        transfer_instrument_id='transferInstrumentId4'
    ),
    status=Status51Enum.BOOKED,
    account_holder=ResourceReference5(
        description='description0',
        id='id0',
        reference='reference4'
    ),
    balance_account=ResourceReference1(
        description='description2',
        id='id2',
        reference='reference2'
    ),
    category_data=BankCategoryData(
        priority=Priority1Enum.INSTANT,
        mtype=Type310Enum.BANK
    ),
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

