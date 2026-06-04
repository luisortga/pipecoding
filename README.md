![image alt](https://github.com/luisortga/pipecoding/blob/3ee869390c47e1bdce5c17cfbecbb3802d995daf/preview.png)

![image alt](https://github.com/luisortga/pipecoding/blob/b1119b90c5d3d9b56664d30bdbbb399936c72449/preview_precaucioin.png)

![image alt](https://github.com/luisortga/pipecoding/blob/45cdd8e107d9c9eabd664c4997ef79da794ff807/preview_error.png)

# pipecoding

## Overview

PipeCoding is a console-based application developed for performing basic piping calculations for **Carbon Steel** and **Stainless Steel** piping systems according to the following international standards:

* ASME B36.10M – Welded and Seamless Wrought Steel Pipe
* ASME B36.19M – Stainless Steel Pipe
* ASME B16.9 – Factory-Made Wrought Butt-Welding Fittings

The application is designed to support piping information commonly found in engineering drawings and material take-offs (MTOs) used by companies such as **PEMEX**, **ICA Fluor**, **Bonatti**, and **Techint**.

---

## Features

* Parse piping specifications from engineering documents.
* Calculate fitting take-outs and center-to-face dimensions.
* Support calculations for:

  * 90° Elbows
  * 45° Elbows
  * Pipe lengths
  * Pipe schedules
  * Nominal Pipe Sizes (NPS)
* Estimate theoretical pipe weight:

  * Weight per meter
  * Total weight
* Support Carbon Steel and Stainless Steel piping systems.

---

## Supported Standards

### Piping Dimensions

* ASME B36.10M

  * Carbon Steel Pipe
  * Alloy Steel Pipe
  * Standard, XS, XXS and Schedule Pipes

* ASME B36.19M

  * Stainless Steel Pipe
  * Schedule 5S
  * Schedule 10S
  * Schedule 40S
  * Schedule 80S

### Materials

#### Carbon Steel

* ASTM A106 Grade B
* ASTM A53 Grade B

#### Stainless Steel

* ASTM A312 TP304
* ASTM A312 TP304L
* ASTM A312 TP316
* ASTM A312 TP316L
* ASTM A358 Grade 304/304L

---

## Example Inputs

```text
10 Pipes, EFW + 100% RT, ASME C3ZCF0T2 6.6 M B36.19/B36.10, ASTM A358 Gr.304/304L Cl.1, BE, -, Imp Tested -196°C, Cryo Serv., S-10S

3 Pipes, Seamless, ASME C4LZMEW8 0.7 M B36.19/B36.10, ASTM A312 Gr.TP304/304L, BE, -, Cryo Serv., S-10S

2 Pulgadas TUBO CED. XS S/COST. A.C. A106 B 5356033 SCA 16.9 M

TUBO CED. XS S/COST. A.C. A106 B 1.1/2 Pulgadas 5356033 SCA 1.8 M
```

---

## Project Structure

```text
Pipecoding/
│
├── src/
│   ├── main.py
│   ├── pipe_funciones.py
│   └── diseño.py
│
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/luisortga/pipecoding.git
cd pipecoding
```

### Install Dependencies

```bash
pip install rich
```

---

## Running the Application

```bash
python src/main.py
```

---

## Docker

Build the image:

```bash
docker build -t pipecoding .
```

Run the container:

```bash
docker run -it pipecoding
```

---

## Technologies

* Python 3.x
* Rich
* Docker

---

## Author @luisortga

PipeCoding was developed as an educational and professional tool for piping engineering calculations and fabrication support.

# Español

# pipecoding

## Descripción General

PipeCoding es una aplicación de consola desarrollada para realizar cálculos básicos de tuberías de **Acero al Carbón** y **Acero Inoxidable**, basada en estándares internacionales utilizados en ingeniería, fabricación y construcción industrial.

El programa trabaja con especificaciones de tubería presentes en planos, listas de materiales (MTO) y documentos técnicos utilizados por empresas como **PEMEX**, **ICA Fluor**, **Bonatti** y **Techint**.

---

## Características

* Interpretación de especificaciones de tubería.
* Cálculo de avances y dimensiones de accesorios.
* Soporte para:

  * Codos de 90°
  * Codos de 45°
  * Longitudes de tubería
  * Cédulas (Schedules)
  * Diámetros nominales (NPS)
* Cálculo de peso teórico:

  * Peso por metro
  * Peso total
* Compatibilidad con tuberías de acero al carbón e inoxidable.

---

## Normas Soportadas

### Dimensiones de Tubería

#### ASME B36.10M

Norma para tuberías de:

* Acero al carbón
* Acero aleado
* Tubería estándar
* Cédula XS
* Cédula XXS
* Schedules comerciales

#### ASME B36.19M

Norma para tuberías de acero inoxidable:

* Schedule 5S
* Schedule 10S
* Schedule 40S
* Schedule 80S

#### ASME B16.9

Accesorios soldados a tope:

* Codos 45°
* Codos 90°
* Tees
* Reducciones
* Caps

---

## Materiales Considerados

### Acero al Carbón

* ASTM A106 Grado B
* ASTM A53 Grado B

### Acero Inoxidable

* ASTM A312 TP304
* ASTM A312 TP304L
* ASTM A312 TP316
* ASTM A312 TP316L
* ASTM A358 Grado 304/304L

---

## Ejemplos de Entrada

```text
10 Pipes, EFW + 100% RT, ASME C3ZCF0T2 6.6 M B36.19/B36.10, ASTM A358 Gr.304/304L Cl.1, BE, -, Imp Tested -196°C, Cryo Serv., S-10S

3 Pipes, Seamless, ASME C4LZMEW8 0.7 M B36.19/B36.10, ASTM A312 Gr.TP304/304L, BE, -, Cryo Serv., S-10S

2 Pulgadas TUBO CED. XS S/COST. A.C. A106 B 5356033 SCA 16.9 M

TUBO CED. XS S/COST. A.C. A106 B 1.1/2 Pulgadas 5356033 SCA 1.8 M
```

---

## Estructura del Proyecto

```text
Pipecoding/
│
├── src/
│   ├── main.py
│   ├── pipe_funciones.py
│   └── diseño.py
│
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## Instalación

### Clonar Repositorio

```bash
git clone https://github.com/luisortga/pipecoding.git
cd pipecoding
```

### Instalar Dependencias

```bash
pip install rich
```

---

## Ejecución

```bash
python src/main.py
```

---

## Docker

Construir la imagen:

```bash
docker build -t pipecoding .
```

Ejecutar el contenedor:

```bash
docker run -it pipecoding
```

---

## Tecnologías Utilizadas

* Python 3.x
* Rich
* Docker

---

## Objetivo del Proyecto

PipeCoding busca facilitar cálculos rápidos de tubería para estudiantes, diseñadores de tuberías, proyectistas, supervisores de obra y profesionales de ingeniería mecánica involucrados en proyectos industriales, petroquímicos y energéticos.

