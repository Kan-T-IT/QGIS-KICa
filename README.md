# KICa - KAN Imagery Catalog 

## QGIS Plugin - Remote Sensors Catalogue 


*  QGIS Minimum Version: 3.22

*  [Code Documentation](https://kan-t-it.github.io/QGIS-KICa/)

*  [Plugins Documentation](https://kan-t-it.github.io/QGIS-KICa-Doc/)

*  [Download Plugin Release](https://github.com/Kan-T-IT/QGIS-KICa/releases)

*  [QGIS Plugins Repository](https://plugins.qgis.org/plugins/kan_imagery_catalog/)


## Contributing

This plugins is a project that integrates different platforms to access from QGIS and one can collaborate, either on Bugs or Pull Requests. 


### Development Environment Configuration

As a first point, it is important to be able to configure the development environment, which we will describe below: 


#### Pre-requisites Recommended

* Operating System: Linux
* Python 3.9
* QGIS 3.22 or higher
* PyQt5
* QT Designer


#### Steps to install PyQt5 on linux

    `sudo apt install qtcreator pyqt5-dev-tools`

    `sudo apt install python3-pyqt5`

#### Steps to install QT Designer on linux

    `sudo apt install qttools5-dev-tools`

    `sudo apt install qttools5-dev`


### How to work with Project

To collaborate on this QGIS plugin project, please follow these steps:

1. Clone the project repository:
   ```
   git clone https://github.com/Kan-T-IT/QGIS-KICa.git
   ```

2. Navigate to the project directory:
   ```
   cd qgis-imagery-catalogue
   ```

3. Create a Python virtual environment:
   ```
   python3 -m venv env
   ```

4. Activate the virtual environment:
   ```
   source env/bin/activate
   ```

5. Install the project dependencies from the `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```

6. Update the path to the QGIS plugin directory (the destination for the compiled plugin):

   - In QGIS, access the user profile settings by going to `Settings/User Profiles/Open Active Profile Folder`.
   - Within the profile directory, navigate to the `python/plugins` folder.

   Update this path in two specific locations:

   - In the `deploy.sh` file, modify the **PLUGIN_DIR** variable.
   - In the `src/pb_tool.cfg` file, update the **plugin_path** key.

The `deploy.sh` script automates the necessary tasks to generate the plugin files, including:

- Compiling template files
- Compiling the resource file
- Copying the resulting files to the local plugin directory

**Important:** Ensure that the `deploy.sh` script has execution permissions. If not, assign them using the following command:
   ```
   chmod +x deploy.sh
   ```


## Project Code Documentation

To update the project's code documentation, perform the following steps from the project's root directory:

1. Generate the documentation:
   ```
   make docs
   ```

2. If you wish to force a recompilation of the documentation, use the following command:
   ```
   make -B docs
   ```

**Important:** When updating the documentation, it is recommended to also run the `deploy.sh` script to ensure that the PDF file in the project's root is updated.

To access the documentation in HTML format, follow these steps:

1. Start an HTTP server from the project's root directory:
   ```
   python3 -m http.server 8000 -d docs/build/html/
   ```

2. Open your web browser and navigate to the following address:
   ```
   http://127.0.0.1:8000
   ```
