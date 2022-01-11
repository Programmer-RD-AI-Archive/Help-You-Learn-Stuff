-- DROP TABLE TEST
-- CREATE TABLE TEST
-- (
--     Rank int,
-- );
-- INSERT INTO [TEST]
--     ( [Rank] )
-- VALUES
--     (1)
-- SELECT *
-- FRO/M TEST
-- DROP TABLE Accounts
-- DROP TABLE Contact_Us
-- CREATE TABLE Accounts ([ID] int IDENTITY(1,1), Rank INT, [Email] varchar(max),[User_Name] varchar(max), [Password] varchar(max))
-- CREATE TABLE Contact_Us (ID int IDENTITY(1,1),  Email varchar(max),Question varchar(max))
-- DROP TABLE Accounts
-- DROP TABLE Contact_Us
-- DROP TABLE TEST

-- INSERT INTO [Accounts]
-- ( [Rank] , [Email] ,[User_Name] , [Password] )
-- VALUES
-- (5, 'go2ranuga@gmail.com', 'Programmer-RD-AI', 'dGVzdA==')

-- SELECT *
-- FROM Contact_Us
-- CREATE TABLE Courses
-- (
--     [ID] int IDENTITY(1,1),
--     [Name] varchar(max),
--     [Image] varchar(max)
-- )


-- CREATE TABLE Courses_Content (
--     [ID] int IDENTITY(1,1),
-- )
-- DROP TABLE Accounts
-- DROP TABLE Contact_Us
-- DROP TABLE TEST
-- DROP TABLE Courses_Content
-- DROP TABLE Courses
-- SELECT table_name FROM information_schema.tables
-- CREATE TABLE Questions
-- (
--     label varchar(max),
--     content varchar(max),
--     html varchar(max),
--    name varchar(max),
-- )
-- SELECT * FROM Questions

-- CREATE TABLE TEST
-- (
--     test1 object,
-- )
-- INSERT INTO [TEST]
--     ( [test1] )
-- VALUES
--     ({"test":"test"})
-- DROP TABLE Questions;
-- CREATE TABLE Questions
-- (
--     [ID] int IDENTITY(1,1),
--     [html] varchar(max),
--     [name] varchar(max),
-- )
-- SELECT *
-- FROM Questions;
SELECT *
FROM Accounts
-- INSERT INTO Questions (html, name)
-- VALUES ('Cardinal','Tom B. Erichsen');

-- DROP TABLE Resources
-- CREATE TABLE Resources
-- (
--     [ID] int IDENTITY(1,1),
--     [method_of_resource] Int,
--     [link_of_resource] varchar(max),
--     [title] varchar(max),
--     [description] varchar(max)
-- )
-- DELETE FROM Resources WHERE ID=1
-- SELECT *
-- FROM Resources

-- UPDATE Resources
-- SET title='ttt'
-- WHERE ID=7;

-- SELECT *
-- FROM Resources
-- DROP TABLE Courses
-- CREATE TABLE Courses
-- (
--     [ID] int IDENTITY(1,1),
--     [Whole_Content] varchar(max),
--     [Info] varchar(max),
--     [Image] varchar(max),
--     [Name] varchar(max),
--     [Marks] varchar(max)
--     -- [Description] varchar(max)
-- )
SELECT *
FROM Courses;
-- DROP TABLE TEST;
-- CREATE TABLE [TEST]
-- (
--     [Testing_Object] varchar(max)
-- )
-- INSERT INTO [TEST]
--     ( [Testing_Object])
-- VALUES
--     ('{"1": [["te", "3", "question"]], "2": [["te", "3", "question"]]}')
SELECT *
FROM TEST