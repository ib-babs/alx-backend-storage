-- Trigger to decrease item quantity
CREATE TRIGGER decrease_quantity
AFTER
INSERT on orders FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE NAME = NEW.item_name;