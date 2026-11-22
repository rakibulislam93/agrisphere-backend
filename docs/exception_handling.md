
# Exception Handling

## Purpose
Use common exceptions to keep API error responses consistent.

## Available Exceptions

| Exception | When to use |
|---|---|
| `BadRequestException` | The request is invalid. |
| `UnauthorizedException` | The user is not authenticated. |
| `ForbiddenException` | The user does not have permission. |
| `NotFoundException` | The requested resource does not exist. |
| `ConflictException` | The request conflicts with existing data. |
| `ValidationException` | Custom business validation fails. |

## Serializer Validation

Use DRF's built-in `serializers.ValidationError` for serializer validation.

```python
raise serializers.ValidationError({
    "name": "This field is required."
})
```

Do not use custom `ValidationException` for normal serializer validation.

## Guidelines

- Use the correct exception for each situation.
- Keep error messages short and clear.
- Never expose sensitive information.
- Use meaningful and unique error codes.
- Do not use exceptions for normal program flow.
- Add documentation when creating a new exception.

## Important

Use DRF authentication and permission classes for normal authentication and permission checks.

**Location:** `common/exceptions/`
