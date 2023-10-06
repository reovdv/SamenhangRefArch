import re

def replace_IDs_FORA(filename):
    updated_content = re.sub(r'urn:uuid:', 'http://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-', filename)

    updated_content = re.sub(r'http://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-id-', 'http://www.gemmaonline.nl/index.php/GEMMA2/0.9/id-', updated_content)

    return updated_content

with open('referentiearchitecturen_rdf/GEMMA_rdf.xml', encoding='utf-8') as f:
        file = f.read()

updated_xml = replace_IDs_FORA(file)

with open('referentiearchitecturen_rdf/GEMMA_rdf_fixed.xml', 'w', encoding='utf-8') as f:
    f.write(updated_xml)
