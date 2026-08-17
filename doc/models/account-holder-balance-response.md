
# Account Holder Balance Response

## Structure

`AccountHolderBalanceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_per_account` | [`List[AccountDetailBalance]`](../../doc/models/account-detail-balance.md) | Optional | A list of each account and their balances. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |
| `total_balance` | [`DetailBalance1`](../../doc/models/detail-balance-1.md) | Optional | The total balance of the account holder. |

## Example

```python
from adyen.models.account_detail_balance import AccountDetailBalance
from adyen.models.account_holder_balance_response import AccountHolderBalanceResponse
from adyen.models.amount import Amount
from adyen.models.detail_balance_1 import DetailBalance1
from adyen.models.detail_balance_3 import DetailBalance3
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType

account_holder_balance_response = AccountHolderBalanceResponse(
    balance_per_account=[
        AccountDetailBalance(
            account_code='accountCode8',
            detail_balance=DetailBalance3(
                balance=[
                    Amount(
                        currency='currency4',
                        value=128
                    ),
                    Amount(
                        currency='currency4',
                        value=128
                    )
                ],
                on_hold_balance=[
                    Amount(
                        currency='currency8',
                        value=72
                    ),
                    Amount(
                        currency='currency8',
                        value=72
                    ),
                    Amount(
                        currency='currency8',
                        value=72
                    )
                ],
                pending_balance=[
                    Amount(
                        currency='currency2',
                        value=254
                    )
                ]
            )
        ),
        AccountDetailBalance(
            account_code='accountCode8',
            detail_balance=DetailBalance3(
                balance=[
                    Amount(
                        currency='currency4',
                        value=128
                    ),
                    Amount(
                        currency='currency4',
                        value=128
                    )
                ],
                on_hold_balance=[
                    Amount(
                        currency='currency8',
                        value=72
                    ),
                    Amount(
                        currency='currency8',
                        value=72
                    ),
                    Amount(
                        currency='currency8',
                        value=72
                    )
                ],
                pending_balance=[
                    Amount(
                        currency='currency2',
                        value=254
                    )
                ]
            )
        ),
        AccountDetailBalance(
            account_code='accountCode8',
            detail_balance=DetailBalance3(
                balance=[
                    Amount(
                        currency='currency4',
                        value=128
                    ),
                    Amount(
                        currency='currency4',
                        value=128
                    )
                ],
                on_hold_balance=[
                    Amount(
                        currency='currency8',
                        value=72
                    ),
                    Amount(
                        currency='currency8',
                        value=72
                    ),
                    Amount(
                        currency='currency8',
                        value=72
                    )
                ],
                pending_balance=[
                    Amount(
                        currency='currency2',
                        value=254
                    )
                ]
            )
        )
    ],
    invalid_fields=[
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType(
                field='field6',
                field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0'
            )
        ),
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType(
                field='field6',
                field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0'
            )
        ),
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType(
                field='field6',
                field_name=FieldNameEnum.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0'
            )
        )
    ],
    psp_reference='pspReference8',
    result_code='resultCode4',
    total_balance=DetailBalance1(
        balance=[
            Amount(
                currency='currency4',
                value=128
            )
        ],
        on_hold_balance=[
            Amount(
                currency='currency8',
                value=72
            ),
            Amount(
                currency='currency8',
                value=72
            ),
            Amount(
                currency='currency8',
                value=72
            )
        ],
        pending_balance=[
            Amount(
                currency='currency2',
                value=254
            ),
            Amount(
                currency='currency2',
                value=254
            )
        ]
    )
)
```

