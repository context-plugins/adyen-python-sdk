# Payments

```python
payments_api = client.payments
```

## Class Name

`PaymentsApi`

## Methods

* [Post-Card Details](../../doc/controllers/payments.md#post-card-details)
* [Post-Payment Methods](../../doc/controllers/payments.md#post-payment-methods)
* [Post-Payments](../../doc/controllers/payments.md#post-payments)
* [Post-Payments-Details](../../doc/controllers/payments.md#post-payments-details)
* [Post-Sessions](../../doc/controllers/payments.md#post-sessions)
* [Get-Sessions-Session Id](../../doc/controllers/payments.md#get-sessions-session-id)
* [Post-Authorise](../../doc/controllers/payments.md#post-authorise)
* [Post-Authorise 3 D](../../doc/controllers/payments.md#post-authorise-3-d)
* [Post-Authorise 3 Ds 2](../../doc/controllers/payments.md#post-authorise-3-ds-2)
* [Post-Get Authentication Result](../../doc/controllers/payments.md#post-get-authentication-result)
* [Post-Retrieve 3 Ds 2 Result](../../doc/controllers/payments.md#post-retrieve-3-ds-2-result)
* [Post-Payments-Cancel](../../doc/controllers/payments.md#post-payments-cancel)
* [Post-Payments-Confirm](../../doc/controllers/payments.md#post-payments-confirm)
* [Post-Payments-Details 1](../../doc/controllers/payments.md#post-payments-details-1)


# Post-Card Details

Use this endpoint to get information about the card or network token that enables you to decide on the routing of the transaction and the eligibility of the card for the type of transaction.

If you include [your supported brands](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cardDetails__reqParam_supportedBrands) in the request, the response also tells you if you support each [brand that was identified on the card](https://docs.adyen.com/api-explorer/Checkout/latest/post/cardDetails#responses-200-brands).

If you have an API-only integration and collect card data, use this endpoint to find out if the shopper's card is co-bad. For co-badged cards, you must let the shopper choose the brand to pay with  if you support both brands.

## Server-side API libraries

We provide open-source [server-side API libraries](https://docs.adyen.com/development-resources/libraries/) in several languages:

- PHP
- Java
- Node.js
- .NET
- Go
- Python
- Ruby
- Apex (beta)

See our [integration examples](https://github.com/adyen-examples#%EF%B8%8F-official-integration-examples) for example uses of the libraries.

## Developer resources

BIN Lookup API is available through a Postman collection. Click the button below to create a fork, then set the environment variables at **Environments**&nbsp;>&nbsp;**Adyen&nbsp;APIs**.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/25716737-677c7679-a695-4ebb-91da-68b4e7c9228a?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D25716737-677c7679-a695-4ebb-91da-68b4e7c9228a%26entityType%3Dcollection%26workspaceId%3Da8d63f9f-cfc7-4810-90c5-9e0c60030d3e#?env%5BAdyen%20APIs%5D=W3sia2V5IjoiWC1BUEktS2V5IiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoic2VjcmV0In0seyJrZXkiOiJZT1VSX01FUkNIQU5UX0FDQ09VTlQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJZT1VSX0NPTVBBTllfQUNDT1VOVCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6IllPVVJfQkFMQU5DRV9QTEFURk9STSIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

```python
def post_card_details(self,
                     idempotency_key=None,
                     body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`CardDetailsRequest`](../../doc/models/card-details-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`CardDetailsResponse`](../../doc/models/card-details-response.md)

## Example Usage

```python
body = CardDetailsRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    card_number='411111'
)

result = payments_api.post_card_details(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "brands": [
    {
      "type": "visa",
      "supported": true
    },
    {
      "type": "cartebancaire",
      "supported": true
    }
  ],
  "fundingSource": "CREDIT",
  "isCardCommercial": false,
  "issuingCountryCode": "FR"
}
```


# Post-Payment Methods

Retrieves the list of available payment methods for the transaction, based on the transaction information like amount, country, and currency.

```python
def post_payment_methods(self,
                        idempotency_key=None,
                        body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`PaymentMethodsRequest`](../../doc/models/payment-methods-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`PaymentMethodsResponse`](../../doc/models/payment-methods-response.md)

## Example Usage

```python
body = PaymentMethodsRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT'
)

result = payments_api.post_payment_methods(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "paymentMethods": [
    {
      "name": "ACH Direct Debit",
      "type": "ach"
    },
    {
      "name": "Adyen Voucher",
      "type": "adyen_test_voucher"
    },
    {
      "name": "AfterPay Invoice",
      "type": "afterpay_default"
    },
    {
      "name": "AfterPay DirectDebit",
      "type": "afterpay_directdebit"
    },
    {
      "name": "Afterpay",
      "type": "afterpaytouch"
    },
    {
      "name": "Cards",
      "type": "scheme"
    },
    {
      "name": "AliPay",
      "type": "alipay"
    },
    {
      "name": "AliPay HK",
      "type": "alipay_hk"
    },
    {
      "name": "AliPay",
      "type": "alipay_wap"
    },
    {
      "name": "Android Pay",
      "type": "androidpay"
    },
    {
      "name": "Apple Pay",
      "type": "applepay"
    },
    {
      "name": "Credit Card via AsiaPay",
      "type": "asiapay"
    },
    {
      "name": "China UnionPay",
      "type": "asiapay_unionpay"
    },
    {
      "name": "Baby Gift Card",
      "type": "babygiftcard"
    },
    {
      "name": "Baloto",
      "type": "baloto"
    },
    {
      "name": "BancNet",
      "type": "bancnet"
    },
    {
      "name": "Bank Transfer (BG)",
      "type": "bankTransfer_BG"
    },
    {
      "name": "Bank Transfer (CH)",
      "type": "bankTransfer_CH"
    },
    {
      "name": "Bank Transfer (DE)",
      "type": "bankTransfer_DE"
    },
    {
      "name": "Bank Transfer (FI)",
      "type": "bankTransfer_FI"
    },
    {
      "name": "Bank Transfer (GB)",
      "type": "bankTransfer_GB"
    },
    {
      "name": "Bank Transfer (HU)",
      "type": "bankTransfer_HU"
    },
    {
      "name": "SEPA Bank Transfer",
      "type": "bankTransfer_IBAN"
    },
    {
      "name": "Bank Transfer (IE)",
      "type": "bankTransfer_IE"
    },
    {
      "name": "Electronic Bank Transfer (MX)",
      "type": "bankTransfer_MX_linked"
    },
    {
      "name": "Bank Transfer (MX)",
      "type": "bankTransfer_MX_offline"
    },
    {
      "name": "Bank Transfer (NL)",
      "type": "bankTransfer_NL"
    },
    {
      "name": "Bank Transfer (PL)",
      "type": "bankTransfer_PL"
    },
    {
      "name": "Bank Transfer (SE)",
      "type": "bankTransfer_SE"
    },
    {
      "name": "Bank Transfer (US)",
      "type": "bankTransfer_US"
    },
    {
      "name": "Payconiq by Bancontact",
      "type": "bcmc_mobile"
    },
    {
      "name": "Bijenkorf Cadeaucard",
      "type": "bijcadeaucard"
    },
    {
      "name": "99Bill",
      "type": "bill99"
    },
    {
      "name": "Online Banking India",
      "type": "billdesk_online"
    },
    {
      "name": "UPI",
      "type": "billdesk_upi"
    },
    {
      "name": "Wallets India",
      "type": "billdesk_wallet"
    },
    {
      "name": "Blik",
      "type": "blik"
    },
    {
      "name": "Bloemen Giftcard",
      "type": "bloemengiftcard"
    },
    {
      "name": "Boekenbon Giftcard",
      "type": "boekenbon"
    },
    {
      "name": "Boleto",
      "type": "boleto"
    },
    {
      "name": "Boleto Bancario",
      "type": "boletobancario_santander"
    },
    {
      "name": "Bradesco",
      "type": "bradesco"
    },
    {
      "name": "Cash-Ticket",
      "type": "cashticket"
    },
    {
      "name": "CashU",
      "type": "cashu"
    },
    {
      "name": "CCAvenue",
      "type": "ccavenue"
    },
    {
      "name": "Mula Checkout",
      "type": "cellulant"
    },
    {
      "name": "Chasin Giftcard",
      "type": "chasingiftcard"
    },
    {
      "name": "Clearpay",
      "type": "clearpay"
    },
    {
      "name": "ClickandBuy",
      "type": "clickandbuy"
    },
    {
      "name": "Paiement en 3 fois par Cartes Bancaires",
      "type": "cofinoga_3xcb"
    },
    {
      "name": "Costes Giftcard",
      "type": "costesgiftcard"
    },
    {
      "name": "custom_settlement",
      "type": "custom_settlement"
    },
    {
      "name": "DANA",
      "type": "dana"
    },
    {
      "name": "DineroMail",
      "type": "dineromail"
    },
    {
      "name": "Online bank transfer.",
      "type": "directEbanking"
    },
    {
      "name": "Direct Debit Brazil - Banco do Brazil",
      "type": "directdebit_BR_bancodobrasil"
    },
    {
      "name": "Direct Debit Brazil - Bradesco",
      "type": "directdebit_BR_bradesco"
    },
    {
      "name": "Direct Debit Brazil - Caixa Economica Federal",
      "type": "directdebit_BR_caixa"
    },
    {
      "name": "Direct Debit Brazil - HSBC",
      "type": "directdebit_BR_hsbc"
    },
    {
      "name": "Direct Debit Brazil - Itau",
      "type": "directdebit_BR_itau"
    },
    {
      "name": "Direct Debit Brazil - Santander",
      "type": "directdebit_BR_santander"
    },
    {
      "name": "BACS Direct Debit",
      "type": "directdebit_GB"
    },
    {
      "name": "Alfamart",
      "type": "doku_alfamart"
    },
    {
      "name": "BCA Bank Transfer",
      "type": "doku_bca_va"
    },
    {
      "name": "BNI VA",
      "type": "doku_bni_va"
    },
    {
      "name": "BRI VA",
      "type": "doku_bri_va"
    },
    {
      "name": "CIMB VA",
      "type": "doku_cimb_va"
    },
    {
      "name": "Danamon VA",
      "type": "doku_danamon_va"
    },
    {
      "name": "Indomaret",
      "type": "doku_indomaret"
    },
    {
      "name": "Mandiri VA",
      "type": "doku_mandiri_va"
    },
    {
      "name": "OVO",
      "type": "doku_ovo"
    },
    {
      "name": "Bank Transfer",
      "type": "doku_permata_lite_atm"
    },
    {
      "name": "DOKU wallet",
      "type": "doku_wallet"
    },
    {
      "name": "Dragonpay Prepaid Credits",
      "type": "dragonpay_credits"
    },
    {
      "name": "Online Banking",
      "type": "dragonpay_ebanking"
    },
    {
      "name": "GCash",
      "type": "dragonpay_gcash"
    },
    {
      "name": "Over The Counter Banks",
      "type": "dragonpay_otc_banking"
    },
    {
      "name": "OTC non-Bank via Dragonpay",
      "type": "dragonpay_otc_non_banking"
    },
    {
      "name": "Convenience Stores",
      "type": "dragonpay_otc_philippines"
    },
    {
      "name": "7/11",
      "type": "dragonpay_seveneleven"
    },
    {
      "name": "eagleeye_voucher",
      "type": "eagleeye_voucher"
    },
    {
      "name": "Finnish E-Banking",
      "type": "ebanking_FI"
    },
    {
      "name": "Pay-easy ATM",
      "type": "econtext_atm"
    },
    {
      "name": "Online Banking",
      "type": "econtext_online"
    },
    {
      "name": "7-Eleven",
      "type": "econtext_seven_eleven"
    },
    {
      "name": "Convenience Stores",
      "type": "econtext_stores"
    },
    {
      "name": "eft_directdebit_CA",
      "type": "eft_directdebit_CA"
    },
    {
      "name": "Lastschrift (ELV)",
      "type": "elv"
    },
    {
      "name": "Bank Payment",
      "type": "entercash"
    },
    {
      "name": "Nationale Entertainment Card",
      "type": "entertainmentcard"
    },
    {
      "name": "EPS",
      "type": "eps"
    },
    {
      "name": "Expert Cadeaukaart",
      "type": "expertgiftcard"
    },
    {
      "name": "3x Oney",
      "type": "facilypay_3x"
    },
    {
      "name": "4x Oney",
      "type": "facilypay_4x"
    },
    {
      "name": "Fashioncheque",
      "type": "fashioncheque"
    },
    {
      "name": "Fawry",
      "type": "fawry"
    },
    {
      "name": "FijnCadeau",
      "type": "fijncadeau"
    },
    {
      "name": "Fleurop Bloemenbon",
      "type": "fleuropbloemenbon"
    },
    {
      "name": "Fonq Giftcard",
      "type": "fonqgiftcard"
    },
    {
      "name": "Gall & Gall",
      "type": "gallgall"
    },
    {
      "name": "GCash",
      "type": "gcash"
    },
    {
      "name": "Generic GiftCard",
      "type": "genericgiftcard"
    },
    {
      "name": "GiftFor2",
      "type": "giftfor2card"
    },
    {
      "name": "Givex",
      "type": "givex"
    },
    {
      "name": "Globe GCash",
      "type": "globegcash"
    },
    {
      "name": "Goldsmiths Card",
      "type": "goldsmithscard"
    },
    {
      "name": "GoPay Wallet",
      "type": "gopay_wallet"
    },
    {
      "name": "OVO",
      "type": "grabpay_ID"
    },
    {
      "name": "GrabPay",
      "type": "grabpay_PH"
    },
    {
      "name": "GrabPay",
      "type": "grabpay_SG"
    },
    {
      "name": "Hallmark Card",
      "type": "hallmarkcard"
    },
    {
      "name": "HDFC",
      "type": "hdfc"
    },
    {
      "name": "Hunkemoller Member Card",
      "type": "hmclub"
    },
    {
      "name": "Hunkemoller Lingerie Card",
      "type": "hmlingerie"
    },
    {
      "name": "iDEAL",
      "type": "ideal"
    },
    {
      "name": "igive",
      "type": "igive"
    },
    {
      "name": "Korean Account Transfer (IniPay)",
      "type": "inicisIniPay_accounttransfer"
    },
    {
      "name": "Korean Credit Cards (IniPay)",
      "type": "inicisIniPay_creditcard"
    },
    {
      "name": "Korean Mobile Phone (IniPay)",
      "type": "inicisIniPay_mobilephone"
    },
    {
      "name": "Korean Virtual Account (IniPay)",
      "type": "inicisIniPay_virtualaccount"
    },
    {
      "name": "Korean Account Transfer (Mobile)",
      "type": "inicisMobile_accounttransfer"
    },
    {
      "name": "Korean Credit Cards (Mobile)",
      "type": "inicisMobile_creditcard"
    },
    {
      "name": "Korean Mobile Phone (Mobile)",
      "type": "inicisMobile_mobilephone"
    },
    {
      "name": "Korean Virtual Account (Mobile)",
      "type": "inicisMobile_virtualaccount"
    },
    {
      "name": "Korean Credit Cards",
      "type": "inicis_creditcard"
    },
    {
      "name": "Interac® Online",
      "type": "interac"
    },
    {
      "name": "Instant EFT",
      "type": "ipay"
    },
    {
      "name": "iPay88",
      "type": "ipay88"
    },
    {
      "name": "isracard",
      "type": "isracard"
    },
    {
      "name": "Phone Payment",
      "type": "ivr"
    },
    {
      "name": "Landline phone",
      "type": "ivrLandline"
    },
    {
      "name": "Mobile phone",
      "type": "ivrMobile"
    },
    {
      "name": "Kado Wereld",
      "type": "kadowereld"
    },
    {
      "name": "KakaoPay",
      "type": "kakaopay"
    },
    {
      "name": "Karen Millen Card",
      "type": "karenmillen"
    },
    {
      "name": "Karen Millen GiftCard",
      "type": "karenmillengiftcard"
    },
    {
      "name": "Bank Transfer",
      "type": "kcp_banktransfer"
    },
    {
      "name": "Korea–issued cards",
      "type": "kcp_creditcard"
    },
    {
      "name": "PayCo",
      "type": "kcp_payco"
    },
    {
      "name": "Naver Pay",
      "type": "kcp_naverpay"
    },
    {
      "name": "Virtual Account via KCP",
      "type": "kcp_va"
    },
    {
      "name": "Pay later with Klarna.",
      "type": "klarna"
    },
    {
      "name": "Pay over time with Klarna.",
      "type": "klarna_account"
    },
    {
      "name": "Buy Now, Pay Later with Billie",
      "type": "klarna_b2b"
    },
    {
      "name": "Pay now with Klarna.",
      "type": "klarna_paynow"
    },
    {
      "name": "Leisure Card",
      "type": "leisurecard"
    },
    {
      "name": "China Credit Card",
      "type": "lianlianpay_creditcard"
    },
    {
      "name": "China Debit Card",
      "type": "lianlianpay_debitcard"
    },
    {
      "name": "China Online Banking - Credit Card",
      "type": "lianlianpay_ebanking_credit"
    },
    {
      "name": "China Online Banking - Debit Card",
      "type": "lianlianpay_ebanking_debit"
    },
    {
      "name": "China Online Banking - Enterprise",
      "type": "lianlianpay_ebanking_enterprise"
    },
    {
      "name": "Loods5 Cadeaukaart",
      "type": "loods5giftcard"
    },
    {
      "name": "Loods5 Tegoedbon",
      "type": "loods5prepaidcard"
    },
    {
      "name": "Love2Shop GiftCard",
      "type": "love2shop"
    },
    {
      "name": "mada",
      "type": "mada"
    },
    {
      "name": "Mappin & Webb Card",
      "type": "mappinwebbcard"
    },
    {
      "name": "MB WAY",
      "type": "mbway"
    },
    {
      "name": "Amazon Pay",
      "type": "amazonpay"
    },
    {
      "name": "Mercado Pago",
      "type": "mercadopago"
    },
    {
      "name": "MobilePay",
      "type": "mobilepay"
    },
    {
      "name": "AliPay via Razer Merchant Services",
      "type": "molpay_alipay"
    },
    {
      "name": "7-Eleven",
      "type": "molpay_cash"
    },
    {
      "name": "CIMB Virtual Account",
      "type": "molpay_cimb_va"
    },
    {
      "name": "Malaysia E-Banking via Razer Merchant Services",
      "type": "molpay_ebanking_MY"
    },
    {
      "name": "Vietnam E-Banking",
      "type": "molpay_ebanking_VN"
    },
    {
      "name": "Malaysia E-Banking",
      "type": "molpay_ebanking_fpx_MY"
    },
    {
      "name": "eNETS Debit",
      "type": "molpay_enetsd"
    },
    {
      "name": "epay",
      "type": "molpay_epay"
    },
    {
      "name": "Esapay",
      "type": "molpay_esapay"
    },
    {
      "name": "MyClear FPX",
      "type": "molpay_fpx"
    },
    {
      "name": "Maybank2u",
      "type": "molpay_maybank2u"
    },
    {
      "name": "Nganluong",
      "type": "molpay_nganluong"
    },
    {
      "name": "Convenience Stores Thailand",
      "type": "molpay_paysbuy"
    },
    {
      "name": "MOLPoints",
      "type": "molpay_points"
    },
    {
      "name": "RHB Now",
      "type": "molpay_rhb"
    },
    {
      "name": "SAM by SingPost",
      "type": "molpay_singpost"
    },
    {
      "name": "MOLWallet",
      "type": "molpay_wallet"
    },
    {
      "name": "MoMo ATM",
      "type": "momo_atm"
    },
    {
      "name": "Momo Wallet",
      "type": "momo_wallet"
    },
    {
      "name": "Moneybookers",
      "type": "moneybookers"
    },
    {
      "name": "Multibanco",
      "type": "multibanco"
    },
    {
      "name": "De Nationale Musicalcard",
      "type": "musicalcard"
    },
    {
      "name": "Nationale Bioscoopbon",
      "type": "nationalebioscoopbon"
    },
    {
      "name": "Nationale Tuinbon",
      "type": "nationaletuinbon"
    },
    {
      "name": "Nationale Verwen Cadeaubon",
      "type": "nationaleverwencadeaubon"
    },
    {
      "name": "BankAxess",
      "type": "netaxept_bankaxess"
    },
    {
      "name": "NETELLER",
      "type": "neteller"
    },
    {
      "name": "Onebip",
      "type": "onebip"
    },
    {
      "name": "One Two Three",
      "type": "onetwothree"
    },
    {
      "name": "Online Banking PL",
      "type": "onlineBanking_PL"
    },
    {
      "name": "Online banking",
      "type": "openbanking_UK"
    },
    {
      "name": "Oxxo",
      "type": "oxxo"
    },
    {
      "name": "Pathe Giftcard",
      "type": "pathegiftcard"
    },
    {
      "name": "PayBright",
      "type": "paybright"
    },
    {
      "name": "Maya Wallet",
      "type": "paymaya_wallet"
    },
    {
      "name": "PayPal",
      "type": "paypal"
    },
    {
      "name": "Paysafecard",
      "type": "paysafecard"
    },
    {
      "name": "Payshop",
      "type": "payshop"
    },
    {
      "name": "PayD AMT via Paythru",
      "type": "paythru_amt"
    },
    {
      "name": "EFT via Paythru",
      "type": "paythru_eft"
    },
    {
      "name": "PayTM",
      "type": "paytm"
    },
    {
      "name": "PayU UPI",
      "type": "payu_IN_upi"
    },
    {
      "name": "EFT Pro via PayU",
      "type": "payu_ZA_eftpro"
    },
    {
      "name": "Google Pay",
      "type": "paywithgoogle"
    },
    {
      "name": "pix",
      "type": "pix"
    },
    {
      "name": "Plastix",
      "type": "plastix"
    },
    {
      "name": "Pluim",
      "type": "pluimgiftcard"
    },
    {
      "name": "Podium Card",
      "type": "podiumcard"
    },
    {
      "name": "POLi",
      "type": "poli"
    },
    {
      "name": "PPS",
      "type": "pps"
    },
    {
      "name": "Primera Cadeaukaart",
      "type": "primeracadeaucard"
    },
    {
      "name": "Illicado Gift Card",
      "type": "prosodie_illicado"
    },
    {
      "name": "PSE",
      "type": "pse"
    },
    {
      "name": "Qiwi Wallet",
      "type": "qiwiwallet"
    },
    {
      "name": "RatePay Invoice",
      "type": "ratepay"
    },
    {
      "name": "RatePay Direct Debit",
      "type": "ratepay_directdebit"
    },
    {
      "name": "Rituals Giftcard",
      "type": "rituals"
    },
    {
      "name": "Rob Peetoom Giftcard",
      "type": "robpeetoomgiftcard"
    },
    {
      "name": "SafetyPay",
      "type": "safetypay"
    },
    {
      "name": "SafetyPay Cash",
      "type": "safetypay_cash"
    },
    {
      "name": "Shoes&Accessories Cadeau",
      "type": "sagiftcard"
    },
    {
      "name": "Score Giftcard",
      "type": "scoregiftcard"
    },
    {
      "name": "SEB Direktbetalning",
      "type": "sebdirectpayment"
    },
    {
      "name": "SEPA Direct Debit",
      "type": "sepadirectdebit"
    },
    {
      "name": "7-Eleven",
      "type": "seveneleven"
    },
    {
      "name": "Premium SMS",
      "type": "sms"
    },
    {
      "name": "SVS",
      "type": "svs"
    },
    {
      "name": "Swish",
      "type": "swish"
    },
    {
      "name": "TCS Test GiftCard",
      "type": "tcstestgiftcard"
    },
    {
      "name": "TenPay",
      "type": "tenpay"
    },
    {
      "name": "The Sting Giftcard",
      "type": "thestinggiftcard"
    },
    {
      "name": "TrueMoney",
      "type": "truemoney"
    },
    {
      "name": "Trustly",
      "type": "trustly"
    },
    {
      "name": "Online Banking by Trustpay",
      "type": "trustpay"
    },
    {
      "name": "TWINT",
      "type": "twint"
    },
    {
      "name": "Ukash",
      "type": "ukash"
    },
    {
      "name": "UnionPay",
      "type": "unionpay"
    },
    {
      "name": "UPI Collect",
      "type": "upi_collect"
    },
    {
      "name": "Valuelink",
      "type": "valuelink"
    },
    {
      "name": "V&D Cadeaukaart",
      "type": "vdcadeaucard"
    },
    {
      "name": "Vipps",
      "type": "vipps"
    },
    {
      "name": "Visa Checkout",
      "type": "visacheckout"
    },
    {
      "name": "VVV Cadeaubon",
      "type": "vvvcadeaubon"
    },
    {
      "name": "VVV Giftcard",
      "type": "vvvgiftcard"
    },
    {
      "name": "Webshop Giftcard",
      "type": "webshopgiftcard"
    },
    {
      "name": "WeChat Pay",
      "type": "wechatpayMiniProgram"
    },
    {
      "name": "WeChat Pay",
      "type": "wechatpayQR"
    },
    {
      "name": "WeChat Pay",
      "type": "wechatpayWeb"
    },
    {
      "name": "WE Fashion Giftcard",
      "type": "wefashiongiftcard"
    },
    {
      "name": "Western Union",
      "type": "westernunion"
    },
    {
      "name": "Winkel Cheque",
      "type": "winkelcheque"
    },
    {
      "name": "WOS Card",
      "type": "woscard"
    },
    {
      "name": "Alfa-Click",
      "type": "yandex_alfaclick"
    },
    {
      "name": "Pay using bank card",
      "type": "yandex_bank_card"
    },
    {
      "name": "Cash terminals",
      "type": "yandex_cash"
    },
    {
      "name": "Pay using installments",
      "type": "yandex_installments"
    },
    {
      "name": "YooMoney",
      "type": "yandex_money"
    },
    {
      "name": "Promsvyazbank",
      "type": "yandex_promsvyazbank"
    },
    {
      "name": "SberPay",
      "type": "yandex_sberbank"
    },
    {
      "name": "WebMoney",
      "type": "yandex_webmoney"
    },
    {
      "name": "Your Gift",
      "type": "yourgift"
    },
    {
      "name": "Zip",
      "type": "zip"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Payments

Sends payment parameters (like amount, country, and currency) together with other required input details collected from the shopper. To know more about required parameters for specific payment methods, refer to our [payment method guides](https://docs.adyen.com/payment-methods).
The response depends on the [payment flow](https://docs.adyen.com/payment-methods#payment-flow):

* For a direct flow, the response includes a `pspReference` and a `resultCode` with the payment result, for example **Authorised** or **Refused**.
* For a redirect or additional action, the response contains an `action` object.

```python
def post_payments(self,
                 idempotency_key=None,
                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`PaymentRequest`](../../doc/models/payment-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`PaymentResponse`](../../doc/models/payment-response.md)

## Example Usage

```python
body = PaymentRequest(
    amount=Amount2(
        currency='USD',
        value=1000
    ),
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    payment_method=ApplePayDetails(
        apple_pay_token='VNRWtuNlNEWkRCSm1xWndjMDFFbktkQU...',
        mtype=Type7Enum.APPLEPAY
    ),
    reference='Your order number',
    return_url='https://your-company.example.com/...'
)

result = payments_api.post_payments(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "resultCode": "IdentifyShopper",
  "action": {
    "paymentData": "Ab02b4c0!BQABAgCuZFJrQOjSsl\\/zt+...",
    "paymentMethodType": "scheme",
    "authorisationToken": "Ab02b4c0!BQABAgAvrX03p...",
    "subtype": "fingerprint",
    "token": "eyJ0aHJlZURTTWV0aG9kTm90aWZpY...",
    "type": "threeDS2"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Payments-Details

Submits details for a payment created using `/payments`. This step is only needed when no final state has been reached on the `/payments` request, for example when the shopper was redirected to another page to complete the payment.

```python
def post_payments_details(self,
                         idempotency_key=None,
                         body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`PaymentDetailsRequest`](../../doc/models/payment-details-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`PaymentDetailsResponse`](../../doc/models/payment-details-response.md)

## Example Usage

```python
body = PaymentDetailsRequest(
    details=PaymentCompletionDetails1(
        redirect_result='X6XtfGC3!Y...'
    )
)

result = payments_api.post_payments_details(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "resultCode": "Authorised",
  "pspReference": "V4HZ4RBFJGXXGN82"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Sessions

Creates a payment session for [Drop-in](https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Drop-in), [Components](https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Components), and [Hosted Checkout](https://docs.adyen.com/online-payments/build-your-integration/sessions-flow/?platform=Web&integration=Hosted+Checkout) integrations.

The response contains encrypted payment session data. The front end then uses the session data to make any required server-side calls for the payment flow.

You get the payment outcome asynchronously, in an [AUTHORISATION](https://docs.adyen.com/api-explorer/#/Webhooks/latest/post/AUTHORISATION) webhook.

```python
def post_sessions(self,
                 idempotency_key=None,
                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`CreateCheckoutSessionRequest`](../../doc/models/create-checkout-session-request.md) | Body, Optional | - |

## Response Type

**201**: Created - the request has been fulfilled and has resulted in one or more new resources being created.

[`CreateCheckoutSessionResponse`](../../doc/models/create-checkout-session-response.md)

## Example Usage

```python
body = CreateCheckoutSessionRequest(
    amount=Amount18(
        currency='EUR',
        value=100
    ),
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    reference='YOUR_PAYMENT_REFERENCE',
    return_url='https://your-company.example.com/checkout?shopperOrder=12xy..',
    country_code='NL'
)

result = payments_api.post_sessions(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "amount": {
    "currency": "EUR",
    "value": 100
  },
  "countryCode": "NL",
  "expiresAt": "2022-01-11T13:53:18+01:00",
  "id": "CS451F2AB1ED897A94",
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "reference": "YOUR_PAYMENT_REFERENCE",
  "returnUrl": "https://your-company.example.com/checkout?shopperOrder=12xy..",
  "sessionData": "Ab02b4c0!BQABAgBfYI29..."
}
```


# Get-Sessions-Session Id

Returns the status of the payment session with the `sessionId` and `sessionResult` specified in the path.

```python
def get_sessions_session_id(self,
                           session_id,
                           session_result)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_id` | `str` | Template, Required | A unique identifier of the session. |
| `session_result` | `str` | Query, Required | The `sessionResult` value from the Drop-in or Component. |

## Response Type

**200**: OK - the request has succeeded.

[`SessionResultResponse`](../../doc/models/session-result-response.md)

## Example Usage

```python
session_id = 'sessionId8'

session_result = 'sessionResult8'

result = payments_api.get_sessions_session_id(
    session_id,
    session_result
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "CS12345678",
  "status": "completed"
}
```


# Post-Authorise

Creates a payment with a unique reference (`pspReference`) and attempts to obtain an authorisation hold. For cards, this amount can be captured or cancelled later. Non-card payment methods typically don't support this and will automatically capture as part of the authorisation.

> This endpoint is [inactive](https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle) and is no longer supported for new integrations.
> 
> * If you are building a new integration, use the Checkout API [`/payments`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments) endpoint instead.
> * If you have an existing integration using this endpoint, reach out to your Adyen contact and [migrate to the Checkout API](https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api).

> The Checkout API enables your [online payments](https://docs.adyen.com/online-payments) integration to accept all supported payment methods, use the latest features, and access more benefits.

```python
def post_authorise(self,
                  body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentRequest1`](../../doc/models/payment-request-1.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`PaymentResult`](../../doc/models/payment-result.md)

## Example Usage

```python
body = PaymentRequest1(
    amount=Amount(
        currency='USD',
        value=1500
    ),
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    reference='YOUR_REFERENCE_NUMBER',
    account_info=AccountInfo(
        account_creation_date=dateutil.parser.parse('2019-01-17T13:42:40+01:00')
    ),
    billing_address=Address(
        city='New York',
        country='US',
        house_number_or_name='37C',
        postal_code='10039',
        street='Redwood Block',
        state_or_province='NY'
    ),
    browser_info=BrowserInfo(
        accept_header='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        color_depth=24,
        java_enabled=False,
        language='en',
        screen_height=723,
        screen_width=1536,
        time_zone_offset=0,
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    ),
    card=Card3(
        cvc='737',
        expiry_month='03',
        expiry_year='2030',
        holder_name='John Smith',
        number='4917610000000000'
    ),
    shopper_email='s.hopper@test.com',
    shopper_ip='192.0.2.1',
    three_ds_2_request_data=ThreeDS2RequestData11(
        device_channel='browser',
        notification_url='https://www.example.com/YOUR_3DS_NOTIFICATION_URL'
    )
)

result = payments_api.post_authorise(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Authorise 3 D

For an authenticated 3D Secure session, completes the payment authorisation. This endpoint must receive the `md` and `paResponse` parameters that you get from the card issuer after a shopper pays via 3D Secure.

> This endpoint is [inactive](https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle) and is no longer supported for new integrations.
> 
> * If you are building a new integration, use the Checkout API [`/payments/details`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/details) endpoint instead.
> * If you have an existing integration using this endpoint, reach out to your Adyen contact and [migrate to the Checkout API](https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api).

> The Checkout API enables your [online payments](https://docs.adyen.com/online-payments) integration to accept all supported payment methods, use the latest features, and access more benefits.

```python
def post_authorise_3_d(self,
                      body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentRequest3d`](../../doc/models/payment-request-3-d.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`PaymentResult`](../../doc/models/payment-result.md)

## Example Usage

```python
body = PaymentRequest3d(
    md='31h..........vOXek7w',
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    pa_response='eNqtmF........wGVA4Ch',
    shopper_ip='61.294.12.12'
)

result = payments_api.post_authorise_3_d(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Authorise 3 Ds 2

For an authenticated 3D Secure 2 session, completes the payment authorisation. This endpoint must receive the `threeDS2Token` and `threeDS2Result` parameters.

> This endpoint is [inactive](https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle) and is no longer supported for new integrations.
> 
> * If you are building a new integration, use the Checkout API [`/payments/details`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/details) endpoint instead.
> * If you have an existing integration using this endpoint, reach out to your Adyen contact and [migrate to the Checkout API](https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api).

> The Checkout API enables your [online payments](https://docs.adyen.com/online-payments) integration to accept all supported payment methods, use the latest features, and access more benefits.

```python
def post_authorise_3_ds_2(self,
                         body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentRequest3ds2`](../../doc/models/payment-request-3-ds-2.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`PaymentResult`](../../doc/models/payment-result.md)

## Example Usage

```python
body = PaymentRequest3ds2(
    amount=Amount(
        currency='EUR',
        value=1000
    ),
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    reference='YOUR_ORDER_NUMBER',
    three_ds_2_request_data=ThreeDS2RequestData11(
        device_channel='app',
        three_ds_comp_ind='Y'
    ),
    three_ds_2_token='— - BINARY DATA - -'
)

result = payments_api.post_authorise_3_ds_2(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Get Authentication Result

Return the authentication result after doing a 3D Secure authentication only.

```python
def post_get_authentication_result(self,
                                  body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AuthenticationResultRequest`](../../doc/models/authentication-result-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`AuthenticationResultResponse`](../../doc/models/authentication-result-response.md)

## Example Usage

```python
body = AuthenticationResultRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    psp_reference='9935272408535455'
)

result = payments_api.post_get_authentication_result(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Retrieve 3 Ds 2 Result

Retrieves the `threeDS2Result` after doing a 3D Secure 2 authentication only.

```python
def post_retrieve_3_ds_2_result(self,
                               body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ThreeDS2ResultRequest`](../../doc/models/three-ds-2-result-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`ThreeDS2ResultResponse`](../../doc/models/three-ds-2-result-response.md)

## Example Usage

```python
body = ThreeDS2ResultRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    psp_reference='9935272408535455'
)

result = payments_api.post_retrieve_3_ds_2_result(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Payments-Cancel

Cancels the payment. Returns a URL for user redirection.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_payments_cancel(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CancelPaymentRequest`](../../doc/models/cancel-payment-request.md) | Body, Required | - |

## Response Type

**200**: OK - The request has succeeded.

[`CancelPaymentResponse`](../../doc/models/cancel-payment-response.md)

## Example Usage

```python
body = CancelPaymentRequest(
    token='TOKEN_PLACEHOLDER'
)

result = payments_api.post_payments_cancel(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "links": {
    "cancel": {
      "href": "https://cancelUrl.com"
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request is malformed or is not the expected format. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Service Error - An unrecoverable error occurred while trying to perform the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Post-Payments-Confirm

Confirms the payment using Strong Customer Authentication (SCA).

    To confirm a payment you must make this request two times:
    
    1. Make this request to initiate SCA and receive the WWW-Authenticate header.
    2. After the user completes the SCA challenge, make this request again, including the updated WWW-Authenticate header.
    
    The second response provides a redirection URL that guides the user to a payment success or failure page.

For more information, see our [documentation](https://docs.adyen.com/business-accounts/send-funds-ideal-integration).

:information_source: **Note** This endpoint does not require authentication.

```python
def post_payments_confirm(self,
                         body,
                         www_authenticate=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ConfirmPaymentRequest`](../../doc/models/confirm-payment-request.md) | Body, Required | - |
| `www_authenticate` | `str` | Header, Optional | Header for authenticating through SCA: Contains information for an SCA challenge for A2A payments. |

## Response Type

**200**: OK - The request has succeeded.

[`ConfirmPaymentResponse`](../../doc/models/confirm-payment-response.md)

## Example Usage

```python
body = ConfirmPaymentRequest(
    balance_account_id='BA00000000000000000000000',
    token='TOKEN_PLACEHOLDER'
)

result = payments_api.post_payments_confirm(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "links": {
    "success": {
      "href": "https://successUrl.com"
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request is malformed or is not the expected format. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - The API credential used in the request is invalid or does not have the right permissions. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Service Error - An unrecoverable error occurred while trying to perform the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Post-Payments-Details 1

Returns the details of an open payment, which you must show to the user. Also provides a token required to [confirm](https://docs.adyen.com/api-explorer/a2a-payments/latest/post/payments/confirm) or [cancel](https://docs.adyen.com/api-explorer/a2a-payments/latest/post/payments/cancel) the payment.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_payments_details_1(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`IdealPaymentDetailsRequest`](../../doc/models/ideal-payment-details-request.md) | Body, Required | - |

## Response Type

**200**: OK - The request has succeeded.

[`PaymentDetailsResponse1`](../../doc/models/payment-details-response-1.md)

## Example Usage

```python
body = IdealPaymentDetailsRequest(
    payload='https://ext.tx.ideal.nl/2/AXE4R72TLPRCRN6Y4FDZX7MZHJQ?sig=BGBCQEIIA2F3CF7KR2SVLSJEDUJABL62V7TI4Y2LJPJIJBZEP6HXCHXPQCLTAEIB2FNUD3COVRNIT27TT7NFKYD5UJCUY4NMPS4NUCTKA6KIBHSRXWI',
    source=PaymentSource2Enum.REDIRECT,
    method='ideal'
)

result = payments_api.post_payments_details_1(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "details": {
    "amount": {
      "currency": "EUR",
      "value": 200
    },
    "counterparty": {
      "accountHolder": {
        "fullName": "Test company"
      },
      "accountIdentification": {
        "iban": "NL29ADYX0000000000",
        "type": "iban"
      }
    },
    "description": "MyStoreDemo-Donation-1754056596388",
    "expiresAt": "2025-08-01T14:16:42.887Z"
  },
  "token": "TOKEN_PLACEHOLDER"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - The request is malformed or is not the expected format. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Service Error - An unrecoverable error occurred while trying to perform the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

