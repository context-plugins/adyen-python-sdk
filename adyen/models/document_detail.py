from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.document_type import DocumentTypeOrStr


class DocumentDetail(SdkBaseModel):
    account_holder_code: Optional[str] = Field(default=UNSET, alias="accountHolderCode")
    """The code of account holder, to which the document applies."""

    bank_account_uuid: Optional[str] = Field(default=UNSET, alias="bankAccountUUID")
    """The Adyen-generated
    https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-bankAccountDetails-bankAccountUUID
    to which the document must be linked. Refer to `Bank account check
    <https://docs.adyen.com/classic-platforms/verification-checks/bank-account-check#uploading-a-bank-statement>`__ for
    details on when a document should be submitted. >Required if the ``documentType`` is **BANK_STATEMENT**, where a
    document is being submitted in order to verify a bank account."""

    description: Optional[str] = UNSET
    """Description of the document."""

    document_type: DocumentTypeOrStr = Field(alias="documentType")
    """The type of the document. Refer to `Verification checks
    <https://docs.adyen.com/classic-platforms/verification-checks>`__ for details on when each document type should be
    submitted and for the accepted file formats.

    Permitted values:
    * **BANK_STATEMENT**: A file containing a bank statement or other document proving ownership of a specific bank
        account.
    * **COMPANY_REGISTRATION_SCREENING** (Supported from v5 and later): A file containing a company registration
        document.
    * **CONSTITUTIONAL_DOCUMENT**: A file containing information about the account holder's legal arrangement.
    * **PASSPORT**: A file containing the identity page(s) of a passport.
    * **ID_CARD_FRONT**: A file containing only the front of the ID card. In order for a document to be usable, both the
        **ID_CARD_FRONT** and **ID_CARD_BACK** must be submitted.
    * **ID_CARD_BACK**: A file containing only the back of the ID card. In order for a document to be usable, both the
        **ID_CARD_FRONT** and **ID_CARD_BACK** must be submitted.
    * **DRIVING_LICENCE_FRONT**: A file containing only the front of the driving licence. In order for a document to be
        usable, both the **DRIVING_LICENCE_FRONT** and **DRIVING_LICENCE_BACK** must be submitted.
    * **DRIVING_LICENCE_BACK**: A file containing only the back of the driving licence. In order for a document to be
        usable, both the **DRIVING_LICENCE_FRONT** and **DRIVING_LICENCE_FRONT** must be submitted."""

    filename: Optional[str] = UNSET
    """Filename of the document."""

    legal_arrangement_code: Optional[str] = Field(default=UNSET, alias="legalArrangementCode")
    """The Adyen-generated
    https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-legalArrangements-legalArrangementCode
    to which the document must be linked."""

    legal_arrangement_entity_code: Optional[str] = Field(default=UNSET, alias="legalArrangementEntityCode")
    """The Adyen-generated
    https://docs.adyen.com/api-explorer/#/Account/v6/post/createAccountHolder__resParam_accountHolderDetails-legalArrangements-legalArrangementEntities-legalArrangementEntityCode
    to which the document must be linked."""

    shareholder_code: Optional[str] = Field(default=UNSET, alias="shareholderCode")
    """The Adyen-generated
    https://docs.adyen.com/api-explorer/#/Account/latest/post/createAccountHolder__resParam_accountHolderDetails-businessDetails-shareholders-shareholderCode
    to which the document must be linked. Refer to `Verification checks
    <https://docs.adyen.com/classic-platforms/verification-checks>`__ for details on when a document should be
    submitted. >Required if the account holder has a ``legalEntity`` of type **Business** and the ``documentType`` is
    either **PASSPORT**, **ID_CARD_FRONT**, **ID_CARD_BACK**, **DRIVING_LICENCE_FRONT**, or **DRIVING_LICENCE_BACK**."""

    signatory_code: Optional[str] = Field(default=UNSET, alias="signatoryCode")
    """The Adyen-generated
    https://docs.adyen.com/api-explorer/#/Account/v6/post/createAccountHolder__resParam_accountHolderDetails-businessDetails-signatories-signatoryCode
    to which the document must be linked."""


class DocumentDetailDict(TypedDict):
    account_holder_code: NotRequired[str]
    bank_account_uuid: NotRequired[str]
    description: NotRequired[str]
    document_type: DocumentTypeOrStr
    filename: NotRequired[str]
    legal_arrangement_code: NotRequired[str]
    legal_arrangement_entity_code: NotRequired[str]
    shareholder_code: NotRequired[str]
    signatory_code: NotRequired[str]
