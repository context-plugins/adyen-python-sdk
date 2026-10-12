from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.three_dsrequestor_challenge_ind import ThreeDsrequestorChallengeIndOrStr
from .phone1 import Phone1, Phone1Dict
from .phone2 import Phone2, Phone2Dict
from .phone3 import Phone3, Phone3Dict


class CheckoutSessionThreeDs2RequestData3(SdkBaseModel):
    """The cardholder phone number need to be part of the authentication message for payment data. It is a requirement
    for Visa Secure Authentication Data Field Mandate effective August 2024."""

    home_phone: Optional[Phone3] = Field(default=UNSET, alias="homePhone")
    """The home phone number provided by the cardholder. The phone number must consist of a country code, followed by
    the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``, and did not send the shopper's phone number in ``telephoneNumber``."""

    mobile_phone: Optional[Phone1] = Field(default=UNSET, alias="mobilePhone")
    """The mobile phone number provided by the cardholder. The phone number must consist of a country code, followed by
    the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``, and did not send the shopper's phone number in ``telephoneNumber``."""

    three_ds_requestor_challenge_ind: Optional[ThreeDsrequestorChallengeIndOrStr] = Field(
        default=UNSET, alias="threeDSRequestorChallengeInd"
    )
    """Indicates whether a challenge is requested for this transaction. Possible values:
    * **01** — No preference
    * **02** — No challenge requested
    * **03** — Challenge requested (3DS Requestor preference)
    * **04** — Challenge requested (Mandate)
    * **05** — No challenge (transactional risk analysis is already performed)
    * **06** — Data Only"""

    work_phone: Optional[Phone2] = Field(default=UNSET, alias="workPhone")
    """The work phone number provided by the cardholder. The phone number must consist of a country code, followed by
    the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``, and did not send the shopper's phone number in ``telephoneNumber``."""


class CheckoutSessionThreeDs2RequestData3Dict(TypedDict):
    home_phone: NotRequired[Phone3Dict]
    mobile_phone: NotRequired[Phone1Dict]
    three_ds_requestor_challenge_ind: NotRequired[ThreeDsrequestorChallengeIndOrStr]
    work_phone: NotRequired[Phone2Dict]
