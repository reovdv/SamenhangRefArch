from bs4 import BeautifulSoup

#Read in the 'ArchiMate Model Exchange File Format' file
#These files are often used to exchange reference architectures
def read_XML_and_replace_ID_and_write_to_XML(filename):
    soup = BeautifulSoup(filename, "xml")

    element_tags = soup.find_all('element')

    for element_tag in element_tags:
        identifier = element_tag.get('identifier')

        property_tags_with_propid_8 = element_tag.find('property', {"propertyDefinitionRef" : "id-614359c532be4788a39d2cb103db1ee9"})
        
        correct_ID = property_tags_with_propid_8.find('value').text

        element_tag['identifier'] = correct_ID

    return soup.prettify()

with open('referentiearchitecturen_xml/FORA.xml', encoding='utf-8') as f:
        file = f.read()

updated_xml = read_XML_and_replace_ID_and_write_to_XML(file)

with open('referentiearchitecturen_xml/veranderde_referentiearchitecturen_xml/FORA_veranderd.xml', 'w', encoding='utf-8') as f:
    f.write(updated_xml)