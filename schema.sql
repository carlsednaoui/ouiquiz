DROP TABLE if exists users;
DROP TABLE if exists quizzes;
DROP TABLE if exists questions;

CREATE TABLE users
(
id INTEGER PRIMARY KEY,
email TEXT,
password TEXT
);

insert INTO users ("email", "password") VALUES ("carl_1@example.com", "secure");
insert INTO users ("email", "password") VALUES ("carl_2@example.com", "secure");
insert INTO users ("email", "password") VALUES ("carl_3@example.com", "secure");

CREATE TABLE quizzes
(
id INTEGER PRIMARY KEY,
title TEXT,
user_id INTEGER,
FOREIGN KEY(user_id) REFERENCES users(id)
);

insert INTO quizzes ("user_id", "title") VALUES (1, "Quiz #1 for user 1");
insert INTO quizzes ("user_id", "title") VALUES (1, "Quiz #2 for user 1");
insert INTO quizzes ("user_id", "title") VALUES (1, "Quiz #3 for user 1");
insert INTO quizzes ("user_id", "title") VALUES (2, "Quiz #1 for user 2");

CREATE TABLE questions
(
id INTEGER PRIMARY KEY,
title TEXT,
quiz_id INTEGER,
FOREIGN KEY(quiz_id) REFERENCES quizzes(id)
);

insert INTO questions ("quiz_id", "title") VALUES (1, "Question 1 for quiz 1");
insert INTO questions ("quiz_id", "title") VALUES (1, "Question 2 for quiz 1");
insert INTO questions ("quiz_id", "title") VALUES (1, "Question 3 for quiz 1");
insert INTO questions ("quiz_id", "title") VALUES (2, "Question 1 for quiz 2");


-- Write some more queries!!
-- Get all the quizzes for a given user
-- look for a sqlite graphical tool?