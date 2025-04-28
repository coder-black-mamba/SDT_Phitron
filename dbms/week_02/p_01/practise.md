Questions

What is the difference between Data and Information
Describe Primary Key, Composite Primary Key, Foreign Key with example
Write five numeric type Data Types of MySQL
Create a table named Employee with EmployeeId, EmployeeName, EmployeeSalary and JoiningDate
Create table
Insert 2 employee data
Delete 1 employee data



## 📚 1. **Difference between Data and Information**

| **Data** | **Information** |
|:--------|:----------------|
| Raw, unprocessed facts (e.g., numbers, words) without context. | Processed, organized data that has meaning and can be useful. |
| Example: `95`, `Apple`, `John` | Example: "John bought 95 apples." |
| Cannot directly support decision-making. | Helps in making decisions based on context and meaning. |

---

## 🔑 2. **Primary Key, Composite Primary Key, and Foreign Key with Example**

- **Primary Key**  
  - A column that uniquely identifies each row in a table.
  - Example:
    ```sql
    CREATE TABLE Students (
      student_id INT PRIMARY KEY,
      student_name VARCHAR(100)
    );
    ```

- **Composite Primary Key**  
  - Two or more columns together uniquely identify each row.
  - Example:
    ```sql
    CREATE TABLE CourseRegistrations (
      student_id INT,
      course_id INT,
      PRIMARY KEY (student_id, course_id)
    );
    ```

- **Foreign Key**  
  - A column that links one table to the primary key of another table.
  - Example:
    ```sql
    CREATE TABLE Orders (
      order_id INT PRIMARY KEY,
      student_id INT,
      FOREIGN KEY (student_id) REFERENCES Students(student_id)
    );
    ```

---

## 🔢 3. **Five Numeric Data Types in MySQL**

| **Data Type** | **Description** |
|:--------------|:----------------|
| `TINYINT` | Very small integer |
| `SMALLINT` | Small integer |
| `MEDIUMINT` | Medium-sized integer |
| `INT` (or `INTEGER`) | Standard integer |
| `BIGINT` | Very large integer |

---

## 🛠️ 4. **MySQL Table Creation, Insert Data, and Delete Data**

### Step 1: Create `Employee` Table
```sql
CREATE TABLE Employee (
    EmployeeId INT PRIMARY KEY,
    EmployeeName VARCHAR(100),
    EmployeeSalary DECIMAL(10,2),
    JoiningDate DATE
);
```

### Step 2: Insert 2 Employees
```sql
INSERT INTO Employee (EmployeeId, EmployeeName, EmployeeSalary, JoiningDate)
VALUES 
(1, 'John Doe', 50000.00, '2023-01-15'),
(2, 'Jane Smith', 60000.00, '2024-03-20');
```

### Step 3: Delete 1 Employee
```sql
DELETE FROM Employee
WHERE EmployeeId = 1;
```
- This deletes **John Doe**.

---

Would you also like me to show how to **view** the table after inserting and deleting using a `SELECT` query? (I can add that too if you want!) 🌟