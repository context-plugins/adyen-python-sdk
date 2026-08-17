
# Transfer Category Data

## Data Type

`BankCategoryData | InternalCategoryData | IssuedCard | PlatformPayment`

## Cases

| Type |
|  --- |
| [`BankCategoryData`](../../../doc/models/bank-category-data.md) |
| [`InternalCategoryData`](../../../doc/models/internal-category-data.md) |
| [`IssuedCard`](../../../doc/models/issued-card.md) |
| [`PlatformPayment`](../../../doc/models/platform-payment.md) |

## BankCategoryData

### Initialization Code

#### Example

```python
value = BankCategoryData(
    mtype=Type310Enum.BANK
)
```

## InternalCategoryData

### Initialization Code

#### Example

```python
value = InternalCategoryData(
    mtype=Type411Enum.INTERNAL
)
```

## IssuedCard

### Initialization Code

#### Example

```python
value = IssuedCard(
    mtype=Type511Enum.ISSUEDCARD
)
```

## PlatformPayment

### Initialization Code

#### Example

```python
value = PlatformPayment(
    mtype=Type63Enum.PLATFORMPAYMENT
)
```

