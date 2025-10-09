<div align="right">
  Leia em outros idiomas: 
  <a title="Inglês" href="./README.en.md">🇬🇧</a>
  <a title="Português" href="./README.pt.md">🇧🇷</a>
</div>

# ¿Cansado de la complejidad innecesaria?

- **¿De seguir tutoriales interminables que construyen castillos en el aire con decenas de nodos?**
- **¿De montar buffers con Redis o bases de datos para algo que solo vive unos segundos?**
- **¿De los "vendedores de humo"?**

`gblabs-n8n-buffer` es tu solución. Un buffer simple, potente y directo para sistemas de chat en n8n.

## La verdad sobre las herramientas "No-Code"

n8n es una plataforma maravillosa, sin duda. Nos da una agilidad increíble. Pero seamos honestos: como toda herramienta, tiene sus límites. La falta de orientación a objetos o un paralelismo real nos recuerda algo importante.

El verdadero poder no viene solo de arrastrar y soltar nodos, sino de **entender los fundamentos**. La promesa de que "ya no necesitas saber programar" es el hechizo más común de los vendedores de humo de nuestra era. Muchas de las "soluciones" que verás por ahí, por ejemplo, simplemente descartan mensajes cuando dos conversaciones chocan, un "detalle" que convenientemente omiten.

Este nodo es un pequeño manifiesto. Una prueba de que, con un poco de código y lógica de la vieja escuela, podemos superar las limitaciones nativas para construir soluciones más eficientes y elegantes.

## Saber programar sigue siendo una habilidad indispensable. No te dejes engañar.


![Smoke Seller](./smokeseller.png "Algunos te venden 'soluciones mágicas', nosotros te damos código que funciona.")
<div align="center">
  <em>⚠️ DANGER ⚠️</em>
</div>

## ¿Cómo funciona? La simpleza es poder.

En lugar de montar una infraestructura compleja, nos apoyamos en una de las capacidades más básicas y potentes: **la memoria RAM.**

1.  **Variables Globales**: Usamos una simple variable global en n8n para mantener la cola de mensajes.
2.  **Buffer en RAM**: Cada mensaje nuevo de una sesión se guarda en un array en memoria. Rápido, directo, sin latencia de red ni de disco.
3.  **Timeout Inteligente**: El buffer espera unos segundos (configurable). Si llega un mensaje nuevo, el contador se reinicia. Si pasa el tiempo sin actividad, ¡listo!
4.  **Concatenación y Envío**: Todos los mensajes en el buffer se unen en un solo texto y se envían al siguiente nodo.
5.  **Desaparición Efímera**: Una vez procesado, el buffer de esa sesión se limpia de la RAM. No necesita persistencia porque su propósito es temporal, vive solo por unos segundos.

Es así de simple. Sin bases de datos, sin configuraciones complejas, sin dependencias externas.

## Diagrama de Flujo

```mermaid
graph TD
    A["Start: Mensaje Entrante"] --> B{"Buffer para SessionID existe?"};
    B -- "No" --> C["Crea nuevo buffer para SessionID"];
    C --> D;
    B -- "Sí" --> D["Agrega mensaje y timestamp al buffer"];
    D --> E["Inicia/Reinicia Timeout"];
    E --> F["...espera timeout..."];
    F --> G{"¿Es este el último mensaje recibido?"};
    G -- "Sí<br/>(no llegaron nuevos mensajes)" --> H["Procesa el Buffer"];
    H --> I["1. Concatena todos los mensajes"];
    I --> J["2. Envía el resultado final"];
    J --> K["3. Elimina el buffer de la sesión"];
    K --> L["Fin"];
    G -- "No<br/>(llegó un mensaje nuevo)" --> M["No hace nada<br/>(el nuevo mensaje se encargará)"];
    M --> L;
```

## Instalación

```bash
npm install n8n-nodes-gbplabs-chat-buffer
```
Luego, reinicia tu instancia de n8n.

## Uso

Busca el nodo `Chat Buffer` y agrégalo a tu workflow. Configura los parámetros:

-   **Session ID**: El identificador único de la conversación (ej: `{{ $json.jid }}`).
-   **Message**: El contenido del mensaje a "bufferear" (ej: `{{ $json.textMessageContent }}`).
-   **Timeout (ms)**: Cuántos milisegundos esperar (por defecto: `3000`).
-   **Separator**: El texto que unirá los mensajes (por defecto: `. `).

---

Desarrollado con ❤️ y un poco de rebeldía por:

**Pablo Luis Sánchez Stahlschmidt**  
*gbplabs@gmail.com*
*Desde la nueva tierra de la libertad 🇦🇷*


Y con la invaluable colaboración del gran:

**Federico Pereira**  
*lordbasex@gmail.com*
*Y sí, también desde la nueva tierra de la libertad 🇦🇷*

