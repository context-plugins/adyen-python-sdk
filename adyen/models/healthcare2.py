from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Healthcare2(SdkBaseModel):
    """Healthcare auto-substantiation amounts for FSA/HSA card transactions. The amounts are used to qualify for reduced
    interchange rates on healthcare-eligible cards."""

    dental_value: Optional[int] = Field(default=UNSET, alias="dentalValue")
    """The dental amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000"""

    other_medical_value: Optional[int] = Field(default=UNSET, alias="otherMedicalValue")
    """The other medical amount not covered by the specific categories, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000"""

    prescription_value: Optional[int] = Field(default=UNSET, alias="prescriptionValue")
    """The prescription/Rx amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000"""

    total_healthcare_value: int = Field(alias="totalHealthcareValue")
    """The total healthcare amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000"""

    vision_prescription_value: Optional[int] = Field(default=UNSET, alias="visionPrescriptionValue")
    """The vision/optical prescription amount, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000"""


class Healthcare2Dict(TypedDict):
    dental_value: NotRequired[int]
    other_medical_value: NotRequired[int]
    prescription_value: NotRequired[int]
    total_healthcare_value: int
    vision_prescription_value: NotRequired[int]
