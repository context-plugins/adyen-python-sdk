from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..account_holder_resource import AccountHolderResource, AccountHolderResourceDict
from ..legal_entity_resource import LegalEntityResource, LegalEntityResourceDict
from ..payment_instrument_resource import PaymentInstrumentResource, PaymentInstrumentResourceDict

Resource: TypeAlias = Annotated[
    (
        Annotated[AccountHolderResource, Tag("accountHolder")]
        | Annotated[LegalEntityResource, Tag("legalEntity")]
        | Annotated[PaymentInstrumentResource, Tag("paymentInstrument")]
    ),
    WireDiscriminator("type"),
]

ResourceDict: TypeAlias = AccountHolderResourceDict | LegalEntityResourceDict | PaymentInstrumentResourceDict
