"""
@author Jerry on 2016-3-24
"""
import Tkconstants
import Tkinter
import tkFileDialog
import tkMessageBox
from FileDialog import *
from ScrolledText import ScrolledText
from xml.etree.ElementTree import fromstring, parse, XML, ElementTree

if __name__ == '__main__':
    root_tree = parse('xml.xml')
    # print list(root_tree.iter('property'))
    root = root_tree.getroot()
    results = []
    h1="Map<String, String> requiredColumns = adapTableSetting.getRequiredColumns();"
    h2="requiredColumns.clear();"
    model_1='requiredColumns.put("'
    key1 = 'alarm name'
    model_2='", webApplicationContext.getMessage("'
    value1='Alarm_number'
    model_3='", null, "Required", locale));'

    hh1='Map<String, String> customizeColumns = adapTableSetting.getCustomizeColumns();'
    hh2='customizeColumns.clear();'
    hhmodel_1='customizeColumns.put("'
    hhkey1='Alarm text'
    hhmodel_2='", webApplicationContext.getMessage("'
    hhvalue_1='Alarm_text'
    hhmodel_3='", null, "Required", locale));'

    # result = h1+h2
    # result = hh1+hh2
    # with open('out_code.txt', 'a') as f:
    #     f.write(result+"\n")

    for child in root:
        for child2 in child:
            key = child2.attrib['key']
            value = child2.attrib['value']
            split_key = key.replace(' ', '_')

            # result = model_1+key+model_2+split_key+model_3
            # with open('out_code.txt', 'a') as f:
            #     f.write(result+"\n")

            # result = hhmodel_1+key+hhmodel_2+split_key+hhmodel_3
            with open('out_code.txt', 'a') as f:
                f.write(split_key+'='+value+"\n")
