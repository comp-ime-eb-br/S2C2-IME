class XMLSchemaGenerator():
    START = '<?xml version="1.0" encoding="UTF-8" ?><xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"><xs:element name="result"><xs:complexType><xs:all><xs:element name="radioFrequency"><xs:complexType><xs:sequence><xs:element name="instant" maxOccurs="unbounded"><xs:complexType><xs:sequence><xs:element name="station" minOccurs="0" maxOccurs="unbounded"><xs:complexType><xs:all>'
    END = '</xs:all><xs:attribute name="name" type="xs:string" use="required"/></xs:complexType></xs:element></xs:sequence><xs:attribute name="time" type="xs:string" use="required"/></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="performance"><xs:complexType><xs:sequence><xs:element name="instance" minOccurs="0" maxOccurs="unbounded"><xs:complexType><xs:all><xs:element name="value" type="xs:string"/></xs:all><xs:attribute name="name" type="xs:string" use="required"/><xs:attribute name="time" type="xs:string" use="required"/><xs:attribute name="source" type="xs:string" use="required"/><xs:attribute name="destination" type="xs:string" use="required"/></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element></xs:all><xs:attribute name="roundID" type="xs:string" use="required"/></xs:complexType></xs:element></xs:schema>'


    def generate(self, radioFrequencyParams):
        xsElements = ""
        for radioFrequencyParam in radioFrequencyParams:
            paramName = str(radioFrequencyParam)
            xsElement = '<xs:element name="{}" type="xs:string"/>'.format(paramName)
            xsElements += xsElement

        return '{}{}{}'.format(self.START, xsElements, self.END)