from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type191(str, Enum):
    """Type of Partnership.

    Possible values:
    * **limitedPartnership**
    * **generalPartnership**
    * **familyPartnership**
    * **commercialPartnership**
    * **publicPartnership**
    * **otherPartnership**
    * **gbr**
    * **gmbh**
    * **kgaa**
    * **cv**
    * **vof**
    * **maatschap**
    * **privateFundLimitedPartnership**
    * **businessTrustEntity**
    * **businessPartnership**
    * **limitedLiabilityPartnership**
    * **eg**
    * **cooperative**
    * **vos**
    * **comunidadDeBienes**
    * **herenciaYacente**
    * **comunidadDePropietarios**
    * **sep**
    * **sca**
    * **bt**
    * **kkt**
    * **scs**
    * **snc**"""

    LIMITED_PARTNERSHIP = "limitedPartnership"
    GENERAL_PARTNERSHIP = "generalPartnership"
    FAMILY_PARTNERSHIP = "familyPartnership"
    COMMERCIAL_PARTNERSHIP = "commercialPartnership"
    PUBLIC_PARTNERSHIP = "publicPartnership"
    OTHER_PARTNERSHIP = "otherPartnership"
    GBR = "gbr"
    GMBH = "gmbh"
    KGAA = "kgaa"
    CV = "cv"
    VOF = "vof"
    MAATSCHAP = "maatschap"
    PRIVATE_FUND_LIMITED_PARTNERSHIP = "privateFundLimitedPartnership"
    BUSINESS_TRUST_ENTITY = "businessTrustEntity"
    BUSINESS_PARTNERSHIP = "businessPartnership"
    LIMITED_LIABILITY_PARTNERSHIP = "limitedLiabilityPartnership"
    EG = "eg"
    COOPERATIVE = "cooperative"
    VOS = "vos"
    COMUNIDAD_DE_BIENES = "comunidadDeBienes"
    HERENCIA_YACENTE = "herenciaYacente"
    COMUNIDAD_DE_PROPIETARIOS = "comunidadDePropietarios"
    SEP = "sep"
    SCA = "sca"
    BT = "bt"
    KKT = "kkt"
    SCS = "scs"
    SNC = "snc"

    __str__ = str.__str__


Type191OrStr: TypeAlias = Annotated[Type191 | str, open_enum_validator(Type191)]
