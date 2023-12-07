USE lab_3;
DROP TRIGGER IF EXISTS trg_update_menu_dish;

CREATE TABLE IF NOT EXISTS `lab_3`.`menu_log` (
  `log_id` INT NOT NULL AUTO_INCREMENT,
  `menu_id` INT NOT NULL,
  `action` VARCHAR(45) NOT NULL,
  `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`log_id`)
)
ENGINE = InnoDB;

DELIMITER //
CREATE TRIGGER trg_menu_log
AFTER UPDATE ON menu
FOR EACH ROW
BEGIN
    INSERT INTO menu_log (menu_id, action)
    VALUES (OLD.id, 'Updated');
END;
//
DELIMITER ;

UPDATE menu SET description = 'New Description' WHERE id = 1;

-- Check the contents of the menu_log table to see the log entry
SELECT * FROM menu_log;