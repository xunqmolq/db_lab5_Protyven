SELECT * FROM review;
CREATE TABLE new_data_table AS SELECT * FROM review;
DELETE FROM new_data_table;

DO $$
  DECLARE
     stars   review.stars%TYPE;
	 review_id review.review_id%TYPE;
  BEGIN
  	 review_id := 0;
	 
 	 FOR counter IN 1..10
		 LOOP
			 INSERT INTO new_data_table(stars,review_id)
			 VALUES (ROUND((random()* (5-1) + 1)::numeric, 2), review_id + counter);
		 END LOOP;
  END;
  $$
 
SELECT * FROM new_data_table;
