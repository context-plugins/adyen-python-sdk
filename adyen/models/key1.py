from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Key1(SdkBaseModel):
    """The key you share with Adyen to secure local communications when using Terminal API."""

    identifier: Optional[str] = UNSET
    """The unique identifier of the shared key."""

    passphrase: Optional[str] = UNSET
    """The secure passphrase to protect the shared key. Must consist of:

    * At least 12 characters.

    * At least 1 uppercase letter: ``[A-Z]``.

    * At least 1 lowercase letter: ``[a-z]``.

    * At least 1 digit: ``[0-9]``.

     * At least 1 special character. Limited to the following: ``~``, ``!``, ``@``, ``#``, ``$``, ``%``, ``^``, ``&``,
            ``*``, ``(``, ``)``, ``_``, ``+``, ``=``, ``}``, ``{``, ``]``, ``[``, ``;``, ``:``, ``?``, ``.``, ``,``,
            ``>``, ``<``."""

    version: Optional[int] = UNSET
    """The version number of the shared key."""


class Key1Dict(TypedDict):
    identifier: NotRequired[str]
    passphrase: NotRequired[str]
    version: NotRequired[int]
