CREATE DATABASE Bookdatabase;

use Bookdatabase;
SET SQL_SAFE_UPDATES = 0;
create table author(au_id INT PRIMARY KEY AUTO_INCREMENT, authorName VARCHAR(100), biography VARCHAR(10000), theirBooks VARCHAR(2999));

create table books(title VARCHAR(100), au_id INT, authorName VARCHAR(100), isbn  VARCHAR(20) PRIMARY KEY, FOREIGN KEY (au_id) REFERENCES author(au_id));

create table accounts(id INT PRIMARY KEY AUTO_INCREMENT, userName varchar(100), passwrd varchar(10000), favouriteBook varchar(100));

create table favbooks(id INT, isbn VARCHAR(20), FOREIGN KEY (id) REFERENCES accounts(id), FOREIGN KEY (isbn) REFERENCES books(isbn));

INSERT INTO books(title, authorName, isbn)
VALUES 
	("Harry Potter and the philosophers stone", "JK. Rowling", "0000000"),
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
SELECT 'uname', 'pass' 
WHERE 'uname' NOT IN (SELECT userName FROM accounts);

SELECT Books.title, Count(accounts.favouriteBook) as numberOfFavourites
FROM Books
CROSS JOIN accounts
WHERE Books.title = accounts.favouriteBook
GROUP BY books.title;

UPDATE accounts SET favouriteBook = 'blood meridian' WHERE userName = 'test'; 

CREATE PROCEDURE booksearch(IN book_att VARCHAR(100))
SELECT * FROM books LEFT JOIN (SELECT Books.title, Count(accounts.favouriteBook) as numberOfFavourites
FROM Books
CROSS JOIN accounts
WHERE Books.title = accounts.favouriteBook
GROUP BY books.title) AS favbooks ON favbooks.title = books.title WHERE books.title LIKE '%%' OR books.authorName LIKE '%%' OR books.isbn LIKE '%%';

DELIMITER $$
CREATE PROCEDURE addfavbook(IN bookname VARCHAR(255), uid INT)
BEGIN 
UPDATE accounts SET favouriteBook = bookname WHERE id = uid;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE addtofavs(IN uid INT, isbn VARCHAR(20))
BEGIN 
INSERT INTO favbooks(id, isbn) VALUES (uid, isbn);
END $$
DELIMITER ;
