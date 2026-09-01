from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WalletPurpose(str, Enum):
    """The purpose of a digital wallet transaction."""

    IDENTIFIED_BOLETO = "identifiedBoleto"
    TRANSFER_DIFFERENT_WALLET = "transferDifferentWallet"
    TRANSFER_OWN_WALLET = "transferOwnWallet"
    TRANSFER_SAME_WALLET = "transferSameWallet"
    UNIDENTIFIED_BOLETO = "unidentifiedBoleto"

    __str__ = str.__str__


WalletPurposeOrStr: TypeAlias = Annotated[WalletPurpose | str, open_enum_validator(WalletPurpose)]
