-- Total de usuários por grupo experimental
SELECT group_name, COUNT(DISTINCT user_id) AS total_users
FROM experiment_participants
GROUP BY group_name;

-- Eventos por etapa do funil
SELECT event_name, COUNT(*) AS total_events
FROM events
GROUP BY event_name
ORDER BY total_events DESC;

-- Usuários únicos por grupo e etapa
SELECT p.group_name, e.event_name, COUNT(DISTINCT e.user_id) AS unique_users
FROM experiment_participants p
JOIN events e ON p.user_id = e.user_id
GROUP BY p.group_name, e.event_name
ORDER BY p.group_name, unique_users DESC;
