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