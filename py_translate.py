# coding =  utf-8
# @author: Jerry

import sys

reload(sys)
sys.setdefaultencoding("utf-8")
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xml.etree.ElementTree import fromstring, parse, XML, ElementTree


def append_result_to_file(result):
    with open('out_translate.txt', 'a') as f:
        f.write(result + "\n")


def translate(key):
    input_text = driver.find_element_by_id("inputText")
    translate_btn = driver.find_element_by_id("translateBtn")
    sleep(0.5)
    input_text.clear()
    input_text.send_keys(key)
    translate_btn.send_keys(Keys.ENTER)
    sleep(0.5)
    translated_result = driver.find_element_by_class_name("translated_result")
    sleep(0.5)
    result = translated_result.find_element_by_class_name("tgt")
    sleep(0.5)
    return result.text


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    root_tree = parse('xml.xml')
    root = root_tree.getroot()
    driver.get("http://fanyi.youdao.com/translate")
    for child in root:
        for child2 in child:
            key = child2.attrib['key']
            value = child2.attrib['value']
            split_key = key.replace(' ', '_')
            try:
                result = split_key + '=' + translate(value)
            except:
                 driver.refresh()
                 result = split_key + '=' + translate(value)

            append_result_to_file(result)
