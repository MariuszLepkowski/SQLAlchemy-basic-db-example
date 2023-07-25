from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import create_engine, String, Float
import os


class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = 'employees'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    position: Mapped[str] = mapped_column(String(40))
    salary: Mapped[float] = mapped_column(Float)


db_name = "employees.db"
engine = create_engine(f"sqlite:///{db_name}", echo=True)
Base.metadata.create_all(engine)

# Check if the file was created
if os.path.isfile(db_name):
    print(f"Database file '{db_name}' created successfully!")
else:
    print(f"Error: Unable to create database file '{db_name}'.")

try:
    Session = sessionmaker(bind=engine)
    session = Session()

    employee1 = Employee(name="John Doe", position="Manager", salary=50000.0)
    employee2 = Employee(name="Jane Smith", position="Engineer", salary=60000.0)

    # Add the new employees to the session
    session.add(employee1)
    session.add(employee2)
    # Commit the changes to the database
    session.commit()

except Exception as e:
    print(f"Error: {e}")
