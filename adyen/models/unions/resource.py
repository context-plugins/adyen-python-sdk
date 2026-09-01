from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..account_holder_resource import AccountHolderResource, AccountHolderResourceDict
from ..legal_entity_resource import LegalEntityResource, LegalEntityResourceDict
from ..payment_instrument_resource import PaymentInstrumentResource, PaymentInstrumentResourceDict

Resource: TypeAlias = Annotated[
    AccountHolderResource | LegalEntityResource | PaymentInstrumentResource, Field(discriminator="type_")
]

ResourceDict: TypeAlias = AccountHolderResourceDict | LegalEntityResourceDict | PaymentInstrumentResourceDict
