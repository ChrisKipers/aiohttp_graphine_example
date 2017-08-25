CREATE DATABASE aiohttp_graphine_example;

CREATE TABLE question (
  id INTEGER NOT NULL AUTO_INCREMENT,
  question_text VARCHAR(200) NOT NULL,
  pub_date DATE NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE choice (
  id INTEGER NOT NULL AUTO_INCREMENT,
  question_id INTEGER NOT NULL,
  choice_text VARCHAR(200) NOT NULL,
  votes INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (id),
  FOREIGN KEY (question_id) REFERENCES question(id)
);