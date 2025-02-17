# Git Repository Exposure Scanner

A Python-based tool to detect exposed `.git` directories and files on a target website. This tool helps identify misconfigured web servers that expose sensitive `.git` repositories, which can lead to information leakage.

---

## Features
- Scans for exposed `.git` files and directories (e.g., `.git/HEAD`, `.git/config`).
- Extracts branch names from `.git/HEAD`.
- Detects exposed Git configurations.
- Simple and easy-to-use command-line interface.

---

## Author Information
- **Author**: Ved Kumar
- **Email**: devkumarmahto204@outlook.com
- **GitHub**: [devkumar-swipe](https://github.com/devkumar-swipe)
- **Tool Version**: 1.0.0

---

## Uses of This Tool
This tool is designed for:
- **Security Researchers**: To identify misconfigured web servers that expose `.git` repositories.
- **Developers**: To check if their websites accidentally expose `.git` directories.
- **Penetration Testers**: To include in their reconnaissance phase for identifying potential information leaks.
- **Bug Bounty Hunters**: To find vulnerabilities related to exposed `.git` repositories.

---

## Installation

### Prerequisites
- Python 3.x installed on your system.
- `pip` for installing dependencies.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/devkumar-swipe/gitfinder.git
   cd gitfinder
