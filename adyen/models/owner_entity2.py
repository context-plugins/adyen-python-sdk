from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OwnerEntity2(SdkBaseModel):
    """Contains information about the resource that owns the document."""

    id: str
    """Unique identifier of the resource that owns the document. For ``type`` **legalEntity**, this value is the unique
    identifier of the `legal entity
    <https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id>`__. For ``type``
    **bankAccount**, this value is the unique identifier of the `transfer instrument
    <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id>`__."""

    type_: str = Field(alias="type")
    """Type of resource that owns the document.

    Possible values: **legalEntity**, **bankAccount**."""


class OwnerEntity2Dict(TypedDict):
    id: str
    type_: str
