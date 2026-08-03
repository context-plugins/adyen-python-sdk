
# Payment Methods Response

*This model accepts additional fields of type Any.*

## Structure

`PaymentMethodsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_methods` | [`List[PaymentMethod]`](../../doc/models/payment-method.md) | Optional | Detailed list of payment methods required to generate payment forms. |
| `stored_payment_methods` | [`List[StoredPaymentMethod3]`](../../doc/models/stored-payment-method-3.md) | Optional | List of all stored payment methods. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.app_identifier_info import AppIdentifierInfo
from adyen.models.funding_source import FundingSource
from adyen.models.payment_method import PaymentMethod
from adyen.models.payment_method_upi_apps import PaymentMethodUpiApps
from adyen.models.payment_methods_response import PaymentMethodsResponse
from adyen.models.stored_payment_method_3 import StoredPaymentMethod3

payment_methods_response = PaymentMethodsResponse(
    payment_methods=[
        PaymentMethod(
            apps=[
                PaymentMethodUpiApps(
                    id='id6',
                    name='name6',
                    app_identifier_info=AppIdentifierInfo(
                        android_package_id='androidPackageId8',
                        ios_scheme='iosScheme8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                PaymentMethodUpiApps(
                    id='id6',
                    name='name6',
                    app_identifier_info=AppIdentifierInfo(
                        android_package_id='androidPackageId8',
                        ios_scheme='iosScheme8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            brand='brand6',
            brands=[
                'brands3'
            ],
            configuration={
                'key0': 'configuration2',
                'key1': 'configuration1',
                'key2': 'configuration0'
            },
            funding_source=FundingSource.DEBIT,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        PaymentMethod(
            apps=[
                PaymentMethodUpiApps(
                    id='id6',
                    name='name6',
                    app_identifier_info=AppIdentifierInfo(
                        android_package_id='androidPackageId8',
                        ios_scheme='iosScheme8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                PaymentMethodUpiApps(
                    id='id6',
                    name='name6',
                    app_identifier_info=AppIdentifierInfo(
                        android_package_id='androidPackageId8',
                        ios_scheme='iosScheme8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            brand='brand6',
            brands=[
                'brands3'
            ],
            configuration={
                'key0': 'configuration2',
                'key1': 'configuration1',
                'key2': 'configuration0'
            },
            funding_source=FundingSource.DEBIT,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        PaymentMethod(
            apps=[
                PaymentMethodUpiApps(
                    id='id6',
                    name='name6',
                    app_identifier_info=AppIdentifierInfo(
                        android_package_id='androidPackageId8',
                        ios_scheme='iosScheme8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                PaymentMethodUpiApps(
                    id='id6',
                    name='name6',
                    app_identifier_info=AppIdentifierInfo(
                        android_package_id='androidPackageId8',
                        ios_scheme='iosScheme8',
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            brand='brand6',
            brands=[
                'brands3'
            ],
            configuration={
                'key0': 'configuration2',
                'key1': 'configuration1',
                'key2': 'configuration0'
            },
            funding_source=FundingSource.DEBIT,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    stored_payment_methods=[
        StoredPaymentMethod3(
            bank_account_number='bankAccountNumber2',
            bank_location_id='bankLocationId6',
            brand='brand6',
            cashtag='cashtag0',
            expiry_month='expiryMonth6',
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

