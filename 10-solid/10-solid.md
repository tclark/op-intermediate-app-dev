## IN608
## Intermediate Application Development
---

## Session 10: SOLID

### Introduction
In the 1990’s (and earlier), software developers noted that a distressing number of projects went badly or failed outright. Literature emerged examining reasons for this analysing why this was happening and what could be done to improve software development.
Among other things, practioners sought to identify a set of good development practices and patterns. One very influential article was *Design Principles and Design Patterns* by Robert C. Martin. Martin noted that problems arise when software changes, either during initial development or later in its life. He called these problems “rot” and he identified various types of this rot.

**Causes of rot**

  - *Rigidity*: Code that is difficult to change because changes to one part requires changes to many other parts
  - *Fragility*: Making a change at one point in the code causes it to break in other parts
  - *Immobility*: Modules can’t be moved into other projects or places within a project even when the intended function is the same.
  - *Viscosity*: It’s easier to make changes in a bad or hackish way than in a "good" way.

Most of these problems stem from overly tight coupling of modules or badly structured dependencies.

Martin went on to identify five design principles that help make code resistent to rot. These have come to be known as the SOILD principles. He didn't coin the term "SOLID" however. In part that's because he didn't describe them in the same order and he didn't use the same names in all cases. Today howver, the programming community generally recognises the SOLID principles as a cornerstone of object oriented software design. (N.B.: It's also a common source of job interview questions for new developers.)

Each of the SOLID principles has a concise description that is commonly used to identify it. In practice I've never found those statements to be very helpful. I prefer to focus on examples that illustrate the principles. Below we'll look at each of them and consider some examples.

---

### Single Responsibility Principle
**A class should have only one reason to change.**

Consider a class with methods like this:

```
class ReportGenerator:
    def read_data(self):
      ...
    def calculate_results(self):
      ...
    def write_report(self):
      ...
```

We might change this class if
  1. the data sources change,
  2. the formulas to calculate results change, 
  3. the report format changes.
This code is immobile. If we need to use the `calculate_results()` method in a different setting, this class isn’t useful.

We can fix this by splitting the code into three classes, each with a **single responsibility**.

```
class DataReader

class ResultsCalculator

class ReportWriter
```

---

### Open-Closed Principle

**A class should be open for extension but closed for modification.**

Basically, this means we chould be able to add capablities to a class by adding new code, but not modifying the exisiting code.

Consider this class:

```
class DataRecord:
    save_to_db()
    if db_type == MYSQL:
        # mysql-specific code
    elif db_type == POSTGRES:
        # postgres-specific code
    ...
```

Now suppose we want to add support for SQL Server. This code is viscous, and probably also rigid. The giveaway is the if/elif stucture. If a structure like that shows up in one method, the odds are good that it will show up in other methods of the class. So whenever we want to add support for another DBMS, we have to find all of the places where have database-specific code. Often it's even worse because there will be some code that is database specific and some that it not, but it can run together in a way that's hard to sort out.

The most obvious way to fix this is to create a base `DataRecord` class, and then subclass it for specific database systems. Then we extend capabilities by addiing a new subclass with out modifying the exisiting ones.  Alternatively we could *inject* a database-specific module at runtime that handles that functionality.

---

### Liskov Substitution Principle

**Objects of a class should be replaceable by instances of subclasses.**

Suppose that we start our project using MySQL and build a MySQL interface class. Later we decide to add support for Postgres, so we create a new class that inherits from the original MySQL class since it has the same behaviours. But there is never a case where we ask for a MySQL object and will be happy getting a Postgres one instead. This is a violation of the "is-a" concept in object inheritance. A class that works with Postgres is not (ususally) a class that works with MySQL.

Even though this isn't the same problem that we had in the example above, it has the same solution. We need to start with a base `Database` class that defines all of the behaviours we expect an object of this type to have.  The we create subclases for specific database types. If we write code that relies on the features of a `Database` object, then it will work with a MySQL subclass, a Postgres subclass, and so on.

---

### Interface Segregation Principle

**A class should not depend on an interface it does not use.**

Database examples have been working for us. Let's keep it going. Suppose, having learned our lessons with the examples above, we have a nice hierarchy of database classes.

```
                        Database
                            |
                            |
                ---------------------------
               |            |              |
            MySQL        Postgres        SQL Server
```

Now our `Database` class defines a common interface that all of our subclasses support. Now let's add another subclass to support ZODB.

```
                        Database
                            |
                            |
                --------------------------------------------
               |            |              |                |
            MySQL        Postgres        SQL Server        ZODB
```

The problem is that ZODB is an object database, while the previous classes all worked with relational databases. The base class may contain code that is specific to relational databases that ZODB does not use. Our ZODB class may be required to implement methods that just don't make sense and are likely to require hackish workarounds.

Here's how we fix this:
  - Let `Database` define an interface common to all database systems.
  - Let `RelationalDB` define the interface for relational databases.
  - Let `ObjectDB` define the interface for object databases.
  - Database-specific subclasses can inherit from teh appropriate parent class.

```
                                         Database
                                             |
                             ----------------------------------
                            |                                  |
                        RelationsDB                        ObjectDB
                            |                                  |
                            |                                  |
                ---------------------------                    |
               |            |              |                   |
            MySQL        Postgres        SQL Server           ZODB
```

___


### Daependency Inversion Principle
**High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.**

This is, I think, the hardest one to get your head around. An good example is the key to making it clear.

Earlier I said that we could inject a database-specific object into a `DataRecord` object to avoid Open-Closed violations. Here's the **wrong** way to do it:

```
class DataRecord:

    def __init__(self):
        self.db = MySQL()
        ...
```

`DataRecord` is a high-level class that represents some abstraction of a colletion of data. `MySQL` is a low-level module that deals with saving to and loading data from a database. If we need to make changes to `MySQL`, then we might also have to change `DataRecord`. 

We fix this by defining an interface `Database` that tells `DataRecord` what it can expect and tells `MySQL` what it should provide.

```
        DataRecord ----- Database
                            |
                            |
                          MySQL
 ```

 In this situation, `MySQL` inherits from or implements `Database` while `DataRecord` uses Database. `DataRecord`'s `self.db` can be any object that provides the `Database` interface. This also solves the problem of swapping out different types of database systems and their corresponding classes.

 ---

 ### References

There's good news and bad news:
  - The good news is that there is **a lot** of stuff written about SOLID principles.
  - The bad news is that most of it isn't very good.

  In the introduction I mentioned Martin's article that kicked things off. You can access a copy of it at 

  https://fi.ort.edu.uy/innovaportal/file/2032/1/design_principles.pdf

  It's a good article, but there's a lot to take in and some of the language and examples are pretty dated. But it is of some historical interest and worth a look.
  
