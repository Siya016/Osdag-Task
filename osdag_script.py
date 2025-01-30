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
#     """Set up the Conda environment with Osdag installation."""
#     env_name = "osdag-env"
#     try:
#         # Step 1: Create Conda environment with Osdag installed directly
#         print(f"Creating Conda environment '{env_name}' with 'osdag' pre-installed...")
#         subprocess.run(["conda", "create", "-n", env_name, "osdag::osdag", "-c", "conda-forge", "-y"], check=True)
#         print(f"Conda environment '{env_name}' created successfully with 'osdag' installed.")
        
#         # Step 2: Activate the Conda environment
#         print(f"Activating Conda environment '{env_name}'...")
#         activation_command = f"conda activate {env_name}"
#         subprocess.run(activation_command, shell=True, check=True)
#         print(f"Conda environment '{env_name}' activated successfully.")
        
#         # Optional: Verify 'osdag' installation
#         print("Verifying 'osdag' installation...")
#         result = subprocess.run(["conda", "list", "-n", env_name], check=True, text=True, capture_output=True)
#         if "osdag" in result.stdout:
#             print("'osdag' is installed successfully in the environment.")
#         else:
#             raise Exception("'osdag' does not appear to be installed.")
#     except subprocess.CalledProcessError as process_error:
#         print(f"Error during setup process: {process_error}")
#         sys.exit(1)
#     except Exception as general_error:
#         print(f"An unexpected error occurred: {general_error}")
#         sys.exit(1)

# # Call the function to set up the environment
# setup_conda_env()



# def install_latex_packages():
#     """Install the required LaTeX packages."""
#     latex_packages = [
#         "geometry",
#         "graphicx",
#         "amsmath",
#         "hyperref"
#     ]
#     try:
#         # Check if MiKTeX or TeX Live is available and install LaTeX packages
#         print("Checking for LaTeX package manager...")
#         subprocess.run(["miktex-console", "--install", "--yes"] + latex_packages, check=True)
#         print("LaTeX packages installed successfully!")
#     except subprocess.CalledProcessError:
#         print(
#             "Failed to install LaTeX packages using MiKTeX. Please ensure MiKTeX or TeX Live is installed and accessible in your PATH.")
#         sys.exit(1)


# def launch_osdag():
#     """Launch Osdag."""
#     try:
#         import osdag
#         print("Osdag is installed and working!")
#     except ImportError:
#         print("Osdag module is not installed. Please check your setup.")
#         sys.exit(1)


# if __name__ == "__main__":
#     try:
#         if not check_conda_version():
#             installer_path = download_miniconda_installer()
#             if install_miniconda(installer_path):
#                 configure_conda_path()
#                 print("Verifying Miniconda installation...")
#                 subprocess.run(["conda", "--version"], check=True)
#         setup_conda_env()
#         install_latex_packages()
#         launch_osdag()
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         sys.exit(1)

# import os
# import subprocess
# import sys
# import time 
# import shutil


# def parse_version(version_str):
#     """Safely parse version strings into comparable tuples."""
#     try:
#         return tuple(map(int, version_str.split(".")))
#     except ValueError:
#         # Handle non-standard version formats (e.g., 24.11.1)
#         return tuple(int(part) if part.isdigit() else 0 for part in version_str.split("."))



# def check_conda_version():
#     """Check if Miniconda is installed and meets the version requirement."""
#     required_version = "4.10.0"
#     try:
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




# def initialize_conda(required_version="4.10.0"):

#     try:
#         print("Checking if Conda is installed...")
#         # Check if Conda is available
#         conda_path = shutil.which("conda")
#         if not conda_path:
#             print("Conda not found in PATH. Please ensure Miniconda is installed.")
#             sys.exit(1)
        
#         # Check Conda version
#         result = subprocess.run(["conda", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         if result.returncode != 0:
#             print(f"Error checking Conda version: {result.stderr.strip()}")
#             sys.exit(1)
        
#         current_version = result.stdout.strip().split()[-1]
#         print(f"Current Conda version: {current_version}")
        
#         # Compare versions using a safe parsing method
#         if parse_version(current_version) < parse_version(required_version):
#             print(f"Your Conda version ({current_version}) is lower than the required version ({required_version}). Please update Conda.")
#             sys.exit(1)
        
#         print("Initializing Conda for the shell...")
#         # Run `conda init` if not already initialized
#         init_result = subprocess.run(["conda", "init"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         if init_result.returncode != 0:
#             print(f"Error initializing Conda: {init_result.stderr.strip()}")
#             sys.exit(1)
        
#         print("Conda initialized successfully. Restarting the script to apply changes...")
#         time.sleep(2)  # Pause before restarting
#         os.execv(sys.executable, ['python'] + sys.argv)  # Restart the script
        
#     except FileNotFoundError as e:
#         print(f"Error: {e}. Ensure that the required files are present and try again.")
#         if "base_library.zip" in str(e):
#             print("It seems you're running this script in a packaged environment. Ensure all dependencies are bundled correctly.")
#         sys.exit(1)
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         sys.exit(1)
        




# def setup_conda_env():
#     """Set up the Conda environment with Osdag installation."""
#     env_name = "osdag-env"
#     try:
#         print(f"Creating Conda environment '{env_name}' with Python 3.8...")
#         subprocess.run(["conda", "create", "-n", env_name, "python=3.8", "-y"], check=True)
#         print(f"Conda environment '{env_name}' created successfully.")

#         # Activate the environment and install dependencies
#         print(f"Activating Conda environment '{env_name}'...")
#         activation_command = f"conda activate {env_name}"
#         os.system(activation_command)

#         print("Installing required packages...")
#         subprocess.run(["conda", "install", "-n", env_name, "-c", "conda-forge", "numpy", "scipy", "matplotlib", "-y"], check=True)
#         print("Required packages installed successfully.")
#     except subprocess.CalledProcessError as process_error:
#         print(f"Error during Conda environment setup: {process_error}")
#         sys.exit(1)


# def install_latex_packages():
#     """Install the required LaTeX packages."""
#     latex_packages = [
#         "geometry",
#         "graphicx",
#         "amsmath",
#         "hyperref"
#     ]
#     try:
#         print("Checking for LaTeX package manager...")
#         result = subprocess.run(
#             ["miktex-console", "--install", "--yes"] + latex_packages,
#             check=True
#         )
#         if result.returncode == 0:
#             print("LaTeX packages installed successfully!")
#         else:
#             print("LaTeX package installation completed with warnings.")
#     except FileNotFoundError:
#         print("LaTeX package manager (MiKTeX/TeX Live) not found. Please ensure it is installed and added to your PATH.")
#         sys.exit(1)
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to install LaTeX packages: {e}")
#         sys.exit(1)



# def launch_osdag():
#     """Launch Osdag."""
#     try:
#         import osdag
#         print("Osdag is installed and working!")
#     except ImportError:
#         print("Osdag module is not installed. Please check your setup.")
#         sys.exit(1)


# if __name__ == "__main__":
#     try:
#         if not check_conda_version():
#             installer_path = download_miniconda_installer()
#             if install_miniconda(installer_path):
#                 configure_conda_path()
#                 print("Verifying Miniconda installation...")
#                 subprocess.run(["conda", "--version"], check=True)

#          # Ensure Conda is initialized before proceeding
#         initialize_conda()

#         setup_conda_env()
#         install_latex_packages()
#         launch_osdag()
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         sys.exit(1)


# import os
# import subprocess
# import sys
# import time
# import shutil

# def parse_version(version_str):
#     """Safely parse version strings into comparable tuples."""
#     try:
#         return tuple(map(int, version_str.split(".")))
#     except ValueError:
#         return tuple(int(part) if part.isdigit() else 0 for part in version_str.split("."))

# def check_conda_version():
#     """Check if Miniconda is installed and meets the version requirement."""
#     required_version = "4.10.0"
#     try:
#         result = subprocess.run(["conda", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         if result.returncode == 0:
#             installed_version = result.stdout.strip().split()[1]
#             if parse_version(installed_version) >= parse_version(required_version):
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

# def initialize_conda(required_version="4.10.0"):
#     """Ensure Conda is initialized and meets version requirements."""
#     try:
#         print("Checking if Conda is installed...")
#         conda_path = shutil.which("conda")
#         if not conda_path:
#             print("Conda not found in PATH. Please ensure Miniconda is installed.")
#             sys.exit(1)
        
#         result = subprocess.run(["conda", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         if result.returncode != 0:
#             print(f"Error checking Conda version: {result.stderr.strip()}")
#             sys.exit(1)
        
#         current_version = result.stdout.strip().split()[-1]
#         print(f"Current Conda version: {current_version}")
        
#         if parse_version(current_version) < parse_version(required_version):
#             print(f"Your Conda version ({current_version}) is lower than the required version ({required_version}). Please update Conda.")
#             sys.exit(1)
        
#         print("Initializing Conda for the shell...")
#         init_result = subprocess.run(["conda", "init"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         if init_result.returncode != 0:
#             print(f"Error initializing Conda: {init_result.stderr.strip()}")
#             sys.exit(1)
        
#         print("Conda initialized successfully. Restarting the script to apply changes...")
#         time.sleep(2)
#         os.execv(sys.executable, ['python'] + sys.argv)
        
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         sys.exit(1)

# def setup_conda_env():
#     """Set up the Conda environment."""
#     env_name = "osdag-env"
#     try:
#         print(f"Creating Conda environment '{env_name}'...")
#         subprocess.run(["conda", "create", "-n", env_name, "python=3.8", "-y"], check=True)
#         print(f"Conda environment '{env_name}' created successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Error creating Conda environment: {e}")
#         sys.exit(1)

# def install_latex_packages():
#     """Install required LaTeX packages."""
#     latex_packages = ["geometry", "graphicx", "amsmath", "hyperref"]
#     try:
#         print("Installing LaTeX packages...")
#         subprocess.run(["miktex-console", "--install", "--yes"] + latex_packages, check=True)
#         print("LaTeX packages installed successfully!")
#     except FileNotFoundError:
#         print("LaTeX package manager not found. Install MiKTeX or TeX Live.")
#         sys.exit(1)

# def launch_osdag():
#     """Launch Osdag."""
#     try:
#         import osdag
#         print("Osdag is installed and working!")
#     except ImportError:
#         print("Osdag module is not installed. Please check your setup.")
#         sys.exit(1)

# if __name__ == "__main__":
#     try:
#         if not check_conda_version():
#             installer_path = download_miniconda_installer()
#             if install_miniconda(installer_path):
#                 configure_conda_path()
#         initialize_conda()
#         setup_conda_env()
#         install_latex_packages()
#         launch_osdag()
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         sys.exit(1)
import os
import subprocess
import sys
import shutil

CONDA_PATH = shutil.which("conda")
ENV_NAME = "osdag-env"

def run_command(command, shell=True):
    """Run a shell command and exit if it fails."""
    result = subprocess.run(command, shell=shell, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def setup_conda_env():
    """Create and set up a Conda environment for Osdag."""
    print(f"Setting up Conda environment '{ENV_NAME}'...")
    run_command(f"{CONDA_PATH} create -n {ENV_NAME} -c conda-forge osdag -y")
    print(f"Conda environment '{ENV_NAME}' created successfully.")

def launch_osdag():
    """Activate Conda environment and launch Osdag."""
    print("Launching Osdag...")
    run_command(f"{CONDA_PATH} run -n {ENV_NAME} osdag")
    print("Osdag launched successfully!")

if __name__ == "__main__":
    if not CONDA_PATH:
        print("Conda is not installed. Please install Miniconda first.")
        sys.exit(1)
    
    if not os.path.exists(os.path.expanduser(f"~/.conda/envs/{ENV_NAME}")):
        setup_conda_env()
    
    launch_osdag()

