import requests
from xml.etree import ElementTree
import pandas as pd



Codigopais = 'ALB'
url = 'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_'+Codigopais+'.xml'


GHO_filtrados = ['Number of deaths'
,'Number of infant deaths'
,'Number of under-five deaths'
,'Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)'
,'Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)'
,'Estimates of number of homicides'
,'Crude suicide rates (per 100 000 population)'
,'Mortality rate attributed to unintentional poisoning (per 100 000 population)'
,'Number of deaths attributed to non-communicable diseases, by type of disease and sex'
,'Estimated road traffic death rate (per 100 000 population)'
,'Estimated number of road traffic deaths'
,'Mean BMI (crude estimate)'
,'Mean BMI (age-standardized estimate)'
,'Prevalence of obesity among adults, BMI > 30 (age-standardized estimate) (%)'
,'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)'
,'Prevalence of overweight among adults, BMI > 25 (age-standardized estimate) (%)'
,'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)'
,'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)",' #todo: puede que esta linea no deba tener: ",
,'Prevalence of thinness among children and adolescents, BMI < -2 standard deviations below the median (crude estimate) (%)'
,'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)'
,'Estimate of daily cigarette smoking prevalence (%)'
,'Estimate of daily tobacco smoking prevalence (%)'
,'Estimate of current cigarette smoking prevalence (%)'
,'Estimate of current tobacco smoking prevalence (%)'
,'Mean systolic blood pressure (crude estimate)'
,'Mean fasting blood glucose (mmol/l) (crude estimate)'
,'Mean Total Cholesterol (crude estimate)'
]

response = requests.get(url)
tree = ElementTree.fromstring(response.content)


df = pd.DataFrame()

if response.status_code == 200:

    for fact in tree:
        dic_aux = {}

        if fact.find('GHO').text in GHO_filtrados: #si tiene los GHO que quiero
            for child in fact:
                dic_aux_aux = {}
                if child.tag in ['GHO','COUNTRY', 'SEX', 'YEAR', 'GHECAUSES', 'AGEGROUP', 'Display', 'Numeric', 'Low', 'High']:
                    #if child.tag == 'GHO' and (child.text in GHO_filtrados):
                    dic_aux.update({child.tag: child.text})
                    #dic_aux_aux.update({child.tag: child.text})
                    #if dic_aux_aux['GHO'] in GHO_filtrados: # estoy asumiendo que el primer elemnto a leer es GHO
                        #dic_aux.update(dic_aux_aux)

        df = df.append(dic_aux, ignore_index=True)

df = df.dropna(how='all')
print(df)
print(df[['GHO','COUNTRY', 'SEX', 'YEAR', 'GHECAUSES']])
print(df[['AGEGROUP', 'Display', 'Numeric', 'Low', 'High']])
print(df.head(200))