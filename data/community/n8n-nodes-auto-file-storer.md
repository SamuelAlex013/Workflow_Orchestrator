# AutoFileStorer & AutoFileStorerExplorer Nodes

## Overview

The **AutoFileStorer** and **AutoFileStorerExplorer** nodes work together to store and explore files within a specified directory in an n8n workflow.

* **AutoFileStorer**: Stores uploaded files to the disk and can optionally hash filenames for uniqueness.
* **AutoFileStorerExplorer**: Lists files in a directory with detailed metadata such as MIME type, size, and last modified date.

## Features

* **File Storage**: Save uploaded files to a specified directory, with optional hashing for unique filenames.
* **File Exploration**: List stored files and return metadata such as file name, path, MIME type, size, and last modified date.
* **Metadata Support**: Provides file details for effective file management in workflows.

## Node Properties

### AutoFileStorer

* **Directory Path**: Specify where to store the files (default is `./n8n_storage/uploaded_files`).
* **Hash Filenames**: Option to hash filenames using MD5 to ensure uniqueness.

### AutoFileStorerExplorer

* **Directory Path**: Specify the directory to explore (default from config or `./n8n_storage/uploaded_files`).

## Inputs/Outputs

### AutoFileStorer Outputs

Stores files in the specified directory and outputs metadata, including:

* `fileName`: The name of the file.
* `filePath`: The path where the file is stored.
* `fileOriginName`: The original file name before storage.

### AutoFileStorerExplorer Outputs

Lists files and their metadata:

* `fileName`: The name of the file.
* `filePath`: The full path to the file.
* `fileMimeType`: The MIME type of the file.
* `fileSize`: The size of the file in bytes.
* `lastModifiedDate`: The date the file was last modified.

![Preview in action](https://github.com/user-attachments/assets/87f0bfce-3107-4987-9ae5-8b85502c73cb)

## Warnings

* **File Overwriting** (AutoFileStorer): Files will be overwritten if not hashed (if the same file already exists).
* **File Duplication** (AutoFileStorer): Files with hashed names may result in duplicates if uploaded multiple times (if the same file is uploaded multiple times).
* **Directory Access** (AutoFileStorerExplorer): Ensure n8n has read permissions to the directory.

## Error Handling

* **Invalid Path**: If the directory doesn't exist or isn't accessible, an error will be thrown.
* **Permission Denied**: Ensure proper file permissions for reading and writing to the directory.

## Conclusion

The **AutoFileStorer** and **AutoFileStorerExplorer** nodes provide a simple and effective way to manage file uploads and file exploration in n8n workflows, offering flexibility with file handling and retrieval.
