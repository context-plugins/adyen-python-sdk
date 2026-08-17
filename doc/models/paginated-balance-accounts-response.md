
# Paginated Balance Accounts Response

## Structure

`PaginatedBalanceAccountsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_accounts` | [`List[BalanceAccountBase]`](../../doc/models/balance-account-base.md) | Required | List of balance accounts. |
| `has_next` | `bool` | Required | Indicates whether there are more items on the next page. |
| `has_previous` | `bool` | Required | Indicates whether there are more items on the previous page. |

## Example

```python
import dateutil.parser

from adyen.models.balance_account_base import BalanceAccountBase
from adyen.models.paginated_balance_accounts_response import PaginatedBalanceAccountsResponse
from adyen.models.platform_payment_configuration_1 import PlatformPaymentConfiguration1

paginated_balance_accounts_response = PaginatedBalanceAccountsResponse(
    balance_accounts=[
        BalanceAccountBase(
            account_holder_id='accountHolderId0',
            id='id8',
            default_currency_code='defaultCurrencyCode2',
            description='description8',
            metadata={
                'key0': 'metadata5',
                'key1': 'metadata6',
                'key2': 'metadata7'
            },
            platform_payment_configuration=PlatformPaymentConfiguration1(
                sales_day_closing_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                settlement_delay_days=80
            )
        )
    ],
    has_next=False,
    has_previous=False
)
```

