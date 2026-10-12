from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.product_type2 import ProductType2OrStr
from .policy2 import Policy2, Policy2Dict


class AuthenticationSessionRequest(SdkBaseModel):
    allow_origin: str = Field(alias="allowOrigin")
    """The URL where the component will appear. In your live environment, you must protect the URL with an SSL
    certificate and ensure that it starts with ``https://``."""

    policy: Policy2
    """An object that contains a description of the allowed resources and roles for the requested session."""

    product: ProductType2OrStr
    """The type of component.

    For `Onboarding components <https://docs.adyen.com/platforms/onboard-users/components>`__, set this to
    **onboarding**.

    For `Platform Experience components <https://docs.adyen.com/platforms/build-user-dashboards>`__, set this to
    **platform**."""


class AuthenticationSessionRequestDict(TypedDict):
    allow_origin: str
    policy: Policy2Dict
    product: ProductType2OrStr
