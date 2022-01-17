-- Contact_Us
DROP TABLE Contact_Us;

CREATE TABLE Contact_Us (
    ID int IDENTITY(1, 1),
    Email varchar(max),
    Question varchar(max)
);

SELECT
    *
FROM
    Contact_Us;

-- Accounts
DROP TABLE Accounts;

CREATE TABLE Accounts (
    [ID] int IDENTITY(1, 1),
    Rank INT,
    [Email] varchar(max),
    [User_Name] varchar(max),
    [Password] varchar(max)
);

SELECT
    *
FROM
    Accounts;

-- All of the tables
SELECT
    table_name
FROM
    information_schema.tables;

-- Questions
DROP TABLE Questions;

CREATE TABLE Questions (
    label varchar(max),
    content varchar(max),
    html varchar(max),
    name varchar(max),
);

SELECT
    *
FROM
    Questions;

-- Resources
DROP TABLE Resources;

CREATE TABLE Resources (
    [ID] int IDENTITY(1, 1),
    [method_of_resource] Int,
    [link_of_resource] varchar(max),
    [title] varchar(max),
    [description] varchar(max)
);

SELECT
    *
FROM
    Resources;

-- Courses
DROP TABLE Courses; 
CREATE TABLE Courses (
    [ID] int IDENTITY(1, 1),
    [Whole_Content] varchar(max),
    [Info] varchar(max),
    [Image] varchar(max),
    [Name] varchar(max),
    [Marks] varchar(max) -- [Description] varchar(max)
);

SELECT
    *
FROM
    Courses;

-- TEST
DROP TABLE TEST;

CREATE TABLE [TEST] ([Testing_Object] varchar(max));

INSERT INTO
    [TEST] ([Testing_Object])
VALUES
    (
        '{"1": [["te", "3", "question"]], "2": [["te", "3", "question"]]}'
    );

SELECT
    *
FROM
    TEST;
