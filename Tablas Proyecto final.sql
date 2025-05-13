CREATE TABLE usuario (
id INT PRIMARY KEY,
email VARCHAR (50) NOT NULL,
password VARCHAR (100) NOT NULL,
name VARCHAR (100) NOT NULL
);
CREATE TABLE proyecto (
id INT PRIMARY KEY,
name VARCHAR (100),
description VARCHAR(200),
status VARCHAR (50)
);
CREATE TABLE roles (
id INT PRIMARY KEY,
name_rol VARCHAR (100),
description VARCHAR (200)
);
INSERT INTO roles (id, name_rol, description) VALUES
(1, 'PMO', 'Project Management Officer'),
(2, 'Scrum Master', 'Facilitador del equipo Scrum'),
(3, 'Desarrollador', 'Encargado del desarrollo de software');
CREATE TABLE historia_usuario (
    id INT PRIMARY KEY,
    titulo VARCHAR(100),
    proyecto_id INT,
    estado VARCHAR(50),
    puntos_historia INT,
    tiempo_estimado INT,
    user_id INT,
    scrum_master_id INT,
    FOREIGN KEY (proyecto_id) REFERENCES proyecto(id),
    FOREIGN KEY (user_id) REFERENCES usuario(id),
    FOREIGN KEY (scrum_master_id) REFERENCES usuario(id)
);
CREATE TABLE tarea (
    id INT PRIMARY KEY,
    historial_usuario_id INT,
    descripcion TEXT,
    estado VARCHAR(50),
    FOREIGN KEY (historial_usuario_id) REFERENCES historia_usuario(id)
);
CREATE TABLE historial (
    id INT PRIMARY KEY,
    tarea_id INT,
    usuario_id INT,
    accion VARCHAR(100),
    fecha DATE,
    detalles TEXT,
    modulo VARCHAR(100),
    FOREIGN KEY (tarea_id) REFERENCES tarea(id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);
CREATE TABLE usuario_proyecto (
proyecto_id INT,
rol_id INT,
usuario_id INT,
  PRIMARY KEY (proyecto_id, usuario_id),
  FOREIGN KEY (proyecto_id) REFERENCES proyecto(id),
  FOREIGN KEY (rol_id) REFERENCES roles(id),
  FOREIGN KEY (usuario_id) REFERENCES usuario(id));
CREATE TABLE invitacion (
  id INT PRIMARY KEY,
  email VARCHAR(50) NOT NULL,
  proyecto_id INT,
  status VARCHAR(20),
  token VARCHAR(100),
  FOREIGN KEY (proyecto_id) REFERENCES proyecto(id)
);








