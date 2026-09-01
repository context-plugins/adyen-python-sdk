from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OnboardingLink(SdkBaseModel):
    url: Optional[str] = UNSET
    """The URL of the hosted onboarding page where you need to redirect your user. This URL:

     - Expires after 4 minutes.

    - Can only be used once.

    - Can only be clicked once by the user.

    If the link expires, you need to create a new link."""


class OnboardingLinkDict(TypedDict):
    url: NotRequired[str]
