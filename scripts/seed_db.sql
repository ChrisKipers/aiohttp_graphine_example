USE aiohttp_graphine_example;

INSERT INTO question (id, question_text, pub_date)
VALUES (1, "What is my name", DATE("2017-1-1"));

INSERT INTO choice (question_id, choice_text)
VALUES (1, "Chris"), (1, "Youlan");