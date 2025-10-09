# Avito n8n Custom Node

[English](#english) | [Русский](#русский)

---

## English

### 🚀 Overview

**Avito n8n Custom Node** is a powerful custom node for n8n automation platform that provides seamless integration with Avito API for Business. This node adds convenient functionality for working with Avito API directly in the n8n interface, solving critical authentication and token management issues.

### ✨ Key Features

- **🔧 Convenient API Integration**: Direct access to Avito API functionality within n8n interface
- **🔑 Automatic Token Management**: Solves the 403 Forbidden token refresh problem that standard HTTP Request node cannot handle
- **📊 Comprehensive API Coverage**: Support for Items, Promotions, Ratings & Reviews, and Autoload resources
- **⚡ Built-in Rate Limiting**: Intelligent request throttling to respect API limits
- **🛡️ Robust Error Handling**: Detailed error messages and automatic retry mechanisms

### 🎯 Problem Solved

This node specifically addresses a critical limitation in n8n's standard OAuth2 implementation:

- **Standard HTTP Request node** cannot select custom error codes for token refresh
- **Avito API returns 403 Forbidden** when tokens expire, but n8n only handles 401 Unauthorized by default
- While technically possible to create Avito credentials with HTTP Request node, **tokens must be manually recreated every 24 hours**, which is extremely inconvenient
- **This node completely solves this problem** with automatic token refresh on 403 status codes

### 📋 Supported Avito API Methods

#### 🏠 **Items (Объявления)**
- `GET /items/v2/list` - Get user items list
- `GET /items/v2/item/{itemId}` - Get item information
- `PUT /items/v1/item/{itemId}/price` - Update item price
- `POST /items/v1/item/{itemId}/vas` - Apply additional services (VAS)
- `GET /items/v1/vas/prices` - Get VAS prices
- `GET /stats/v1/accounts/{userId}/items` - Get items analytics
- `GET /stats/v1/accounts/{userId}/items/{itemId}/calls` - Get call statistics
- `GET /stats/v1/accounts/{userId}/items/shallow` - Get shallow statistics

#### 🎯 **Promotions (Продвижение)**
- `GET /promotion/v1/items/bids` - Get promotion bids
- `GET /promotion/v1/items` - Get promotions by item IDs
- `DELETE /promotion/v1/items` - Remove promotions
- `PUT /promotion/v1/items/auto` - Set auto promotion
- `PUT /promotion/v1/items/manual` - Set manual promotion

#### ⭐ **Ratings & Reviews (Рейтинги и отзывы)**
- `GET /ratings/v1/info` - Get rating information
- `GET /ratings/v1/reviews` - Get reviews list with pagination
- `POST /ratings/v1/answers` - Create review answer
- `DELETE /ratings/v1/answers/{answerId}` - Remove review answer

#### 📤 **Autoload (Автозагрузка)**
- `GET /autoload/v1/user-docs/tree` - Get category tree
- `GET /autoload/v1/user-docs/node/{nodeSlug}/fields` - Get category fields
- `GET /autoload/v2/profile` - Get profile settings
- `PUT /autoload/v2/profile` - Create/update profile
- `GET /autoload/v3/reports` - Get reports list
- `GET /autoload/v3/reports/last_completed_report` - Get last report
- `GET /autoload/v3/reports/{reportId}` - Get specific report
- `GET /autoload/v2/reports/{reportId}/items` - Get report items
- `GET /autoload/v2/reports/{reportId}/items/fees` - Get report items fees
- `POST /autoload/v1/upload` - Upload file
- `GET /autoload/v2/items` - Get autoload items info
- `GET /autoload/v2/items/avito_ids` - Get Avito IDs by ad IDs
- `GET /autoload/v2/ads` - Get ad IDs by Avito IDs

### 🛠️ Installation

1. Copy the node files to your n8n custom nodes directory
2. Restart your n8n instance
3. The "Avito" node will appear in your n8n nodes palette

### ⚙️ Configuration

1. **Create Avito OAuth2 Credentials**:
   - Go to n8n Settings → Credentials
   - Add new "Avito OAuth2 API" credential
   - Choose grant type (Client Credentials recommended for testing)
   - Enter your `client_id` and `client_secret` from [Avito Developers](https://www.avito.ru/professionals/api)

2. **Configure the Node**:
   - Select resource (Items, Promotions, Ratings, Autoload)
   - Choose operation
   - Fill in required parameters
   - The node handles authentication automatically

### 💡 Development Note

**95% of this code was written using Claude AI assistant**, demonstrating the power of AI-assisted development for creating complex integrations.

### ⚠️ Disclaimer

- **The author is not responsible** for any issues or consequences arising from the use of this application
- **The author has no affiliation** with Avito or n8n developers
- **The author owes nothing to anyone** - this project was created purely out of enthusiasm for personal purposes
- **Users can request new features and bug fixes**, however this does not obligate the author to implement them
- **Use at your own risk** - always test thoroughly in development environment first

### 📄 License

This project is provided as-is under MIT license. See LICENSE file for details.

### 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and enhancement requests.

---

## Русский

### 🚀 Обзор

**Avito n8n Custom Node** — это мощная кастомная нода для платформы автоматизации n8n, которая обеспечивает бесшовную интеграцию с API Авито для бизнеса. Эта нода добавляет удобный функционал для работы с API Авито прямо в интерфейсе n8n, решая критические проблемы аутентификации и управления токенами.

### ✨ Ключевые особенности

- **🔧 Удобная интеграция с API**: Прямой доступ к функциональности API Авито в интерфейсе n8n
- **🔑 Автоматическое управление токенами**: Решает проблему обновления токенов при 403 Forbidden, которую стандартная HTTP Request нода не может обработать
- **📊 Полное покрытие API**: Поддержка ресурсов Объявлений, Продвижения, Рейтингов и отзывов, Автозагрузки
- **⚡ Встроенное ограничение запросов**: Умное регулирование запросов для соблюдения лимитов API
- **🛡️ Надежная обработка ошибок**: Подробные сообщения об ошибках и автоматические механизмы повтора

### 🎯 Решаемая проблема

Эта нода специально решает критическое ограничение в стандартной реализации OAuth2 в n8n:

- **В стандартной HTTP Request ноде** нельзя выбрать кастомный код ошибки для обновления токена
- **API Авито возвращает 403 Forbidden** при истечении токенов, а n8n по умолчанию обрабатывает только 401 Unauthorized
- Хотя технически можно создать credentials для Авито с HTTP Request нодой, **токены приходится вручную пересоздавать каждые 24 часа**, что крайне неудобно
- **Эта нода полностью решает эту проблему** автоматическим обновлением токенов при получении 403 статуса

### 📋 Поддерживаемые методы API Авито

#### 🏠 **Объявления (Items)**
- `GET /items/v2/list` - Получить список объявлений пользователя
- `GET /items/v2/item/{itemId}` - Получить информацию об объявлении
- `PUT /items/v1/item/{itemId}/price` - Обновить цену объявления
- `POST /items/v1/item/{itemId}/vas` - Применить дополнительные услуги (VAS)
- `GET /items/v1/vas/prices` - Получить цены VAS
- `GET /stats/v1/accounts/{userId}/items` - Получить аналитику объявлений
- `GET /stats/v1/accounts/{userId}/items/{itemId}/calls` - Получить статистику звонков
- `GET /stats/v1/accounts/{userId}/items/shallow` - Получить поверхностную статистику

#### 🎯 **Продвижение (Promotions)**
- `GET /promotion/v1/items/bids` - Получить ставки продвижения
- `GET /promotion/v1/items` - Получить продвижения по ID объявлений
- `DELETE /promotion/v1/items` - Удалить продвижения
- `PUT /promotion/v1/items/auto` - Установить автопродвижение
- `PUT /promotion/v1/items/manual` - Установить ручное продвижение

#### ⭐ **Рейтинги и отзывы (Ratings & Reviews)**
- `GET /ratings/v1/info` - Получить информацию о рейтинге
- `GET /ratings/v1/reviews` - Получить список отзывов с пагинацией
- `POST /ratings/v1/answers` - Создать ответ на отзыв
- `DELETE /ratings/v1/answers/{answerId}` - Удалить ответ на отзыв

#### 📤 **Автозагрузка (Autoload)**
- `GET /autoload/v1/user-docs/tree` - Получить дерево категорий
- `GET /autoload/v1/user-docs/node/{nodeSlug}/fields` - Получить поля категории
- `GET /autoload/v2/profile` - Получить настройки профиля
- `PUT /autoload/v2/profile` - Создать/обновить профиль
- `GET /autoload/v3/reports` - Получить список отчетов
- `GET /autoload/v3/reports/last_completed_report` - Получить последний отчет
- `GET /autoload/v3/reports/{reportId}` - Получить конкретный отчет
- `GET /autoload/v2/reports/{reportId}/items` - Получить элементы отчета
- `GET /autoload/v2/reports/{reportId}/items/fees` - Получить комиссии элементов отчета
- `POST /autoload/v1/upload` - Загрузить файл
- `GET /autoload/v2/items` - Получить информацию об элементах автозагрузки
- `GET /autoload/v2/items/avito_ids` - Получить ID Авито по ID объявлений
- `GET /autoload/v2/ads` - Получить ID объявлений по ID Авито

### ⚙️ Настройка

1. **Создайте Avito OAuth2 Credentials**:
   - Перейдите в Настройки n8n → Credentials
   - Добавьте новую учетную запись "Avito OAuth2 API"
   - Выберите тип авторизации (Client Credentials рекомендуется для тестирования)
   - Введите ваши `client_id` и `client_secret` из [Авито для разработчиков](https://www.avito.ru/professionals/api)

2. **Настройте ноду**:
   - Выберите ресурс (Объявления, Продвижение, Рейтинги, Автозагрузка)
   - Выберите операцию
   - Заполните обязательные параметры
   - Нода автоматически обрабатывает аутентификацию

### 💡 Заметка о разработке

**Этот проект был разработан с обширной помощью ИИ (95% Claude AI)**, демонстрируя современные подходы к разработке с помощью ИИ.

### ⚠️ Отказ от ответственности

- Это независимая community нода, не имеющий официальной связи с платформой Авито или n8n
- **Данное программное обеспечение предоставляется "КАК ЕСТЬ" без каких-либо гарантий, явных или подразумеваемых**
- **Автор отказывается от любой ответственности за ущерб, потерю данных или иные последствия**, возникающие в результате использования данного программного обеспечения
- Как и в любом проекте с открытым исходным кодом, могут существовать ошибки и критические проблемы - **пользователи несут полную ответственность** за тестирование и валидацию
- Используйте на свое усмотрение и тщательно тестируйте перед использованием в продакшене
- Запросы на новые функции и сообщения об ошибках приветствуются, хотя время ответа может варьироваться
- Проект предоставляется на условиях лицензии MIT

### 📄 Лицензия

Этот проект предоставляется как есть под лицензией MIT. См. файл LICENSE для подробностей.

### 📝 Примечание о требованиях верификации n8n

Эта нода намеренно отклоняется от рекомендации n8n использовать **только английский язык** для интерфейсов и документации нод. Это решение принято по следующим причинам:

- Нода ориентирована преимущественно на **русскоязычную аудиторию**, работающую с Авито (российская торговая площадка)
- n8n в настоящее время **не поддерживает мультиязычные интерфейсы**, что делает невозможной реализацию правильной локализации
- Использование русского языка значительно улучшает **пользовательский опыт** для целевой аудитории
- Это может препятствовать официальной верификации ноды n8n, но **удобство использования приоритетнее верификации**

Если n8n добавит поддержку мультиязычности в будущем, нода может быть обновлена для поддержки обоих языков с целью потенциальной верификации.

### 🤝 Вклад в проект

Вклады приветствуются! Пожалуйста, не стесняйтесь отправлять issues и запросы на улучшения.

---

### 🔗 Полезные ссылки

- [Авито API для разработчиков](https://developers.avito.ru/)
- [Документация n8n](https://docs.n8n.io/)
- [Рекомендации по деплою приложения](https://docs.n8n.io/integrations/creating-nodes/deploy/)