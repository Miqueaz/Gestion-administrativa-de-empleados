-- SQLBook: Code
-- Active: 1699156146979@@127.0.0.1@3307@maquila3

--/=========CONSULTAS==========/

-- 1. Información de un empleado
    -- a. Número del empleado
    -- b. Nombre completo del empleado, en una columna
    -- c. Dirección de empleado, en una columna
    -- d. Número de teléfono
    -- e. Horario de trabajo
    -- f. Nombre del puesto de trabajo
    -- g. Nombre del área de trabajo donde se encuentra

SELECT 
Emp.numero AS Numero_del_empleado,
CONCAT(Emp.NombrePila, ' ', Emp.PrimerApellido, ' ', Emp.SegundoApellido) AS Empleado,
CONCAT(Emp.DirCalle, ' ', Emp.DirNumero, ' ', Emp.DirColonia) AS Dirección,
Emp.NumTel AS Teléfono,
Emp.Horario AS Horario,
P.Nombre AS Puesto,
AT.Nombre AS Area_de_Trabajo
FROM Empleados AS Emp
INNER JOIN Puestos AS P ON Emp.Puesto = P.numero
INNER JOIN AreasDeTrabajo AS AT ON Emp.AreaTrabajo = AT.numero
WHERE Emp.numero = 1;



-- 2. Empleados de un área de trabajo
    -- a. Nombre del área de trabajo
    -- b. Nombre completo del jefe del área de trabajo, en una columna
    -- c. Nombre completo del empleado, en una columna
    -- d. Nombre del puesto de trabajo del empleado

SELECT 
    AT.Nombre AS Area_de_Trabajo,
    CONCAT(EmpJefe.NombrePila, ' ', EmpJefe.PrimerApellido, ' ', EmpJefe.SegundoApellido) AS Jefe_del_Area,
    CONCAT(Emp.NombrePila, ' ', Emp.PrimerApellido, ' ', Emp.SegundoApellido) AS Empleado,
    P.Nombre AS Puesto
FROM 
    Empleados AS Emp
INNER JOIN 
    Empleados AS EmpJefe ON Emp.JefeArea = EmpJefe.numero
INNER JOIN 
    Puestos AS P ON Emp.Puesto = P.numero
INNER JOIN 
    AreasDeTrabajo AS AT ON Emp.AreaTrabajo = AT.numero
WHERE 
    AT.numero = 1;


-- 3. Tareas realizadas en un área de trabajo
    -- a. Nombre del área de trabajo
    -- b. Número de la tarea
    -- c. Descripción de la tarea

   SELECT
    AT.Nombre AS Nombre_Area_Trabajo,
    T.numero AS Numero_Tarea,
    T.orden AS Descripcion_Tarea
FROM
    Tareas AS T
INNER JOIN
    AreasDeTrabajo AS AT ON T.AreaTrabajo = AT.numero
WHERE
    AT.numero = (
        SELECT numero
        FROM AreasDeTrabajo
        WHERE Nombre = 'Almacenamiento');


-- 4. Bitácora de actividades de un empleado
    -- a. Número del empleado
    -- b. Número de la bitácora del empleado
    -- c. Título de la bitácora
    -- d. Descripción de la meta
    -- e. Fecha de inicio de la meta
    -- f. Fecha final de la meta
    -- g. Número de la actividad
    -- h. Descripción de la actividad
    -- i. Tiempo de la actividad

    SELECT 
    Emp.numero as NumEmpleado,
    B.numero as Bitacora,
    B.Titulo as Titulo_Bitacora,
    MT.Meta as Meta_Descripcion,
    MT.FechaInicio as FechaInicioMeta,
    MT.FechaFinal as FechaFinalMeta,
    Act.numero as NumActividad,
    Act.Descripcion as Actividad,
    BA.Tiempo as TiempoDeActividad,
    EST.`Descripcion`
    FROM Empleados as Emp
    INNER JOIN Bitacoras as B on Emp.numero = B.Empleado
    INNER JOIN Metas as MT on B.metas = MT.numero
    INNER JOIN Bit_Act as BA on B.numero = BA.Bitacora
    INNER JOIN Actividades as Act on BA.`Actividad` = Act.numero
    INNER JOIN Estados as EST on Act.`Estado` = EST.numero
    WHERE Emp.numero = 1;

-- 5. Bitácora de tareas de un empleado
    -- a. Número del empleado
    -- b. Número de la bitácora del empleado
    -- c. Título de la bitácora
    -- d. Descripción de la meta
    -- e. Fecha de inicio de la meta
    -- f. Fecha final de la meta
    -- g. Número de la tarea
    -- h. Descripción de la tarea
    -- i. Fecha de inicio de la tarea
    -- j. Fecha final de la tarea

    SELECT 
    Emp.numero as NumEmpleado,
    B.numero as Bitacora,
    B.Titulo as Titulo_Bitacora,
    MT.Meta as Meta_Descripcion,
    MT.FechaInicio as FechaInicioMeta,
    MT.FechaFinal as FechaFinalMeta,
    TR.numero as NumTarea,
    TR.Orden as Tarea,
    BT.FechaInicio as FechaInicioTarea,
    BT.FechaFinal as FechaFinalTarea
    FROM Empleados as Emp
    INNER JOIN Bitacoras as B on Emp.numero = B.Empleado
    INNER JOIN Metas as MT on B.metas = MT.numero
    INNER JOIN Bit_Tarea as BT on B.numero = BT.Bitacora
    INNER JOIN Tareas as TR on B.numero = TR.numero
    WHERE Emp.numero = 1;


-- 6. Bitácora de errores de un empleado
    -- a. Número del empleado
    -- b. Número de la bitácora del empleado
    -- c. Título de la bitácora
    -- d. Descripción de la meta
    -- e. Fecha de inicio de la meta
    -- f. Fecha final de la meta
    -- g. Número del error
    -- h. Descripción del error
    -- i. Número de la solución
    -- j. Descripción de la solución

    SELECT 
    Emp.numero as NumEmpleado,
    B.numero as Bitacora,
    B.Titulo as Titulo_Bitacora,
    MT.Meta as Meta_Descripcion,
    MT.FechaInicio as FechaInicioMeta,
    MT.FechaFinal as FechaFinalMeta,
    ER.numero as NumError,
    ER.Descripcion as `Error`,
    SL.numero as NumSolucion,
    SL.Descripcion as Solucion
    FROM Empleados as Emp
    INNER JOIN Bitacoras as B on Emp.numero = B.Empleado
    INNER JOIN Metas as MT on B.metas = MT.numero
    INNER JOIN Errores as ER on B.numero = ER.Bitacora
    INNER JOIN Soluciones as SL on ER.numero = SL.Error
    WHERE Emp.numero = 1;

-- 7. Modelos realizados en un área de trabajo
    -- a. Nombre del área de trabajo
    -- b. Nombre del modelo
    -- c. Descripción del modelo
    SELECT
    at.nombre AS Nombre_Area_Trabajo,
    m.nombre AS Nombre_Modelo,
    m.descripcion AS Descripcion_Modelo
FROM
    Modelos AS m
INNER JOIN
    AT_Modelos AS am ON m.numero = am.modelo
INNER JOIN
    AreasDeTrabajo AS at ON am.area = at.numero
WHERE at.numero = '5';

-- 8. Piezas utilizadas en un modelo
    -- a. Nombre del modelo
    -- b. Nombre de la pieza utilizada
    -- c. Cantidad de piezas utilizadas
    SELECT
    m.nombre AS Nombre_Modelo,
    p.nombre AS Nombre_Pieza,
    mp.TotalPiezas AS Cantidad_Piezas_Utilizadas
FROM
    Modelo_Piezas AS mp
INNER JOIN
    Modelos AS m ON mp.modelo = m.numero
INNER JOIN 
    Piezas AS p ON mp.pieza = p.numero
WHERE m.numero = 1
GROUP BY Nombre_Pieza;


-- 9. Piezas utilizadas en un área de trabajo
    -- a. Nombre del área de trabajo
    -- b. Nombre de la pieza utilizada
    -- c. Cantidad de piezas utilizadas
 SELECT
    AT.nombre AS Nombre_Area_Trabajo,
    P.nombre AS Nombre_Pieza,
    AP.cantidadPieza AS Cantidad_Piezas_Utilizadas
FROM
    AT_Piezas AS AP
INNER JOIN
    AreasDeTrabajo AS AT ON AP.area = AT.numero
INNER JOIN
    Piezas AS P ON AP.pieza = P.numero
WHERE AT.numero = 1;

-- 10. Materiales utilizados en una pieza
    -- a. Nombre de la pieza
    -- b. Nombre del material utilizado
SELECT
    P.nombre AS Nombre_Pieza,
    M.nombre AS Nombre_Material_Utilizado
FROM
    Piezas AS P
INNER JOIN
    Piezas_Material AS PM ON P.numero = PM.pieza
INNER JOIN
    Materiales AS M ON PM.material = M.numero
WHERE P.numero= 2;

-- Cantidad de empleados en las areas de trabajo

SELECT 
    AT.Nombre AS Area_de_Trabajo,
    COUNT(numero) AS Empleado,
FROM 
    Empleados AS Emp
INNER JOIN 
    AreasDeTrabajo AS AT ON Emp.AreaTrabajo = AT.numero
GROUP BY Area_de_Trabajo;