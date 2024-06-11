
---
---
# 0. SQLite Type [Link](https://www.sqlite.org/datatype3.html)
- text
- numeric
- integer
- real
- boob
  
#### In MySQL there are three main data types: string, numeric, and date and time. [Link](https://dev.mysql.com/doc/refman/8.4/en/data-types.html); [Link2](https://www.w3schools.com/sql/sql_datatypes.asp)


---
---
# 1. CREATE Database and CREATE Table in SQLite
> On macOS, you don’t need to do anything to install sqlite. It’s preinstalled in all modern versions of macOS.
> All you need to do is to open a terminal and run the `sqlite3` command.
```dash
cd Lecture4-SQL
sqlite3
control+c control+c 退出
```
In SQLite, `sqlite3` command is used to create a new SQLite database. You do not need to have any special privilege to create a database.
Following is the basic syntax of sqlite3 command to create a database: −
```dash
$sqlite3 DatabaseName.db
```

- another way to create database in a text file
```dash
cd Lecture4-SQL
touch flights.sql
sqlite3 flights.sql
```

#### SQLite CREATE TABLE statement is used to create a new table in any of the given database. Creating a basic table involves naming the table and defining its columns and each column's data type.

Following is the basic syntax of CREATE TABLE statement.
```sql
CREATE TABLE database_name.table_name(
   column1 datatype PRIMARY KEY(one or more columns),
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype
);
```
`CREATE TABLE` is the keyword telling the database system to create a new table. The unique name or identifier for the table follows the `CREATE TABLE` statement. Optionally, you can specify database_name along with table_name.

- CREATE TABLE TableName follows in parentheses are a comma-separated list of columns that should be present in the table 
- Each separated comma has the name of the column, the type of the column, the constraints of the column
  - NOT NULL Constraint − Ensures that a column cannot have NULL value.

  - DEFAULT Constraint − Provides a default value for a column when none is specified.

  - UNIQUE Constraint − Ensures that all values in a column are different.

  - PRIMARY Key − Uniquely identifies each row/record in a database table.

  - CHECK Constraint − Ensures that all values in a column satisfies certain conditions.

E.g.,
```sql
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL,
);
```

- Check the table after creating the flights table
```sql
.tables
```


---
---
# 2. INSERT Query
#### SQLite INSERT INTO Statement is used to add new rows of data into a table in the database.
Following are the two basic syntaxes of `INSERT INTO` statement.
```sql
INSERT INTO TABLE_NAME [(column1, column2, column3,...columnN)]  
VALUES (value1, value2, value3,...valueN);
```
Here, column1, column2,...columnN are the names of the columns in the table into which you want to insert data.

You may not need to specify the column(s) name in the SQLite query if you are adding values for all the columns of the table. However, make sure the order of the values is in the same order as the columns in the table. The SQLite INSERT INTO syntax would be as follows −
```sql
INSERT INTO TABLE_NAME VALUES (value1,value2,value3,...valueN);
```
E.g.,
```sql
INSERT INTO flights (origin, destination, duration) VALUES ("New York", "London", 415);
INSERT INTO flights (origin, destination, duration) VALUES ("Shanghai", "Paris", 760);
INSERT INTO flights (origin, destination, duration) VALUES ("Istanbul", "Tokyo", 700);
INSERT INTO flights (origin, destination, duration) VALUES ("New York", "Paris", 435);
INSERT INTO flights (origin, destination, duration) VALUES ("Moscow", "Paris", 245);
INSERT INTO flights (origin, destination, duration) VALUES ("Lima", "New York", 455);
```
> make the table nicer
```sql
.mode columns
.headers yes
SELECT * FROM flights;
```


---
---
# 3. SELECT Query
SQLite `SELECT` statement is used to fetch the data from a SQLite database table which returns data in the form of a result table. These result tables are also called **result sets**.

Following is the basic syntax of SQLite SELECT statement.
```sql
SELECT column1, column2, columnN FROM table_name;
```
Here, column1, column2 ... are the fields of a table, whose values you want to fetch. If you want to fetch all the fields available in the field, then you can use the following syntax −
```sql
SELECT * FROM table_name;
```

E.g., 
```sql
SELECT * FROM flights;
```
```sql
SELECT origin, destination FROM flights;
```

---
---
# 4. WHERE Clause
SQLite `WHERE` clause is used to specify a condition while fetching the data from one table or multiple tables.

If the given condition is satisfied, means true, then it returns the specific value from the table. You will have to use WHERE clause to filter the records and fetching only necessary records.

The WHERE clause not only is used in `SELECT` statement, but it is also used in `UPDATE`, `DELETE` statement, etc., which will be covered in subsequent chapters.

Following is the basic syntax of SQLite SELECT statement with WHERE clause.
```sql
SELECT column1, column2, columnN 
FROM table_name
WHERE [condition]
```
You can specify a condition using [Comparision or Logical Operators](https://www.tutorialspoint.com/sqlite/sqlite_operators.htm) such as >, <, =, LIKE, NOT, etc. 
E.g.,
```sql
SELECT * 
FROM flights
WHERE origin = "New York";
```
```sql
SELECT * 
FROM flights
WHERE duration > 500;
```
```sql
SELECT * 
FROM flights
WHERE duration > 500
OR destination = "Paris";
```
Following SELECT statement lists down all the records where NAME starts with 'a', does not matter what comes befor or after 'a'.
```sql
SELECT * 
FROM flights
WHERE origin = "%a%";
```

---
---
# 5. Useful Functions
1. `COUNT` Function
   
    SQLite COUNT aggregate function is used to count the number of rows in a database table.

2. `MAX` Function

    SQLite MAX aggregate function allows us to select the highest (maximum) value for a certain column.

3. `MIN` Function

    SQLite MIN aggregate function allows us to select the lowest (minimum) value for a certain column.

4. `AVG` Function

    SQLite AVG aggregate function selects the average value for certain table column.

5. `SUM` Function

    SQLite SUM aggregate function allows selecting the total for a numeric column.

6. `RANDOM` Function

    SQLite RANDOM function returns a pseudo-random integer between -9223372036854775808 and +9223372036854775807.

7. `ABS` Function

    SQLite ABS function returns the absolute value of the numeric argument.

8. `UPPER` Function

    SQLite UPPER function converts a string into upper-case letters.

9. `LOWER` Function

    SQLite LOWER function converts a string into lower-case letters.

10. `LENGTH` Function

    SQLite LENGTH function returns the length of a string.

11. `sqlite_version` Function

    SQLite sqlite_version function returns the version of the SQLite library.

---
---
# 6. UPDATE Query
SQLite `UPDATE` Query is used to modify the existing records in a table. You can use WHERE clause with UPDATE query to update selected rows, **otherwise all the rows would be updated**.

Following is the basic syntax of UPDATE query with WHERE clause.
```sql
UPDATE table_name
SET column1 = value1, column2 = value2...., columnN = valueN
WHERE [condition];
```
E.g.，
```sql
UPDATE flighes
SET duration = 430
WHERE origin = "New York"
AND destination = "London";
```

---
---
# 7. DELETE Query
SQLite `DELETE` Query is used to delete the existing records from a table. You can use WHERE clause with DELETE query to delete the selected rows, otherwise all the records would be deleted.

Following is the basic syntax of DELETE query with WHERE clause.
```sql
DELETE FROM table_name
WHERE [condition];
```
E.g.,
```sql
DELETE FROM flights
WHERE destination = "Tokyo";
```

---
---
# 8. Other Clauses
- LIKE
- LIMIT
- ORDER BY
- GROUP BY
- HAVING

---
---
# 9. JOINS

---
## 9.1 The INNER JOIN
`INNER JOIN` creates a new result table by combining column values of two tables (table1 and table2) based upon the join-predicate. The query compares each row of table1 with each row of table2 to find all pairs of rows which satisfy the join-predicate. When the join-predicate is satisfied, the column values for each matched pair of rows of A and B are combined into a result row.

An `INNER JOIN` is the most common and default type of join. You can use INNER keyword optionally.

Following is the syntax of `INNER JOIN` −
```sql
SELECT ... FROM table1 [INNER] JOIN table2 ON conditional_expression ...
```
To avoid redundancy and keep the phrasing shorter, INNER JOIN conditions can be declared with a USING expression. This expression specifies a list of one or more columns.
```sql
SELECT ... FROM table1 JOIN table2 USING ( column1 ,... ) ...
```

A NATURAL JOIN is similar to a JOIN...USING, only it automatically tests for equality between the values of every column that exists in both tables −
```sql
SELECT ... FROM table1 NATURAL JOIN table2...
```
E.g.,
```sql
SELECT first_name, origin, destination 
FROM flights 
JOIN passengers 
ON passengers.flight_id = flights.id;
```

---
## 9.2 The OUTER JOIN
`OUTER JOIN` is an extension of INNER JOIN. Though SQL standard defines three types of OUTER JOINs: **LEFT, RIGHT, and FULL**, SQLite only supports the `LEFT OUTER JOIN`.

OUTER JOINs have a condition that is identical to INNER JOINs, expressed using an ON, USING, or NATURAL keyword. The initial results table is calculated the same way. Once the primary JOIN is calculated, an OUTER JOIN will take any unjoined rows from one or both tables, pad them out with NULLs, and append them to the resulting table.

Following is the syntax of LEFT OUTER JOIN −
```sql
SELECT ... FROM table1 LEFT OUTER JOIN table2 ON conditional_expression ...
```
To avoid redundancy and keep the phrasing shorter, OUTER JOIN conditions can be declared with a USING expression. This expression specifies a list of one or more columns.
```sql
SELECT ... FROM table1 LEFT OUTER JOIN table2 USING ( column1 ,... ) ...
```

---
---
# 10. Indexes
Indexes are special lookup tables that the database search engine can use to speed up data retrieval. Simply put, an index is a pointer to data in a table. An index in a database is very similar to an index in the back of a book.

For example, if you want to reference all pages in a book that discuss a certain topic, you first refer to the index, which lists all topics alphabetically and are then referred to one or more specific page numbers.

An index helps speed up SELECT queries and WHERE clauses, but it slows down data input, with UPDATE and INSERT statements. Indexes can be created or dropped with no effect on the data.

Creating an index involves the CREATE INDEX statement, which allows you to name the index, to specify the table and which column or columns to index, and to indicate whether the index is in an ascending or descending order.

Indexes can also be unique, similar to the UNIQUE constraint, in that the index prevents duplicate entries in the column or combination of columns on which there's an index.

Following is the basic syntax of CREATE INDEX.
```sql
CREATE INDEX index_name ON table_name;
```

## 10.1 Single-Column Indexes
A single-column index is one that is created based on only one table column. The basic syntax is as follows −
```sql
CREATE INDEX index_name
ON table_name (column_name);
```
E.g., `sqlite> CREATE INDEX salary_index ON COMPANY (salary);`
```sql
CREATE INDEX index_name
ON flights (last_name);
```

## 10.2 Unique Indexes
Unique indexes are used not only for performance, but also for data integrity. A unique index does not allow any duplicate values to be inserted into the table. The basic syntax is as follows −
```sql
CREATE UNIQUE INDEX index_name
on table_name (column_name);
```

## 10.3 Composite Indexes
A composite index is an index on two or more columns of a table. The basic syntax is as follows −
```sql
CREATE INDEX index_name
on table_name (column1, column2);
```
Whether to create a single-column index or a composite index, take into consideration the column(s) that you may use very frequently in a query's WHERE clause as filter conditions.

Should there be only one column used, a single-column index should be the choice. Should there be two or more columns that are frequently used in the WHERE clause as filters, the composite index would be the best choice.

## 10.4 Implicit Indexes
Implicit indexes are indexes that are automatically created by the database server when an object is created. Indexes are automatically created for primary key constraints and unique constraints.
















































