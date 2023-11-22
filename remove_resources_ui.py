""" Auxiliar module for update QtDesigner templates """
import glob
from xml.etree.ElementTree import ElementTree


def remove_node(file, nodo):
    """Remove node from xml file"""

    tree = ElementTree()
    tree.parse(file)
    root = tree.getroot()
    for i in root:
        if i.tag == nodo:
            root.remove(i)
    tree.write(file, encoding='UTF-8', xml_declaration=True)


if __name__ == '__main__':
    # This removes 'resources_rc' from the UI files,
    # otherwise, the build process is likely to return an error.

    print("Deleting 'resources_rc' from template files...")
    path = './src/'
    for file in glob.glob(path + '*.ui') + glob.glob(path + 'ui/*.ui'):
        try:
            remove_node(file, 'resources')
        except:  # noqa: E722    # pylint: disable=bare-except
            pass
        print(file)
