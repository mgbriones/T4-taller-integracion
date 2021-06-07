import requests
from xml.etree import ElementTree
import pandas as pd



Codigopais = 'ALB'
url = 'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_'+Codigopais+'.xml'

response = requests.get(url)
tree = ElementTree.fromstring(response.content)


df = pd.DataFrame()

if response.status_code == 200:

    '''
    for child in tree.findall('Fact'):
        dic_aux = {}
        if child.find('GHO'):
            gho = child.find('GHO').text
            dic_aux.update({'GHO': gho})
            print({'GHO': gho})
        if child.find('COUNTRY'):
            COUNTRY = child.find('COUNTRY').text
            dic_aux.update({'COUNTRY': COUNTRY})
        if child.find('SEX'):
            SEX = child.find('SEX').text
            dic_aux.update({'SEX': SEX})

        if child.find('YEAR'):
            YEAR = child.find('YEAR').text
            dic_aux.update({'YEAR': YEAR})

        if child.find('GHECAUSES'):
            GHECAUSES = child.find('GHECAUSES').text
            dic_aux.update({'GHECAUSES': GHECAUSES})

        if child.find('AGEGROUP'):
            AGEGROUP = child.find('AGEGROUP').text
            dic_aux.update({'AGEGROUP': AGEGROUP})

        if child.find('Display'):
            Display = child.find('Display').text
            dic_aux.update({'Display': Display})

        if child.find('Numeric'):
            Numeric = child.find('Numeric').text
            dic_aux.update({'Numeric': Numeric})

        if child.find('Low'):
            Low = child.find('Low').text
            dic_aux.update({'Low': Low})

        if child.find('High'):
            High = child.find('High').text
            dic_aux.update({'High': High})

        print(dic_aux)
        print('\n\n-------------\n\n')
'''

    for fact in tree:
        dic_aux = {}
        for child in fact:

            if child.tag in ['GHO','COUNTRY', 'SEX', 'YEAR', 'GHECAUSES', 'AGEGROUP', 'Display', 'Numeric', 'Low', 'High']:
                dic_aux.update({child.tag: child.text} )

        df = df.append(dic_aux, ignore_index=True)

print(df)
