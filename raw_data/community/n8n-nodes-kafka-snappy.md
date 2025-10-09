# Kafka Custom Node for n8n

This package provides a custom Kafka node for [n8n](https://n8n.io/), an extendable workflow automation tool. This custom node extends the existing Kafka functionality by adding support for multiple compression codecs and allowing users to select the desired compression type when producing messages.

## Features

- **Support for Multiple Compression Codecs**: Automatically decode messages compressed with Snappy or Gzip.
- **Compression Type Selection for Producer**: Choose between Snappy, Gzip, and no compression when sending messages.
- **Seamless Integration**: Fully compatible with n8n's existing Kafka functionalities, providing a smooth user experience.

## Usage

### Producer Node

The producer node allows you to configure various options, including the compression type for messages:

- **Compression**: Choose between 'None', 'Gzip', and 'Snappy' compression types.
- **Acks**: Specify whether the producer should wait for acknowledgments from all replicas.
- **Timeout**: Set the timeout duration for awaiting a response in milliseconds.

## Contribution

Contributions are welcome! Feel free to open issues and submit pull requests to enhance the functionality of this custom Kafka node.

## License

This project is licensed under the MIT License.

---

This custom Kafka node for n8n enhances the existing Kafka functionalities by supporting Snappy and Gzip compression codecs and providing options to select the compression type for producing messages. It ensures seamless integration and easy usage with n8n's workflow automation, making it an essential tool for efficient and flexible Kafka message handling.
