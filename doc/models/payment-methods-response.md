
# Payment Methods Response

## Structure

`PaymentMethodsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_methods` | [`List[PaymentMethod]`](../../doc/models/payment-method.md) | Optional | Detailed list of payment methods required to generate payment forms. |
| `stored_payment_methods` | [`List[StoredPaymentMethod3]`](../../doc/models/stored-payment-method-3.md) | Optional | List of all stored payment methods. |

## Example

```python
from adyen.models.app_identifier_info_1 import AppIdentifierInfo1
from adyen.models.funding_source_9_enum import FundingSource9Enum
from adyen.models.payment_method import PaymentMethod
from adyen.models.payment_method_upi_apps import PaymentMethodUPIApps
from adyen.models.payment_methods_response import PaymentMethodsResponse
from adyen.models.stored_payment_method_3 import StoredPaymentMethod3

payment_methods_response = PaymentMethodsResponse(
    payment_methods=[
        PaymentMethod(
            apps=[
                PaymentMethodUPIApps(
                    id='id6',
                    name='name6',
                    app_identifier_info=AppIdentifierInfo1(
                        android_package_id='androidPackageId8',
                        ios_scheme='iosScheme8'
                    )
                ),
                PaymentMethodUPIApps(
                    id='id6',
                    name='name6',
                    app_identifier_info=AppIdentifierInfo1(
                        android_package_id='androidPackageId8',
                        ios_scheme='iosScheme8'
                    )
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
            funding_source=FundingSource9Enum.DEBIT
        ),
        PaymentMethod(
            apps=[
                PaymentMethodUPIApps(
                    id='id6',
                    name='name6',
                    app_identifier_info=AppIdentifierInfo1(
                        android_package_id='androidPackageId8',
                        ios_scheme='iosScheme8'
                    )
                ),
                PaymentMethodUPIApps(
                    id='id6',
                    name='name6',
                    app_identifier_info=AppIdentifierInfo1(
                        android_package_id='androidPackageId8',
                        ios_scheme='iosScheme8'
                    )
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
            funding_source=FundingSource9Enum.DEBIT
        ),
        PaymentMethod(
            apps=[
                PaymentMethodUPIApps(
                    id='id6',
                    name='name6',
                    app_identifier_info=AppIdentifierInfo1(
                        android_package_id='androidPackageId8',
                        ios_scheme='iosScheme8'
                    )
                ),
                PaymentMethodUPIApps(
                    id='id6',
                    name='name6',
                    app_identifier_info=AppIdentifierInfo1(
                        android_package_id='androidPackageId8',
                        ios_scheme='iosScheme8'
                    )
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
            funding_source=FundingSource9Enum.DEBIT
        )
    ],
    stored_payment_methods=[
        StoredPaymentMethod3(
            bank_account_number='bankAccountNumber2',
            bank_location_id='bankLocationId6',
            brand='brand6',
            cashtag='cashtag0',
            expiry_month='expiryMonth6'
        )
    ]
)
```

