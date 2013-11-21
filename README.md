# Notes


## Debug
    import ipdb
    ipdb.set_trace()
    dir(xxxxx)

## SQL

### To create DB
    sqlite3 database.db < schema.sql

### To get quiz title with a user's email
    SELECT title FROM quizzes WHERE user_id = (SELECT id FROM users WHERE email = "carltest2@example.com");

    SELECT title FROM questions WHERE quiz_id = (SELECT quiz_id FROM quizzes WHERE user_id = (SELECT user_id FROM users WHERE email = "carl_1@example.com"));

### Crazy magic
    SELECT users.email, quizzes.title, questions.title FROM users, quizzes, questions WHERE users.email = "carl_1@example.com" AND users.id = quizzes.user_id AND questions.id = questions.quiz_id;
    
    SELECT users.email, quizzes.id FROM users, quizzes WHERE users.id = quizzes.user_id AND users.id = 1;

    SELECT quizzes.title, questions.title, users.email FROM quizzes, questions, users WHERE questions.quiz_id = quizzes.id AND quizzes.user_id = users.id AND quizzes.id = 1;