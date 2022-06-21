# Extract Images from PDF

* CLI tool to extract images from multiple pdf files as PNG. 
* Also generates a html file for thumbnails. 
* Demo: [Input](./src/Demo%20-%20Apple%20pie%20-%20Wikipedia.pdf) | [Output](./dist/Demo%20-%20Apple%20pie%20-%20Wikipedia.html)


## Installation

1. Check if Python is installed with `python -V` or `python3 -V`:
   ```cmd
   $ python -V
   Python 3.10.5
   ```
   If you have the Python Launcher installed, you can run `py -0` to show if multiple Python versions are installed:
   ```cmd
   $ py -0
   Installed Pythons found by py Launcher for Windows
    -3.10-64 *
    -3.6-64
   ```
   Run `py -0p` to show all Python installations and their paths:
   ```cmd
   $ py -0p
   Installed Pythons found by py Launcher for Windows
    -3.10-64       C:\Users\SomeUser\AppData\Local\Programs\Python\Python310\python.exe *
    -3.6-64        C:\Users\SomeUser\AppData\Local\Programs\Python\Python36\python.exe
   ```
2. Install `virtualenv` with `pip install virtualenv`.
3. Activate the virtual environment with `venv\Scripts\activate.bat`:
   ```cmd
   $ .\venv\Scripts\activate
   (env) $ 
   ```
4. Install the dependencies locally (in environment) with `pip install -r requirements.txt`.


## Usage

1. Copy at least one `.pdf` file to `src/`.
2. Start the virtual environment with
   ```cmd
   $ .\venv\Scripts\activate
   (env) $ 
   ```
3. Run the main script via `python .\main.py`. This runs the image extraction:
   ```cmd
   (env) $ python .\main.py
   Demo - Apple pie - Wikipedia: 100%|██████████████| 8/8 [00:00<00:00, 250.04it/s]
   ```
4. Deactivate the environment with `Deactivate`:
   ```cmd
   (env) $ deactivate
   $ 
   ```
5. View the extracted images by opening the generated `.html` file in `dist/`. 
