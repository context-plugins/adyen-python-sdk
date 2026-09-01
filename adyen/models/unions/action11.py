from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..checkout_await_action import CheckoutAwaitAction, CheckoutAwaitActionDict
from ..checkout_bank_transfer_action import CheckoutBankTransferAction, CheckoutBankTransferActionDict
from ..checkout_delegated_authentication_action import (
    CheckoutDelegatedAuthenticationAction,
    CheckoutDelegatedAuthenticationActionDict,
)
from ..checkout_native_redirect_action import CheckoutNativeRedirectAction, CheckoutNativeRedirectActionDict
from ..checkout_qr_code_action import CheckoutQrCodeAction, CheckoutQrCodeActionDict
from ..checkout_redirect_action import CheckoutRedirectAction, CheckoutRedirectActionDict
from ..checkout_sdkaction import CheckoutSdkaction, CheckoutSdkactionDict
from ..checkout_three_ds2_action import CheckoutThreeDs2Action, CheckoutThreeDs2ActionDict
from ..checkout_voucher_action import CheckoutVoucherAction, CheckoutVoucherActionDict

Action11: TypeAlias = Annotated[
    (
        CheckoutAwaitAction
        | CheckoutBankTransferAction
        | CheckoutDelegatedAuthenticationAction
        | CheckoutNativeRedirectAction
        | CheckoutQrCodeAction
        | CheckoutRedirectAction
        | CheckoutSdkaction
        | CheckoutThreeDs2Action
        | CheckoutVoucherAction
    ),
    Field(discriminator="type_"),
]
"""Action to be taken for completing the payment."""

Action11Dict: TypeAlias = (
    CheckoutAwaitActionDict
    | CheckoutBankTransferActionDict
    | CheckoutDelegatedAuthenticationActionDict
    | CheckoutNativeRedirectActionDict
    | CheckoutQrCodeActionDict
    | CheckoutRedirectActionDict
    | CheckoutSdkactionDict
    | CheckoutThreeDs2ActionDict
    | CheckoutVoucherActionDict
)
