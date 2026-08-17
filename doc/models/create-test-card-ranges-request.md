
# Create Test Card Ranges Request

## Structure

`CreateTestCardRangesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Required | The code of the account, for which the test card ranges should be created. |
| `account_type_code` | `str` | Required | The type of the account, for which the test card ranges should be created.<br><br>Permitted values:<br><br>* Company<br>* MerchantAccount<br><br>> These values are case-sensitive. |
| `test_card_ranges` | [`List[TestCardRange]`](../../doc/models/test-card-range.md) | Required | A list of test card ranges to create. |

## Example

```python
from adyen.models.avs_address_1 import AvsAddress1
from adyen.models.create_test_card_ranges_request import CreateTestCardRangesRequest
from adyen.models.expiry_month_enum import ExpiryMonthEnum
from adyen.models.test_card_range import TestCardRange
from adyen.models.three_d_directory_server_response_enum import ThreeDDirectoryServerResponseEnum

create_test_card_ranges_request = CreateTestCardRangesRequest(
    account_code='accountCode8',
    account_type_code='accountTypeCode6',
    test_card_ranges=[
        TestCardRange(
            card_holder_name='cardHolderName0',
            expiry_month=ExpiryMonthEnum.DECEMBER,
            expiry_year=138,
            range_end='rangeEnd6',
            range_start='rangeStart4',
            address=AvsAddress1(
                street_address='streetAddress6',
                zip='zip0'
            ),
            cvc='cvc0',
            three_d_directory_server_response=ThreeDDirectoryServerResponseEnum.N,
            three_d_password='threeDPassword2',
            three_d_username='threeDUsername8'
        )
    ]
)
```

