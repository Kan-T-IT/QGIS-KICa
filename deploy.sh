#!/bin/bash

# This script runs the compilation of the templates, packages and deploys plugin files.

### We give a little color to the output...

message () {
    COLOR_TEXT='\e[40;1;37m'
    COLOR_MARGIN='\e[44;1;0m'
    NC='\e[0m'

    if [ "$2" ]; then
        if [ "$2" == "ALERT" ]; then
            COLOR_TEXT='\e[1;41;33m'
            COLOR_MARGIN='\e[0;33m'
        fi

        if [ "$2" == "SUCCESS" ]; then
            COLOR_TEXT='\e[1;37;42m'
            COLOR_MARGIN='\e[44;0m'
        fi
    fi

    text=${COLOR_TEXT}$1${NC}
    margin="-"
    margin=${COLOR_MARGIN}$margin${NC}

    text_lenght=${#text}+16
    total_width=90
    pad_1=$(echo "($total_width - $text_lenght)/2"|bc)
    pad_2=$(echo "($total_width - $text_lenght - $pad_1)"|bc)

    printf '\n'; printf $margin'%.0s' $(seq $total_width); printf '\n';
    printf ${COLOR_TEXT}' %.0s'${NC} $(seq $pad_1); echo -n -e $text;
    printf ${COLOR_TEXT}' %.0s'${NC} $(seq $pad_2); printf '\n';
    printf $margin'%.0s' $(seq $total_width); printf '\n\n';
}

#### Starting processes... ####
PLUGIN_NAME="kan_imagery_catalog"
PLUGIN_DIR="/home/fernando/.local/share/QGIS/QGIS3/profiles/default/python/plugins/"${PLUGIN_NAME}
BASE_DIR=$PWD
SOURCE_DIR=${BASE_DIR}"/src"
ZIP_PATH=${BASE_DIR}"/dist/"${PLUGIN_NAME}".zip"

message "REMOVE 'resource_rc' FROM .ui FILES (FIX: resources_rc error)"
python remove_resources_ui.py


message "COMPILE UI FILES (only ui dir files)"
_files=${SOURCE_DIR}"/ui/*.ui"

for f in $_files;
    do
        fout=${f%%.*}.py;
        echo $f;
        pyuic5 -x $f -o $fout;
    done


message "COMPILE TRANSLATION FILES"
make transcompile

cd ${SOURCE_DIR}

message "COMPILE RESOURCES"
pyrcc5 resources.qrc -o resources.py

message "COMPILE THE OTHER FILES AND MOVES TO PLUGIN DIR"

# The deploy option of pb_tool does not work with subdirectories to copy files,
# That is why they are compiled separately since they were excluded from the configuration
#pb_tool compile --config './pb_tool.cfg'
pb_tool deploy --config_file './pb_tool.cfg' -y

message "CLEAN UNNECESARY FILES FROM PLUGIN DIR"
find ${PLUGIN_DIR} -iname "*.pyc" -delete
find ${PLUGIN_DIR}"/ui/" -iname "*.ui" -delete
find ${PLUGIN_DIR} -iname "__pycache__" -delete
find ${PLUGIN_DIR} -iname ".git" -prune -exec rm -Rf {} \;


message "CREATE ${PLUGIN_NAME}.zip"
rm -f ${ZIP_PATH}
cd ${PLUGIN_DIR}/..; zip -9r ${ZIP_PATH} ${PLUGIN_NAME}

# Copy debug config to remote plugin folder
message "COPY .vscode "
cp -r ${BASE_DIR}/.vscode ${PLUGIN_DIR}/

now="$(date)"
message "PROCESS ENDED!   $now" "SUCCESS"
