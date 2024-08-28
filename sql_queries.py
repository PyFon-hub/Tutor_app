from sqlalchemy import create_engine, URL, Column, Integer, String, REAL, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the database connection

engine = create_engine(url_object, echo=True)

# Create a base class for the table classes to inherit from
Base = declarative_base()

# Define the Students table as a Python class
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    student_name = Column(String(100), nullable=False)
    student_phone = Column(String(20))
    preferable_day = Column(String(15))
    preferable_hour = Column(Time)
    platform_name = Column(String(100), nullable=False)
    hourly_rate = Column(REAL, nullable=False)
    additional_information = Column(String)
    email = Column(String(100))
    parent_name1 = Column(String(100))
    parent_phone1 = Column(String(20))
    parent_name2 = Column(String(100))
    parent_phone2 = Column(String(20))


# Define the TutoringSessions table as a Python class
class TutoringSession(Base):
    __tablename__ = 'tutoring_sessions'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    subject = Column(String(50), nullable=False)
    day = Column(String(15), nullable=False)
    time = Column(Time, nullable=False)
    date = Column(Date, nullable=False)
    tutoring_duration = Column(REAL)
    is_paid_session = Column(Boolean, default=False)
    payment_date = Column(Date)
    payment_method = Column(String(100))
    paid_amount = Column(REAL, CheckConstraint('paid_amount >= 0'))

    # Define a relationship to Student (optional, for ease of access)
    student = relationship("Student")

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create tables in the database
Base.metadata.create_all(engine)

results = session.query(Student).all()

# Print the results
for student in results:
    print(f"ID: {student.id}, Name: {student.student_name}, Phone: {student.student_phone}")