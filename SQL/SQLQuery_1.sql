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
-- FROM TEST
-- DROP TABLE Accounts
-- DROP TABLE Contact_Us
-- SELECT * FROM Accounts
-- SELECT * FROM Contact_Us
CREATE TABLE Accounts (ID int IDENTITY(1,1), Rank INT, Email varchar(max),User_Name varchar(max), Password varchar(max))
CREATE TABLE Contact_Us (ID int IDENTITY(1,1),  Email varchar(max),Question varchar(max))
-- DROP TABLE Accounts
-- DROP TABLE Contact_Us
-- DROP TABLE TEST