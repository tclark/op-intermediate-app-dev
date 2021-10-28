## IN608
## Intermediate Application Development

## Session 22 :  Databases and ORM

### Introduction
Many of the applications that we build and maintain need to store and retrieve data, often in large amounts. Databases, especially relational databases, are one of our primary tools for handling such data. So it's not surprising that we have developed a lot of tooling to help work with relational databases in our code. Note that while we are focussing on relational databases today, most of the principles we're discussing hold for other types of databases.


The match between objects that hold data and relational database records is not perfect. The tools that help manage the connections between the two are generally described as *Object Relational Mapping* (ORM).

**Functions of database/ORM libraries**

  1. Manage connections to a database service
  2. Create and modify database tables
  3. Handle CRUD operations on objects/tables
  4. Abstract out database-specific elements from code

**SQLAlchemy**

The most widely used database/ORM library for Python is *SQLAlchemy*. It's divided into core and ORM modules, making it clear that you can use it without any of the ORM features (although we will). We will use version 1.4 of SQLAlchemy, which includes new features in advance of the 2.0 release. It is not in the Python standard library, so we'll need to use pip to install it.

`pip install --user sqlalchemy==1.4`

or if you're on a Mac, or some Linux distros:

`pip3 install --user sqlalchemy==1.4`

If you're using a virtualenv, then omit the `--user` option.

### Using SQLAlchemy

**Connecting: the Engine**
```
from sqlalchemy import create_engine

# use an SQLite database file names 'practical21.db'
engine = create_engine('sqlite:///practical22.db',
    future=True)
      
# use a remote Postgres dbms
engine = create_engine(
    'postgres://user:password@db.op.ac.nz/dbname')

```

The engine does not immediately connect to the database, it just provides the ability to connect when it is needed.

**A Database-mapped class**

```
from sqlalchemy.orm import declarative_base
from sqlalchemy import Table, Column, Integer, String

Base = declarative_base()
class Cat(Base):
    __tablename__ = 'cats'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)
    colour = Column(String)
    age = Column(Integer)
      
# we can create the table in the database
Base.metadata.create_all(engine)
```

**Creating abd Saving Objects**

```
from sqlalchemy.orm import Session

lola = Cat(name='Lola', breed='Burmese',
  colour='Black', age=10)
shadow = Cat(name='Shadow', colour='Grey')
leo = Cat(name='Leo', breed='Siamese', age=4)

# to work with the ORM features we need a Session
session = Session(engine)
session.add(lola)
session.add(shadow)
session.add(leo)
      
# a commit() is necessary to finally save the cats
session.commit()
```

**Querying**

```
from sqlalchemy import select

query = select(Cat).where(Cat.name == 'Lola')
# just give us the first matching cat
cat = session.execute(query).scalars().first()
query = select(Cat).where(
    Cat.age < 5,
    Cat.colour == 'black')
cats = session.execute(query).scalars()
for cat in cats:
    print(cat.name)
```

**Updating**

```
query = select(Cat).where(Cat.name == 'Lola')
cat = session.execute(query).scalars().first()
cat.age = 11
session.commit()
```

**Deleting**

```
query = select(Cat).where(Cat.name == 'Lola')
cat = session.execute(query).scalars().first()
session.delete(cat)
session.commit()

# or
from sqlalchemy import delete
session.execute(delete(Cat).where(Cat.name == 'Lola'))
session.commit()
```

---
### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `22-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `22-practical` directory.
  4. Follow the directions in the README.md file in the `22-practical` directory.
---

### More Complex Objects

Suppose we want to record veterinary clinics and associate them with cats.

```
class VetClinic(Base):
    __tablename__ = 'clinics'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
```


How do we connect the objects? We want the vet clinic to be an attribute of the Cat class.

**Relationships with foreign keys**

```
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Cat(Base):
    __tablename__ = 'cats'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)
    colour = Column(String)
    age = Column(Integer)
    clinic_id = Column(ForeignKey('clinics.id'))
    clinic = relationship('VetClinic', back_populates='cats')  
```

Now for a `Cat` object, we can access things like this:

`lola.clinic.phone_number`
`lola.clinic = gardens_vets`

And a `VetClinic` has a list of cats.

`clinic.cats.append(lola)`

##References

  - SQLAlchemy: SQLAlchemy: https://www.sqlalchemy.org/
  - SQLAlchemy tutorial (pretty involved): https://docs.sqlalchemy.org/en/14/tutorial/index.html


