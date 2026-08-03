
# Transfer Info

*This model accepts additional fields of type Any.*

## Structure

`TransferInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount5`](../../doc/models/amount-5.md) | Required | - |
| `balance_account_id` | `str` | Optional | The unique identifier of the source [balance account](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id).<br><br>If you want to make a transfer using a **virtual** **bankAccount** assigned to the balance account, you must specify the [payment instrument ID](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments#responses-200-id) of the **virtual** **bankAccount**. If you only specify a balance account ID, Adyen uses the default **physical** **bankAccount** payment instrument assigned to the balance account. |
| `category` | [`Category3`](../../doc/models/category-3.md) | Required | - |
| `counterparty` | [`CounterpartyInfoV3`](../../doc/models/counterparty-info-v3.md) | Required | - |
| `description` | `str` | Optional | Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.<br><br>Supported characters: **[a-z] [A-Z] [0-9] / - ?** **: ( ) . , ' + Space**<br><br>Supported characters for **regular** and **fast** transfers to a US counterparty: **[a-z] [A-Z] [0-9] & $ % # @** **~ = + - _ ' " ! ?**<br><br>**Constraints**: *Maximum Length*: `140` |
| `execution_date` | [`ExecutionDate`](../../doc/models/execution-date.md) | Optional | - |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the source [payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments#responses-200-id).<br><br>If you want to make a transfer using a **virtual** **bankAccount**, you must specify the payment instrument ID of the **virtual** **bankAccount**. If you only specify a balance account ID, Adyen uses the default **physical** **bankAccount** payment instrument assigned to the balance account. |
| `priorities` | [`List[Priority]`](../../doc/models/priority.md) | Optional | The list of priorities for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. You can provide multiple priorities. Adyen will try to pay out using the priority you list first. If that's not possible, it moves on to the next option in the order of your provided priorities.<br><br>Possible values:<br><br>* **regular**: For normal, low-value transactions.<br><br>* **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.<br><br>* **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.<br><br>* **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).<br><br>* **crossBorder**: For high-value transfers to a recipient in a different country.<br><br>* **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).<br><br>Required for transfers with `category` **bank**. For more details, see [fallback priorities](https://docs.adyen.com/payouts/payout-service/payout-to-users/#fallback-priorities). |
| `priority` | [`Priority`](../../doc/models/priority.md) | Optional | - |
| `reference` | `str` | Optional | Your reference for the transfer, used internally within your platform. If you don't provide this in the request, Adyen generates a unique reference.<br><br>**Constraints**: *Maximum Length*: `80` |
| `reference_for_beneficiary` | `str` | Optional | A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both parties involved in the funds movement.<br><br>Supported characters: **a-z**, **A-Z**, **0-9**. The maximum length depends on the `category`.<br><br>- **internal**: 80 characters<br><br>- **bank**: 35 characters when transferring to an IBAN, 15 characters for others. |
| `review` | [`TransferRequestReview`](../../doc/models/transfer-request-review.md) | Optional | - |
| `mtype` | [`Type112`](../../doc/models/type-112.md) | Optional | - |
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
from adyen.models.card_4 import Card4
from adyen.models.card_identification import CardIdentification
from adyen.models.category_3 import Category3
from adyen.models.counterparty_info_v_3 import CounterpartyInfoV3
from adyen.models.execution_date import ExecutionDate
from adyen.models.party_identification import PartyIdentification
from adyen.models.priority import Priority
from adyen.models.transfer_info import TransferInfo
from adyen.models.type_413 import Type413

transfer_info = TransferInfo(
    amount=Amount5(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    category=Category3.BANK,
    counterparty=CounterpartyInfoV3(
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
        transfer_instrument_id='transferInstrumentId4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    balance_account_id='balanceAccountId0',
    description='description8',
    execution_date=ExecutionDate(
        date=dateutil.parser.parse('2016-03-13').date(),
        timezone='timezone0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    payment_instrument_id='paymentInstrumentId0',
    priorities=[
        Priority.INSTANT
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

