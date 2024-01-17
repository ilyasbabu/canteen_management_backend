# API Documentation

### Authentication
```
Header -

Authorization: Token <token>
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
Sample Error Responses - 

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

## 2. Change Password

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
Sample Error Responses - 

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
## 3. Food List for Canteen Manager

**POST** - `api/mobile/canteen/food/list/`

(authentication Required)
```
*new_password
*confirm_password
```
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
Sample Error Responses - 

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