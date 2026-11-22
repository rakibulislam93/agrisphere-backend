
# User and Profile Architecture

## 1. Purpose

AgriSphere will support different types of users.

A user can be a Farmer, Shopkeeper, Dealer, Buyer, or other types in the future.

The system should allow new user types without changing the main User Model.

## 2. Main Decision

We will use one common `CustomUser` model for all users.

The `CustomUser` model will handle:

- User registration
- Login and authentication
- Common user information
- Account status

We will not use a single `user_type` field because one user can have multiple identities.

## 3. Profile System

Each user type will have a separate Profile Model.

Examples:

- `FarmerProfile`
- `ShopkeeperProfile`
- `DealerProfile`
- `BuyerProfile`

Each Profile Model will have a `OneToOneField` relationship with `CustomUser`.

A user can have multiple different profiles.

Example:

Rahim can have:

- One CustomUser account
- One FarmerProfile
- One ShopkeeperProfile

He will use the same account for both.

## 4. Adding New User Types

When we need a new user type:

1. Create a new Django app if needed.
2. Create its Profile Model.
3. Connect it to `CustomUser`.
4. Add its own API and business logic.

We should not need to change the existing CustomUser model.

## 5. Important Rules

- Keep authentication inside the `accounts` app.
- Keep user-specific information inside the relevant Profile Model.
- Do not add separate login systems for different user types.
- Do not use multiple Boolean fields like `is_farmer` or `is_shopkeeper`.
- Keep each module's business logic separate.
- Create profiles only when the user needs that type of functionality.

## 6. Future Considerations

If users need to share data or manage the same business together, we may need a separate ownership or access-management system.

This is not part of the current design.

## 7. Current Architecture

- CustomUser: Common user account.
- FarmerProfile: Farmer information.
- ShopkeeperProfile: Shopkeeper information.
- Other profiles: Added when needed.

**Decision:** One User Account + Multiple Profile Types.
