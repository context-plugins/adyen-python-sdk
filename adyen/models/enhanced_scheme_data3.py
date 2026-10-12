from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .airline1 import Airline1, Airline1Dict
from .car_rental1 import CarRental1, CarRental1Dict
from .healthcare2 import Healthcare2, Healthcare2Dict
from .level_two_three2 import LevelTwoThree2, LevelTwoThree2Dict
from .lodging2 import Lodging2, Lodging2Dict
from .temporary_services2 import TemporaryServices2, TemporaryServices2Dict


class EnhancedSchemeData3(SdkBaseModel):
    """`Enhanced scheme data <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/>`__ that may be
    required for processing the payment and/or interchange savings can apply."""

    airline: Optional[Airline1] = UNSET
    """`Airline enhanced scheme data <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/airline/>`__
    that may be required for processing the transaction and/or for interchange savings."""

    car_rental: Optional[CarRental1] = Field(default=UNSET, alias="carRental")
    """`Car rental enhanced scheme data
    <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/car-rental/>`__ that may be required for
    processing the transaction and/or for interchange savings."""

    healthcare: Optional[Healthcare2] = UNSET
    """Healthcare auto-substantiation amounts for FSA/HSA card transactions. The amounts are used to qualify for reduced
    interchange rates on healthcare-eligible cards."""

    level_two_three: Optional[LevelTwoThree2] = Field(default=UNSET, alias="levelTwoThree")
    """`Level 2 and Level 3 enhanced scheme data
    <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3/>`__ that may be required for processing
    the transaction and/or for interchange savings."""

    lodging: Optional[Lodging2] = UNSET
    """`Lodging enhanced scheme data <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/lodging/>`__
    that may be required for processing the transaction and/or for interchange savings."""

    temporary_services: Optional[TemporaryServices2] = Field(default=UNSET, alias="temporaryServices")
    """`Temporary services enhanced scheme data
    <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/temporary-services/>`__ that may be required for
    processing the transaction and/or for interchange savings."""


class EnhancedSchemeData3Dict(TypedDict):
    airline: NotRequired[Airline1Dict]
    car_rental: NotRequired[CarRental1Dict]
    healthcare: NotRequired[Healthcare2Dict]
    level_two_three: NotRequired[LevelTwoThree2Dict]
    lodging: NotRequired[Lodging2Dict]
    temporary_services: NotRequired[TemporaryServices2Dict]
