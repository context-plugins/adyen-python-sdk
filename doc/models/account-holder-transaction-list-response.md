
# Account Holder Transaction List Response

*This model accepts additional fields of type Any.*

## Structure

`AccountHolderTransactionListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_transaction_lists` | [`List[AccountTransactionList]`](../../doc/models/account-transaction-list.md) | Optional | A list of the transactions. |
| `invalid_fields` | [`List[ErrorFieldType]`](../../doc/models/error-field-type.md) | Optional | Contains field validation errors that would prevent requests from being processed. |
| `psp_reference` | `str` | Optional | The reference of a request. Can be used to uniquely identify the request. |
| `result_code` | `str` | Optional | The result code. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.account_holder_transaction_list_response import AccountHolderTransactionListResponse
from adyen.models.account_transaction_list import AccountTransactionList
from adyen.models.amount_16 import Amount16
from adyen.models.bank_account_detail_1 import BankAccountDetail1
from adyen.models.error_field_type import ErrorFieldType
from adyen.models.field_name import FieldName
from adyen.models.field_type_2 import FieldType2
from adyen.models.transaction import Transaction

account_holder_transaction_list_response = AccountHolderTransactionListResponse(
    account_transaction_lists=[
        AccountTransactionList(
            account_code='accountCode8',
            has_next_page=False,
            transactions=[
                Transaction(
                    amount=Amount16(
                        currency='currency2',
                        value=110,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    bank_account_detail=BankAccountDetail1(
                        account_number='accountNumber8',
                        account_type='accountType4',
                        bank_account_name='bankAccountName4',
                        bank_account_reference='bankAccountReference4',
                        bank_account_uuid='bankAccountUUID0',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    capture_merchant_reference='captureMerchantReference8',
                    capture_psp_reference='capturePspReference6',
                    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                Transaction(
                    amount=Amount16(
                        currency='currency2',
                        value=110,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    bank_account_detail=BankAccountDetail1(
                        account_number='accountNumber8',
                        account_type='accountType4',
                        bank_account_name='bankAccountName4',
                        bank_account_reference='bankAccountReference4',
                        bank_account_uuid='bankAccountUUID0',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    capture_merchant_reference='captureMerchantReference8',
                    capture_psp_reference='capturePspReference6',
                    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                Transaction(
                    amount=Amount16(
                        currency='currency2',
                        value=110,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    bank_account_detail=BankAccountDetail1(
                        account_number='accountNumber8',
                        account_type='accountType4',
                        bank_account_name='bankAccountName4',
                        bank_account_reference='bankAccountReference4',
                        bank_account_uuid='bankAccountUUID0',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    capture_merchant_reference='captureMerchantReference8',
                    capture_psp_reference='capturePspReference6',
                    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AccountTransactionList(
            account_code='accountCode8',
            has_next_page=False,
            transactions=[
                Transaction(
                    amount=Amount16(
                        currency='currency2',
                        value=110,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    bank_account_detail=BankAccountDetail1(
                        account_number='accountNumber8',
                        account_type='accountType4',
                        bank_account_name='bankAccountName4',
                        bank_account_reference='bankAccountReference4',
                        bank_account_uuid='bankAccountUUID0',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    capture_merchant_reference='captureMerchantReference8',
                    capture_psp_reference='capturePspReference6',
                    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                Transaction(
                    amount=Amount16(
                        currency='currency2',
                        value=110,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    bank_account_detail=BankAccountDetail1(
                        account_number='accountNumber8',
                        account_type='accountType4',
                        bank_account_name='bankAccountName4',
                        bank_account_reference='bankAccountReference4',
                        bank_account_uuid='bankAccountUUID0',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    capture_merchant_reference='captureMerchantReference8',
                    capture_psp_reference='capturePspReference6',
                    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                Transaction(
                    amount=Amount16(
                        currency='currency2',
                        value=110,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    bank_account_detail=BankAccountDetail1(
                        account_number='accountNumber8',
                        account_type='accountType4',
                        bank_account_name='bankAccountName4',
                        bank_account_reference='bankAccountReference4',
                        bank_account_uuid='bankAccountUUID0',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    capture_merchant_reference='captureMerchantReference8',
                    capture_psp_reference='capturePspReference6',
                    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    invalid_fields=[
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType2(
                field='field6',
                field_name=FieldName.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType2(
                field='field6',
                field_name=FieldName.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ErrorFieldType(
            error_code=78,
            error_description='errorDescription6',
            field_type=FieldType2(
                field='field6',
                field_name=FieldName.DRIVINGLICENCEFRONT,
                shareholder_code='shareholderCode0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    psp_reference='pspReference2',
    result_code='resultCode8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

