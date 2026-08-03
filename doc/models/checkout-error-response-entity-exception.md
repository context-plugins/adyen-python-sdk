
# Checkout Error Response Entity Exception

*This model accepts additional fields of type Any.*

## Structure

`CheckoutErrorResponseEntityException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Required | - |
| `error_type` | `str` | Required | - |
| `message` | `str` | Required | - |
| `psp_reference` | `str` | Optional | - |
| `status` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except CheckoutErrorResponseEntityException as e:
    print(e)
except ApiException as e:
    print(e)
```

