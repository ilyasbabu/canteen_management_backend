# API Documentation

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
