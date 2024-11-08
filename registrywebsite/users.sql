USE users;
DROP TABLE IF EXISTS studenttests;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS test;
DROP TABLE IF EXISTS faculty;
DROP TABLE IF EXISTS admi;

CREATE TABLE faculty(
	fName VARCHAR(50),
    lName VARCHAR(50),
    facID CHAR(3) PRIMARY KEY,
    email VARCHAR(50),
    password1 VARCHAR(50)
);

CREATE TABLE students(
	username VARCHAR(50),
    password1 VARCHAR(50),
    studentnum INT PRIMARY KEY,
    email VARCHAR(50),
    fName VARCHAR(50),
    lName VARCHAR(50),
    passed ENUM('math', 'science', 'english'),
    currTest ENUM('math', 'science', 'english'),
    teacher CHAR(3),
    CONSTRAINT student_fk_faculty
		FOREIGN KEY (teacher)
		REFERENCES faculty (facID)
);

CREATE TABLE tests(
	examtype ENUM('math', 'science', 'english') PRIMARY KEY,
    proctorName VARCHAR(50),
    proctorID CHAR(3),
    location VARCHAR(50),
    testDate DATE,
    testTime TIME,
    studnum INT
);

CREATE TABLE studenttests(
	studnum INT,
    exam ENUM('math', 'science', 'english'),
    CONSTRAINT studenttest_fk_students
		FOREIGN KEY (studnum)
        REFERENCES students(studentnum),
	CONSTRAINT studenttest_fk_test
		FOREIGN KEY (exam)
        REFERENCES tests(examtype)
);

CREATE TABLE admi(
	username CHAR(5),
    password1 VARCHAR(50)
);