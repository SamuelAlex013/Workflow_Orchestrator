# N8N Kafka Enhanced Nodes

Улучшенные Kafka ноды для n8n с ручным управлением offset'ами, основанные на существующей n8n Kafka ноде.

## 🎯 Подход

Вместо создания библиотеки с нуля, мы модифицируем существующую n8n Kafka ноду, добавляя:

1. **Опцию ручного управления offset'ами** в Kafka Trigger
2. **Возможность коммита offset'ов** в Kafka Response ноде
3. **Автоматический timeout и retry механизм** для обработки зависших сообщений

## ✨ Ключевые особенности

- **🔧 Основана на существующей n8n Kafka ноде** - использует проверенную архитектуру
- **⚙️ Опциональное управление offset'ами** - можно включить/выключить через настройки
- **🛡️ Надежность** - сообщения не теряются при ошибках
- **🔄 Обратная совместимость** - работает как стандартная Kafka нода при отключенном ручном управлении
- **📊 Простота использования** - минимальные изменения в workflow
- **⏰ Автоматический timeout** - обработка зависших сообщений с retry механизмом
- **🚨 Защита от бесконечных циклов** - автоматический коммит при превышении лимита попыток

## 🚀 Установка

```bash
npm install n8n-nodes-kafka-enhanced
```

## 📋 Использование

### 1. Kafka Trigger (Enhanced)

Настройте триггер с опцией **Manual Offset Management**:

- **Topic**: имя топика Kafka
- **From Beginning**: читать с начала топика
- **Manual Offset Management**: ✅ **ВКЛЮЧИТЬ** для ручного управления offset'ами
- **Session ID**: уникальный идентификатор сессии
- **Message Timeout (minutes)**: таймаут обработки сообщения (по умолчанию: 5 минут)
- **Max Retries**: максимальное количество попыток (по умолчанию: 3)
- **Auto Commit on Timeout**: автоматически коммитить offset при превышении лимита попыток

### 2. Kafka Response (Enhanced)

В конце workflow добавьте ноду Kafka Response:

#### Действия в Response ноде:

- **Commit Offset** - подтвердить успешную обработку и закоммитить offset
  - ✅ Offset коммитится
  - ✅ Сообщение считается обработанным
  - ✅ Не будет повторно обработано при перезапуске

- **Mark Failed** - пометить как неудачную (offset НЕ коммитится)
  - ❌ Offset НЕ коммитится
  - 🔄 Сообщение будет обработано заново при перезапуске
  - 🔄 Будет повторно обработано через timeout механизм

#### Автоматически подтягивается из контекста:
- `messageId` - ID сообщения
- `topic` - топик Kafka
- `partition` - партиция
- `offset` - offset сообщения
- `retryCount` - количество попыток
- `isRetry` - это повторная попытка?
- `sessionId` - ID сессии
- `consumerGroupId` - ID группы потребителей

## 🔄 Workflow пример

```
Kafka Trigger (Enhanced) → Process Data → Validate → Kafka Response (Commit Offset)
    [Manual Offset: ON]       ↓
                         Error Handler → Kafka Response (Mark Failed)
```

## ⚙️ Настройки для надежности

### Рекомендуемые настройки:

1. **Manual Offset Management**: ✅ Включено
2. **Message Timeout**: 5 минут
3. **Max Retries**: 3 попытки
4. **Auto Commit on Timeout**: ✅ Включено
5. **Error Handler**: обязательный для всех workflow

### Настройки по умолчанию:

- **Message Timeout**: 5 минут
- **Max Retries**: 3 попытки
- **Auto Commit on Timeout**: включено

## 🚨 Обработка ошибок и timeout

### Что происходит при ошибке:

1. **Ошибка в workflow без Error Handler**:
   - ⏰ Сообщение попадает в timeout механизм
   - 🔄 Через 5 минут (по умолчанию) сообщение повторно обрабатывается
   - 🔄 Максимум 3 попытки (по умолчанию)
   - ✅ После 3 неудачных попыток offset автоматически коммитится

2. **Ошибка с Error Handler**:
   - ❌ Error Handler получает сообщение
   - 🎯 Error Handler должен подключить Kafka Response с действием "Mark Failed"
   - 🔄 Сообщение будет обработано заново

3. **Успешная обработка**:
   - ✅ Kafka Response с действием "Commit Offset"
   - ✅ Offset коммитится
   - ✅ Сообщение считается обработанным

## 📊 Мониторинг и логирование

### Логи в консоли:

- `Retrying message {messageId}, attempt {count}` - повторная попытка
- `Max retries exceeded for message {messageId}, taking action` - превышен лимит попыток
- `Committed offset for failed message {messageId}` - коммит после timeout

### Рекомендации по мониторингу:

1. **Настройте алерты** на превышение timeout
2. **Отслеживайте количество retry** в логах
3. **Мониторьте pending сообщения** в Kafka

## 🔧 Технические детали

### Kafka Trigger
- Использует `autoCommit: false` при включенном ручном управлении
- Передает контекст с consumer reference для коммита
- Сохраняет все настройки существующей n8n Kafka ноды
- Добавляет timeout механизм с retry логикой

### Kafka Response
- Получает consumer reference из контекста
- Выполняет `consumer.commitOffsets()` при успешной обработке
- Не коммитит offset при ошибках, позволяя повторить обработку
- Автоматически подтягивает всю информацию из контекста

### Timeout механизм
- Проверяет pending сообщения каждые 30 секунд
- Retry при превышении timeout
- Автоматический коммит при превышении лимита попыток

## 📖 Документация

- [n8n Kafka Documentation](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kafka/)
- [KafkaJS Documentation](https://kafka.js.org/)

## Лицензия

MIT