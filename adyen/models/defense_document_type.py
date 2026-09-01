from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DefenseDocumentType(SdkBaseModel):
    available: bool
    """When **true**, you've successfully uploaded this type of defense document. When **false**, you haven't uploaded
    this defense document type."""

    defense_document_type_code: str = Field(alias="defenseDocumentTypeCode")
    """The document type code of the defense document."""

    requirement_level: str = Field(alias="requirementLevel")
    """Indicates to what extent the defense document is required in the defense process.

    Possible values:

    * **Required**: You must supply the document.

     * **OneOrMore**: You must supply at least one of the documents with this label.

    * **Optional**: You can choose to supply the document.

    * **AlternativeRequired**: You must supply a generic defense document. To enable this functionality, contact our
        Support Team. When enabled, you can supply a generic defense document for all schemes."""


class DefenseDocumentTypeDict(TypedDict):
    available: bool
    defense_document_type_code: str
    requirement_level: str
