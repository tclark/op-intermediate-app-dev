# Practical  21: SQLAlchemy
To perform today's lab it will be necesary to `pip install sqlalchemy`.

1.  Write an SQLAlchemy mapped class, `Student` with an integer primary
key and with fields for name, , email adderess, and anticipated 
graduation year.

Create an `engine` for a local SQLite database and create your table in
the database.

2. Write code to add five sample students to your table. Then write a
query that returns all five student. Loop over the result set and print
each student's name.

3. Write another query that returns just one student. Get that
student's record and print it's name.


**Stop here**. We will discuss solutions in class.

## Homework

4. Write code for a second  mapped class, `Programme` with a primary 
key, name (e.g., BIT), and a many-to-one relationship with `Student`s.
Add the `ForeignKey` field to the `Student` table. Create the table and
add a sample record to the programme table.

5. Write a query that return your `Programme` record. Add your five 
student to the programme and save it. Then use query to get one 
`Student` and show that it is now linked to the programme.



