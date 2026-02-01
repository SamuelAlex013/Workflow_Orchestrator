# Memory State Node for n8n

Un nodo personalizado para n8n que proporciona funcionalidad de almacenamiento de estado en memoria RAM con concurrencia segura.

## Características

- ✅ **Almacenamiento en memoria**: Los datos se almacenan en la RAM durante la ejecución del workflow
- ✅ **Concurrencia segura**: Utiliza async-mutex para evitar condiciones de carrera
- ✅ **Validación estricta**: Solo acepta objetos JSON válidos (no arrays, no primitivos, no null)
- ✅ **Cinco operaciones**: Set, Get, Get with Default, Delete, Keys
- ✅ **Singleton**: Una única instancia de memoria compartida entre todas las ejecuciones

## Instalación

Seguí la [guía de instalación](https://docs.n8n.io/integrations/community-nodes/installation/) en la documentación de nodos de comunidad de n8n.


## Uso

### Operaciones disponibles

#### 1. Set
Almacena un objeto JSON en memoria para una clave específica.

**Parámetros:**
- `key` (string): La clave para almacenar el valor
- `value` (JSON object): El objeto JSON a almacenar

**Entrada de ejemplo:**
```json
{
  "key": "session:123",
  "value": {
    "userId": 123,
    "state": "awaiting_input",
    "lastAction": "login"
  }
}
```

**Salida:**
```json
{
  "key": "session:123",
  "value": {
    "userId": 123,
    "state": "awaiting_input",
    "lastAction": "login"
  }
}
```

#### 2. Get
Recupera un valor almacenado por su clave.

**Parámetros:**
- `key` (string): La clave a buscar

**Entrada de ejemplo:**
```json
{
  "key": "session:123"
}
```

**Salida (si existe):**
```json
{
  "key": "session:123",
  "value": {
    "userId": 123,
    "state": "awaiting_input",
    "lastAction": "login"
  }
}
```

**Salida (si no existe):**
```json
{
  "key": "session:123",
  "value": null
}
```

#### 3. Get with Default
Recupera un valor almacenado o devuelve un valor por defecto si la clave no existe. **IMPORTANTE**: Si la clave no existe, automáticamente almacena el valor por defecto en la memoria para futuras consultas.

**Parámetros:**
- `key` (string): La clave a buscar
- `defaultValue` (JSON object): El valor por defecto a devolver y almacenar si la clave no existe

**Entrada de ejemplo:**
```json
{
  "key": "user:456",
  "defaultValue": {
    "state": "new",
    "preferences": {}
  }
}
```

**Salida (si la clave no existe - el defaultValue se almacena automáticamente):**
```json
{
  "key": "user:456",
  "value": {
    "state": "new",
    "preferences": {}
  }
}
```

#### 4. Delete
Elimina una clave del almacén en memoria.

**Parámetros:**
- `key` (string): La clave a eliminar

**Entrada de ejemplo:**
```json
{
  "key": "session:123"
}
```

**Salida (siempre exitosa):**
```json
{
  "key": "session:123",
  "success": true
}
```

#### 5. Keys
Lista todas las claves almacenadas con capacidad de filtrado opcional y recuperación de valores.

**Parámetros:**
- `getValues` (boolean, opcional): Si incluir los valores junto con las claves (por defecto: false)
- `filterPattern` (string, opcional): Patrón regex para filtrar las claves

**Entrada de ejemplo (solo claves):**
```json
{
  "getValues": false,
  "filterPattern": ""
}
```

**Salida (solo claves):**
```json
[
  {"key": "session:123"},
  {"key": "user:456"},
  {"key": "config:theme"}
]
```

**Entrada de ejemplo (claves con valores):**
```json
{
  "getValues": true,
  "filterPattern": "^user:.*"
}
```

**Salida (claves filtradas con valores):**
```json
[
  {
    "key": "user:456",
    "value": {
      "state": "new",
      "preferences": {}
    }
  }
]
```

**Ejemplos de filtrado:**
- `""` (vacío): Lista todas las claves
- `^session:.*`: Claves que empiecen con "session:"
- `.*:config$`: Claves que terminen con ":config"
- `user_\d+`: Claves que contengan "user_" seguido de números

## Validaciones y restricciones

### Valores válidos
- ✅ Objetos JSON: `{"key": "value"}`
- ✅ Objetos anidados: `{"user": {"id": 123, "name": "John"}}`
- ✅ Objetos vacíos: `{}`

### Valores no válidos
- ❌ Arrays: `[1, 2, 3]`
- ❌ Primitivos: `"string"`, `123`, `true`
- ❌ Null: `null`
- ❌ Undefined: `undefined`

### Claves
- Las claves se almacenan como strings
- Los espacios en blanco al inicio y final se eliminan automáticamente
- Se permiten caracteres especiales: `:`, `-`, `_`, `.`, `/`, `@`, espacios

## Comportamiento de concurrencia

El nodo utiliza `async-mutex` para garantizar que las operaciones concurrentes sean seguras:

- ✅ Múltiples operaciones `set` concurrentes no corrompen los datos
- ✅ Operaciones mixtas (`set`, `get`, `delete`) son thread-safe
- ✅ No hay condiciones de carrera entre operaciones

## Desarrollo

### Estructura del proyecto

```
├── src/
│   └── MemoryStore.ts          # Implementación del almacén en memoria
├── nodes/
│   └── MemoryState/
│       ├── MemoryState.node.ts  # Implementación del nodo n8n
│       └── memorystate.svg      # Icono del nodo
├── tests/
│   ├── MemoryStore.test.ts      # Tests del almacén
│   └── MemoryState.node.test.ts # Tests del nodo
└── dist/                        # Archivos compilados
```

### Scripts disponibles

```bash
# Ejecutar tests
npm test

# Compilar el proyecto
npm run build

# Desarrollo con recarga automática
npm run dev

# Linting
npm run lint
npm run lintfix

# Formateo
npm run format
```

### Ejecutar tests

```bash
npm test
```

Los tests incluyen:
- Tests unitarios de todas las operaciones
- Tests de validación de entrada
- Tests de concurrencia con alta carga
- Tests de integridad de datos

## Limitaciones

1. **Persistencia**: Los datos solo existen mientras n8n esté ejecutándose. Se pierden al reiniciar.
2. **Memoria**: Los datos se almacenan en RAM, por lo que el consumo de memoria aumenta con el volumen de datos.
3. **Alcance**: El almacén es global para toda la instancia de n8n (singleton).
4. **Sin TTL**: No hay expiración automática de claves (no implementado por requerimiento).

## Casos de uso recomendados

- ✅ Cache temporal de sesiones de usuario
- ✅ Almacenamiento de estado entre pasos de workflow
- ✅ Contador de requests o rate limiting
- ✅ Datos de configuración temporales
- ✅ Cache de respuestas de APIs externas (durante la ejecución)

## Casos de uso NO recomendados

- ❌ Almacenamiento persistente de datos críticos
- ❌ Datos que deben sobrevivir al reinicio de n8n
- ❌ Grandes volúmenes de datos (limitado por RAM)
- ❌ Datos que requieren particionado por usuario/tenant

## Troubleshooting

### Error: "Value must be a non-null JSON object"
- Asegúrate de que el valor sea un objeto JSON válido
- No uses arrays `[]`, primitivos (`string`, `number`, `boolean`) o `null`

### Error: "Key is required and cannot be empty"
- Proporciona una clave no vacía
- Las claves con solo espacios se consideran vacías

### El nodo no aparece en n8n
- Verifica que el archivo esté correctamente copiado
- Reinicia n8n después de la instalación
- Revisa los logs de n8n para errores de carga

### Tests fallan
- Ejecuta `npm install` para instalar dependencias
- Verifica que tienes Node.js 20.15+ instalado
- Ejecuta `npm run build` antes de los tests

## Licencia

MIT License - Ver archivo LICENSE.md para detalles.
