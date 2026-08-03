
# Transfer Data Tracking

## Data Type

`ConfirmationTrackingData | EstimationTrackingData | InternalReviewTrackingData`

## Cases

| Type |
|  --- |
| [`ConfirmationTrackingData`](../../../doc/models/confirmation-tracking-data.md) |
| [`EstimationTrackingData`](../../../doc/models/estimation-tracking-data.md) |
| [`InternalReviewTrackingData`](../../../doc/models/internal-review-tracking-data.md) |

## ConfirmationTrackingData

### Initialization Code

#### Example

```python
value = ConfirmationTrackingData(
    status=Status110.CREDITED,
    mtype=Type834.CONFIRMATION
)
```

## EstimationTrackingData

### Initialization Code

#### Example

```python
value = EstimationTrackingData(
    estimated_arrival_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    mtype=Type84.ESTIMATION
)
```

## InternalReviewTrackingData

### Initialization Code

#### Example

```python
value = InternalReviewTrackingData(
    status=Status44.PENDING,
    mtype=Type90.INTERNALREVIEW
)
```

