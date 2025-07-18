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

---

## Guide to Adding New Providers to the QGIS-KICa Plugin
### **Basic Structure of a Provider**
A provider in the QGIS-KICa plugin must meet the following requirements:

#### **Service Module:**
Create a file in the `services` directory that implements the necessary functions to interact with the provider (e.g., authentication, catalog retrieval, thumbnails, etc.).

#### **Configuration**:
Define the provider's credentials and specific parameters in the plugin's configuration file (`settings.py`).

#### **Core Integration**:
Modify the main modules (`catalogs.py`, `collections.py`, `providers.py`) to include logic specific to the new provider.

### **Steps to Integrate a New Provider**

1. **Create the Provider Module**:

    **Location:** `src/services/<provider_name>.py`

    Implement functions such as:
    - `get_token`: For authentication.
    - `get_catalog`: To retrieve catalog data.
    - `get_thumbnail`: To fetch preview images.
    - `get_quicklook`: To fetch quicklook images.
    - `get_collections`: To list available collections.

2. **Register the Provider in Configuration**:

    In `settings.py`, add the necessary credentials and parameters in `provider_settings`.

      Example:

      ```python
      default_provider_settings = {
          ...
          'new_provider': {'valid': False, 'api_key': '', 'username': '', 'password': ''}
      }
      ```

3. **Modify Core Modules**:

   - In `catalogs.py`, add logic to handle the new provider in functions like `get_catalog`, `get_thumbnail`, `get_quicklook`, etc.
   - In `collections.py`, include logic to retrieve collections from the new provider.
   - In `providers.py`, implement credential validation for the new provider.

4. **Update the GUI**:
   - In `form_settings.py`, add fields for the new provider's credentials and logic to validate them.

### **Practical Example: Adding the "NewProvider"**
1. **Create the Module `new_provider.py`**:

    /src/services/new_provider.py

    ```
    """NewProvider service module."""

    def get_token(username: str, password: str) -> str:
        # Implement authentication logic
        return "token"

    def get_catalog(token: str, search_params: dict) -> dict:
        # Implement logic to retrieve catalog data
        return {"features": []}

    def get_thumbnail(token: str, image_id: str) -> str:
        # Implement logic to fetch thumbnails
        return "thumbnail_url"

    def get_quicklook(token: str, image_id: str) -> str:
        # Implement logic to fetch quicklooks
        return "quicklook_url"
    ```

2. **Register in Configuration**:
   Modify `settings.py`:

   /src/core/settings.py

    ```python
    default_provider_settings = {
        ...
        'new_provider': {'valid': False, 'api_key': '', 'username': '', 'password': ''}
    }
    ```

3. **Modify Core Modules**:
   In `catalogs.py`, add logic to handle "NewProvider":

    src/core/catalogs.py

    ``` python
    if provider == 'new_provider':
        token = new_provider.get_token(
            username=provider_settings['username'],
            password=provider_settings['password'],
        )
        catalogs = new_provider.get_catalog(token=token, search_params=search_params)
    ```

4. **Update the GUI**:
   In `form_settings.py`, add fields for the credentials:

    src/gui/form_settings.py

    ```python
    self.new_provider_settings = self.settings.provider_settings.get('new_provider', {})
    self.new_provider_is_valid = self.new_provider_settings.get('valid', False)
    self.txt_new_provider_username.setText(self.new_provider_settings.get('username'))
    self.txt_new_provider_password.setText(self.new_provider_settings.get('password'))
    self.lbl_new_provider_check_credentials.setText('')
    ```
