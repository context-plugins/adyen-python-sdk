from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.challenge_cancel import ChallengeCancelOrStr
from .enums.exemption_indicator import ExemptionIndicatorOrStr
from .enums.three_dsrequestor_challenge_ind import ThreeDsrequestorChallengeIndOrStr


class ThreeDs2Result1(SdkBaseModel):
    """Result of the 3D Secure 2 authentication."""

    authentication_value: Optional[str] = Field(default=UNSET, alias="authenticationValue")
    """The ``authenticationValue`` value as defined in the 3D Secure 2 specification."""

    cavv_algorithm: Optional[str] = Field(default=UNSET, alias="cavvAlgorithm")
    """The algorithm used by the ACS to calculate the authentication value, only for Cartes Bancaires integrations."""

    challenge_cancel: Optional[ChallengeCancelOrStr] = Field(default=UNSET, alias="challengeCancel")
    """Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has
    been cancelled. For possible values, refer to `3D Secure API reference
    <https://docs.adyen.com/online-payments/3d-secure/api-reference#mpidata>`__."""

    ds_trans_id: Optional[str] = Field(default=UNSET, alias="dsTransID")
    """The ``dsTransID`` value as defined in the 3D Secure 2 specification."""

    eci: Optional[str] = UNSET
    """The ``eci`` value as defined in the 3D Secure 2 specification."""

    exemption_indicator: Optional[ExemptionIndicatorOrStr] = Field(default=UNSET, alias="exemptionIndicator")
    """Indicates the exemption type that was applied by the issuer to the authentication, if exemption applied. Allowed
    values:
    * ``lowValue``
    * ``secureCorporate``
    * ``trustedBeneficiary``
    * ``transactionRiskAnalysis``"""

    message_version: Optional[str] = Field(default=UNSET, alias="messageVersion")
    """The ``messageVersion`` value as defined in the 3D Secure 2 specification."""

    risk_score: Optional[str] = Field(default=UNSET, alias="riskScore")
    """Risk score calculated by Cartes Bancaires Directory Server (DS)."""

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

    three_ds_server_trans_id: Optional[str] = Field(default=UNSET, alias="threeDSServerTransID")
    """The ``threeDSServerTransID`` value as defined in the 3D Secure 2 specification."""

    timestamp: Optional[str] = UNSET
    """The ``timestamp`` value of the 3D Secure 2 authentication."""

    trans_status: Optional[str] = Field(default=UNSET, alias="transStatus")
    """The ``transStatus`` value as defined in the 3D Secure 2 specification."""

    trans_status_reason: Optional[str] = Field(default=UNSET, alias="transStatusReason")
    """Provides information on why the ``transStatus`` field has the specified value. For possible values, refer to `our
    docs <https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values>`__."""

    white_list_status: Optional[str] = Field(default=UNSET, alias="whiteListStatus")
    """The ``whiteListStatus`` value as defined in the 3D Secure 2 specification."""


class ThreeDs2Result1Dict(TypedDict):
    authentication_value: NotRequired[str]
    cavv_algorithm: NotRequired[str]
    challenge_cancel: NotRequired[ChallengeCancelOrStr]
    ds_trans_id: NotRequired[str]
    eci: NotRequired[str]
    exemption_indicator: NotRequired[ExemptionIndicatorOrStr]
    message_version: NotRequired[str]
    risk_score: NotRequired[str]
    three_ds_requestor_challenge_ind: NotRequired[ThreeDsrequestorChallengeIndOrStr]
    three_ds_server_trans_id: NotRequired[str]
    timestamp: NotRequired[str]
    trans_status: NotRequired[str]
    trans_status_reason: NotRequired[str]
    white_list_status: NotRequired[str]
