# # osdag_script.py
# import os
# import subprocess
# import sys
#
#
# def install_miniconda():
#     """Check and install Miniconda if not present."""
#     # Check if conda is available in the system's PATH
#     try:
#         # Run the conda command to check its version
#         result = subprocess.run(["conda", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
#         # If conda is installed, we will get its version
#         if result.returncode == 0:
#             print("Miniconda is already installed.")
#             return
#         else:
#             raise FileNotFoundError("Conda not found")
#     except FileNotFoundError:
#         print("Miniconda not found. Installing Miniconda...")
#         miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
#         installer_path = os.path.join(os.getcwd(), "Miniconda3-latest-Windows-x86_64.exe")
#
#         # Download Miniconda installer
#         subprocess.run(["curl", "-o", installer_path, miniconda_url], check=True)
#
#         # Install Miniconda silently
#         subprocess.run([installer_path, "/S", "/D=" + os.path.expanduser("~\\Miniconda3")], check=True)
#
#
# def setup_conda_env():
#     """Set up the Conda environment for Osdag."""
#     env_name = "osdag-env"
#     subprocess.run(["conda", "create", "-n", env_name, "python=3.8", "-y"], check=True)
#     subprocess.run(["conda", "activate", env_name], shell=True, check=True)
#     subprocess.run(["pip", "install", "osdag"], check=True)
#
# def install_latex_packages():
#     """Install the required LaTeX packages."""
#     latex_packages = [
#         "geometry",
#         "graphicx",
#         "amsmath",
#         "hyperref"
#     ]
#     # Install LaTeX packages if MiKTeX or TeX Live is present (e.g., via MiKTeX's package manager)
#     try:
#         # Attempt to install packages using MiKTeX's command-line tool (Windows example)
#         print("Checking for LaTeX package manager...")
#         subprocess.run(["miktex-console", "--install", "--yes"] + latex_packages, check=True)
#         print("LaTeX packages installed successfully!")
#     except subprocess.CalledProcessError:
#         print("Failed to install LaTeX packages. Please ensure you have a LaTeX distribution installed.")
#
# def launch_osdag():
#     """Launch Osdag."""
#     try:
#         import osdag
#         print("Osdag is installed and working!")
#         # Add the main entry point of Osdag, if any.
#     except ImportError:
#         print("Osdag module is not installed. Please check your setup.")
#
# if __name__ == "__main__":
#     install_miniconda()
#     setup_conda_env()
#     launch_osdag()

# import os
# import subprocess
# import sys


# def check_conda_version():
#     """Check if Miniconda is installed and meets the version requirement."""
#     required_version = "4.10.0"
#     try:
#         # Run conda --version to get the installed version
#         result = subprocess.run(["conda", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         if result.returncode == 0:
#             installed_version = result.stdout.strip().split()[1]
#             if installed_version >= required_version:
#                 print(f"Miniconda version {installed_version} is already installed.")
#                 return True
#             else:
#                 print(f"Your Miniconda version ({installed_version}) is lower than the required version ({required_version}).")
#         else:
#             print("Conda command returned an error.")
#     except FileNotFoundError:
#         print("Miniconda not found.")
#     return False


# def download_miniconda_installer():
#     """Download the Miniconda installer."""
#     miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
#     installer_path = os.path.join(os.getcwd(), "Miniconda3-latest-Windows-x86_64.exe")
#     try:
#         import requests
#     except ImportError:
#         print("Requests library not found. Installing requests...")
#         subprocess.run([sys.executable, "-m", "pip", "install", "requests"], check=True)
#         import requests

#     print(f"Downloading Miniconda from {miniconda_url}...")
#     response = requests.get(miniconda_url, stream=True)
#     if response.status_code == 200:
#         with open(installer_path, 'wb') as file:
#             for chunk in response.iter_content(chunk_size=1024):
#                 file.write(chunk)
#         print(f"Miniconda installer downloaded to {installer_path}.")
#         return installer_path
#     else:
#         print(f"Failed to download Miniconda. HTTP Status Code: {response.status_code}")
#         sys.exit(1)


# def install_miniconda(installer_path):
#     """Install Miniconda silently."""
#     print("Installing Miniconda silently...")
#     install_dir = os.path.expanduser("~\\Miniconda3")
#     try:
#         subprocess.run([installer_path, "/S", f"/D={install_dir}"], check=True)
#         print("Miniconda installation completed.")
#         return True
#     except subprocess.CalledProcessError as e:
#         print(f"Miniconda installation failed: {e}")
#         return False


# def configure_conda_path():
#     """Add Miniconda to PATH environment variable."""
#     conda_bin_path = os.path.expanduser("~\\Miniconda3\\Scripts")
#     if conda_bin_path not in os.environ["PATH"]:
#         os.environ["PATH"] += f";{conda_bin_path}"
#         print("Conda added to PATH.")


# def setup_conda_env():
#     """Set up the Conda environment with fallback to pip for osdag installation."""
#     env_name = "osdag-env"
#     try:
#         print(f"Creating Conda environment '{env_name}'...")
#         subprocess.run(["conda", "create", "-n", env_name, "python=3.8", "-y"], check=True)
#         print(f"Conda environment '{env_name}' created successfully.")
        
#         print(f"Attempting to install 'osdag' via Conda in '{env_name}'...")
#         result = subprocess.run(["conda", "install", "-n", env_name, "osdag", "-y"], check=True)
#         if result.returncode == 0:
#             print(f"'osdag' installed successfully in Conda environment '{env_name}'.")
#         else:
#             raise Exception("Conda installation of 'osdag' failed.")
#     except Exception as conda_error:
#         print(f"Conda installation of 'osdag' failed: {conda_error}")
#         print("Falling back to pip installation...")
#         try:
#             subprocess.run(["conda", "activate", env_name, "&&", "pip", "install", "osdag"], shell=True, check=True)
#             print(f"'osdag' installed successfully via pip in environment '{env_name}'.")
#         except subprocess.CalledProcessError as pip_error:
#             print(f"Failed to install 'osdag' via pip: {pip_error}")
#             sys.exit(1)

import os
import subprocess
import sys


def check_conda_version():
    """Check if Miniconda is installed and meets the version requirement."""
    required_version = "4.10.0"
    try:
        # Run conda --version to get the installed version
        result = subprocess.run(["conda", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            installed_version = result.stdout.strip().split()[1]
            if installed_version >= required_version:
                print(f"Miniconda version {installed_version} is already installed.")
                return True
            else:
                print(f"Your Miniconda version ({installed_version}) is lower than the required version ({required_version}).")
        else:
            print("Conda command returned an error.")
    except FileNotFoundError:
        print("Miniconda not found.")
    return False


def download_miniconda_installer():
    """Download the Miniconda installer."""
    miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
    installer_path = os.path.join(os.getcwd(), "Miniconda3-latest-Windows-x86_64.exe")
    try:
        import requests
    except ImportError:
        print("Requests library not found. Installing requests...")
        subprocess.run([sys.executable, "-m", "pip", "install", "requests"], check=True)
        import requests

    print(f"Downloading Miniconda from {miniconda_url}...")
    response = requests.get(miniconda_url, stream=True)
    if response.status_code == 200:
        with open(installer_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Miniconda installer downloaded to {installer_path}.")
        return installer_path
    else:
        print(f"Failed to download Miniconda. HTTP Status Code: {response.status_code}")
        sys.exit(1)


def install_miniconda(installer_path):
    """Install Miniconda silently."""
    print("Installing Miniconda silently...")
    install_dir = os.path.expanduser("~\\Miniconda3")
    try:
        subprocess.run([installer_path, "/S", f"/D={install_dir}"], check=True)
        print("Miniconda installation completed.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Miniconda installation failed: {e}")
        return False


def configure_conda_path():
    """Add Miniconda to PATH environment variable."""
    conda_bin_path = os.path.expanduser("~\\Miniconda3\\Scripts")
    if conda_bin_path not in os.environ["PATH"]:
        os.environ["PATH"] += f";{conda_bin_path}"
        print("Conda added to PATH.")


def setup_conda_env():
    """Set up the Conda environment with fallback to pip for osdag installation."""
    env_name = "osdag-env"
    try:
        print(f"Creating Conda environment '{env_name}'...")
        subprocess.run(["conda", "create", "-n", env_name, "python=3.8", "-y"], check=True)
        print(f"Conda environment '{env_name}' created successfully.")
        
        print(f"Attempting to install 'osdag' via Conda in '{env_name}'...")
        result = subprocess.run(["conda", "install", "-n", env_name, "osdag", "-y"], check=True)
        if result.returncode == 0:
            print(f"'osdag' installed successfully in Conda environment '{env_name}'.")
        else:
            raise Exception("Conda installation of 'osdag' failed.")
    except Exception as conda_error:
        print(f"Conda installation of 'osdag' failed: {conda_error}")
        print("Falling back to pip installation...")
        try:
            # Use conda run instead of activate
            subprocess.run(["conda", "run", "-n", env_name, "pip", "install", "osdag"], check=True)
            print(f"'osdag' installed successfully via pip in environment '{env_name}'.")
        except subprocess.CalledProcessError as pip_error:
            print(f"Failed to install 'osdag' via pip: {pip_error}")
            sys.exit(1)




def install_latex_packages():
    """Install the required LaTeX packages."""
    latex_packages = [
        "geometry",
        "graphicx",
        "amsmath",
        "hyperref"
    ]
    try:
        # Check if MiKTeX or TeX Live is available and install LaTeX packages
        print("Checking for LaTeX package manager...")
        subprocess.run(["miktex-console", "--install", "--yes"] + latex_packages, check=True)
        print("LaTeX packages installed successfully!")
    except subprocess.CalledProcessError:
        print(
            "Failed to install LaTeX packages using MiKTeX. Please ensure MiKTeX or TeX Live is installed and accessible in your PATH.")
        sys.exit(1)


def launch_osdag():
    """Launch Osdag."""
    try:
        import osdag
        print("Osdag is installed and working!")
    except ImportError:
        print("Osdag module is not installed. Please check your setup.")
        sys.exit(1)


if __name__ == "__main__":
    try:
        if not check_conda_version():
            installer_path = download_miniconda_installer()
            if install_miniconda(installer_path):
                configure_conda_path()
                print("Verifying Miniconda installation...")
                subprocess.run(["conda", "--version"], check=True)
        setup_conda_env()
        install_latex_packages()
        launch_osdag()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# import os
# import subprocess
# import sys
# import platform
#
#
# def install_miniconda():
#     """Check and install Miniconda if not present."""
#     conda_path = os.path.expanduser("~\\Miniconda3")
#     if os.name == "nt" and not os.path.exists(conda_path):  # Windows
#         print("Miniconda not found. Installing Miniconda...")
#         miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
#         installer_path = os.path.join(os.getcwd(), "Miniconda3-latest-Windows-x86_64.exe")
#
#         try:
#             subprocess.run(["curl", "-o", installer_path, miniconda_url], check=True)
#             subprocess.run([installer_path, "/S", "/D=" + conda_path], check=True)
#             print("Miniconda installed successfully.")
#         except subprocess.CalledProcessError:
#             print("Failed to install Miniconda. Please check your network connection.")
#             sys.exit(1)
#     else:
#         print("Miniconda is already installed.")
#
#
# def install_latex_packages():
#     """Install the required LaTeX packages."""
#     latex_packages = [
#         "geometry",
#         "graphicx",
#         "amsmath",
#         "hyperref"
#     ]
#     try:
#         # For Windows: Using MiKTeX console to install specific LaTeX packages
#         if platform.system() == 'Windows':
#             subprocess.run(["miktex-console", "--install", "--yes"] + latex_packages, check=True)
#             print("LaTeX packages installed successfully!")
#         else:
#             print("Please install a LaTeX distribution (MiKTeX or TeX Live) manually.")
#     except subprocess.CalledProcessError:
#         print("Failed to install LaTeX packages. Ensure you have a LaTeX distribution installed.")
#         sys.exit(1)
#
#
# def setup_conda_env():
#     """Set up the Conda environment for Osdag."""
#     env_name = "osdag-env"
#     conda_path = r"C:\Users\HP\anaconda3\Scripts\conda.exe"  # Adjust the path to where Conda is installed
#     try:
#         subprocess.run([conda_path, "create", "-n", env_name, "python=3.8", "-y"], check=True)
#         subprocess.run([conda_path, "activate", env_name], shell=True, check=True)
#         subprocess.run([conda_path, "install", "osdag"], check=True)
#         print("Conda environment setup completed.")
#     except subprocess.CalledProcessError:
#         print("Failed to set up Conda environment. Please ensure Miniconda is installed and accessible.")
#         sys.exit(1)
#
#
# def launch_osdag():
#     """Launch Osdag."""
#     try:
#         import osdag
#         print("Osdag is installed and working!")
#     except ImportError:
#         print("Osdag module is not installed. Please check your setup.")
#         sys.exit(1)
#
#
# if __name__ == "__main__":
#     try:
#         install_miniconda()
#         install_latex_packages()
#         setup_conda_env()
#         launch_osdag()
#     except Exception as e:
#         print(f"An unexpected error occurred: {str(e)}")
#         sys.exit(1)
