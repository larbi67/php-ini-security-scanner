# PHP.ini Security Scanner

This script audits your PHP configuration (php.ini) for security best practices and generates a report highlighting any discrepancies between your current settings and recommended values.

## Features
- Verifies the configuration parameters defined in the php.ini file.
- Checks for settings that are either defined, commented out, or not set.
- Provides recommendations for improving the security of your PHP configuration.
- Generates a detailed report of current and recommended settings.

## Prerequisites
- Python 3.x
- Basic understanding of PHP configuration (php.ini file).

## Installation
1. Clone this repository or download the script file.
2. Ensure you have Python 3.x installed on your system.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using Python : python php_ini_scanner.py
4. Follow the prompts to enter the path to your php.ini file.
5. The script will load and audit the php.ini file.
6. Optionally, save the report to a file.

## Example Report

![Example Report](https://github.com/larbi67/php-ini-security-scanner/blob/main/result.JPG)

Audit Report:

- ID P1 (Authentication) - Configuration 'allow_url_fopen': Current Value = on, Recommended Value = Off
- ID P2 (Session Management) - Configuration 'session.cookie_secure': Current Value = Not Set, Recommended Value = On
- ID P2 (Session Management) - Configuration 'session.cookie_httponly': Current Value = Empty, Recommended Value = On
- ID P2 (Session Management) - Configuration 'session.cookie_samesite': Current Value = Empty, Recommended Value = Strict
- ID P5 (Input/Output Validation) - Configuration 'filter.default': Current Value = Not Set, Recommended Value = unsafe_raw
- ID P6 (XSS Protection) - Configuration 'html_errors': Current Value = on, Recommended Value = Off
- ID P8 (Data Protection) - Configuration 'session.entropy_length': Current Value = Not Set, Recommended Value = 32
- ID P8 (Data Protection) - Configuration 'session.hash_function': Current Value = Not Set, Recommended Value = sha256
- ID P9 (File and Upload Security) - Configuration 'file_uploads': Current Value = on, Recommended Value = Off
- ID P10 (Error Handling) - Configuration 'display_errors': Current Value = on, Recommended Value = Off
- ID P12 (Communication Security) - Configuration 'session.cookie_secure': Current Value = Not Set, Recommended Value = On
- ID P16 (Performance Settings) - Configuration 'max_execution_time': Current Value = 1200000.0, Recommended Value = 30.0
- ID P16 (Performance Settings) - Configuration 'memory_limit': Current Value = 512m, Recommended Value = 128.0
- ID P16 (Performance Settings) - Configuration 'post_max_size': Current Value = 400000m, Recommended Value = 8.0
- ID P16 (Performance Settings) - Configuration 'upload_max_filesize': Current Value = 400000m, Recommended Value = 2.0
- ID P17 (Exposure Settings) - Configuration 'expose_php': Current Value = on, Recommended Value = Off
- ID P17 (Exposure Settings) - Configuration 'disable_functions': Current Value = Empty, Recommended Value = exec,passthru,shell_exec,system

## Best Practices
- Read the php.ini File Line by Line: Carefully review each line in the php.ini file to understand the current configuration settings.
- Backup Your Configuration: Before making any changes, create a backup of your existing php.ini file.
- Understand Each Setting: Ensure you understand the implications of changing each configuration setting, especially in a production environment.
- Regular Audits: Perform regular audits of your PHP configuration to maintain a secure environment.

## Contributing
Feel free to contribute by submitting issues or pull requests. Your contributions are greatly appreciated!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
