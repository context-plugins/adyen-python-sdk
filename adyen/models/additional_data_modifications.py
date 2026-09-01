from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalDataModifications(SdkBaseModel):
    installment_payment_data_selected_installment_option: Optional[str] = Field(
        default=UNSET, alias="installmentPaymentData.selectedInstallmentOption"
    )
    """This is the installment option selected by the shopper. It is required only if specified by the user."""


class AdditionalDataModificationsDict(TypedDict):
    installment_payment_data_selected_installment_option: NotRequired[str]
