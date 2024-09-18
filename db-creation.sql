-- Crear la base de datos
CREATE DATABASE employees_db;

-- Usar la base de datos
USE employees_db;

-- Crear la tabla de empleados
CREATE TABLE employees (
    code VARCHAR(50) PRIMARY KEY,
    employee VARCHAR(100),
    email VARCHAR(100)
);

-- Crear la tabla de detalles de empleados
CREATE TABLE employee_details (
    code VARCHAR(50),
    area VARCHAR(100),
    schedule VARCHAR(100),
    FOREIGN KEY (code) REFERENCES employees(code)
);

-- Crear la tabla combinada de empleados
CREATE TABLE employees_combined (
    code VARCHAR(50),
    employee VARCHAR(100),
    email VARCHAR(100),
    area VARCHAR(100),
    schedule VARCHAR(100),
    PRIMARY KEY (code)
);