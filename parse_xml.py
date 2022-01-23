"""Functions for parsing XML API response """

import xml.etree.ElementTree as ET

def get_slideshow_elements(slideshow):
    slideshow_dict = {}
    for elem in slideshow: 
        slideshow_dict[elem.tag] = slideshow_dict.get(elem.tag, "") + elem.text
    return slideshow_dict

def slideshow_list(xml_string):
    slideshow_list = []
    root = ET.fromstring(xml_string)
    for child in root:
        if child.tag == 'Slideshow':
            slideshow_list.append(get_slideshow_elements(child))
    return slideshow_list