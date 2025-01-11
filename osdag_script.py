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


import os
import subprocess
import sys
import requests

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
            else:
                print(f"Warning: Your Miniconda version ({installed_version}) is lower than the required version ({required_version}). Consider updating Conda.")
        else:
            raise FileNotFoundError("Conda not found")
    except FileNotFoundError:
        print("Miniconda not found. Installing Miniconda...")

def install_miniconda():
    """Install Miniconda if not present."""
    try:
        check_conda_version()  # Check if Conda is installed and its version
    except FileNotFoundError:
        miniconda_url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
        installer_path = os.path.join(os.getcwd(), "Miniconda3-latest-Windows-x86_64.exe")

        # Download Miniconda installer
        try:
            # Check if requests is installed, if not install it
            try:
                import requests
            except ImportError:
                print("Requests library not found. Installing requests...")
                subprocess.run([sys.executable, "-m", "pip", "install", "requests"], check=True)

            # Download Miniconda installer
            print(f"Downloading Miniconda from {miniconda_url}...")
            response = requests.get(miniconda_url)
            with open(installer_path, 'wb') as file:
                file.write(response.content)

            # Install Miniconda silently
            print("Installing Miniconda silently...")
            subprocess.run([installer_path, "/S", "/D=" + os.path.expanduser("~\\Miniconda3")], check=True)

            # Verify installation
            print("Verifying Miniconda installation...")
            subprocess.run([os.path.expanduser("~\\Miniconda3\\Scripts\\conda.exe"), "--version"], check=True)
            print("Miniconda installed successfully.")

        except requests.RequestException as e:
            print(f"Failed to download Miniconda: {e}")
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"Failed to install Miniconda: {e}")
            sys.exit(1)

def setup_conda_env():
    """Set up the Conda environment for Osdag."""
    env_name = "osdag-env"
    try:
        # Create and activate environment
        subprocess.run(["conda", "create", "-n", env_name, "python=3.8", "-y"], check=True)
        subprocess.run(["conda", "activate", env_name], shell=True, check=True)
        subprocess.run(["pip", "install", "osdag"], check=True)
        print("Conda environment 'osdag-env' set up and Osdag installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set up Conda environment or install Osdag: {e}")
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
        check_conda_version()
        install_miniconda()
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
