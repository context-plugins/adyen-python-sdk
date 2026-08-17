
# Account Holder Transaction List Response

## Structure

`AccountHolderTransactionListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_transaction_lists` | [`List[AccountTransactionList]`](../../doc/models/account-transaction-list.md) | Optional | A list of the transactions. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |

## Example

```python
import dateutil.parser

from adyen.models.account_holder_transaction_list_response import AccountHolderTransactionListResponse
from adyen.models.account_transaction_list import AccountTransactionList
from adyen.models.amount import Amount
from adyen.models.bank_account_detail import BankAccountDetail
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name_enum import FieldNameEnum
from adyen.models.field_type import FieldType
from adyen.models.transaction_1 import Transaction1

account_holder_transaction_list_response = AccountHolderTransactionListResponse(
    account_transaction_lists=[
        AccountTransactionList(
            account_code='accountCode8',
            has_next_page=False,
            transactions=[
                Transaction1(
                    amount=Amount(
                        currency='currency2',
                        value=110
                    ),
                    bank_account_detail=BankAccountDetail(
                        account_number='accountNumber8',
                        account_type='accountType4',
                        bank_account_name='bankAccountName4',
                        bank_account_reference='bankAccountReference4',
                        bank_account_uuid='bankAccountUUID0'
                    ),
                    capture_merchant_reference='captureMerchantReference8',
                    capture_psp_reference='capturePspReference6',
                    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                Transaction1(
                    amount=Amount(
                        currency='currency2',
                        value=110
                    ),
                    bank_account_detail=BankAccountDetail(
                        account_number='accountNumber8',
                        account_type='accountType4',
                        bank_account_name='bankAccountName4',
                        bank_account_reference='bankAccountReference4',
                        bank_account_uuid='bankAccountUUID0'
                    ),
                    capture_merchant_reference='captureMerchantReference8',
                    capture_psp_reference='capturePspReference6',
                    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                Transaction1(
                    amount=Amount(
                        currency='currency2',
                        value=110
                    ),
                    bank_account_detail=BankAccountDetail(
                        account_number='accountNumber8',
                        account_type='accountType4',
                        bank_account_name='bankAccountName4',
                        bank_account_reference='bankAccountReference4',
                        bank_account_uuid='bankAccountUUID0'
                    ),
                    capture_merchant_reference='captureMerchantReference8',
                    capture_psp_reference='capturePspReference6',
                    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                )
            ]
        ),
        AccountTransactionList(
            account_code='accountCode8',
            has_next_page=False,
            transactions=[
                Transaction1(
                    amount=Amount(
                        currency='currency2',
                        value=110
                    ),
                    bank_account_detail=BankAccountDetail(
                        account_number='accountNumber8',
                        account_type='accountType4',
                        bank_account_name='bankAccountName4',
                        bank_account_reference='bankAccountReference4',
                        bank_account_uuid='bankAccountUUID0'
                    ),
                    capture_merchant_reference='captureMerchantReference8',
                    capture_psp_reference='capturePspReference6',
                    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                Transaction1(
                    amount=Amount(
                        currency='currency2',
                        value=110
                    ),
                    bank_account_detail=BankAccountDetail(
                        account_number='accountNumber8',
                        account_type='accountType4',
                        bank_account_name='bankAccountName4',
                        bank_account_reference='bankAccountReference4',
                        bank_account_uuid='bankAccountUUID0'
                    ),
                    capture_merchant_reference='captureMerchantReference8',
                    capture_psp_reference='capturePspReference6',
                    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                Transaction1(
                    amount=Amount(
                        currency='currency2',
                        value=110
                    ),
                    bank_account_detail=BankAccountDetail(
                        account_number='accountNumber8',
                        account_type='accountType4',
                        bank_account_name='bankAccountName4',
                        bank_account_reference='bankAccountReference4',
                        bank_account_uuid='bankAccountUUID0'
                    ),
                    capture_merchant_reference='captureMerchantReference8',
                    capture_psp_reference='capturePspReference6',
                    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                )
            ]
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
    psp_reference='pspReference2',
    result_code='resultCode8'
)
```

