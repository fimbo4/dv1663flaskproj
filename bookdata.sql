CREATE DATABASE Bookdatabase;

use Bookdatabase;

create table author(au_id INT PRIMARY KEY AUTO_INCREMENT, authorName VARCHAR(100), biography VARCHAR(10000), theirBooks VARCHAR(2999));

create table books(title VARCHAR(100), au_id INT, authorName VARCHAR(100), isbn  VARCHAR(20) PRIMARY KEY, FOREIGN KEY (au_id) REFERENCES author(au_id));

create table accounts(id INT PRIMARY KEY AUTO_INCREMENT, userName varchar(100), passwrd varchar(10000), favouriteBook varchar(100));

INSERT INTO books(title, authorName, isbn)
VALUES 
	("Harry Potter and the philosophers stone", "JK.Rowling", "0000000"),
    ("Harry Potter and the half-blood prince", "JK. Rowling", "0000002"),
    ("The Way Of Kings", "B.Sanderson", "0000001"),
    ("Stranger in a Strange Land", "Robert A. Heinlein", "0441788386"),
    ("Lord of the Flies", "William Golding", "0307281701"),
    ("Of Mice and Men", "John Steinbeck", "0142000671"),
    ("Life of Pi", "Yann Martel", "0156030209"),
    ("Dune", "Frank Herbert", "9292929292"),
    ("Pride and Prejudice", "Jane Austen", "0192802380");
    
INSERT INTO author(authorName, biography)
values
	("JK. Rowling", "adadadaad"),
    ("B. Sanderson", "WAWWEWEW"),
    ("Robert A. Heinlein", "fdfdf"),
    ("William Golding", "ssdsds"),
    ("John Steinbeck", "jfjf"),
    ("Yane Martel", "jf"),
    ("Jane Austen", "fhfhf");
    
insert into accounts(userName, passwrd)
values
	("addddd",'a'),
    ("sadadasdasdafgwr",'a'),
    ("TheOne",'b '),
    ("AragonStan04",'c'),
    ("AragonStan03",'d'),
    ("JK. Rowling",'e'),
    ("Of Mice and Men",'f');

COME UP WITH A FUNCTION AND A TRIGGER
Increase number of published books for author when new book is added?

DELIMITER $$
CREATE TRIGGER newFavBook
AFTER UPDATE 
ON Accounts
FOR EACH ROW
BEGIN
	IF new.favouriteBook NOT IN (SELECT title FROM Books)
		THEN INSERT INTO Books(title, authorName, isbn) VALUES (new.favouriteBook, "Unknown", "Unknown");
	END IF;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER newAuthor
AFTER INSERT 
ON Books
FOR EACH ROW
BEGIN
	IF new.authorName NOT IN (SELECT authorName FROM Author)
		THEN INSERT INTO author(authorName) VALUES (new.authorName);
	END IF;
END$$
DELIMITER ;

INSERT INTO accounts(userName, passwrd) 
SELECT 'acc35', 'pass1'
WHERE 'acc35' NOT IN (SELECT userName FROM accounts);

SELECT * FROM accounts;

INSERT INTO accounts(userName, passwrd) 
SELECT 'uname', 'pass' 
WHERE 'uname' NOT IN (SELECT userName FROM accounts);
