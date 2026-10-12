**Nombre del proyecto:** Generador Seguro de Contraseñas 
**Integrantes:** Sebastián Guerra

**Fecha:** 11 de Octubre de 2026

**Objetivo del sistema:**
Desarrollar una herramienta basada en Python que mitigue la vulnerabilidad de las cuentas digitales generada por la creación humana de claves. El sistema fuerza el cumplimiento de estándares mínimos para un generador de contraseñas como longitud y variedad de caracteres, para generar cadenas alfanuméricas y de símbolos completamente impredecibles.

**Descripción de funcionalidades:**
El programa opera mediante interacción por consola y cuenta con las siguientes funcionalidades principales:
- **Validación de seguridad:** Bucle estricto que impide la generación de contraseñas con menos de 8 caracteres.
- **Parametrización dinámica:** Permite al usuario decidir la inclusión de caracteres numéricos y símbolos especiales.
- **Generación aleatoria:** Utiliza la librería nativa para seleccionar caracteres al azar iterando sobre la longitud definida, ensamblando una contraseña robusta paso a paso.
