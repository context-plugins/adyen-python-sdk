from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class LegalEntityResource(SdkBaseModel):
    """All Of Resource, LegalEntityResource."""

    type_: Literal["legalEntity"] = Field(default="legalEntity", alias="type")

    legal_entity_id: str = Field(alias="legalEntityId")
    """The unique identifier of the resource connected to the component. For `Onboarding components
    <https://docs.adyen.com/platforms/onboard-users/components>`__, this is the legal entity that has a contractual
    relationship with your platform and owns the `transfer instrument
    <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments>`__. For sole proprietorships, this
    is the legal entity of the individual owner."""


class LegalEntityResourceDict(TypedDict):
    type_: NotRequired[Literal["legalEntity"]]
    legal_entity_id: str
