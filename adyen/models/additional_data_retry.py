from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataRetry(SdkBaseModel):
    retry_chain_attempt_number: Optional[str] = Field(default=UNSET, alias="retry.chainAttemptNumber")
    """The number of times the transaction (not order) has been retried between different payment service providers. For
    instance, the ``chainAttemptNumber`` set to 2 means that this transaction has been recently tried on another
    provider before being sent to Adyen.

    > If you submit ``retry.chainAttemptNumber``, ``retry.orderAttemptNumber``, and ``retry.skipRetry`` values, we also
        recommend you provide the ``merchantOrderReference`` to facilitate linking payment attempts together."""

    retry_order_attempt_number: Optional[str] = Field(default=UNSET, alias="retry.orderAttemptNumber")
    """The index of the attempt to bill a particular order, which is identified by the ``merchantOrderReference`` field.
    For example, if a recurring transaction fails and is retried one day later, then the order number for these attempts
    would be 1 and 2, respectively.

    > If you submit ``retry.chainAttemptNumber``, ``retry.orderAttemptNumber``, and ``retry.skipRetry`` values, we also
        recommend you provide the ``merchantOrderReference`` to facilitate linking payment attempts together."""

    retry_skip_retry: Optional[str] = Field(default=UNSET, alias="retry.skipRetry")
    """The Boolean value indicating whether Adyen should skip or retry this transaction, if possible.

    > If you submit ``retry.chainAttemptNumber``, ``retry.orderAttemptNumber``, and ``retry.skipRetry`` values, we also
        recommend you provide the ``merchantOrderReference`` to facilitate linking payment attempts together."""


class AdditionalDataRetryDict(TypedDict):
    retry_chain_attempt_number: NotRequired[str]
    retry_order_attempt_number: NotRequired[str]
    retry_skip_retry: NotRequired[str]
