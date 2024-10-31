USE users;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS admi;


CREATE TABLE students;
INSERT INTO students (
	username ,
    password1
)
VALUES
(
	"generic",
    "student"
);
CREATE TABLE admi;
INSERT INTO admi (
	username,
    password1
)
VALUES(
	"admin",
    "admin"
);