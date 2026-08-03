
# List Mandates Response

*This model accepts additional fields of type Any.*

## Structure

`ListMandatesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `link` | [`Link`](../../doc/models/link.md) | Required | - |
| `mandates` | [`List[Mandate]`](../../doc/models/mandate.md) | Required | Contains a list of the mandates. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.first import First
from adyen.models.last import Last
from adyen.models.link import Link
from adyen.models.list_mandates_response import ListMandatesResponse
from adyen.models.mandate import Mandate
from adyen.models.mandate_account_identification_2 import MandateAccountIdentification2
from adyen.models.mandate_bank_account import MandateBankAccount
from adyen.models.mandate_party_identification import MandatePartyIdentification
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.previous import Previous

list_mandates_response = ListMandatesResponse(
    link=Link(
        first=First(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        last=Last(
            href='href2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        next=Next(
            href='href4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        previous=Previous(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        mself=Self(
            href='href0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    mandates=[
        Mandate(
            balance_account_id='balanceAccountId4',
            counterparty=MandateBankAccount(
                account_holder=MandatePartyIdentification(
                    full_name='fullName0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                account_identification=MandateAccountIdentification2(
                    mtype='MandateAccountIdentification2',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id4',
            payment_instrument_id='paymentInstrumentId6',
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

