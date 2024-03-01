import platform

def get_system_information():
    system_info = {}
    
    # Get system platform
    system_info['Platform'] = platform.platform()
    
    # Get system architecture
    system_info['Architecture'] = platform.architecture()[0]
    
    # Get system processor
    system_info['Processor'] = platform.processor()
    
    # Get system distribution information
    try:
        distribution_info = platform.linux_distribution()
        system_info['Distribution'] = ' '.join(distribution_info)
    except:
        system_info['Distribution'] = "Not available"
    
    return system_info

if __name__ == "__main__":
    system_info = get_system_information()
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")
