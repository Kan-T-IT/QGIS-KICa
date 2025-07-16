# KICa - KAN Imagery Catalog

## QGIS Plugin - Remote Sensing Catalog


* **Minimum QGIS Version:** 3.22

* [Code Documentation](https://kan-t-it.github.io/QGIS-KICa/)

* [Plugin Documentation](https://kan-t-it.github.io/QGIS-KICa-Doc/)

* [Download Plugin Releases](https://github.com/Kan-T-IT/QGIS-KICa/releases)

* [QGIS Plugin Repository](https://plugins.qgis.org/plugins/kan_imagery_catalog/)

---

## Contributing

This plugin integrates with various platforms to provide access to remote sensing data from within QGIS. You can contribute by reporting bugs or submitting pull requests.

---

## Development Environment Setup

To begin contributing, you’ll need to configure your development environment as described below.

### Recommended Prerequisites

- Linux operating system
- Python 3.9
- QGIS 3.22 or higher
- PyQt5
- Qt Designer
- LaTeX libraries (for documentation generation)

### Install PyQt5

```bash
sudo apt install qtcreator pyqt5-dev-tools
sudo apt install python3-pyqt5
````

### Install Qt Designer

```bash
sudo apt install qttools5-dev-tools
sudo apt install qttools5-dev
```

### Install LaTeX libraries

```bash
sudo apt update
sudo apt install latexmk
sudo apt install texlive-full
```

---

## Working with the Project

To collaborate on the QGIS plugin:

1. Clone the repository:

   ```bash
   git clone https://github.com/Kan-T-IT/QGIS-KICa.git
   ```

2. Navigate to the project directory:

   ```bash
   cd QGIS-KICa
   ```

3. Create a Python virtual environment:

   ```bash
   python3 -m venv env
   ```

4. Activate the virtual environment:

   ```bash
   source env/bin/activate
   ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Install pre-commit hooks:

   ```bash
   pre-commit install
   ```


7. Update the path to your QGIS plugin directory:

   * In QGIS, go to: `Settings > User Profiles > Open Active Profile Folder`.
   * Then go to: `python/plugins`.

   Update this path in the following files:

   * `deploy.sh`: modify the `PLUGIN_DIR` variable.
   * `src/pb_tool.cfg`: update the `plugin_path` value.

### Plugin Deployment

The `deploy.sh` script automates the following tasks:

* Compiling UI templates
* Compiling resource files
* Copying files to the QGIS plugins folder
* Creating a ZIP file in the `/dist` directory

**Note:** Ensure the script is executable:

```bash
chmod +x deploy.sh
```

---

## Code Documentation

To generate or update the code documentation:

### Generate Docs

From the root of the project:

```bash
make docs
```

To force a full rebuild:

```bash
make -B docs
```

### View HTML Documentation

1. Start a local HTTP server:

   ```bash
   python3 -m http.server 8000 -d docs/build/html/
   ```

2. Open in your browser:

   ```
   http://127.0.0.1:8000
   ```

### PDF Documentation

The PDF version of the documentation is located at the root of the project after building.
