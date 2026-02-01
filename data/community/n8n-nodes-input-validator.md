# n8n-nodes-input-validator

The **n8n-nodes-input-validator** is a powerful tool designed to validate input data against specified criteria. It supports multiple data types, including strings, numbers, booleans, dates, and enums, and offers various validation options to ensure data integrity.

## Features

- **String Validation**: Validate strings with options for email, URL, UUID, and regex pattern.
- **Number Validation**: Validate numbers with options for minimum and maximum values.
- **Boolean Validation**: Validate boolean values.
- **Date Validation**: Validate dates in ISO 8601 format.
- **Enum Validation**: Validate values against a set of predefined options.

## Usage

### Properties

The node allows you to configure multiple input fields with various validation criteria. Each input field has the following properties:

- **Validation Type**: The type of validation to perform (`string`, `number`, `boolean`, `date`, `enum`).
- **Required**: Whether the input field is required.
- **String Data**: Data to be validated as a string.
- **String Format**: Specify if the string should be validated as an `email`, `URL`, `UUID`, or match a custom `pattern`.
- **Number Data**: Data to be validated as a number.
- **Boolean Data**: Data to be validated as a boolean.
- **Date Data**: Data to be validated as a date.
- **Enum Values**: Comma-separated list of valid enum values.
- **Pattern**: Regex pattern for string validation.
- **Min**: Minimum value for number validation.
- **Max**: Maximum value for number validation.

### Example Configuration

Here's an example of how to configure the Validator Node:

1. **String Validation**
    - **Validation Type**: `string`
    - **Required**: `true`
    - **String Data**: `example@example.com`
    - **String Format**: `email`

2. **Number Validation**
    - **Validation Type**: `number`
    - **Required**: `true`
    - **Number Data**: `10`
    - **Min**: `2`
    - **Max**: `100`

3. **Boolean Validation**
    - **Validation Type**: `boolean`
    - **Required**: `true`
    - **Boolean Data**: `true`

4. **Date Validation**
    - **Validation Type**: `date`
    - **Required**: `true`
    - **Date Data**: `2024-06-05`

5. **Enum Validation**
    - **Validation Type**: `enum`
    - **Required**: `true`
    - **String Data**: `option1`
    - **Enum Values**: `option1, option2, option3`

### Validation Logic

The validation logic is implemented as follows:

- **String Validation**: Checks if the string matches the specified format (email, URL, UUID, pattern) and if it is not empty when required.
- **Number Validation**: Checks if the number is within the specified range (min and max) and if it is a valid number.
- **Boolean Validation**: Checks if the value is a valid boolean and if it is not empty when required.
- **Date Validation**: Checks if the date is in ISO 8601 format and if it is not empty when required.
- **Enum Validation**: Checks if the value is one of the predefined enum options and if it is not empty when required.

### Error Handling

The node returns a JSON object with the following structure:

```json
{
    "isValid": true,
    "errors": [
        {
            "field": "field_name",
            "message": "Error message"
        }
    ]
}
```

- **isValid**: Indicates whether all validations passed.
- **errors**: An array of error messages for failed validations.

## Development

### Setup

1. Clone the repository.
2. Install dependencies:
    ```sh
    npm install
    ```
3. Build the project:
    ```sh
    npm run build
    ```


