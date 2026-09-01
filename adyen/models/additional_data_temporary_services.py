from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataTemporaryServices(SdkBaseModel):
    enhanced_scheme_data_customer_reference: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.customerReference"
    )
    """The customer code, if supplied by a customer.
    * Encoding: ASCII
    * maxLength: 25"""

    enhanced_scheme_data_employee_name: Optional[str] = Field(default=UNSET, alias="enhancedSchemeData.employeeName")
    """The name or ID of the person working in a temporary capacity.
    * maxLength: 40.
    * Must not be all spaces.
    *Must not be all zeros."""

    enhanced_scheme_data_job_description: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.jobDescription"
    )
    """The job description of the person working in a temporary capacity.
    * maxLength: 40
    * Must not be all spaces.
    *Must not be all zeros."""

    enhanced_scheme_data_regular_hours_rate: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.regularHoursRate"
    )
    """The amount paid for regular hours worked, `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__.
    * maxLength: 7
    * Must not be empty
    * Can be all zeros"""

    enhanced_scheme_data_regular_hours_worked: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.regularHoursWorked"
    )
    """The hours worked.
    * maxLength: 7
    * Must not be empty
    * Can be all zeros"""

    enhanced_scheme_data_request_name: Optional[str] = Field(default=UNSET, alias="enhancedSchemeData.requestName")
    """The name of the person requesting temporary services.
    * maxLength: 40
    * Must not be all zeros
    * Must not be all spaces"""

    enhanced_scheme_data_temp_start_date: Optional[str] = Field(default=UNSET, alias="enhancedSchemeData.tempStartDate")
    """The billing period start date.
    * Format: ddMMyy
    * maxLength: 6"""

    enhanced_scheme_data_temp_week_ending: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.tempWeekEnding"
    )
    """The billing period end date.
    * Format: ddMMyy
    * maxLength: 6"""

    enhanced_scheme_data_total_tax_amount: Optional[str] = Field(
        default=UNSET, alias="enhancedSchemeData.totalTaxAmount"
    )
    """The total tax amount, in `minor units <https://docs.adyen.com/development-resources/currency-codes>`__. For
    example, 2000 means USD 20.00
    * maxLength: 12"""


class AdditionalDataTemporaryServicesDict(TypedDict):
    enhanced_scheme_data_customer_reference: NotRequired[str]
    enhanced_scheme_data_employee_name: NotRequired[str]
    enhanced_scheme_data_job_description: NotRequired[str]
    enhanced_scheme_data_regular_hours_rate: NotRequired[str]
    enhanced_scheme_data_regular_hours_worked: NotRequired[str]
    enhanced_scheme_data_request_name: NotRequired[str]
    enhanced_scheme_data_temp_start_date: NotRequired[str]
    enhanced_scheme_data_temp_week_ending: NotRequired[str]
    enhanced_scheme_data_total_tax_amount: NotRequired[str]
