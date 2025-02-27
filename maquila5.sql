-- Active: 1699156146979@@127.0.0.1@3307@maquila6

/* CREATE DATABASE maquila6;

-- COMANDOS DE USO CONCURRENTE:
use maquila;
SELECT * FROM ;
DROP TABLE  ;

INSERT INTO  ()VALUES
(); */

-- REGLAS DE LA BASE:
-- Cada palabra en los campos empieza con mayuscula excepto "numero" y "metas"; 
-- Las FOREIGN KEYS son las PRIMARY KEYS que solo pasan al singular excepto metas y AreaTrabajo donde se quita la "s" y "De"


-- TABLA: AreasDeTrabajo 
-- Guardar las diferentes areas de tarabajo

CREATE TABLE AreasDeTrabajo (
    numero INT PRIMARY KEY AUTO_INCREMENT, 
    Nombre VARCHAR(30)NOT NULL UNIQUE
)ENGINE=InnoDB;

-- TABLA: Estados
-- Guardar la descripcion de las tareas y actividades

CREATE TABLE Estados (
    numero INT PRIMARY KEY AUTO_INCREMENT, 
    Descripcion VARCHAR(100) NOT NULL
)ENGINE=InnoDB;

-- TABLA: Modelos
-- Guardar los tipos de modelos que trabaja la empresa

CREATE TABLE Modelos (
    numero INT PRIMARY KEY AUTO_INCREMENT, 
    Nombre VARCHAR(30) NOT NULL,
    Descripcion VARCHAR(100) NOT NULL
)ENGINE=InnoDB;

-- TABLA: Piezas
-- Guardar las piezas y la cantidad que tiene la empresa

CREATE TABLE Piezas (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(30) NOT NULL
    ) ENGINE=InnoDB;


-- TABLA: Materiales
-- Guarda el nombre de los materiales que se usan en la empresa

CREATE TABLE Materiales (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(30) NOT NULL,
    Stock INT NOT NULL
) ENGINE=InnoDB;

-- TABLA: Puestos
-- Registra el puesto que ocupa cada empleado en la empresa

CREATE TABLE Puestos (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(30) NOT NULL
) ENGINE=InnoDB;

-- TABLA: Metas
-- Registra los objetivos que quiere realizar la empresa

CREATE TABLE Metas (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    Meta VARCHAR(150) NOT NULL,
    FechaInicio DATE NOT NULL,
    FechaFinal DATE NOT NULL
) ENGINE=InnoDB;

-- TABLA: Tareas
-- Guardar la cantidad de tareas y su orden sobre la bitacora
CREATE Table Tareas (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    Orden VARCHAR(100) NOT NULL,
    AreaTrabajo INT,
    Estado INT,
    CONSTRAINT Foreign Key (AreaTrabajo) REFERENCES AreasDeTrabajo(numero)
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT Foreign Key (Estado) REFERENCES Estados(numero)
    ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;

-- TABLA: Actividades
-- Guardar las actividades que se realizan en la empresa

CREATE TABLE Actividades (
    numero INT PRIMARY KEY AUTO_INCREMENT, 
    Descripcion VARCHAR(100) NOT NULL,
    Tarea INT,
    Estado INT,
    CONSTRAINT Foreign Key (Tarea) REFERENCES Tareas(numero)
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT Foreign Key (Estado) REFERENCES Estados(numero)
    ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;

-- TABLA: Empleados
-- Guardar el tiempo que toman las actividades en la bitcora

CREATE TABLE Empleados (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    Usuario INT,
    NombrePila VARCHAR(30) NOT NULL,
    PrimerApellido VARCHAR(30),
    SegundoApellido VARCHAR(30),
    DirCalle VARCHAR(30) NOT NULL,
    DirNumero VARCHAR(30) NOT NULL,
    DirColonia VARCHAR(30) NOT NULL,
    NumTel VARCHAR(15) NOT NULL,
    Horario VARCHAR(30) NOT NULL,
    JefeArea INT,
    AreaTrabajo INT,
    Puesto INT,
    CONSTRAINT Foreign Key (JefeArea) REFERENCES Empleados(numero)
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT Foreign Key (AreaTrabajo) REFERENCES AreasDeTrabajo(numero)
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT Foreign Key (Puesto) REFERENCES Puestos(numero)
    ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;

-- ALTER TABLE `Empleados` ADD FOREIGN KEY (`Usuario`) REFERENCES `auth_user`(`id`) 
-- ON DELETE CASCADE ON UPDATE CASCADE; 



-- TABLA: Bitacoras
-- Registrar las actividades y metas del empleado

CREATE TABLE Bitacoras (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    Titulo VARCHAR(30) NOT NULL,
    Fecha DATE NULL,
    Empleado INT,
    metas INT,
    CONSTRAINT FOREIGN KEY (Empleado) REFERENCES Empleados(Numero) 
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY (metas) REFERENCES Metas(Numero) 
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB;

-- TABLA: Bit_Tarea
-- Guardar las fechas de las tareas en las bitacoras

CREATE Table Bit_Tarea (
    Bitacora INT,
    Tarea INT,
    FechaInicio DATE NOT NULL,
    FechaFinal DATE,
    HoraInicio TIME NOT NULL,
    HoraFinal TIME,
    CONSTRAINT Foreign Key (Bitacora) REFERENCES Bitacoras(numero)
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT Foreign Key (Tarea) REFERENCES Tareas(numero)
    ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;

-- TABLA: Bit_Act
-- Guardar el tiempo que toman las actividades en la bitcora

CREATE TABLE Bit_Act (
    Bitacora INT, 
    Actividad INT,
    Tiempo TIME NOT NULL,
    CONSTRAINT Foreign Key (Bitacora) REFERENCES Bitacoras(numero)
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT Foreign Key (Actividad) REFERENCES Actividades(numero)
    ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;

-- TABLA: AT_Modelos
-- Guardar las cantidades de modelos en areas de trabajo

CREATE TABLE AT_Modelos (
    Area INT, 
    Modelo INT,
    Cantidad INT NOT NULL,
    CONSTRAINT Foreign Key (Area) REFERENCES AreasDeTrabajo(numero)
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT Foreign Key (Modelo) REFERENCES Modelos(numero)
    ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;

-- TABLA: AT_Piezas
-- Guardar la cantidad de piezas en un en el area de trabajo

CREATE TABLE AT_Piezas (
    Area INT,
    Pieza INT,
    CantidadPieza INT NOT NULL,
    PRIMARY KEY (Area, Pieza),
    CONSTRAINT FOREIGN KEY (Area) REFERENCES AreasDeTrabajo(numero) 
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY (Pieza) REFERENCES Piezas(numero) 
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB;

-- TABLA: Modelo_Piezas
-- Guardar el tiempo que toman las actividades en la bitcora

CREATE TABLE Modelo_Piezas (
    Modelo INT,
    Pieza INT,
    TotalPiezas INT NOT NULL,
    CONSTRAINT Foreign Key (Modelo) REFERENCES Modelos(numero)
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT Foreign Key (Pieza) REFERENCES Piezas(numero)
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB;

-- TABLA: Piezas_Material
-- Registra el tipo material que ocupa cada pieza

CREATE TABLE Piezas_Material (
    Pieza INT,
    Material INT,
    CONSTRAINT FOREIGN KEY (Pieza) REFERENCES Piezas(numero)
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY (Material) REFERENCES Materiales(numero)
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB;

-- TABLA: Errores
-- Registra los errores durante la produccion

CREATE TABLE Errores (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    Descripcion VARCHAR(100) NOT NULL,
    Bitacora INT,
    CONSTRAINT FOREIGN KEY (Bitacora) REFERENCES Bitacoras(numero) 
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB;

-- TABLA: Soluciones
-- Registrar las soluciones planteadas al error

CREATE TABLE Soluciones (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    Descripcion VARCHAR(100) NOT NULL,
    Bitacora INT,
    `Error` INT,
    CONSTRAINT FOREIGN KEY (Bitacora) REFERENCES Bitacoras(numero) 
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY (`Error`) REFERENCES Errores(Numero) 
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB;


/* SELECT CONCAT('DROP TABLE IF EXISTS ', table_name, ';')
FROM information_schema.tables
WHERE table_schema = 'maquila'; */

/* DROP TABLE IF EXISTS Soluciones;
DROP TABLE IF EXISTS Errores;
DROP TABLE IF EXISTS Piezas_Material;
DROP TABLE IF EXISTS Modelo_Piezas;
DROP TABLE IF EXISTS AT_Piezas;
DROP TABLE IF EXISTS Soluciones;
DROP TABLE IF EXISTS Errores;
DROP TABLE IF EXISTS Piezas_Material;
DROP TABLE IF EXISTS Modelo_Piezas;
DROP TABLE IF EXISTS AT_Piezas;
DROP TABLE IF EXISTS AT_Modelos;
DROP TABLE IF EXISTS Bit_Tarea;
DROP TABLE IF EXISTS Bit_Act;
DROP TABLE IF EXISTS Bitacoras;
DROP TABLE IF EXISTS Empleados;
DROP TABLE IF EXISTS Actividades;
DROP TABLE IF EXISTS Tareas;
DROP TABLE IF EXISTS Metas;
DROP TABLE IF EXISTS Puestos;
DROP TABLE IF EXISTS Materiales;
DROP TABLE IF EXISTS Piezas;
DROP TABLE IF EXISTS Modelos;
DROP TABLE IF EXISTS Estados;
DROP TABLE IF EXISTS AreasDeTrabajo;
DROP TABLE IF EXISTS AT_Modelos;
DROP TABLE IF EXISTS Bit_Tarea;
DROP TABLE IF EXISTS Bit_Act;
DROP TABLE IF EXISTS Bitacoras;
DROP TABLE IF EXISTS Empleados;
DROP TABLE IF EXISTS Actividades;
DROP TABLE IF EXISTS Tareas;
DROP TABLE IF EXISTS Metas;
DROP TABLE IF EXISTS Puestos;
DROP TABLE IF EXISTS Materiales;
DROP TABLE IF EXISTS Piezas;
DROP TABLE IF EXISTS Modelos;
DROP TABLE IF EXISTS Estados;
DROP TABLE IF EXISTS AreasDeTrabajo; */

