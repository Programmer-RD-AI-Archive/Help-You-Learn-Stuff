DROP TABLE TEST
CREATE TABLE TEST  
(  
 id_num int IDENTITY(1,1),  
 fname varchar (20),  
 minit char(1),  
 lname varchar(30)  
);  
  
INSERT TEST  
   (fname, minit, lname)  
VALUES  
   ('Karin', 'F', 'Josephs');  
  
SELECT * FROM TEST