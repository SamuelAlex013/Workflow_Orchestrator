# n8n WSL Exec Node

This community node for n8n allows you to execute commands within a Windows Subsystem for Linux (WSL2) container directly from your n8n workflow. It is designed to be run on an n8n instance hosted on a Windows machine.

## Features

-   Execute any command inside a specified WSL container.
-   Automatically discovers and lists available WSL containers.
-   Set a starting directory for your command.
-   Provide arguments for your command.
-   Stream stdout and stderr back to the n8n workflow.
-   Ability to execute tasks under different users such as root, www-data, etc (leave blank for default user).
-   Supports all WSL distros

## Installation

1.  Go to **Settings > Community Nodes** in your n8n instance.
2.  Select **Install**.
3.  Search for `n8n-nodes-wsl-exec` and click **Install**.

## Configuration

-   **WSL2 Container**: Choose from a dropdown list of automatically detected WSL containers, or manually type the name of the container.
-   **Start Directory**: The directory where the command should be executed. Defaults to `~/` (the user's home directory).
-   **Command**: The command to execute (e.g., `ls`, `echo "Hello"`, `python3`).
-   **Arguments**: Any arguments to pass to the command, separated by spaces (e.g., `-l -a`, `my_script.py --verbose`).
-   **Ignore Startup Output**: If your `.bashrc` or other shell startup scripts produce output (like `neofetch`), enable this option to ignore it and only capture the output of the command itself.

## Requirements

-   Windows 10 or Windows 11 with n8n installed on the host machine. n8n should not be installed in a container
-   Windows Subsystem For Linux (WSL/WSL2) Installed and at least one WSL instance setup

## Example Usage

To run a Python script inside a WSL container named `Ubuntu`:

1.  Set **WSL2 Container** to `Ubuntu`.
2.  Set **Command** to `python3`.
3.  Set **Arguments** to `/path/to/your/script.py`.

The node will output the `stdout`, `stderr`, and `exitCode` from the executed command.

## Source Code

The source code for this node is available on GitHub: [https://github.com/KeithIMyers/n8n-wsl-exec](https://github.com/KeithIMyers/n8n-wsl-exec)
