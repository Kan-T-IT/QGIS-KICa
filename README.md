# KAN Imagery Catalog - QGIS Plugin (Satellite Image Catalog Viewer)
---------------------------------------------------------------------

*  QGIS Minimum Version: 3.22

*  Docs: [kan_imagery_catalog.pdf](kan_imagery_catalog.pdf)

*  Plugin Installer: [kan_imagery_catalog.zip](dist/kan_imagery_catalog.zip)


### Development Environment Configuration
Project Repository: https://github.com/Kan-T-IT/QGIS-imagery-catalogue

Prerequisites:
* Operating System: Linux
* Python 3.9
* QGIS 3.22 or higher
* PyQt5

    `sudo apt install qtcreator pyqt5-dev-tools`

    `sudo apt install python3-pyqt5`

* QT Designer

    `sudo apt install qttools5-dev-tools`

    `sudo apt install qttools5-dev`



### To work with the project, follow these steps:

Clone the project:
`git clone https://github.com/Kan-T-IT/QGIS-imagery-catalogue.git`

Enter the project directory:
`cd qgis-imagery-catalogue`

Create a Python virtual environment:
`python3 -m venv env`

Activate it:
`source env/bin/activate`

Install dependencies from the requirements.txt file:
`pip install -r requirements.txt`

Update the path to the QGIS plugin directory (destination of the compiled plugin):

From QGIS, go to `Settings/User Profiles/Open Active Profile Folder`,
and within that directory, go to `python/plugins`. Update this path in the `deploy.sh` file (**PLUGIN_DIR** variable) and in `src/pb_tool.cfg` (key **plugin_path**).

The **deploy.sh** script handles everything necessary to generate the plugin files:
* Compiles template files
* Compiles the resource file
* Copies the resulting files to the local plugin directory

Important: The file requires execution permissions, so assign them first:
`chmod +x deploy.sh`


### Project Documentation
To update the project documentation, execute the following command from the project's root:

`make docs`

If you want to force compilation:

`make -B docs`

**IMPORTANT:** When updating the documentation, it is advisable to run `deploy.sh` to update the PDF file in the project's root.

To view the documentation in HTML version, execute from the project's root:

`python3 -m http.server 8000 -d docs/build/html/`

And access it from the browser:

`http://127.0.0.1:8000`