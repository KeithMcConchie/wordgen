CREATE DATABASE wordgen;

USE wordgen;

DROP TABLE wordlist;

CREATE TABLE wordlist (word CHAR(20) NOT NULL, 
                      pscore INT NOT NULL, 
                      nscore INT NOT NULL, 
                      definition VARCHAR(300),
                      PRIMARY KEY (word));





