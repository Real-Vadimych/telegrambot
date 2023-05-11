CREATE USER telebot;

CREATE DATABASE telenote;
GRANT ALL PRIVILEGES ON DATABASE telenote TO telebot;

\c telebot telebot

CREATE TABLE if not EXISTS notes (
  id VARCHAR(12) PRIMARY KEY,
  person text,
  datetime_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  note text
);
