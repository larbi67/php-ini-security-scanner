import os

# Define security best practices for control points
best_practices = {
    'P1': {
        'description': 'Authentication',
        'settings': {
            'allow_url_fopen': 'Off',
            'log_errors': 'On',
        },
    },
    'P2': {
        'description': 'Session Management',
        'settings': {
            'session.cookie_secure': 'On',
            'session.cookie_httponly': 'On',
            'session.cookie_samesite': 'Strict',
        },
    },
    'P4': {
        'description': 'Injection Protection',
        'settings': {
            'magic_quotes_gpc': 'Off',
        },
    },
    'P5': {
        'description': 'Input/Output Validation',
        'settings': {
            'filter.default': 'unsafe_raw',
        },
    },
    'P6': {
        'description': 'XSS Protection',
        'settings': {
            'html_errors': 'Off',
        },
    },
    'P8': {
        'description': 'Data Protection',
        'settings': {
            'session.entropy_length': '32',
            'session.hash_function': 'sha256',
        },
    },
    'P9': {
        'description': 'File and Upload Security',
        'settings': {
            'file_uploads': 'Off',
        },
    },
    'P10': {
        'description': 'Error Handling',
        'settings': {
            'display_errors': 'Off',
            'log_errors': 'On',
        },
    },
    'P12': {
        'description': 'Communication Security',
        'settings': {
            'session.cookie_secure': 'On',
        },
    },
    'P13': {
        'description': 'Dependency Security',
        'settings': {},
    },
    'P14': {
        'description': 'Monitoring and Logging',
        'settings': {
            'log_errors': 'On',
        },
    },
    'P15': {
        'description': 'API Security',
        'settings': {},
    },
    # Additional configurations
    'P16': {
        'description': 'Performance Settings',
        'settings': {
            'max_execution_time': '30',
            'memory_limit': '128M',
            'post_max_size': '8M',
            'upload_max_filesize': '2M',
        },
    },
    'P17': {
        'description': 'Exposure Settings',
        'settings': {
            'expose_php': 'Off',
            'disable_functions': 'exec,passthru,shell_exec,system',
        },
    },
}

def convert_to_mb(value):
    """
    Convert value with units to megabytes.
    """
    if value.endswith('M'):
        return float(value[:-1])
    elif value.endswith('G'):
        return float(value[:-1]) * 1024
    elif value.isdigit():
        return float(value)
    return value

def normalize_value(value):
    """
    Normalize value for comparison (e.g., convert to lower case, strip spaces).
    """
    if isinstance(value, str):
        return value.strip().lower()
    return value

def load_php_ini(file_path):
    """
    Load the php.ini file and return a parsed configuration.
    """
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith(';'):
                continue
            if '=' in line:
                key, value = line.split('=', 1)
                config[key.strip()] = normalize_value(value.strip())
    return config

def audit_php_ini(config):
    """
    Compare the current configurations in the php.ini file with security best practices.
    """
    audit_results = []
    for point, data in best_practices.items():
        for key, recommended_value in data['settings'].items():
            current_value = config.get(key, 'Not Set')
            
            # Special handling for numeric values with units
            if key in ['max_execution_time', 'memory_limit', 'post_max_size', 'upload_max_filesize']:
                current_value = convert_to_mb(current_value)
                recommended_value = convert_to_mb(recommended_value)
            
            if isinstance(current_value, str) and not current_value.strip():
                current_value = 'Empty'
                
            if isinstance(current_value, float) and isinstance(recommended_value, float):
                if current_value != recommended_value:
                    audit_results.append((point, data['description'], key, current_value, recommended_value))
            elif normalize_value(current_value) != normalize_value(recommended_value):
                audit_results.append((point, data['description'], key, current_value, recommended_value))
    
    return audit_results

def generate_report(audit_results):
    """
    Generate a report based on the audit results.
    """
    report = []
    for point, description, key, current_value, recommended_value in audit_results:
        report.append(f"ID {point} ({description}) - Configuration '{key}': Current Value = {current_value}, Recommended Value = {recommended_value}")
    return "\n".join(report)

def save_report(report, file_path):
    """
    Save the report to a specified file.
    """
    with open(file_path, 'w') as file:
        file.write(report)
    print(f"Report saved to {file_path}")

def main():
    """
    Main function for user interaction.
    """
    print("Welcome to the PHP.ini Security Scanner!")

    # Prompt the user to enter the path to the php.ini file
    file_path = input("Please enter the path to your php.ini file: ")

    # Check if the file exists
    if not os.path.isfile(file_path):
        print("The specified file does not exist. Please check the path and try again.")
        return

    # Load and audit the php.ini file
    config = load_php_ini(file_path)
    audit_results = audit_php_ini(config)

    # Generate the report
    report = generate_report(audit_results)
    print("\nAudit Report:\n")
    print(report)

    # Ask the user if they want to save the report
    save_option = input("\nDo you want to save the report to a file? (yes/no): ").strip().lower()
    if save_option == 'yes':
        # Prompt for the report file path
        report_file_path = input("Please enter the path to save the report file: ")
        save_report(report, report_file_path)
    else:
        print("Report not saved.")

if __name__ == "__main__":
    main()
