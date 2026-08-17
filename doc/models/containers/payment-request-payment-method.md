
# Payment Request Payment Method

## Data Type

`ACHDirectDebit | Affirm | Afterpay | Alma | AmazonPay | ANCV | AndroidPay | ApplePayDetails | AuPay | BACSDirectDebit | BillDesk | BLIK | CardDetails | StoredPaymentMethod | Cellulant | DBarai | DirectDebitAu | Doku | Dragonpay | EBankingFinland | Voucher | EFTDirectDebit | DetailsOfTokensThatAreNotStoredWithAdyen | Fastlane | StoredPaymentMethod2 | GooglePayDetails | IdealDetails | Klarna | KlarnaNetwork | Masterpass | MBWay | MobilePay | MOLPay | OpenInvoice | PayByBankAISDirectDebit | PayByBank | PayPal | PayPay | PayTo | PayU | PayWithGoogleDetails | PaymentDetails | StoredPaymentMethod4 | StoredPaymentMethod5 | PSELatam | RakutenPay | Ratepay | Riverty | SamsungPay | SEPADirectDebit | StoredPaymentMethod6 | Twint | UPICollect | UPIIntent | UPIQR | Vipps | VisaCheckout | WeChatPay | WeChatPayMiniProgram | Zip`

## Cases

| Type |
|  --- |
| [`ACHDirectDebit`](../../../doc/models/ach-direct-debit.md) |
| [`Affirm`](../../../doc/models/affirm.md) |
| [`Afterpay`](../../../doc/models/afterpay.md) |
| [`Alma`](../../../doc/models/alma.md) |
| [`AmazonPay`](../../../doc/models/amazon-pay.md) |
| [`ANCV`](../../../doc/models/ancv.md) |
| [`AndroidPay`](../../../doc/models/android-pay.md) |
| [`ApplePayDetails`](../../../doc/models/apple-pay-details.md) |
| [`AuPay`](../../../doc/models/au-pay.md) |
| [`BACSDirectDebit`](../../../doc/models/bacs-direct-debit.md) |
| [`BillDesk`](../../../doc/models/bill-desk.md) |
| [`BLIK`](../../../doc/models/blik.md) |
| [`CardDetails`](../../../doc/models/card-details.md) |
| [`StoredPaymentMethod`](../../../doc/models/stored-payment-method.md) |
| [`Cellulant`](../../../doc/models/cellulant.md) |
| [`DBarai`](../../../doc/models/d-barai.md) |
| [`DirectDebitAu`](../../../doc/models/direct-debit-au.md) |
| [`Doku`](../../../doc/models/doku.md) |
| [`Dragonpay`](../../../doc/models/dragonpay.md) |
| [`EBankingFinland`](../../../doc/models/e-banking-finland.md) |
| [`Voucher`](../../../doc/models/voucher.md) |
| [`EFTDirectDebit`](../../../doc/models/eft-direct-debit.md) |
| [`DetailsOfTokensThatAreNotStoredWithAdyen`](../../../doc/models/details-of-tokens-that-are-not-stored-with-adyen.md) |
| [`Fastlane`](../../../doc/models/fastlane.md) |
| [`StoredPaymentMethod2`](../../../doc/models/stored-payment-method-2.md) |
| [`GooglePayDetails`](../../../doc/models/google-pay-details.md) |
| [`IdealDetails`](../../../doc/models/ideal-details.md) |
| [`Klarna`](../../../doc/models/klarna.md) |
| [`KlarnaNetwork`](../../../doc/models/klarna-network.md) |
| [`Masterpass`](../../../doc/models/masterpass.md) |
| [`MBWay`](../../../doc/models/mb-way.md) |
| [`MobilePay`](../../../doc/models/mobile-pay.md) |
| [`MOLPay`](../../../doc/models/mol-pay.md) |
| [`OpenInvoice`](../../../doc/models/open-invoice.md) |
| [`PayByBankAISDirectDebit`](../../../doc/models/pay-by-bank-ais-direct-debit.md) |
| [`PayByBank`](../../../doc/models/pay-by-bank.md) |
| [`PayPal`](../../../doc/models/pay-pal.md) |
| [`PayPay`](../../../doc/models/pay-pay.md) |
| [`PayTo`](../../../doc/models/pay-to.md) |
| [`PayU`](../../../doc/models/pay-u.md) |
| [`PayWithGoogleDetails`](../../../doc/models/pay-with-google-details.md) |
| [`PaymentDetails`](../../../doc/models/payment-details.md) |
| [`StoredPaymentMethod4`](../../../doc/models/stored-payment-method-4.md) |
| [`StoredPaymentMethod5`](../../../doc/models/stored-payment-method-5.md) |
| [`PSELatam`](../../../doc/models/pse-latam.md) |
| [`RakutenPay`](../../../doc/models/rakuten-pay.md) |
| [`Ratepay`](../../../doc/models/ratepay.md) |
| [`Riverty`](../../../doc/models/riverty.md) |
| [`SamsungPay`](../../../doc/models/samsung-pay.md) |
| [`SEPADirectDebit`](../../../doc/models/sepa-direct-debit.md) |
| [`StoredPaymentMethod6`](../../../doc/models/stored-payment-method-6.md) |
| [`Twint`](../../../doc/models/twint.md) |
| [`UPICollect`](../../../doc/models/upi-collect.md) |
| [`UPIIntent`](../../../doc/models/upi-intent.md) |
| [`UPIQR`](../../../doc/models/upiqr.md) |
| [`Vipps`](../../../doc/models/vipps.md) |
| [`VisaCheckout`](../../../doc/models/visa-checkout.md) |
| [`WeChatPay`](../../../doc/models/we-chat-pay.md) |
| [`WeChatPayMiniProgram`](../../../doc/models/we-chat-pay-mini-program.md) |
| [`Zip`](../../../doc/models/zip.md) |

## ACHDirectDebit

### Initialization Code

#### Example

```python
value = ACHDirectDebit(
    mtype=TypeEnum.ACH
)
```

## Affirm

### Initialization Code

#### Example

```python
value = Affirm(
    mtype=Type1Enum.AFFIRM
)
```

## Afterpay

### Initialization Code

#### Example

```python
value = Afterpay(
    mtype=Type2Enum.AFTERPAY_DEFAULT
)
```

## Alma

### Initialization Code

#### Example

```python
value = Alma()
```

## AmazonPay

### Initialization Code

#### Example

```python
value = AmazonPay(
    mtype=Type4Enum.AMAZONPAY
)
```

## ANCV

### Initialization Code

#### Example

```python
value = ANCV()
```

## AndroidPay

### Initialization Code

#### Example

```python
value = AndroidPay(
    mtype=Type6Enum.ANDROIDPAY
)
```

## ApplePayDetails

### Initialization Code

#### Example

```python
value = ApplePayDetails(
    apple_pay_token='applePayToken0',
    mtype=Type7Enum.APPLEPAY
)
```

## AuPay

### Initialization Code

#### Example

```python
value = AuPay(
    mtype=Type9Enum.AUPAY
)
```

## BACSDirectDebit

### Initialization Code

#### Example

```python
value = BACSDirectDebit(
    mtype=Type10Enum.DIRECTDEBIT_GB
)
```

## BillDesk

### Initialization Code

#### Example

```python
value = BillDesk(
    issuer='issuer0',
    mtype=Type12Enum.BILLDESK_ONLINE
)
```

## BLIK

### Initialization Code

#### Example

```python
value = BLIK()
```

## CardDetails

### Initialization Code

#### Example

```python
value = CardDetails(
    mtype=Type14Enum.SCHEME
)
```

## StoredPaymentMethod

### Initialization Code

#### Example

```python
value = StoredPaymentMethod(
    mtype=Type16Enum.CASHAPP
)
```

## Cellulant

### Initialization Code

#### Example

```python
value = Cellulant(
    mtype=Type17Enum.CELLULANT
)
```

## DBarai

### Initialization Code

#### Example

```python
value = DBarai(
    mtype=Type20Enum.DBARAI
)
```

## DirectDebitAu

### Initialization Code

#### Example

```python
value = DirectDebitAu(
    holder_name='holderName0',
    mtype=Type22Enum.DIRECTDEBIT_AU
)
```

## Doku

### Initialization Code

#### Example

```python
value = Doku(
    first_name='firstName6',
    last_name='lastName2',
    shopper_email='shopperEmail8',
    mtype=Type23Enum.DOKU_BNI_VA
)
```

## Dragonpay

### Initialization Code

#### Example

```python
value = Dragonpay(
    issuer='issuer2',
    mtype=Type28Enum.DRAGONPAY_OTC_NON_BANKING
)
```

## EBankingFinland

### Initialization Code

#### Example

```python
value = EBankingFinland()
```

## Voucher

### Initialization Code

#### Example

```python
value = Voucher(
    first_name='firstName6',
    last_name='lastName2',
    shopper_email='shopperEmail2',
    telephone_number='telephoneNumber0',
    mtype=Type29Enum.ECONTEXT_STORES
)
```

## EFTDirectDebit

### Initialization Code

#### Example

```python
value = EFTDirectDebit(
    mtype=Type30Enum.EFT_DIRECTDEBIT_CA
)
```

## DetailsOfTokensThatAreNotStoredWithAdyen

### Initialization Code

#### Example

```python
value = DetailsOfTokensThatAreNotStoredWithAdyen(
    stored_payment_method_id='storedPaymentMethodId8'
)
```

## Fastlane

### Initialization Code

#### Example

```python
value = Fastlane(
    fastlane_data='fastlaneData2'
)
```

## StoredPaymentMethod2

### Initialization Code

#### Example

```python
value = StoredPaymentMethod2(
    issuer='issuer4',
    mtype=Type31Enum.EPS
)
```

## GooglePayDetails

### Initialization Code

#### Example

```python
value = GooglePayDetails(
    google_pay_token='googlePayToken8',
    mtype=Type24Enum.GOOGLEPAY
)
```

## IdealDetails

### Initialization Code

#### Example

```python
value = IdealDetails(
    mtype=Type25Enum.IDEAL
)
```

## Klarna

### Initialization Code

#### Example

```python
value = Klarna(
    mtype=Type34Enum.KLARNA
)
```

## KlarnaNetwork

### Initialization Code

#### Example

```python
value = KlarnaNetwork()
```

## Masterpass

### Initialization Code

#### Example

```python
value = Masterpass(
    masterpass_transaction_id='masterpassTransactionId0',
    mtype=Type35Enum.MASTERPASS
)
```

## MBWay

### Initialization Code

#### Example

```python
value = MBWay(
    shopper_email='shopperEmail4',
    telephone_number='telephoneNumber4',
    mtype=Type36Enum.MBWAY
)
```

## MobilePay

### Initialization Code

#### Example

```python
value = MobilePay(
    mtype=Type37Enum.MOBILEPAY
)
```

## MOLPay

### Initialization Code

#### Example

```python
value = MOLPay(
    issuer='issuer0',
    mtype=Type38Enum.MOLPAY_EBANKING_FPX_MY
)
```

## OpenInvoice

### Initialization Code

#### Example

```python
value = OpenInvoice(
    mtype=Type39Enum.OPENINVOICE
)
```

## PayByBankAISDirectDebit

### Initialization Code

#### Example

```python
value = PayByBankAISDirectDebit()
```

## PayByBank

### Initialization Code

#### Example

```python
value = PayByBank()
```

## PayPal

### Initialization Code

#### Example

```python
value = PayPal()
```

## PayPay

### Initialization Code

#### Example

```python
value = PayPay(
    mtype=Type40Enum.PAYPAY
)
```

## PayTo

### Initialization Code

#### Example

```python
value = PayTo(
    mtype=Type41Enum.PAYTO
)
```

## PayU

### Initialization Code

#### Example

```python
value = PayU()
```

## PayWithGoogleDetails

### Initialization Code

#### Example

```python
value = PayWithGoogleDetails(
    google_pay_token='googlePayToken0',
    mtype=Type26Enum.PAYWITHGOOGLE
)
```

## PaymentDetails

### Initialization Code

#### Example

```python
value = PaymentDetails()
```

## StoredPaymentMethod4

### Initialization Code

#### Example

```python
value = StoredPaymentMethod4()
```

## StoredPaymentMethod5

### Initialization Code

#### Example

```python
value = StoredPaymentMethod5(
    mtype=Type45Enum.PAYBYBANK_PIX
)
```

## PSELatam

### Initialization Code

#### Example

```python
value = PSELatam(
    bank='bank4',
    client_type='clientType4',
    identification='identification4',
    identification_type='identificationType8'
)
```

## RakutenPay

### Initialization Code

#### Example

```python
value = RakutenPay(
    mtype=Type47Enum.RAKUTENPAY
)
```

## Ratepay

### Initialization Code

#### Example

```python
value = Ratepay(
    mtype=Type48Enum.RATEPAY
)
```

## Riverty

### Initialization Code

#### Example

```python
value = Riverty(
    mtype=Type49Enum.RIVERTY
)
```

## SamsungPay

### Initialization Code

#### Example

```python
value = SamsungPay(
    samsung_pay_token='samsungPayToken6',
    mtype=Type50Enum.SAMSUNGPAY
)
```

## SEPADirectDebit

### Initialization Code

#### Example

```python
value = SEPADirectDebit(
    iban='iban4',
    owner_name='ownerName4',
    mtype=Type51Enum.SEPADIRECTDEBIT
)
```

## StoredPaymentMethod6

### Initialization Code

#### Example

```python
value = StoredPaymentMethod6()
```

## Twint

### Initialization Code

#### Example

```python
value = Twint()
```

## UPICollect

### Initialization Code

#### Example

```python
value = UPICollect()
```

## UPIIntent

### Initialization Code

#### Example

```python
value = UPIIntent()
```

## UPIQR

### Initialization Code

#### Example

```python
value = UPIQR()
```

## Vipps

### Initialization Code

#### Example

```python
value = Vipps(
    telephone_number='telephoneNumber0',
    mtype=Type54Enum.VIPPS
)
```

## VisaCheckout

### Initialization Code

#### Example

```python
value = VisaCheckout(
    visa_checkout_call_id='visaCheckoutCallId0',
    mtype=Type55Enum.VISACHECKOUT
)
```

## WeChatPay

### Initialization Code

#### Example

```python
value = WeChatPay(
    mtype=Type56Enum.WECHATPAY
)
```

## WeChatPayMiniProgram

### Initialization Code

#### Example

```python
value = WeChatPayMiniProgram(
    mtype=Type57Enum.WECHATPAYMINIPROGRAM
)
```

## Zip

### Initialization Code

#### Example

```python
value = Zip(
    mtype=Type58Enum.ZIP
)
```

