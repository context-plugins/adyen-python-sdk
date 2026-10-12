from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.resource import Resource, ResourceDict


class Policy2(SdkBaseModel):
    """An object that contains a description of the allowed resources and roles for the requested session."""

    resources: Optional[list[Resource]] = UNSET
    """An object containing the type and the unique identifier of the user of the component.

    For `Onboarding components <https://docs.adyen.com/platforms/onboard-users/components>`__, this is the ID of the
    legal entity that has a contractual relationship with your platform. For sole proprietorships, use the ID of the
    legal entity of the individual owner.

    For `Platform Experience components <https://docs.adyen.com/platforms/build-user-dashboards>`__, this is the ID of
    the account holder that is associated with the balance account shown in the component."""

    roles: Optional[list[str]] = UNSET
    """The name of the role required to use the component."""


class Policy2Dict(TypedDict):
    resources: NotRequired[list[ResourceDict]]
    roles: NotRequired[list[str]]
