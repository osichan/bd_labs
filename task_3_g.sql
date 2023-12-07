USE lab_3;

DROP TRIGGER IF EXISTS trg_check_paycard;

DELIMITER //
CREATE TRIGGER trg_check_paycard
BEFORE INSERT
 
ON buyer FOR EACH ROW
BEGIN
    IF NEW.paycard REGEXP '00$' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid paycard: Cannot end with two zeros';
    END IF;
END;
//
DELIMITER ;

INSERT INTO buyer (person_id, paycard) VALUES (11, '1234567890123400');

