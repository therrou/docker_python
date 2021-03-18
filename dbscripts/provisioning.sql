DROP TABLE IF EXISTS greetings;

CREATE TABLE greetings (
	id serial primary key,
	time timestamp default Now(),
	text text
)
