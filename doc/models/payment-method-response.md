
# Payment Method Response

*This model accepts additional fields of type Any.*

## Structure

`PaymentMethodResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`PaginationLinks`](../../doc/models/pagination-links.md) | Optional | - |
| `data` | [`List[ManagementPaymentMethod]`](../../doc/models/management-payment-method.md) | Optional | The list of supported payment methods and their details. |
| `items_total` | `int` | Required | Total number of items. |
| `pages_total` | `int` | Required | Total number of pages. |
| `types_with_errors` | [`List[TypesWithError]`](../../doc/models/types-with-error.md) | Optional | The payment method types that were not successfully requested and their corresponding errors. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.accel_response_info import AccelResponseInfo
from adyen.models.affirm_response_info import AffirmResponseInfo
from adyen.models.afterpay_touch_response_info import AfterpayTouchResponseInfo
from adyen.models.alipay_plus_response_info import AlipayPlusResponseInfo
from adyen.models.first import First
from adyen.models.last import Last
from adyen.models.management_payment_method import ManagementPaymentMethod
from adyen.models.mself import Self
from adyen.models.next import Next
from adyen.models.pagination_links import PaginationLinks
from adyen.models.payment_method_response import PaymentMethodResponse
from adyen.models.prev import Prev
from adyen.models.processing_type import ProcessingType
from adyen.models.transaction_description_info import TransactionDescriptionInfo
from adyen.models.type_33 import Type33
from adyen.models.types_with_error import TypesWithError

payment_method_response = PaymentMethodResponse(
    items_total=108,
    pages_total=70,
    links=PaginationLinks(
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
        mself=Self(
            href='href0',
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
        prev=Prev(
            href='href8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    data=[
        ManagementPaymentMethod(
            id='id0',
            accel=AccelResponseInfo(
                processing_type=ProcessingType.BILLPAY,
                transaction_description=TransactionDescriptionInfo(
                    doing_business_as_name='doingBusinessAsName0',
                    mtype=Type33.FIXED,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            affirm=AffirmResponseInfo(
                public_api_key='publicApiKey4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            afterpay_touch=AfterpayTouchResponseInfo(
                support_email='supportEmail8',
                support_url='supportUrl4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            alipay_plus=AlipayPlusResponseInfo(
                settlement_currency_code='settlementCurrencyCode0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            allowed=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ManagementPaymentMethod(
            id='id0',
            accel=AccelResponseInfo(
                processing_type=ProcessingType.BILLPAY,
                transaction_description=TransactionDescriptionInfo(
                    doing_business_as_name='doingBusinessAsName0',
                    mtype=Type33.FIXED,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            affirm=AffirmResponseInfo(
                public_api_key='publicApiKey4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            afterpay_touch=AfterpayTouchResponseInfo(
                support_email='supportEmail8',
                support_url='supportUrl4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            alipay_plus=AlipayPlusResponseInfo(
                settlement_currency_code='settlementCurrencyCode0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            allowed=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ManagementPaymentMethod(
            id='id0',
            accel=AccelResponseInfo(
                processing_type=ProcessingType.BILLPAY,
                transaction_description=TransactionDescriptionInfo(
                    doing_business_as_name='doingBusinessAsName0',
                    mtype=Type33.FIXED,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            affirm=AffirmResponseInfo(
                public_api_key='publicApiKey4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            afterpay_touch=AfterpayTouchResponseInfo(
                support_email='supportEmail8',
                support_url='supportUrl4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            alipay_plus=AlipayPlusResponseInfo(
                settlement_currency_code='settlementCurrencyCode0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            allowed=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    types_with_errors=[
        TypesWithError.ABRAPETITE_DEBIT
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

