from lxml import etree

def validate_xml(xml_filename, xsd_filename):
    xml_doc = etree.parse(xml_filename)
    xsd_doc = etree.parse(xsd_filename)
    xsd = etree.XMLSchema(xsd_doc)

    if xsd.validate(xml_doc):
        print("XML is valid against the XSD schema.")
    else:
        print("XML is not valid against the XSD schema.")
        for error in xsd.error_log:
            print(f"Line {error.line}, Column {error.column}: {error.message}")

if __name__ == "__main__":
    xml_filename = "employees.xml"
    xsd_filename = "employee_schema.xsd"
    validate_xml(xml_filename, xsd_filename)