from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class TemporaryServices(SdkBaseModel):
    employee_name: Optional[str] = Field(default=UNSET, alias="employeeName")
    """The name or ID of the person working in a temporary capacity.
    * Format: ASCII
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``enhancedSchemeData.employeeName``"""

    end_date: Optional[Date] = Field(default=UNSET, alias="endDate")
    """The billing period end date.
    * Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: yyyy-MM-dd
    * **additionalData key:** ``enhancedSchemeData.tempWeekEnding``"""

    hour_rate: Optional[int] = Field(default=UNSET, alias="hourRate")
    """The hourly rate for the temporary services, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * For example, 2000 means USD 20.00.
    * Encoding: Numeric
    * Max value: 10000000000
    * **additionalData key:** ``enhancedSchemeData.regularHoursRate``"""

    hours_worked: Optional[int] = Field(default=UNSET, alias="hoursWorked")
    """The number of hours worked during the billing period.
    * Format: Numeric
    * **additionalData key:** ``enhancedSchemeData.regularHoursWorked``"""

    job_description: Optional[str] = Field(default=UNSET, alias="jobDescription")
    """The job description of the person working in a temporary capacity.
    * Format: ASCII
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``enhancedSchemeData.jobDescription``"""

    service_requestor: Optional[str] = Field(default=UNSET, alias="serviceRequestor")
    """The name of the person requesting the temporary services.
    * Format: ASCII
    * Must not start with a space or be all spaces.
    * Must not be all zeros.
    * **additionalData key:** ``enhancedSchemeData.requestName``"""

    start_date: Optional[Date] = Field(default=UNSET, alias="startDate")
    """The billing period start date.
    * Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: yyyy-MM-dd
    * **additionalData key:** ``enhancedSchemeData.tempStartDate``"""


class TemporaryServicesDict(TypedDict):
    employee_name: NotRequired[str]
    end_date: NotRequired[Date]
    hour_rate: NotRequired[int]
    hours_worked: NotRequired[int]
    job_description: NotRequired[str]
    service_requestor: NotRequired[str]
    start_date: NotRequired[Date]
