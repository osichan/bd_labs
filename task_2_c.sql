USE lab_3;

DROP FUNCTION IF EXISTS calculate_rate;

DELIMITER //

CREATE FUNCTION `calculate_rate`(
  operation VARCHAR(3)
) RETURNS int
    READS SQL DATA
BEGIN
    DECLARE result DECIMAL DEFAULT 0.0;

    IF operation = 'min' THEN
        SELECT MIN(rate) INTO result FROM object;
    ELSEIF operation = 'max' THEN
        SELECT MAX(rate) INTO result FROM object;
    ELSEIF operation = 'avg'  THEN
        SELECT AVG(rate) INTO result FROM object;
    ELSEIF operation = 'sum'  THEN
        SELECT SUM(rate) INTO result FROM object;
    END IF;

    RETURN result;
END //

DELIMITER ;

SELECT calculate_rate('avg');
