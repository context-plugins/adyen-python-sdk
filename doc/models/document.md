
# Document

## Structure

`Document`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attachment` | [`Attachment1`](../../doc/models/attachment-1.md) | Optional | Object that contains the document. |
| `attachments` | [`List[Attachment]`](../../doc/models/attachment.md) | Optional | Array that contains the document. The array supports multiple attachments for uploading different sides or pages of a document. |
| `creation_date` | `datetime` | Optional, Read-only | The creation date of the document. |
| `description` | `str` | Required | Your description for the document. |
| `expiry_date` | `str` | Optional | The expiry date of the document, in YYYY-MM-DD format. |
| `file_name` | `str` | Optional | The filename of the document. |
| `id` | `str` | Optional, Read-only | The unique identifier of the document. |
| `issuer_country` | `str` | Optional | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the document was issued. For example, **US**. |
| `issuer_state` | `str` | Optional | The state or province where the document was issued (AU only). |
| `modification_date` | `datetime` | Optional, Read-only | The modification date of the document. |
| `number` | `str` | Optional | The number in the document. |
| `owner` | [`OwnerEntity2`](../../doc/models/owner-entity-2.md) | Optional | Contains information about the resource that owns the document. |
| `mtype` | [`Type84Enum`](../../doc/models/type-84-enum.md) | Required | Type of document, used when providing an ID number or uploading a document. The possible values depend on the legal entity type.<br><br>* For **organization**, the `type` values can be **proofOfAddress**, **registrationDocument**, **vatDocument**, **proofOfOrganizationTaxInfo**, **proofOfOwnership**, **proofOfIndustry**, **proofOfSignatory**, **proofOfDirector**, or **proofOfFundingOrWealthSource**.<br><br>* For **individual**, the `type` values can be **identityCard**, **driversLicense**, **passport**, **liveSelfie**, **proofOfNationalIdNumber**, **proofOfResidency**, **proofOfIndustry**, **proofOfIndividualTaxId**, **proofOfFundingOrWealthSource** or **proofOfRelationship**.<br><br>* For **soleProprietorship**, the `type` values can be **constitutionalDocument**, **proofOfAddress**, or **proofOfIndustry**.<br><br>* For **trust**, the `type` value is **constitutionalDocument**.<br><br>* For **unincorporatedPartnership**, the `type` value is **constitutionalDocument**.<br><br>* Use **bankStatement** to upload documents for a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id). |

## Example

```python
from adyen.models.attachment import Attachment
from adyen.models.attachment_1 import Attachment1
from adyen.models.document import Document
from adyen.models.type_84_enum import Type84Enum

document = Document(
    description='description6',
    mtype=Type84Enum.PASSPORT,
    attachment=Attachment1(
        content='content2',
        content_type='contentType4',
        filename='filename0',
        page_name='pageName0',
        page_type='pageType6'
    ),
    attachments=[
        Attachment(
            content='content4',
            content_type='contentType6',
            filename='filename2',
            page_name='pageName2',
            page_type='pageType8'
        ),
        Attachment(
            content='content4',
            content_type='contentType6',
            filename='filename2',
            page_name='pageName2',
            page_type='pageType8'
        ),
        Attachment(
            content='content4',
            content_type='contentType6',
            filename='filename2',
            page_name='pageName2',
            page_type='pageType8'
        )
    ],
    expiry_date='expiryDate4',
    file_name='fileName0'
)
```

