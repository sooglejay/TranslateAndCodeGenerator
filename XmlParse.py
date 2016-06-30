# coding =  utf-8
# @author: Jerry

import xml.etree.ElementTree as ET


class ExportImportConfig:
    def __init__(self):
        self.tablename = None
        self.exportConfig = None
        self.exportDelimiter = None
        self.exportFilePrefix = None
        self.importExport = None


class InstanceConfig:
    def __init__(self):
        self.instanceName = None
        self.ExportImportConfigList = []  # contains a list of InstanceConfig


class DatabaseConfig:
    def __init__(self):
        self.host = None
        self.user = None
        self.password = None
        self.port = None
        self.instanceConfigList = []  # contains a list of InstanceConfig


def getMysqlImportExportConfig():
    tree = ET.parse('./xml.xml')
    root = tree.getroot()
    databaseList = []
    for db in root.iter('database'):
        database = DatabaseConfig()
        database.host = db.find('host').text
        database.user = db.find('username').text
        database.password = db.find('password').text
        database.port = int(db.find('port').text)
        database.instanceConfigList = []
        for inst in db.iter('instance'):
            instance = InstanceConfig()
            instance.instanceName = inst.get('name')
            for ex_im in db.iter('export-import'):
                ex_im_config = ExportImportConfig()
                ex_im_config.tablename = ex_im.get('tablename')
                ex_im_config.exportConfig = ex_im.find('exportConfigure').text
                ex_im_config.exportDelimiter = ex_im.find('exportDelimiter').text
                ex_im_config.importExport = ex_im.find('importConfigure').text
                ex_im_config.exportFilePrefix = ex_im.find('exportFilePrefix').text
                #                print ex_im_config.tablename,ex_im_config.exportConfig ,ex_im_config.importExport
                print ex_im_config.exportDelimiter, ex_im_config.exportFilePrefix
                instance.ExportImportConfigList.append(ex_im_config)
            database.instanceConfigList.append(instance)
        databaseList.append(database)
    return databaseList


if __name__ == '__main__':
    exportlist = getMysqlImportExportConfig()
    print 'lend exportlist =', len(exportlist)
    for db in exportlist:
        print db.user, db.password, db.port
        for inst in db.instanceConfigList:
            print db.instanceConfigList
