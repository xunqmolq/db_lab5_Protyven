INSERT INTO brand(brand_name)
VALUES
	('Wei Wei'),
	('Tasty Bite'),
	('Ve Wong'),
	('Westbrae'),
	('Six Fortune'),
	('Sutah');
	
INSERT INTO review(stars, review_id)
VALUES
	(3.25, 610),
	(3.25, 623),
	(4, 1061),
	(0.5, 1),
	(1, 7),
	(2, 9);

INSERT INTO ramen(variety, style, country, review_id, brand_name)
VALUES
	('"A" Series Artificial Chicken', 'Pack', 'Taiwan', 610, 'Wei Wei'),
	('"A" Series Vegetarian', 'Pack', 'Taiwan', 623, 'Wei Wei' ),
	('1 Step-1 Minute Asian Noodles Toasted Sesame', 'Pack', 'USA', 1061, 'Tasty Bite'),
	('Miso Ramen', 'Pack', 'USA', 1, 'Westbrae'),
	('Mushroom Pork', 'Pack', 'Vietnam', 7, 'Ve Wong'),
	('Cup Noodle', 'Cup', 'South Korea', 9, 'Sutah');