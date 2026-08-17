
# List Mandates Response

## Structure

`ListMandatesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `link` | [`Link2`](../../doc/models/link-2.md) | Required | Contains links to the next and previous page whenever applicable. |
| `mandates` | [`List[Mandate1]`](../../doc/models/mandate-1.md) | Required | Contains a list of the mandates. |

## Example

```python
import dateutil.parser

from adyen.models.link_2 import Link2
from adyen.models.links_element import LinksElement
from adyen.models.list_mandates_response import ListMandatesResponse
from adyen.models.mandate_1 import Mandate1
from adyen.models.mandate_account_identification_2 import MandateAccountIdentification2
from adyen.models.mandate_bank_account_2 import MandateBankAccount2
from adyen.models.mandate_party_identification_2 import MandatePartyIdentification2

list_mandates_response = ListMandatesResponse(
    link=Link2(
        first=LinksElement(
            href='href2'
        ),
        last=LinksElement(
            href='href2'
        ),
        next=LinksElement(
            href='href4'
        ),
        previous=LinksElement(
            href='href0'
        ),
        mself=LinksElement(
            href='href0'
        )
    ),
    mandates=[
        Mandate1(
            balance_account_id='balanceAccountId4',
            counterparty=MandateBankAccount2(
                account_holder=MandatePartyIdentification2(
                    full_name='fullName0'
                ),
                account_identification=MandateAccountIdentification2(
                    mtype='MandateAccountIdentification2'
                )
            ),
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id4',
            payment_instrument_id='paymentInstrumentId6'
        )
    ]
)
```

