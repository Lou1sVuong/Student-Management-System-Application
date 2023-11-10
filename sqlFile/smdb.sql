select *
from studentgrades
where studentid not in (select studentid from subject)

--dau 3 rot 2
select *
from student
where studentid in(select studentid
				  from studentgrades
				  where grades >= 5
				  group by studentid
				  having count(*) = 3)
and studentid in (select studentid
				  from studentgrades
				  where grades < 5
				  group by studentid
				  having count(*) = 2)
				  
--sv nao thi dau tat ca mon hoc			 	  
select distinct Y.*
from studentgrades X, student Y
where X.studentid = Y.studentid
	and not exists(select *
				  from subject
				  where subjectid not in
				  	(select subjectid from studentgrades
					where grades >=5
						and X.studentid = studentid))
						
select studentid
from studentgrades
where grades >=5
group by studentid
having count(*) = ( select count(*) from subject)
--------------------------------------
create table Subject 
( 
	SubjectID char(3) primary key,
	SubjectName varchar(30),
	Units int
)

insert into Subject
values
	('S01','Toan',2),
	('S02','Van',3),
	('S03','Anh',2),
	('S04','Ly',4),
	('S05','Hoa',2)
select * from Subject
delete from Subject

drop table Subject
------------------------------------------------------
create table Classes
( 
	ClassID char(3) primary key,
	ClassName varchar(30),
	ClassYear varchar(30)
)
insert into Classes
values
	('C01','Computer Science','2020-2024'),
	('C02','Computer Science','2020-2024'),
	('C03','CN22CLCG','2020-2024')
	
select * from Classes
delete from Classes
drop table Classes
--------------------------------------------------
create table Student 
( 
	StudentID char(3) primary key , 
	StudentName varchar(30), 
	StudentAddress varchar(30), 
	ClassID char(3)
)
insert into Student
values
	('T21', 'Student21','New York', 'K01'),
	('T01', 'Student01','New York', 'C01'),
	('T02', 'Student02','Los Angeles', 'C01'),
	('T03', 'Student03','New York', 'C01'),
	('T04', 'Student04','Chicago', 'C01'),
	('T05', 'Student05','Philadelphia', 'C01'),
	('T06', 'Student06','New York', 'C01'),
	('T07', 'Student07','Chicago', 'C01'),
	('T08', 'Student08','Houston', 'C02'),
	('T09', 'Student09','New York', 'C02'),
	('T10', 'Student10','Los Angeles', 'C02'),
	('T11', 'Student11','New York', 'C02'),
	('T12', 'Student12','newrk', 'C02'),
	('T13', 'Student13','Chicago', 'C02'),
	('T14', 'Student14','Houston', 'C02'),
	('T15', 'Student15','Los Angeles', 'C03'),
	('T16', 'Student16','New York', 'C03'),
	('T17', 'Student17','New York', 'C03'),
	('T18', 'Student18','Los Angeles', 'C03'),
	('T19', 'Student19','New York', 'C03'),
	('T20', 'Student20','Chicago', 'C03')
select * from Student

delete from Student
drop table Student
-------------------------------------------------------
create table StudentGrades 
( 
	StudentID char(3), 
	SubjectID char(3), 
	Grades float,
	primary key(StudentID, SubjectID)
)
insert into StudentGrades
values
--đậu hết
('T01','S01',10),
('T01','S02',8),
('T01','S03',8),
('T01','S04',9),
('T01','S05',8),

--đậu 3 rớt 2
('T02','S01',6),
('T02','S02',7),
('T02','S03',8),
('T02','S04',3),
('T02','S05',4),

--đậu hết
('T03','S01',8),
('T03','S02',7),
('T03','S03',8),
('T03','S04',9),
('T03','S05',8),

--rớt hết
('T04','S01',4),
('T04','S02',2),
('T04','S03',3),
('T04','S04',3),
('T04','S05',3),

--đậu 3 rớt 2
('T05','S01',6),
('T05','S02',7),
('T05','S03',8),
('T05','S04',3),
('T05','S05',4),


	
select * from StudentGrades
delete from StudentGrades

drop table StudentGrades
------------------------------------------
5.1. Show Students of class ID = ”C02”.

select * 
from student
where ClassID='C01'
------------------------------------------
5.2. Show Students of class name = ”Computer Science”. ( skill kết tự nhiên )

select A.*
From Student A, Classes B
where A.ClassID = B.ClassID
		and ClassName='Computer Science'
		
------------------------------------------
5.3. Show Students (All information) of class year = ”2020-2024”.

select A.*
From Student A, Classes B
where A.ClassID = B.ClassID
		and ClassYear='2020-2024'

------------------------------------------
5.4. Show Subject name and units of the Subject ID = “S01”.

select SubjectName,Units
from Subject
where SubjectID='S01'

------------------------------------------
5.5. Grades of Subject ID = ”S02” of Student ID = ”T02”.

select Grades
from StudentGrades
where SubjectID='S02' and StudentID='T02'

------------------------------------------
5.6. Find Subject (ID, Name and Grades) that Student ID = ”T02” fail.

select StudentID,SubjectName,Grades
from Subject A, StudentGrades B
where A.SubjectID = B.SubjectID
		and Grades < 5

------------------------------------------
5.7. Show all the Subject (*) that Student ID = ”T03” never took the exam.

select *
from Subject
where SubjectID not in (
						select SubjectID
						from StudentGrades
						where StudentID='T03'
						)						
------------------------------------------
5.8. Number of Students for each class.

select ClassID, count(*) as si_so
from Student
Group by ClassID

--lop co ss nho hon 7 :
select ClassID, count(*) as si_so
from Student
Group by ClassID
having count(*) < 7

------------------------------------------
5.9. Find the classes with the largest number of students.

SELECT ClassID, COUNT(*) AS si_so
FROM Student
GROUP BY ClassID
HAVING COUNT(*) >= All(
    SELECT COUNT(*)
	FROM Student
	GROUP BY ClassID
)
------------------------------------------
5.10. GPA (grade point average) of student ID = ”T02”.

SELECT StudentID, round(cast(avg(Grades) as numeric) , 2)
FROM StudentGrades
WHERE StudentID = 'T02'
GROUP BY StudentID

------------------------------------------
5.11. GPA for each student.

SELECT StudentID, round(cast(avg(Grades) as numeric) , 2) as diem_tb
FROM StudentGrades
GROUP BY StudentID

------------------------------------------
5.12. GPA of class ID = ”C02”.

SELECT ClassID, round(cast(avg(Grades) as numeric) , 2) as diem_tb
FROM Student A, StudentGrades B
where A.StudentID = B.StudentID
	and	ClassID='C02'
GROUP BY ClassID

------------------------------------------
5.14. Find students have the largest GPA.

SELECT StudentID, round(cast(avg(Grades) as numeric) , 2) as diem_tb
FROM StudentGrades
GROUP BY StudentID
HAVING AVG(Grades) >= ALL(
    SELECT round(cast(avg(Grades) as numeric) , 2)
	FROM StudentGrades
	GROUP BY StudentID
)
------------------------------------------
5.15. Find students (ID and Name) have the largest GPA.

select A.studentid, B.studentname, round(cast (avg(grades) as numeric), 2)
from studentgrades A, student B
where A.studentid = B.studentid
 group by a.studentid, b.studentname
having round(cast (avg(grades) as numeric), 2) >= all(select round(cast (avg(grades) as numeric), 2)
					  from studentgrades A, student B
                      where A.studentid = B.studentid 
                       group by a.studentid, b.studentname)

------------------------------------------
select * from Subject 

insert into subject
values('S09')

delete from subject
where subjectID = 'S07'

Alter table subject
alter column subjectName
set not null

Alter table subject
alter column Units
set not null

Alter table subject
add unique(subjectName)
--ex :
insert into subject
values('S10','Toan','4')

alter table subject
add Constraint units
check(Units > 0)

insert into subject
values('S11','xxx',-4)
--
select * from Classes 

insert into subject
values('S09')

delete from subject
where subjectID = 'S07'

Alter table Classes
alter column className
set not null

Alter table Classes
alter column classYear
set not null

Alter table Student
Add Constraint VN1
Foreign key (ClassID)
References Classes (ClassID)

Alter table StudentGrades
Add Constraint VN2
Foreign key (StudentID)
References Student(StudentID)

