USE lab_3;

DROP PROCEDURE IF EXISTS get_avg;

DELIMITER //

CREATE PROCEDURE `get_avg`(
  IN operation VARCHAR(3)
)
BEGIN
  DECLARE result INT;
  SET result = calculate_rate(operation);
  SELECT result;
END//

DELIMITER ;

CALL get_avg("max");