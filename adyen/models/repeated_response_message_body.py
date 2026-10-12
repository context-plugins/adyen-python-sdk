from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_acquisition_response import CardAcquisitionResponse, CardAcquisitionResponseDict
from .card_reader_apduresponse import CardReaderApduresponse, CardReaderApduresponseDict
from .loyalty_response import LoyaltyResponse, LoyaltyResponseDict
from .payment_response4 import PaymentResponse4, PaymentResponse4Dict
from .reversal_response import ReversalResponse, ReversalResponseDict
from .stored_value_response import StoredValueResponse, StoredValueResponseDict


class RepeatedResponseMessageBody(SdkBaseModel):
    loyalty_response: Optional[LoyaltyResponse] = Field(default=UNSET, alias="LoyaltyResponse")
    """It conveys Information related to the Loyalty transaction processed by the POI System. Content of the Loyalty
    Response message."""

    payment_response: Optional[PaymentResponse4] = Field(default=UNSET, alias="PaymentResponse")
    """It conveys Information related to the Payment transaction processed by the POI System. Content of the Payment
    Response message."""

    reversal_response: Optional[ReversalResponse] = Field(default=UNSET, alias="ReversalResponse")
    """It conveys Information related to the reversal processed by the POI System. Content of the Reversal Response
    message."""

    stored_value_response: Optional[StoredValueResponse] = Field(default=UNSET, alias="StoredValueResponse")
    """It conveys Information related to the Stored Value transaction processed by the POI System. Content of the Stored
    Value Response message."""

    card_acquisition_response: Optional[CardAcquisitionResponse] = Field(default=UNSET, alias="CardAcquisitionResponse")
    """It conveys Information related to the payment and loyalty cards read and processed by the POI System and entered
    by the Customer. Content of the Card Acquisition Response message."""

    card_reader_apdu_response: Optional[CardReaderApduresponse] = Field(default=UNSET, alias="CardReaderAPDUResponse")
    """Content of the Card Reader APDU Response message. It contains the result of the requested service, APDU response
    sent by the chip of the card in response to the APDU request."""


class RepeatedResponseMessageBodyDict(TypedDict):
    loyalty_response: NotRequired[LoyaltyResponseDict]
    payment_response: NotRequired[PaymentResponse4Dict]
    reversal_response: NotRequired[ReversalResponseDict]
    stored_value_response: NotRequired[StoredValueResponseDict]
    card_acquisition_response: NotRequired[CardAcquisitionResponseDict]
    card_reader_apdu_response: NotRequired[CardReaderApduresponseDict]
