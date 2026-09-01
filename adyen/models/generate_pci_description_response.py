from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GeneratePciDescriptionResponse(SdkBaseModel):
    content: Optional[str] = UNSET
    """The generated questionnaires in a base64 encoded format."""

    language: Optional[str] = UNSET
    """The two-letter `ISO-639-1 <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`__ language code for the
    questionnaire. For example, **en**."""

    pci_template_references: Optional[list[str]] = Field(default=UNSET, alias="pciTemplateReferences")
    """The array of Adyen-generated unique identifiers for the questionnaires. If empty, the user is not required to
    sign questionnaires."""


class GeneratePciDescriptionResponseDict(TypedDict):
    content: NotRequired[str]
    language: NotRequired[str]
    pci_template_references: NotRequired[list[str]]
