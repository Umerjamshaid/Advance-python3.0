Certainly! Here's a README template for all five tasks, summarizing each one and including instructions for setup, usage, and descriptions of the logic for each task.

---

# Bill Splitting Application

This repository contains five different tasks for calculating shared bills using various algorithms. Each task involves creating an API endpoint that processes bill-related information and displays the results in a user-friendly HTML interface.

---

## Table of Contents
1. [Task 1: Equal Split](#task-1-equal-split)
2. [Task 2: Weighted Split](#task-2-weighted-split)
3. [Task 3: Split with Shared Items](#task-3-split-with-shared-items)
4. [Task 4: Split by Percentage](#task-4-split-by-percentage)
5. [Task 5: Split by Exact Amount](#task-5-split-by-exact-amount)
6. [Installation and Setup](#installation-and-setup)
7. [How to Use](#how-to-use)

---

## Task 1: Equal Split

### Description
This task splits the total bill amount equally among all users. Users are required to input their IDs and the total bill amount. The API will calculate the equal share for each user.

### API Endpoint: `/equal_split/`
- **Method**: POST
- **Inputs**:
  - `user_ids`: A comma-separated string of user IDs.
  - `total_bill_amount`: The total bill to be divided.
  
### Output:
Each user’s share is displayed in an HTML format along with their respective IDs.

---

## Task 2: Weighted Split

### Description
This task divides the bill based on weights assigned to each user. The more weight a user has, the higher the portion of the bill they are required to pay.

### API Endpoint: `/weighted_split/`
- **Method**: POST
- **Inputs**:
  - `user_ids`: A comma-separated string of user IDs.
  - `total_bill_amount`: The total bill to be divided.
  - `weights`: A comma-separated string of weights corresponding to each user.

### Output:
The bill split for each user is based on their weight, calculated and displayed in the UI.

---

## Task 3: Split with Shared Items

### Description
This task splits the bill where some items are shared among specific users. Users input their IDs, the total bill amount, and the price of shared items, as well as which users are sharing those items.

### API Endpoint: `/split_with_shared_items/`
- **Method**: POST
- **Inputs**:
  - `user_ids`: A comma-separated string of user IDs.
  - `total_bill_amount`: The total bill amount.
  - `items_with_prices`: The total price of shared items.
  - `user_IDs_for_each_shared_item`: A comma-separated string of user IDs sharing specific items.

### Output:
Each user’s total bill and share of the shared items are displayed in the UI.

---

## Task 4: Split by Percentage

### Description
This task splits the total bill based on percentages assigned to each user. The percentages must add up to 100%.

### API Endpoint: `/split_by_percentage/`
- **Method**: POST
- **Inputs**:
  - `user_ids`: A comma-separated string of user IDs.
  - `total_bill_amount`: The total bill amount.
  - `percentages`: A comma-separated string of percentages corresponding to each user.

### Output:
The bill split for each user is based on the provided percentages, with the results shown in the UI.

---

## Task 5: Split by Exact Amount

### Description
This task allows users to manually input exact amounts for each user to split the bill. This can be useful for custom bill-splitting scenarios.

### API Endpoint: `/split_by_exact_amount/`
- **Method**: POST
- **Inputs**:
  - `user_ids`: A comma-separated string of user IDs.
  - `exact_amounts`: A comma-separated string of exact amounts each user has to pay.

### Output:
The exact amounts are assigned to each user, and the result is displayed in the UI.

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

- Equal Split: `http://127.0.0.1:8000/equal_split/`
- Weighted Split: `http://127.0.0.1:8000/weighted_split/`
- Split with Shared Items: `http://127.0.0.1:8000/split_with_shared_items/`
- Split by Percentage: `http://127.0.0.1:8000/split_by_percentage/`
- Split by Exact Amount: `http://127.0.0.1:8000/split_by_exact_amount/`

### 2. Fill Out the Form
For each task, simply fill in the required inputs (user IDs, bill amounts, weights, etc.) and submit the form. The results will be displayed on the same page.

---

## Contributing

If you'd like to contribute to this project, feel free to open a pull request or issue. All contributions are welcome!

---

## License

This project is licensed under the MIT License.

---
