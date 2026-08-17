
# Payment Receipt

Customer or Merchant payment receipt.
If the payment receipts are printed by the Sale system and the POI or the Sale does not implement the Print exchange (Basic profile).

## Structure

`PaymentReceipt`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_qualifier` | [`DocumentQualifier1Enum`](../../doc/models/document-qualifier-1-enum.md) | Required | Qualification of the document to print to the Cashier or the Customer.<br>SaleReceipt or CashierReceipt.<br>Possible values:<br><br>* **CashierReceipt**<br>* **CustomerReceipt**<br>* **Document**<br>* **Journal**<br>* **SaleReceipt**<br>* **Voucher** |
| `integrated_print_flag` | `bool` | Optional | Type of the print integrated to other prints. |
| `required_signature_flag` | `bool` | Optional | Indicate that the cardholder payment receipt requires a physical signature by the Customer.<br><br>**Default**: `False` |
| `output_content` | [`OutputContent1`](../../doc/models/output-content-1.md) | Required | Content to display or print. |

## Example

```python
from adyen.models.character_height_1_enum import CharacterHeight1Enum
from adyen.models.character_width_1_enum import CharacterWidth1Enum
from adyen.models.document_qualifier_1_enum import DocumentQualifier1Enum
from adyen.models.output_barcode_1 import OutputBarcode1
from adyen.models.output_content_1 import OutputContent1
from adyen.models.output_format_1_enum import OutputFormat1Enum
from adyen.models.output_text import OutputText
from adyen.models.payment_receipt import PaymentReceipt
from adyen.models.predefined_content_1 import PredefinedContent1

payment_receipt = PaymentReceipt(
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
```

