USE lab_3;
DROP TRIGGER IF EXISTS trg_block_person_modification;

DELIMITER //
CREATE TRIGGER trg_block_person_modification
BEFORE UPDATE ON person
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modification of data in the person table is not allowed';
END;
//
DELIMITER ;

UPDATE person SET email = 'updated.email@example.com' WHERE id = 1;
