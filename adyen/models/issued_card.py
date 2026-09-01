from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pan_entry_mode import PanEntryModeOrStr
from .enums.processing_type1 import ProcessingType1OrStr
from .enums.type511 import Type511OrStr
from .relayed_authorisation_data2 import RelayedAuthorisationData2, RelayedAuthorisationData2Dict
from .three_dsecure2 import ThreeDsecure2, ThreeDsecure2Dict
from .transfer_notification_validation_fact import (
    TransferNotificationValidationFact,
    TransferNotificationValidationFactDict,
)


class IssuedCard(SdkBaseModel):
    authorisation_type: Optional[str] = Field(default=UNSET, alias="authorisationType")
    """The authorisation type. For example, **defaultAuthorisation**, **preAuthorisation**, **finalAuthorisation**"""

    pan_entry_mode: Optional[PanEntryModeOrStr] = Field(default=UNSET, alias="panEntryMode")
    """Indicates the method used for entering the PAN to initiate a transaction.

    Possible values: **manual**, **chip**, **magstripe**, **contactless**, **cof**, **ecommerce**, **token**."""

    processing_type: Optional[ProcessingType1OrStr] = Field(default=UNSET, alias="processingType")
    """Contains information about how the payment was processed.

    Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **purchaseWithCashback**,
    **recurring**, **token**."""

    relayed_authorisation_data: Optional[RelayedAuthorisationData2] = Field(
        default=UNSET, alias="relayedAuthorisationData"
    )
    """If you are using relayed authorisation, this object contains information from the relayed authorisation response
    from your server."""

    scheme_trace_id: Optional[str] = Field(default=UNSET, alias="schemeTraceId")
    """The identifier of the original payment. This ID is provided by the scheme and can be alphanumeric or numeric,
    depending on the scheme. The ``schemeTraceID`` should refer to an original ``schemeUniqueTransactionID`` provided in
    an earlier payment (not necessarily processed by Adyen). A ``schemeTraceId`` is typically available for
    authorization adjustments or recurring payments."""

    scheme_unique_transaction_id: Optional[str] = Field(default=UNSET, alias="schemeUniqueTransactionId")
    """The unique identifier created by the scheme. This ID can be alphanumeric or numeric depending on the scheme."""

    three_d_secure: Optional[ThreeDsecure2] = Field(default=UNSET, alias="threeDSecure")
    """The data of the result from the 3DS authentication."""

    type_: Optional[Type511OrStr] = Field(default=UNSET, alias="type")
    """**issuedCard**"""

    validation_facts: Optional[list[TransferNotificationValidationFact]] = Field(default=UNSET, alias="validationFacts")
    """The evaluation of the validation facts. See `validation checks
    <https://docs.adyen.com/issuing/validation-checks>`__ for more information."""


class IssuedCardDict(TypedDict):
    authorisation_type: NotRequired[str]
    pan_entry_mode: NotRequired[PanEntryModeOrStr]
    processing_type: NotRequired[ProcessingType1OrStr]
    relayed_authorisation_data: NotRequired[RelayedAuthorisationData2 | RelayedAuthorisationData2Dict]
    scheme_trace_id: NotRequired[str]
    scheme_unique_transaction_id: NotRequired[str]
    three_d_secure: NotRequired[ThreeDsecure2 | ThreeDsecure2Dict]
    type_: NotRequired[Type511OrStr]
    validation_facts: NotRequired[list[TransferNotificationValidationFact | TransferNotificationValidationFactDict]]
