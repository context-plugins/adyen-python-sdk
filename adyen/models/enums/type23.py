from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type23(str, Enum):
    """**doku**"""

    DOKU_MANDIRI_VA = "doku_mandiri_va"
    DOKU_CIMB_VA = "doku_cimb_va"
    DOKU_DANAMON_VA = "doku_danamon_va"
    DOKU_BNI_VA = "doku_bni_va"
    DOKU_PERMATA_LITE_ATM = "doku_permata_lite_atm"
    DOKU_BRI_VA = "doku_bri_va"
    DOKU_BCA_VA = "doku_bca_va"
    DOKU_ALFAMART = "doku_alfamart"
    DOKU_INDOMARET = "doku_indomaret"
    DOKU_WALLET = "doku_wallet"
    DOKU_OVO = "doku_ovo"

    __str__ = str.__str__


Type23OrStr: TypeAlias = Annotated[Type23 | str, open_enum_validator(Type23)]
