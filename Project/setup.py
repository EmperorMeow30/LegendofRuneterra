# Import/Modules/Libraries
import subprocess

def download_nltk_data():
    import nltk
    nltk.download('words')

def install_packages():
    subprocess.run(["pip", "install", "nltk", "pyfiglet", "pygame", "json"])

# Run installation tasks
install_packages()
download_nltk_data()