# API Documentation

### APIs

1. [Login](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#1-login)
2. [Logout](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#2-logout)
3. [Change Password](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#3-change-password)
4. [Food List for Canteen Manager](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#3-food-list-for-canteen-manager)

### Authentication
```
Header -

Authorization: Token <token>
```

Authentication Error Messages
```
{
  "detail": "Authentication credentials were not provided."
}

[
  "Invalid token."
]
```

## 1. Login

**POST** - `api/mobile/login/`
```
*username
*password
```
Sample Success Response - 

```
{
  "result": true,
  "msg": "Logged In Succesfully",
  "data": {
    "auth_token": "x8s1lo39jeyi1yx",
    "username": "admin",
    "name": "None None",
    "type": "ADMIN"
  }
}
```
Sample Error Response - 

```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "Invalid Username or Password"
  ]
}

{
  "result": false,
  "msg": "ERROR",
  "data": [
    "PASSWORD: This field is required."
  ]
}
```

---

## 2. Logout

**POST** - `api/mobile/logout/`

(authentication Required)

Sample Success Response - 

```
{
  "result": true,
  "msg": "Logged Out Succesfully",
  "data": {}
}
```
Sample Error Response - 

```
[
  "Invalid token."
]
```

---

## 3. Change Password

**POST** - `api/mobile/change-password/`

(authentication Required)
```
*new_password
*confirm_password
```
Sample Success Response - 

```
{
  "result": true,
  "msg": "Password changed successfully",
  "data": {}
}
```
Sample Error Response - 

```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "NEW_PASSWORD: This field is required.",
    "CONFIRM_PASSWORD: This field is required."
  ]
}
```

---
## 4. Food List for Canteen Manager

**GET** - `api/mobile/canteen/food/list/`

(authentication Required)

Sample Success Response - 

```
{
  "result": true,
  "msg": "SUCCESS",
  "data": [
    {
      "id": 1,
      "name": "Paneer Tikka",
      "price": "1",
      "quantity": 100,
      "is_approved": true,
      "approved_by": "Teacher 1",
      "is_todays_special": true
    },
    {
      "id": 2,
      "name": "Masala Dosa",
      "price": "1",
      "quantity": 100,
      "is_approved": false,
      "approved_by": "",
      "is_todays_special": false
    },
    {
      "id": 3,
      "name": "Chicken Tikka",
      "price": "1",
      "quantity": 100,
      "is_approved": false,
      "approved_by": "",
      "is_todays_special": false
    },
    {
      "id": 4,
      "name": "Chicken Biryani",
      "price": "1",
      "quantity": 100,
      "is_approved": true,
      "approved_by": "Teacher 1",
      "is_todays_special": false
    },
    {
      "id": 5,
      "name": "Chicken 65",
      "price": "1",
      "quantity": 100,
      "is_approved": false,
      "approved_by": "",
      "is_todays_special": false
    }
  ]
}
```
Sample Error Response - 

```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "You Should be a CANTEEN MANAGER to access this API"
  ]
}
```

---