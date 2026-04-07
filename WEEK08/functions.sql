-- =========================================
-- FUNCTIONS
-- =========================================

-- 1. Search contacts by pattern (раздутый)
CREATE OR REPLACE FUNCTION search_contacts_full(pattern_text TEXT)
RETURNS TABLE (
    contact_id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    phone_number VARCHAR,
    row_num INT
)
AS $$
BEGIN
    IF pattern_text IS NULL OR pattern_text = '' THEN
        RETURN QUERY
        SELECT 
            p.contact_id,
            COALESCE(p.first_name, 'Unknown') AS first_name,
            COALESCE(p.last_name, 'Unknown') AS last_name,
            p.phone_number,
            ROW_NUMBER() OVER (ORDER BY p.contact_id) AS row_num
        FROM phonebook p;
    ELSE
        RETURN QUERY
        SELECT 
            p.contact_id,
            COALESCE(p.first_name, 'Unknown') AS first_name,
            COALESCE(p.last_name, 'Unknown') AS last_name,
            p.phone_number,
            ROW_NUMBER() OVER (ORDER BY p.contact_id) AS row_num
        FROM phonebook p
        WHERE p.first_name ILIKE '%' || pattern_text || '%'
           OR p.last_name ILIKE '%' || pattern_text || '%'
           OR p.phone_number ILIKE '%' || pattern_text || '%';
    END IF;
END;
$$ LANGUAGE plpgsql;


-- 2. Pagination function (раздутый)
CREATE OR REPLACE FUNCTION get_contacts_paginated_full(limit_count INT, offset_count INT)
RETURNS TABLE (
    contact_id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    phone_number VARCHAR,
    row_num INT
)
AS $$
BEGIN
    IF limit_count <= 0 THEN
        limit_count := 10;
    END IF;
    IF offset_count < 0 THEN
        offset_count := 0;
    END IF;

    RETURN QUERY
    SELECT 
        p.contact_id,
        COALESCE(p.first_name, 'Unknown') AS first_name,
        COALESCE(p.last_name, 'Unknown') AS last_name,
        p.phone_number,
        ROW_NUMBER() OVER (ORDER BY p.contact_id) AS row_num
    FROM phonebook p
    ORDER BY p.contact_id
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;