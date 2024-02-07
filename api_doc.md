# API Documentation

### APIs

1. [Login](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#1-login)
2. [Logout](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#2-logout)
3. [Change Password](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#3-change-password)
4. [Food List for Canteen Manager](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#4-food-list-for-canteen-manager)
5. [Food Category Dropdown](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#5-food-category-dropdown)
6. [Food Create](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#6-food-create)
7. [Food Details for Canteen Manager](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#7-food-details-for-canteen-manager)
8. [Food Update for Canteen Manager](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#8-food-update-for-canteen-manager)
9. [Food Delete for Canteen Manager](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#9-food-delete-for-canteen-manager)
10. [Food List for Teacher](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#10-food-list-for-teacher)
11. [Food Detail for Teacher](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#11-food-detail-for-teacher)
12. [Food Approve](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#12-food-approve)
13. [Food Mark as todays Special](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#13-food-mark-as-todays-special)
14. [Food List for Student](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#14-food-list-for-student)
15. [Department Dropdown](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#15-department-dropdown)
16. [Student Register](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#16-student-register)
17. [Place Order](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#17-place-order)
18. [Order List For Student](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#18-order-list-for-student)
19. [Order Detail For Student](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#19-order-detail-for-student)
20. [Order Status Dropdown](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#20-order-status-dropdown)
21. [Order Status Change](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#21-order-status-change)
22. [Order List for Manager](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#22-order-list-for-manger)
23. [Order Detail for Manager](https://github.com/ilyasbabu/canteen_management_backend/blob/master/api_doc.md#23-order-detail-for-manger)


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

authentication Required (Manager, Student, Teacher)

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

authentication Required (Manager, Student, Teacher)
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

authentication Required (Manager)

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

## 5. Food Category Dropdown

**GET** - `api/mobile/canteen/food/category/dropdown/`

authentication Required (Manager, Student, Teacher)

Sample Success Response - 
```
{
  "result": true,
  "msg": "SUCCESS",
  "data": [
    {
      "id": 1,
      "name": "Vegetarian"
    },
    {
      "id": 2,
      "name": "Non-Vegetarian"
    },
    {
      "id": 3,
      "name": "Dessert"
    },
    {
      "id": 4,
      "name": "Snacks"
    },
    {
      "id": 5,
      "name": "Drinks"
    }
  ]
}
```

---

## 6. Food Create

**POST** - `api/mobile/canteen/food/create/`

authentication Required (Manager)
```
*name
*quantity
*price
*category_id
image
```
Sample Success Response - 

```
{
  "result": true,
  "msg": "Food Created Successfully",
  "data": {}
}
```
Sample Error Response - 

```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "Invalid Food Category"
  ]
}
```

---

## 7. Food Details For Canteen Manager

**GET** - `api/mobile/canteen/food/detail/[food_id]/`

authentication Required (Manager)

Sample Success Response - 

```
{
  "result": true,
  "msg": "SUCCESS",
  "data": {
    "id": 1,
    "name": "Paneer Tikka",
    "price": "50",
    "quantity": 100,
    "is_approved": true,
    "is_todays_special": true,
    "category_id": 1,
    "approved_by_id": 1,
    "image_url": "https://res.cloudinary.com/do6mh6z0s/image/upload/v1707292467/canteen_management/t5jrdentco4iztmlf67t.jpg",
    "category_name": "Vegetarian",
    "approved_by_name": "Teacher 1"
  }
}
```
Sample Error Response - 

```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "Invalid Food"
  ]
}
```

---

## 8. Food Update For Canteen Manager

**POST** - `api/mobile/canteen/food/update/[food_id]/`

authentication Required (Manager)
```
*name
*quantity
*price
*category_id
image
```
Sample Success Response - 
```
{
  "result": true,
  "msg": "Food Updated Successfully",
  "data": {}
}
```
Sample Error Response - 
```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "Invalid Food"
  ]
}
```

---

## 9. Food Delete For Canteen Manager

**POST** - `api/mobile/canteen/food/delete/[food_id]/`

authentication Required (Manager)

Sample Success Response - 
```
{
  "result": true,
  "msg": "Food Deleted Successfully",
  "data": {}
}
```
Sample Error Response - 
```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "Invalid Food"
  ]
}
```

---

## 10. Food List for Teacher

**GET** - `api/mobile/teacher/food/list/`

authentication Required (Teacher)

Sample Success Response - 

```
{
  "result": true,
  "msg": "SUCCESS",
  "data": [
    {
      "id": 5,
      "name": "Chicken 65",
      "price": "50",
      "quantity": 100,
      "image_url": "https://res.cloudinary.com/do6mh6z0s/image/upload/v1707292467/canteen_management/t5jrdentco4iztmlf67t.jpg",
      "is_approved": false
    },
    {
      "id": 4,
      "name": "Chicken Biryani",
      "price": "50",
      "quantity": 100,
      "image_url": "https://res.cloudinary.com/do6mh6z0s/image/upload/v1707292467/canteen_management/t5jrdentco4iztmlf67t.jpg",
      "is_approved": true
    },
    {
      "id": 3,
      "name": "Chicken Tikka",
      "price": "50",
      "quantity": 100,
      "image_url": null,
      "is_approved": false
    },
    {
      "id": 2,
      "name": "Masala Dosa",
      "price": "50",
      "quantity": 100,
      "image_url": "https://res.cloudinary.com/do6mh6z0s/image/upload/v1707292467/canteen_management/t5jrdentco4iztmlf67t.jpg",
      "is_approved": false
    },
    {
      "id": 1,
      "name": "Paneer Tikka",
      "price": "50",
      "quantity": 100,
      "image_url": null,
      "is_approved": true
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
    "You Should be a TEACHER to access this API"
  ]
}
```
---

## 11. Food Detail for Teacher

**GET** - `api/mobile/teacher/food/detail/[food_id]`

authentication Required (Teacher)

Sample Success Response - 

```
{
  "result": true,
  "msg": "SUCCESS",
  "data": {
    "id": 2,
    "name": "Masala Dosa",
    "price": "50",
    "quantity": 100,
    "is_approved": false,
    "category_id": 1,
    "category_name": "Vegetarian",
    "image_url": "https://res.cloudinary.com/do6mh6z0s/image/upload/v1707292467/canteen_management/t5jrdentco4iztmlf67t.jpg"
  }
}
```
Sample Error Response - 

```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "You Should be a TEACHER to access this API"
  ]
}
```
---

## 12. Food Approve

**POST** - `api/mobile/teacher/food/approve/[food_id]`

authentication Required (Teacher)

Sample Success Response - 

```
{
  "result": true,
  "msg": "Food Approved Successfully",
  "data": {}
}
```
Sample Error Response - 

```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "Food already approved"
  ]
}
```
---

## 13. Food Mark as Todays Special

**POST** - `api/mobile/canteen/food/mark-as-todays-special/[food_id]/`

authentication Required (Manager)

Sample Success Response - 

```
{
  "result": true,
  "msg": "Food Marked as Todays Special 🎉",
  "data": {}
}
```
Sample Error Response - 

```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "Food already marked as todays special"
  ]
}
```
---


## 14. Food List for Student

**POST** - `api/mobile/student/food/list/`

authentication Required (Student)

Sample Success Response - 

```
{
  "result": true,
  "msg": "SUCCESS",
  "data": [
    {
      "id": 15,
      "name": "Mango Juice",
      "price": "50",
      "quantity": 100,
      "category": "Drinks",
      "image_url": "https://res.cloudinary.com/do6mh6z0s/image/upload/v1707292467/canteen_management/t5jrdentco4iztmlf67t.jpg",
      "is_todays_special": false
    },
    {
      "id": 9,
      "name": "Chicken Sandwich",
      "price": "50",
      "quantity": 100,
      "category": "Snacks",
      "image_url": "https://res.cloudinary.com/do6mh6z0s/image/upload/v1707292467/canteen_management/t5jrdentco4iztmlf67t.jpg",
      "is_todays_special": false
    },
    {
      "id": 8,
      "name": "Chicken Roll",
      "price": "50",
      "quantity": 100,
      "category": "Drinks",
      "image_url": "https://res.cloudinary.com/do6mh6z0s/image/upload/v1707292467/canteen_management/t5jrdentco4iztmlf67t.jpg",
      "is_todays_special": false
    }
  ]
}
```

---


## 15. Department Dropdown

**GET** - `api/mobile/student/department/dropdown/`

Sample Success Response - 

```
{
  "result": true,
  "msg": "SUCCESS",
  "data": [
    {
      "value": "COMPUTER_SCIENCE",
      "text": "Computer Science"
    },
    {
      "value": "COMMERCE",
      "text": "Commerce"
    },
    {
      "value": "HOTEL_MANAGEMENT",
      "text": "Hotel Management"
    },
    {
      "value": "ENGLISH",
      "text": "English"
    },
    {
      "value": "ECONOMICS",
      "text": "Economics"
    }
  ]
}
```
---

## 16. Student Register

**POST** - `api/mobile/student/register/`
```
*mobile
*name
*password
*confirm_password
*department
```
Sample Success Response - 

```
{
  "result": true,
  "msg": "Registered Successfully!",
  "data": null
}
```
Sample Error Response - 

```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "Password and Confirm Password must be same"
  ]
}
```
---

## 17. Place Order

**POST** - `api/mobile/student/order/`

authentication Required (Student)

```
*products (list of dictionaries, ex - [{"id":1,"quantity":2},{"id":5,"quantity":1}])
*delivery_time (ex - "Jan 31 2023 18:50:00")
```
Sample Success Response - 

```
{
  "result": true,
  "msg": "Order Placed Succesfully",
  "data": null
}
```
Sample Error Response - 

```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "No enough Quantity for Paneer Tikka"
  ]
}
```
---


## 18. Order List for student

**GET** - `api/mobile/student/order/list/`

authentication Required (Student)

Sample Success Response - 

```
{
  "result": true,
  "msg": "SUCCESS",
  "data": [
    {
      "id": 1,
      "order_id": "ORDER20240131001",
      "total_price": 350.0,
      "status": "Order Placed"
    },
    {
      "id": 2,
      "order_id": "ORDER20240131002",
      "total_price": 150.0,
      "status": "Order Placed"
    }
  ]
}
```

---

## 19. Order Detail for Student

**GET** - `api/mobile/student/order/detail/[order_id]`

authentication Required (Student)

Sample Success Response - 

```
{
  "result": true,
  "msg": "SUCCESS",
  "data": {
    "order_id": "ORDER20240131001",
    "total_price": 350.0,
    "total_quantity": 7,
    "delivery_time": "31-01-2023 18:50:00",
    "status": "Order Placed",
    "remarks": null,
    "items": [
      {
        "id": 1,
        "food_id": "1",
        "food_name": "Paneer Tikka",
        "quantity": 1,
        "price": 50.0,
        "image_url": null
      },
      {
        "id": 2,
        "food_id": "4",
        "food_name": "Chicken Biryani",
        "quantity": 6,
        "price": 300.0,
        "image_url": null
      }
    ]
  }
}
```
Sample Error Response - 

```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "Order not found"
  ]
}
```
---

## 20. Order Status Dropdown

**GET** - `api/mobile/canteen/order/status/dropdown/`

authentication Required (Manager)

Sample Success Response - 

```
{
  "result": true,
  "msg": "SUCCESS",
  "data": [
    {
      "value": "PLACED",
      "text": "Order Placed"
    },
    {
      "value": "APPROVED",
      "text": "Order Approved"
    },
    {
      "value": "REJECTED",
      "text": "Order Rejected"
    },
    {
      "value": "READY",
      "text": "Order Ready To be Delivered"
    },
    {
      "value": "DELIVERED",
      "text": "Order Delivered"
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

## 21. Order Status Change

**POST** - `api/mobile/canteen/order/status/change/[order_id]/`

authentication Required (Manager)

```
*status (from dropdown)
*remarks

```

Sample Success Response - 

```
{
  "result": true,
  "msg": "Order Status Changed 🎉",
  "data": {}
}
```
Sample Error Response - 

```
{
  "result": false,
  "msg": "ERROR",
  "data": [
    "Invalid Status"
  ]
}
```
---

## 22. Order List for manager

**GET** - `api/mobile/canteen/order/list/`

authentication Required (Manager)

Sample Success Response - 

```
{
  "result": true,
  "msg": "SUCCESS",
  "data": [
    {
      "id": 1,
      "order_id": "ORDER20240131001",
      "total_price": 350.0,
      "status": "Order Ready To be Delivered",
      "student": "Jhon"
    },
    {
      "id": 2,
      "order_id": "ORDER20240131002",
      "total_price": 350.0,
      "status": "Order Placed",
      "student": "Jhon"
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

## 23. Order Detail for manger

**POST** - `api/mobile/canteen/order/detail/[order_id]/`

authentication Required (Manager)

Sample Success Response - 

```
{
  "result": true,
  "msg": "SUCCESS",
  "data": {
    "order_id": "ORDER20240131001",
    "total_price": 350.0,
    "total_quantity": 7,
    "delivery_time": "31-01-2023 18:50:00",
    "status": "Order Ready To be Delivered",
    "remarks": "as",
    "student": "Jhon",
    "items": [
      {
        "id": 1,
        "food_id": "1",
        "food_name": "Paneer Tikka",
        "quantity": 1,
        "price": 50.0,
        "image_url": null
      },
      {
        "id": 2,
        "food_id": "4",
        "food_name": "Chicken Biryani",
        "quantity": 6,
        "price": 300.0,
        "image_url": null
      }
    ]
  }
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
