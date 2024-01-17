-- Create or update user_0d_1 with all privileges
-- Grant all privileges to user_0d_1
-- Flush privileges to apply changes
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';
FLUSH PRIVILEGES;
