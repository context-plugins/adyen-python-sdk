
# Payment Method Response

## Structure

`PaymentMethodResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks1`](../../doc/models/pagination-links-1.md) | Optional | Pagination references. |
| `data` | [`List[ManagementPaymentMethod]`](../../doc/models/management-payment-method.md) | Optional | The list of supported payment methods and their details. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |
| `types_with_errors` | [`List[TypesWithErrorEnum]`](../../doc/models/types-with-error-enum.md) | Optional | The payment method types that were not successfully requested and their corresponding errors. |

## Example

```python
from adyen.models.accel_response_info_1 import AccelResponseInfo1
from adyen.models.affirm_response_info_1 import AffirmResponseInfo1
from adyen.models.afterpay_touch_response_info_1 import AfterpayTouchResponseInfo1
from adyen.models.alipay_plus_response_info_1 import AlipayPlusResponseInfo1
from adyen.models.links_element_10 import LinksElement10
from adyen.models.links_element_11 import LinksElement11
from adyen.models.links_element_12 import LinksElement12
from adyen.models.links_element_13 import LinksElement13
from adyen.models.links_element_9 import LinksElement9
from adyen.models.management_payment_method import ManagementPaymentMethod
from adyen.models.pagination_links_1 import PaginationLinks1
from adyen.models.payment_method_response import PaymentMethodResponse
from adyen.models.processing_type_enum import ProcessingTypeEnum
from adyen.models.transaction_description_response_info_1 import TransactionDescriptionResponseInfo1
from adyen.models.type_8_enum import Type8Enum
from adyen.models.types_with_error_enum import TypesWithErrorEnum

payment_method_response = PaymentMethodResponse(
    items_total=108,
    pages_total=70,
    links=PaginationLinks1(
        first=LinksElement9(
            href='href2'
        ),
        last=LinksElement10(
            href='href2'
        ),
        mself=LinksElement13(
            href='href0'
        ),
        next=LinksElement11(
            href='href4'
        ),
        prev=LinksElement12(
            href='href8'
        )
    ),
    data=[
        ManagementPaymentMethod(
            id='id0',
            accel=AccelResponseInfo1(
                processing_type=ProcessingTypeEnum.BILLPAY,
                transaction_description=TransactionDescriptionResponseInfo1(
                    doing_business_as_name='doingBusinessAsName0',
                    mtype=Type8Enum.FIXED
                )
            ),
            affirm=AffirmResponseInfo1(
                public_api_key='publicApiKey4'
            ),
            afterpay_touch=AfterpayTouchResponseInfo1(
                support_email='supportEmail8',
                support_url='supportUrl4'
            ),
            alipay_plus=AlipayPlusResponseInfo1(
                settlement_currency_code='settlementCurrencyCode0'
            ),
            allowed=False
        ),
        ManagementPaymentMethod(
            id='id0',
            accel=AccelResponseInfo1(
                processing_type=ProcessingTypeEnum.BILLPAY,
                transaction_description=TransactionDescriptionResponseInfo1(
                    doing_business_as_name='doingBusinessAsName0',
                    mtype=Type8Enum.FIXED
                )
            ),
            affirm=AffirmResponseInfo1(
                public_api_key='publicApiKey4'
            ),
            afterpay_touch=AfterpayTouchResponseInfo1(
                support_email='supportEmail8',
                support_url='supportUrl4'
            ),
            alipay_plus=AlipayPlusResponseInfo1(
                settlement_currency_code='settlementCurrencyCode0'
            ),
            allowed=False
        ),
        ManagementPaymentMethod(
            id='id0',
            accel=AccelResponseInfo1(
                processing_type=ProcessingTypeEnum.BILLPAY,
                transaction_description=TransactionDescriptionResponseInfo1(
                    doing_business_as_name='doingBusinessAsName0',
                    mtype=Type8Enum.FIXED
                )
            ),
            affirm=AffirmResponseInfo1(
                public_api_key='publicApiKey4'
            ),
            afterpay_touch=AfterpayTouchResponseInfo1(
                support_email='supportEmail8',
                support_url='supportUrl4'
            ),
            alipay_plus=AlipayPlusResponseInfo1(
                settlement_currency_code='settlementCurrencyCode0'
            ),
            allowed=False
        )
    ],
    types_with_errors=[
        TypesWithErrorEnum.ABRAPETITE_DEBIT
    ]
)
```

