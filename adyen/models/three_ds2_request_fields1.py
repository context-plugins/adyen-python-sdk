from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .acct_info import AcctInfo, AcctInfoDict
from .device_render_options import DeviceRenderOptions, DeviceRenderOptionsDict
from .enums.acct_type import AcctTypeOrStr
from .enums.addr_match1 import AddrMatch1OrStr
from .enums.challenge_indicator import ChallengeIndicatorOrStr
from .enums.three_dsrequestor_challenge_ind import ThreeDsrequestorChallengeIndOrStr
from .enums.trans_type import TransTypeOrStr
from .enums.transaction_type import TransactionTypeOrStr
from .phone1 import Phone1, Phone1Dict
from .phone2 import Phone2, Phone2Dict
from .phone3 import Phone3, Phone3Dict
from .sdkephem_pub_key1 import SdkephemPubKey1, SdkephemPubKey1Dict
from .three_dsrequestor_authentication_info import (
    ThreeDsrequestorAuthenticationInfo,
    ThreeDsrequestorAuthenticationInfoDict,
)
from .three_dsrequestor_prior_authentication_info import (
    ThreeDsrequestorPriorAuthenticationInfo,
    ThreeDsrequestorPriorAuthenticationInfoDict,
)


class ThreeDs2RequestFields1(SdkBaseModel):
    """Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer
    to `Online payments <https://docs.adyen.com/online-payments>`__ or `Classic integration
    <https://docs.adyen.com/classic-integration>`__ documentation."""

    acct_info: Optional[AcctInfo] = Field(default=UNSET, alias="acctInfo")
    """Additional information about the cardholder’s account provided by the 3DS Requestor."""

    acct_type: Optional[AcctTypeOrStr] = Field(default=UNSET, alias="acctType")
    """Indicates the type of account. For example, for a multi-account card product. Length: 2 characters. Allowed
    values:
    * **01** — Not applicable
    * **02** — Credit
    * **03** — Debit"""

    acquirer_bin: Optional[str] = Field(default=UNSET, alias="acquirerBIN")
    """Required for `authentication-only integration
    <https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only>`__. The acquiring BIN
    enrolled for 3D Secure 2. This string should match the value that you will use in the authorisation. Use 123456 on
    the Test platform."""

    acquirer_merchant_id: Optional[str] = Field(default=UNSET, alias="acquirerMerchantID")
    """Required for `authentication-only integration
    <https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only>`__. The merchantId that is
    enrolled for 3D Secure 2 by the merchant's acquirer. This string should match the value that you will use in the
    authorisation. Use 123456 on the Test platform."""

    addr_match: Optional[AddrMatch1OrStr] = Field(default=UNSET, alias="addrMatch")
    """Indicates whether the cardholder shipping Address and cardholder billing address are the same. Allowed values:
    * **Y** — Shipping Address matches Billing Address.
    * **N** — Shipping Address does not match Billing Address."""

    authentication_only: bool = Field(default=False, alias="authenticationOnly")
    """If set to true, you will only perform the `3D Secure 2 authentication
    <https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only>`__, and not the payment
    authorisation."""

    challenge_indicator: Optional[ChallengeIndicatorOrStr] = Field(default=UNSET, alias="challengeIndicator")
    """Possibility to specify a preference for receiving a challenge from the issuer. Allowed values:
    * ``noPreference``
    * ``requestNoChallenge``
    * ``requestChallenge``
    * ``requestChallengeAsMandate``"""

    device_render_options: Optional[DeviceRenderOptions] = Field(default=UNSET, alias="deviceRenderOptions")
    """Display options for the 3D Secure 2 SDK. Optional and only for ``deviceChannel`` **app**."""

    home_phone: Optional[Phone3] = Field(default=UNSET, alias="homePhone")
    """The home phone number provided by the cardholder. The phone number must consist of a country code, followed by
    the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``, and did not send the shopper's phone number in ``telephoneNumber``."""

    mcc: Optional[str] = UNSET
    """Required for merchants that have been enrolled for 3D Secure 2 by another party than Adyen, mostly
    `authentication-only integrations
    <https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only>`__. The ``mcc`` is a
    four-digit code with which the previously given ``acquirerMerchantID`` is registered at the scheme."""

    merchant_name: Optional[str] = Field(default=UNSET, alias="merchantName")
    """Required for `authentication-only integration
    <https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only>`__. The merchant name that
    the issuer presents to the shopper if they get a challenge. We recommend to use the same value that you will use in
    the authorization. Maximum length is 40 characters.
    > Optional for a `full 3D Secure 2 integration
        <https://docs.adyen.com/online-payments/3d-secure/native-3ds2/api-integration>`__. Use this field if you are
        enrolled for 3D Secure 2 with us and want to override the merchant name already configured on your account."""

    message_version: Optional[str] = Field(default=UNSET, alias="messageVersion")
    """The ``messageVersion`` value indicating the 3D Secure 2 protocol version."""

    mobile_phone: Optional[Phone1] = Field(default=UNSET, alias="mobilePhone")
    """The mobile phone number provided by the cardholder. The phone number must consist of a country code, followed by
    the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``, and did not send the shopper's phone number in ``telephoneNumber``."""

    notification_url: Optional[str] = Field(default=UNSET, alias="notificationURL")
    """URL to where the issuer should send the ``CRes``. Required if you are not using components for ``channel``
    **Web** or if you are using classic integration ``deviceChannel`` **browser**."""

    pay_token_ind: Optional[bool] = Field(default=UNSET, alias="payTokenInd")
    """Value **true** indicates that the transaction was de-tokenised prior to being received by the ACS."""

    payment_authentication_use_case: Optional[str] = Field(default=UNSET, alias="paymentAuthenticationUseCase")
    """Indicates the type of payment for which an authentication is requested (message extension)"""

    purchase_instal_data: Optional[str] = Field(default=UNSET, alias="purchaseInstalData")
    """Indicates the maximum number of authorisations permitted for instalment payments. Length: 1–3 characters."""

    recurring_expiry: Optional[str] = Field(default=UNSET, alias="recurringExpiry")
    """Date after which no further authorisations shall be performed. Format: YYYYMMDD"""

    recurring_frequency: Optional[str] = Field(default=UNSET, alias="recurringFrequency")
    """Indicates the minimum number of days between authorisations. Maximum length: 4 characters."""

    sdk_app_id: Optional[str] = Field(default=UNSET, alias="sdkAppID")
    """The ``sdkAppID`` value as received from the 3D Secure 2 SDK."""

    sdk_ephem_pub_key: Optional[SdkephemPubKey1] = Field(default=UNSET, alias="sdkEphemPubKey")
    """The ``sdkEphemPubKey`` value as received from the 3D Secure 2 SDK."""

    sdk_max_timeout: int = Field(default=60, alias="sdkMaxTimeout")
    """The maximum amount of time in minutes for the 3D Secure 2 authentication process. Optional and only for
    ``deviceChannel`` set to **app**. Defaults to **60** minutes."""

    sdk_reference_number: Optional[str] = Field(default=UNSET, alias="sdkReferenceNumber")
    """The ``sdkReferenceNumber`` value as received from the 3D Secure 2 SDK."""

    sdk_trans_id: Optional[str] = Field(default=UNSET, alias="sdkTransID")
    """The ``sdkTransID`` value as received from the 3D Secure 2 SDK."""

    three_ds_comp_ind: Optional[str] = Field(default=UNSET, alias="threeDSCompInd")
    """Completion indicator for the device fingerprinting."""

    three_ds_requestor_authentication_ind: Optional[str] = Field(
        default=UNSET, alias="threeDSRequestorAuthenticationInd"
    )
    """Indicates the type of Authentication request."""

    three_ds_requestor_authentication_info: Optional[ThreeDsrequestorAuthenticationInfo] = Field(
        default=UNSET, alias="threeDSRequestorAuthenticationInfo"
    )
    """Information about how the 3DS Requestor authenticated the cardholder before or during the transaction"""

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

    three_ds_requestor_id: Optional[str] = Field(default=UNSET, alias="threeDSRequestorID")
    """Required for `authentication-only integration
    <https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only>`__ for Visa. Unique 3D Secure
    requestor identifier assigned by the Directory Server when you enrol for 3D Secure 2."""

    three_ds_requestor_name: Optional[str] = Field(default=UNSET, alias="threeDSRequestorName")
    """Required for `authentication-only integration
    <https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only>`__ for Visa. Unique 3D Secure
    requestor name assigned by the Directory Server when you enrol for 3D Secure 2."""

    three_ds_requestor_prior_authentication_info: Optional[ThreeDsrequestorPriorAuthenticationInfo] = Field(
        default=UNSET, alias="threeDSRequestorPriorAuthenticationInfo"
    )
    """Information about how the 3DS Requestor authenticated the cardholder as part of a previous 3DS transaction."""

    three_ds_requestor_url: Optional[str] = Field(default=UNSET, alias="threeDSRequestorURL")
    """URL of the (customer service) website that will be shown to the shopper in case of technical errors during the 3D
    Secure 2 process."""

    trans_type: Optional[TransTypeOrStr] = Field(default=UNSET, alias="transType")
    """Identifies the type of transaction being authenticated. Length: 2 characters. Allowed values:
    * **01** — Goods/Service Purchase
    * **03** — Check Acceptance
    * **10** — Account Funding
    * **11** — Quasi-Cash Transaction
    * **28** — Prepaid Activation and Load"""

    transaction_type: Optional[TransactionTypeOrStr] = Field(default=UNSET, alias="transactionType")
    """Identify the type of the transaction being authenticated."""

    white_list_status: Optional[str] = Field(default=UNSET, alias="whiteListStatus")
    """The ``whiteListStatus`` value returned from a previous 3D Secure 2 transaction, only applicable for 3D Secure 2
    protocol version 2.2.0."""

    work_phone: Optional[Phone2] = Field(default=UNSET, alias="workPhone")
    """The work phone number provided by the cardholder. The phone number must consist of a country code, followed by
    the number. If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``, and did not send the shopper's phone number in ``telephoneNumber``."""


class ThreeDs2RequestFields1Dict(TypedDict):
    acct_info: NotRequired[AcctInfoDict]
    acct_type: NotRequired[AcctTypeOrStr]
    acquirer_bin: NotRequired[str]
    acquirer_merchant_id: NotRequired[str]
    addr_match: NotRequired[AddrMatch1OrStr]
    authentication_only: NotRequired[bool]
    challenge_indicator: NotRequired[ChallengeIndicatorOrStr]
    device_render_options: NotRequired[DeviceRenderOptionsDict]
    home_phone: NotRequired[Phone3Dict]
    mcc: NotRequired[str]
    merchant_name: NotRequired[str]
    message_version: NotRequired[str]
    mobile_phone: NotRequired[Phone1Dict]
    notification_url: NotRequired[str]
    pay_token_ind: NotRequired[bool]
    payment_authentication_use_case: NotRequired[str]
    purchase_instal_data: NotRequired[str]
    recurring_expiry: NotRequired[str]
    recurring_frequency: NotRequired[str]
    sdk_app_id: NotRequired[str]
    sdk_ephem_pub_key: NotRequired[SdkephemPubKey1Dict]
    sdk_max_timeout: NotRequired[int]
    sdk_reference_number: NotRequired[str]
    sdk_trans_id: NotRequired[str]
    three_ds_comp_ind: NotRequired[str]
    three_ds_requestor_authentication_ind: NotRequired[str]
    three_ds_requestor_authentication_info: NotRequired[ThreeDsrequestorAuthenticationInfoDict]
    three_ds_requestor_challenge_ind: NotRequired[ThreeDsrequestorChallengeIndOrStr]
    three_ds_requestor_id: NotRequired[str]
    three_ds_requestor_name: NotRequired[str]
    three_ds_requestor_prior_authentication_info: NotRequired[ThreeDsrequestorPriorAuthenticationInfoDict]
    three_ds_requestor_url: NotRequired[str]
    trans_type: NotRequired[TransTypeOrStr]
    transaction_type: NotRequired[TransactionTypeOrStr]
    white_list_status: NotRequired[str]
    work_phone: NotRequired[Phone2Dict]
