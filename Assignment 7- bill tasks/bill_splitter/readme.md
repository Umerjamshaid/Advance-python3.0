# Bill Splitting Application

This repository contains five different tasks for calculating shared bills using various algorithms. Each task involves creating an API endpoint that processes bill-related information and displays the results in a user-friendly HTML interface.

---

## Table of Contents
1. [Task 1: Basic Bill Splitting](#task-1-basic-bill-splitting)
2. [Task 2: Uneven Bill Splitting](#task-2-uneven-bill-splitting)
3. [Task 3: Including Tip and Tax](#task-3-including-tip-and-tax)
4. [Task 4: Handling Discounts](#task-4-handling-discounts)
5. [Task 5: Advanced Bill Splitting with Shared Items](#task-5-advanced-bill-splitting-with-shared-items)
6. [Installation and Setup](#installation-and-setup)
7. [How to Use](#how-to-use)

---

## Task 1: Basic Bill Splitting

### Description
This task splits the total bill amount evenly among all users. Users are required to input their IDs and the total bill amount. The API will calculate the equal share for each user.

### API Endpoint: `/split-evenly/`
- **Method**: POST
- **Inputs**:
  - `user_ids`: A comma-separated string of user IDs.
  - `total_bill_amount`: The total bill to be divided.

### Output:
Each user’s share is displayed in an HTML format along with their respective IDs.

---

## Task 2: Uneven Bill Splitting

### Description
This task divides the bill unevenly based on individual contributions. Users input their IDs, respective contributions, and the total bill amount. The API calculates how much each user needs to pay or receive.

### API Endpoint: `/split-unevenly/`
- **Method**: POST
- **Inputs**:
  - `user_ids`: A comma-separated string of user IDs.
  - `contributions`: A comma-separated string of each user's contribution.
  - `total_bill_amount`: The total bill amount.

### Output:
The bill split for each user is based on their contributions, showing how much each user owes or should receive, displayed in the UI.

---

## Task 3: Including Tip and Tax

### Description
This task splits the total bill including a tip and tax among users. Users input their IDs, total bill amount, tip percentage, and tax percentage, and the API calculates each user’s share, including tip and tax.

### API Endpoint: `/split-including-tip-tax/`
- **Method**: POST
- **Inputs**:
  - `user_ids`: A comma-separated string of user IDs.
  - `total_bill_amount`: The total bill to be divided.
  - `tip_percentage`: Tip percentage to be added.
  - `tax_percentage`: Tax percentage to be added.

### Output:
The bill split for each user, including their share of the tip and tax, is displayed in the UI.

---

## Task 4: Handling Discounts

### Description
This task applies a discount to the total bill before splitting it evenly among users. Users input their IDs, total bill amount, and discount percentage, and the API calculates each user’s share after the discount is applied.

### API Endpoint: `/split-with-discount/`
- **Method**: POST
- **Inputs**:
  - `user_ids`: A comma-separated string of user IDs.
  - `total_bill_amount`: The total bill amount before the discount.
  - `discount_percentage`: Discount percentage to be applied.

### Output:
The bill split for each user after the discount is applied, displayed in the UI.

---

## Task 5: Advanced Bill Splitting with Shared Items

### Description
This task splits a bill where some items are shared among specific users. Users input their IDs, the total bill amount, the price of shared items, and which users are sharing those items. The API calculates the share for each user, including shared items.

### API Endpoint: `/split-with-shared-items/`
- **Method**: POST
- **Inputs**:
  - `user_ids`: A comma-separated string of user IDs.
  - `total_bill_amount`: The total bill amount.
  - `items_with_prices`: A comma-separated string of prices for shared items.
  - `user_IDs_for_each_shared_item`: A comma-separated string of user IDs sharing specific items.

### Output:
Each user’s total bill and share of the shared items are displayed in the UI.

---

## Installation and Setup

### Prerequisites
- Python 3.x
- Django

### Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/bill-splitting-app.git
    cd bill-splitting-app
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

---

## How to Use

### 1. Access the Form
Once the development server is running, you can access the HTML form for each task by navigating to the corresponding URL in your browser:

- Basic Bill Splitting: `http://127.0.0.1:8000/split-evenly/`
- Uneven Bill Splitting: `http://127.0.0.1:8000/split-unevenly/`
- Including Tip and Tax: `http://127.0.0.1:8000/split-including-tip-tax/`
- Handling Discounts: `http://127.0.0.1:8000/split-with-discount/`
- Advanced Bill Splitting with Shared Items: `http://127.0.0.1:8000/split-with-shared-items/`

### 2. Fill Out the Form
For each task, simply fill in the required inputs (user IDs, bill amounts, etc.) and submit the form. The results will be displayed on the same page.

---

## Contributing

If you'd like to contribute to this project, feel free to open a pull request or issue. All contributions are welcome!

---

## License

This project is licensed under the MIT License.
