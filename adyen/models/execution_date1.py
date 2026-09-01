from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class ExecutionDate1(SdkBaseModel):
    """Contains information about the date when the transfer will be processed. The execution date must be within 30
    days of the current date.

    Until the execution date:
    - The ``status`` of the transfer remains as **received**.
    - The ``reason`` of the transfer remains as **pending**."""

    date: Optional[Date] = UNSET
    """The date when the transfer will be processed. This date must be:
    * Within 30 days of the current date.
    * In the `ISO 8601 format <https://www.iso.org/iso-8601-date-and-time-format.html>`__ **YYYY-MM-DD**. For example:
        2025-01-31"""

    timezone: Optional[str] = UNSET
    """The timezone that applies to the execution date. Use a timezone identifier from the `tz database
    <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__.

    Example: **America/Los_Angeles**.
     Default value: **Europe/Amsterdam**."""


class ExecutionDate1Dict(TypedDict):
    date: NotRequired[Date]
    timezone: NotRequired[str]
