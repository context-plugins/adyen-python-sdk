
# Loyalty Response

It conveys Information related to the Loyalty transaction processed by the POI System.
Content of the Loyalty Response message.

## Structure

`LoyaltyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response11`](../../doc/models/response-11.md) | Required | Result of a message request processing. |
| `sale_data` | [`SaleData1`](../../doc/models/sale-data-1.md) | Required | Data related to the Sale System. |
| `poi_data` | [`POIData1`](../../doc/models/poi-data-1.md) | Required | Data related to the POI System. |
| `loyalty_result` | [`List[LoyaltyResult]`](../../doc/models/loyalty-result.md) | Optional | Data related to the result of a processed loyalty transaction.<br>If loyalty account identified. |
| `payment_receipt` | [`List[PaymentReceipt]`](../../doc/models/payment-receipt.md) | Optional | - |

## Example

```python
import dateutil.parser

from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.document_qualifier_1_enum import DocumentQualifier1Enum
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.error_condition_1_enum import ErrorCondition1Enum
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.loyalty_account_1 import LoyaltyAccount1
from adyen.models.loyalty_account_id_2 import LoyaltyAccountID2
from adyen.models.loyalty_acquirer_data_1 import LoyaltyAcquirerData1
from adyen.models.loyalty_response import LoyaltyResponse
from adyen.models.loyalty_result import LoyaltyResult
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content_1 import OutputContent1
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_text import OutputText
from adyen.models.payment_receipt import PaymentReceipt
from adyen.models.poi_data_1 import POIData1
from adyen.models.predefined_content_1 import PredefinedContent1
from adyen.models.response_11 import Response11
from adyen.models.result_11_enum import Result11Enum
from adyen.models.sale_data_1 import SaleData1
from adyen.models.sale_terminal_data_1 import SaleTerminalData1
from adyen.models.transaction_id_type import TransactionIDType
from adyen.models.transaction_id_type_1 import TransactionIDType1
from adyen.models.transaction_id_type_2 import TransactionIDType2

loyalty_response = LoyaltyResponse(
    response=Response11(
        result=Result11Enum.PARTIAL,
        error_condition=ErrorCondition1Enum.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8'
    ),
    sale_data=SaleData1(
        sale_transaction_id=TransactionIDType1(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        operator_id='OperatorID8',
        operator_language='OperatorLanguage2',
        shift_number='ShiftNumber0',
        sale_reference_id='SaleReferenceID8',
        sale_terminal_data=SaleTerminalData1(
            totals_group_id='TotalsGroupID4'
        )
    ),
    poi_data=POIData1(
        poi_transaction_id=TransactionIDType2(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        poi_reconciliation_id=52
    ),
    loyalty_result=[
        LoyaltyResult(
            loyalty_account=LoyaltyAccount1(
                loyalty_account_id=LoyaltyAccountID2(
                    entry_mode=[
                        EntryModeEnum.FILE
                    ],
                    identification_type=IdentificationType11Enum.ISOTRACK2,
                    loyalty_id='LoyaltyID4',
                    identification_support=IdentificationSupport1Enum.HYBRIDCARD
                ),
                loyalty_brand='LoyaltyBrand0'
            ),
            current_balance=171.12,
            loyalty_acquirer_data=LoyaltyAcquirerData1(
                loyalty_acquirer_id='LoyaltyAcquirerID4',
                approval_code='ApprovalCode4',
                loyalty_transaction_id=TransactionIDType(
                    transaction_id='TransactionID6',
                    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                host_reconciliation_id='HostReconciliationID4'
            )
        ),
        LoyaltyResult(
            loyalty_account=LoyaltyAccount1(
                loyalty_account_id=LoyaltyAccountID2(
                    entry_mode=[
                        EntryModeEnum.FILE
                    ],
                    identification_type=IdentificationType11Enum.ISOTRACK2,
                    loyalty_id='LoyaltyID4',
                    identification_support=IdentificationSupport1Enum.HYBRIDCARD
                ),
                loyalty_brand='LoyaltyBrand0'
            ),
            current_balance=171.12,
            loyalty_acquirer_data=LoyaltyAcquirerData1(
                loyalty_acquirer_id='LoyaltyAcquirerID4',
                approval_code='ApprovalCode4',
                loyalty_transaction_id=TransactionIDType(
                    transaction_id='TransactionID6',
                    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                host_reconciliation_id='HostReconciliationID4'
            )
        ),
        LoyaltyResult(
            loyalty_account=LoyaltyAccount1(
                loyalty_account_id=LoyaltyAccountID2(
                    entry_mode=[
                        EntryModeEnum.FILE
                    ],
                    identification_type=IdentificationType11Enum.ISOTRACK2,
                    loyalty_id='LoyaltyID4',
                    identification_support=IdentificationSupport1Enum.HYBRIDCARD
                ),
                loyalty_brand='LoyaltyBrand0'
            ),
            current_balance=171.12,
            loyalty_acquirer_data=LoyaltyAcquirerData1(
                loyalty_acquirer_id='LoyaltyAcquirerID4',
                approval_code='ApprovalCode4',
                loyalty_transaction_id=TransactionIDType(
                    transaction_id='TransactionID6',
                    time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                ),
                host_reconciliation_id='HostReconciliationID4'
            )
        )
    ],
    payment_receipt=[
        PaymentReceipt(
            document_qualifier=DocumentQualifier1Enum.CUSTOMERRECEIPT,
            output_content=OutputContent1(
                output_format=OutputFormat1Enum.XHTML,
                predefined_content=PredefinedContent1(
                    reference_id='ReferenceID0',
                    language='Language2'
                ),
                output_text=[
                    OutputText(
                        text='Text6',
                        character_set=194,
                        start_row=74,
                        start_column=220,
                        character_width=CharacterWidth1Enum.SINGLEWIDTH,
                        character_height=CharacterHeight1Enum.SINGLEHEIGHT
                    )
                ],
                output_xhtml='OutputXHTML2',
                output_barcode=OutputBarcode1(
                    barcode_value='BarcodeValue2'
                )
            ),
            integrated_print_flag=False,
            required_signature_flag=False
        )
    ]
)
```

