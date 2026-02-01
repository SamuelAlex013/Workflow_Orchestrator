# n8n-nodes-custom-email-send

[![npm version](https://badge.fury.io/js/n8n-nodes-send-email-personalizado.svg)](https://www.npmjs.com/package/n8n-nodes-send-email-personalizado)
[![npm downloads](https://img.shields.io/npm/dt/n8n-nodes-send-email-personalizado.svg)](https://www.npmjs.com/package/n8n-nodes-send-email-personalizado)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este paquete incluye un nodo personalizado para [n8n](https://n8n.io) que permite **enviar correos electrónicos avanzados usando credenciales SMTP** ya configuradas en n8n, con soporte para **cabeceras personalizadas** y funcionalidades orientadas principalmente a la gestión de listas de correo y cumplimiento de buenas prácticas de email marketing.

---

## 🎯 Propósito principal

Este nodo fue creado principalmente para facilitar el uso de la cabecera **List-Unsubscribe** en tus envíos, permitiendo agregarla fácilmente desde el campo de encabezados personalizados. Así, puedes cumplir con los requisitos de plataformas como Gmail y Outlook para la gestión de bajas automáticas en listas de correo.

---

## ✨ Funcionalidades

- Envío de correos por SMTP usando credenciales de n8n
- Soporte para **cabeceras personalizadas** en formato JSON (ejemplo: `List-Unsubscribe`)
- **Modo de prueba**: Envía correos de prueba a una dirección específica sin afectar destinatarios reales
- **Validación robusta**: Validación automática de formato de emails
- Por defecto, el campo de encabezados personalizados incluye las cabeceras `List-Unsubscribe` y `List-Unsubscribe-Post` recomendadas para facilitar la baja automática
- Soporte para:
  - Texto y/o HTML en el cuerpo del correo
  - Adjuntos (archivos y eventos de calendario `.ics`)
  - CC y BCC (copias y copias ocultas)
  - Reply-To personalizado
  - Fecha personalizada de envío
  - Ignorar problemas SSL (para servidores con certificados autofirmados)
  - Prioridad del correo (alta, normal, baja)
  - In-Reply-To y References (para hilos de correo)
  - Opción para incluir créditos del autor al final del mensaje (opcional)
- Basado en **nodemailer**

---

## 🧪 Ejemplo de uso

1. Añade el nodo **Enviar Email Personalizado** a tu flujo en n8n.
2. Configura los campos principales:
   - Dirección de destino (`toEmail`)
   - Asunto (`subject`)
   - Formato de correo (`emailFormat`: texto, HTML o ambos)
   - Mensaje (`text` y/o `html`)
3. Opcionalmente, configura:
   - **Cabeceras personalizadas** en formato JSON (por defecto ya incluye List-Unsubscribe):
     ```json
     {
       "List-Unsubscribe": "<mailto:unsubscribe@tudominio.com>",
       "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
     }
     ```
   - Adjuntos: rutas de archivos separados por coma o contenido de evento de calendario (ICS).
   - **Modo de prueba**: Activa el modo de prueba con email específico y prefijo personalizable para el asunto.
   - CC/BCC: correos separados por coma.
   - Reply-To: dirección de respuesta.
   - Fecha personalizada.
   - Prioridad del correo.
   - In-Reply-To y References.
   - Opción para incluir créditos del autor.

---

## ⚙️ Opciones disponibles

- **Encabezados personalizados (JSON)**: Permite definir cualquier cabecera extra. Por defecto incluye las cabeceras recomendadas para List-Unsubscribe.
- **Modo de prueba**: Envía emails de prueba a una dirección específica sin afectar destinatarios reales, con prefijo personalizable en el asunto (por defecto `[TEST]`).
- **Adjuntos**: Rutas de archivos o binarios de n8n.
- **Evento de calendario (ICS)**: Pega el contenido de un archivo `.ics` para enviar invitaciones de calendario.
- **Correo CC/BCC**: Para enviar copias y copias ocultas.
- **Reply-To Email**: Dirección de respuesta.
- **Fecha personalizada**: Fecha de envío.
- **Ignorar problemas SSL**: Permite conexiones inseguras (solo si confías en el servidor).
- **Prioridad**: Alta, normal o baja.
- **In-Reply-To**: Message-ID al que responde este correo.
- **References**: IDs de mensajes previos para hilos.
- **Incluir créditos del autor**: Añade una línea de crédito al final del mensaje (opcional).

--- 

## 🚀 Cómo agregar este nodo a tus flujos de n8n (Community Nodes)

1. **Instala el paquete en tu instancia de n8n:**

   Ve a **Settings > Community Nodes** en tu instancia de n8n y haz clic en **Install Community Node**.  
   Busca o pega el nombre del paquete:

   ```
   n8n-nodes-custom-email-send
   ```

   O instala desde terminal en la carpeta de tu n8n:

   ```bash
   npm install n8n-nodes-custom-email-send
   ```

  Marca la casilla **"I understand the risks"** para continuar con la instalación.

2. **Reinicia n8n** si es necesario para que el nodo aparezca en el editor.

---

> **Nota:**  
> Si no ves el nodo tras instalarlo, asegúrate de estar usando una versión de n8n compatible con Community Nodes y de haber reiniciado

## 📝 Notas

- El campo de encabezados personalizados incluye por defecto las cabeceras `List-Unsubscribe` y `List-Unsubscribe-Post` recomendadas para facilitar la baja automática en clientes de correo como Gmail y Outlook. Puedes editarlas o borrarlas según tus necesidades.
- Puedes ingresar múltiples correos en los campos `to`, `cc` y `bcc` separados por coma.
- Para adjuntos binarios, usa los helpers de n8n o rutas absolutas.

---
---

## � Working On

**🧪 Testing con Jest (En progreso)**
- Implementación de tests unitarios para todas las funciones de utilidad
- Cobertura completa de las 9 funciones principales (`parseEmails`, `validateEmail`, `buildEmailContent`, etc.)
- Tests de casos extremos y validación de errores
- Configuración de Jest para TypeScript

*El objetivo es asegurar la calidad y confiabilidad del código refactorizado antes de la release final de v1.2.0.*

---

## �📋 Changelog

### v1.2.0 (03-08-2025) 🚧 **[EN TESTING]**
**Refactorización mayor - Código limpio y modular:**
- 🏗️ **Arquitectura mejorada**: Código completamente refactorizado siguiendo principios de clean code
- 📁 **Separación de responsabilidades**: Código organizado en módulos (`email.utils.ts`, `email.types.ts`)
- 🔧 **Funciones de utilidad**: 9 funciones puras y reutilizables para procesamiento de emails
- 🛡️ **TypeScript mejorado**: Tipado más robusto y interfaces bien definidas
- 🧪 **Preparado para testing**: Estructura modular lista para pruebas unitarias
- 🔍 **Mantenibilidad**: Código más limpio, legible y fácil de mantener

**Mejoras técnicas:**
- ✨ Funciones extraídas: `parseEmails`, `validateEmail`, `buildEmailContent`, etc.
- 📦 Constantes organizadas: `EMAIL_FORMATS`, `PRIORITIES`, `DEFAULT_HEADERS`

> **⚠️ Nota**: Esta versión está en fase de testing. Aunque mantiene total compatibilidad, se recomienda probar en entorno de desarrollo antes de usar en producción.

### v1.1.0
**Nuevas funcionalidades:**
- ✨ **Modo de prueba**: Permite enviar emails de prueba a una dirección específica sin afectar los destinatarios reales
- 🎯 **Prefijo personalizable**: El modo de prueba permite configurar un prefijo personalizado para el asunto (por defecto `[TEST]`) o dejarlo vacío para mantener el asunto original
- 🔧 **Validación mejorada**: Validación más robusta de direcciones de email
- 📝 **Campo JSON mejorado**: Los encabezados personalizados ahora usan tipo JSON para mejor validación y formato

**Mejoras:**
- 📧 El modo de prueba tiene prefijo configurable y email de prueba obligatorio
- 🗑️ En modo de prueba se eliminan CC, BCC y Reply-To para evitar envíos accidentales
- 📊 La respuesta incluye información sobre si se usó modo de prueba y los destinatarios originales

### v1.0.1
- 🚀 Versión inicial con soporte para encabezados personalizados y funcionalidades básicas de SMTP

---

## 👨‍💻 Autor

**Desarrollado por Cristianemek**  
[GitHub](https://github.com/cristianemek)