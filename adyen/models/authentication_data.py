from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.attempt_authentication import AttemptAuthenticationOrStr
from .three_dsrequest_data2 import ThreeDsrequestData2, ThreeDsrequestData2Dict


class AuthenticationData(SdkBaseModel):
    attempt_authentication: Optional[AttemptAuthenticationOrStr] = Field(default=UNSET, alias="attemptAuthentication")
    """Indicates when 3D Secure authentication should be attempted. This overrides all other rules, including `Dynamic
    3D Secure settings <https://docs.adyen.com/risk-management/dynamic-3d-secure>`__.

    Possible values:

    * **always**: Perform 3D Secure authentication.
    * **never**: Don't perform 3D Secure authentication. If PSD2 SCA or other national regulations require
        authentication, the transaction gets declined."""

    authentication_only: bool = Field(default=False, alias="authenticationOnly")
    """Required to trigger the `authentication-only flow
    <https://docs.adyen.com/online-payments/3d-secure/authentication-only/>`__. If set to **true**, you will only
    perform the 3D Secure 2 authentication, and will not proceed to the payment authorization. Default: **false**."""

    three_ds_request_data: Optional[ThreeDsrequestData2] = Field(default=UNSET, alias="threeDSRequestData")
    """Object with additional parameters for the 3D Secure authentication flow."""


class AuthenticationDataDict(TypedDict):
    attempt_authentication: NotRequired[AttemptAuthenticationOrStr]
    authentication_only: NotRequired[bool]
    three_ds_request_data: NotRequired[ThreeDsrequestData2Dict]
