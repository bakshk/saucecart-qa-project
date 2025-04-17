# Test Cases – SauceCart QA Project

## 🔐 Login Functionality

| Test Case ID | Description | Steps | Expected Result |
|--------------|-------------|-------|------------------|
| TC_LOGIN_001 | Valid login | 1. Go to login<br>2. Enter correct username/password<br>3. Click Login | Redirect to Inventory page |
| TC_LOGIN_002 | Invalid login | Enter wrong credentials | Error message is displayed |
| TC_LOGIN_003 | Blank login | Submit form with empty fields | Validation error shown |

---

## 🛒 Add to Cart

| Test Case ID | Description | Steps | Expected Result |
|--------------|-------------|-------|------------------|
| TC_CART_001 | Add single item | 1. Log in<br>2. Click “Add to cart” | Cart icon shows 1 |
| TC_CART_002 | Remove item | Add item, then click “Remove” | Cart icon updates to 0 |
| TC_CART_003 | Multiple items | Add 3 items | Cart shows 3 |

---

## 💳 Checkout

| Test Case ID | Description | Steps | Expected Result |
|--------------|-------------|-------|------------------|
| TC_CHECKOUT_001 | Successful checkout | Add item → Go to cart → Checkout → Fill form → Finish | Thank you message appears |
| TC_CHECKOUT_002 | Missing info | Leave checkout form blank | Error messages shown |
