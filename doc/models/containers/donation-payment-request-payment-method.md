
# Donation Payment Request Payment Method

## Data Type

`ApplePayDonations | CardDonations | GooglePayDonations | IdealDonations | PayWithGoogleDonations | StoredPaymentMethod1`

## Cases

| Type |
|  --- |
| [`ApplePayDonations`](../../../doc/models/apple-pay-donations.md) |
| [`CardDonations`](../../../doc/models/card-donations.md) |
| [`GooglePayDonations`](../../../doc/models/google-pay-donations.md) |
| [`IdealDonations`](../../../doc/models/ideal-donations.md) |
| [`PayWithGoogleDonations`](../../../doc/models/pay-with-google-donations.md) |
| [`StoredPaymentMethod1`](../../../doc/models/stored-payment-method-1.md) |

## ApplePayDonations

### Initialization Code

#### Example

```python
value = ApplePayDonations(
    apple_pay_token='applePayToken4',
    mtype=Type7Enum.APPLEPAY
)
```

## CardDonations

### Initialization Code

#### Example

```python
value = CardDonations(
    mtype=Type14Enum.SCHEME
)
```

## GooglePayDonations

### Initialization Code

#### Example

```python
value = GooglePayDonations(
    google_pay_token='googlePayToken0',
    mtype=Type24Enum.GOOGLEPAY
)
```

## IdealDonations

### Initialization Code

#### Example

```python
value = IdealDonations(
    mtype=Type25Enum.IDEAL
)
```

## PayWithGoogleDonations

### Initialization Code

#### Example

```python
value = PayWithGoogleDonations(
    google_pay_token='googlePayToken2',
    mtype=Type26Enum.PAYWITHGOOGLE
)
```

## StoredPaymentMethod1

### Initialization Code

#### Example

```python
value = StoredPaymentMethod1(
    mtype=Type27Enum.SEPADIRECTDEBIT
)
```

