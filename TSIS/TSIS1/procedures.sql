-- =========================================
-- PROCEDURES
-- =========================================

-- 1. UPSERT procedure (раздутый)
CREATE OR REPLACE PROCEDURE upsert_contact_full(p_first_name VARCHAR, p_last_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_phone !~ '^[0-9]{11}$' THEN
        RAISE NOTICE 'Invalid phone: %', p_phone;
        RETURN;
    END IF;

    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_first_name AND last_name = p_last_name) THEN
        UPDATE phonebook SET phone_number = p_phone
        WHERE first_name = p_first_name AND last_name = p_last_name;
        RAISE NOTICE 'Updated contact: % %', p_first_name, p_last_name;
    ELSE
        INSERT INTO phonebook(first_name, last_name, phone_number)
        VALUES(p_first_name, p_last_name, p_phone);
        RAISE NOTICE 'Inserted contact: % %', p_first_name, p_last_name;
    END IF;
END;
$$;


-- 2. Mass insert procedure
CREATE OR REPLACE PROCEDURE insert_many_contacts_full(p_first_names TEXT[], p_last_names TEXT[], p_phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    invalid_contacts TEXT := '';
BEGIN
    FOR i IN 1..array_length(p_first_names, 1) LOOP
        IF p_phones[i] ~ '^[0-9]{11}$' THEN
            CALL upsert_contact_full(p_first_names[i], p_last_names[i], p_phones[i]);
        ELSE
            invalid_contacts := invalid_contacts || p_first_names[i] || ' ' || p_last_names[i] || '(' || p_phones[i] || '), ';
        END IF;
    END LOOP;

    IF invalid_contacts <> '' THEN
        RAISE NOTICE 'Invalid contacts skipped: %', invalid_contacts;
    END IF;
END;
$$;


-- 3. Delete procedure
CREATE OR REPLACE PROCEDURE delete_contact_full(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = p_value OR last_name = p_value OR phone_number = p_value;
END;
$$;