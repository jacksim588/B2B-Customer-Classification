import requests
import os
import pandas as pd
from tqdm.auto import tqdm
from lxml import html
from bs4 import BeautifulSoup
from xml.etree import cElementTree as ET
import csv


'''

Initiating Variables

'''
Lines = []
NumBlankFiles = 0
directory = r'C:\Users\Clamfighter\Machine_Learning_Project\my_env\Heggle\B2B Customer Identification\Data Gathering\Data\Accounts_Monthly_Data-November2019'
leng = int(len(os.listdir(directory)))
print(leng)
currentlen = 1
loop = tqdm(total = leng, position=0, leave=False)
PeriodZeroTags = ['Period_TMinusZero','C','FY1']
PeriodOneTags = ['Period_TMinusOne','F','FY2']
columns = ['Month',
            'Company Number',
           'Company Name',
           'TurnoverRevenueY0',
           'TurnoverRevenueY1',
           'CostSalesY0',
           'CostSalesY1',
           'GrossProfitLossY0',
           'GrossProfitLossY1',
           'DistributionCostsY1',
           'DistributionCostsY2',
           'AdministrativeExpensesY0',
           'AdministrativeExpensesY1',
           'RawMaterialsConsumablesUsedY0',
           'RawMaterialsConsumablesUsedY1',
           'StaffCostsEmployeeBenefitsExpenseY0',
           'StaffCostsEmployeeBenefitsExpenseY1',
           'OperatingProfitLossY0',
           'OperatingProfitLossY1',
           'TaxTaxCreditOnProfitOrLossOnOrdinaryActivitiesY0',
           'TaxTaxCreditOnProfitOrLossOnOrdinaryActivitiesY1',
           'ProfitLossOnOrdinaryActivitiesAfterTaxY0',
           'ProfitLossOnOrdinaryActivitiesAfterTaxY1',
           'ExtraordinaryProfitLossAfterTaxY0',
           'ExtraordinaryProfitLossAfterTaxY1',
           'OtherTaxesNotAlreadyShownY0',
           'OtherTaxesNotAlreadyShownY1',
           'TotalAssetsLessCurrentLiabilitiesY0',
           'TotalAssetsLessCurrentLiabilitiesY1',
           'TotalAssetsY0',
           'TotalAssetsY1',
           'TotalLiabilitiesY0',
           'TotalLiabilitiesY1',
           'NetCashGeneratedFromOperationsY0',
           'NetCashGeneratedFromOperationsY1',
           'NetCashFlowsFromUsedInInvestingActivitiesY0',
           'NetCashFlowsFromUsedInFinancingActivitiesY1',
           'NameParentEntity',
           'NameUltimateParentGroupIfNotParentEntity',
           'NameUltimateControllingPartyIfNotUltimateParent',
           'NameMostSeniorParentEntityProducingPubliclyAvailableFinancialStatements',
           'ParentLargestGroupInWhichResultsAreConsolidatedHeading',
           'WagesSalariesY0',
           'WagesSalariesY1',
           'PremisesCostsY0',
           'PremisesCostsY1',
           'UtilitiesCostsY0',
           'UtilitiesCostsY1',
           'TaxTaxCreditOnProfitOrLossOnOrdinaryActivitiesY0',
           'TaxTaxCreditOnProfitOrLossOnOrdinaryActivitiesY1',
           'AverageNumberEmployeesDuringPeriodY0',
           'AverageNumberEmployeesDuringPeriodY1',
           'ProductionAverageNumberEmployeesY0',
           'ProductionAverageNumberEmployeesY1',
           'SalesMarketingDistributionAverageNumberEmployeesY0',
           'SalesMarketingDistributionAverageNumberEmployeesY1',
           'IncomeStatementBankingFinanceSectorHeadingY0',
           'IncomeStatementBankingFinanceSectorHeadingY1',
           'TotalOperatingIncomeY0',
           'TotalOperatingIncomeY1',
           'NetOperatingIncomeY0',
           'NetOperatingIncomeY1',
           'EmployeesTotalY0',
           'EmployeesTotalY1',
           'AverageNumberDirectorsY0',
           'AverageNumberDirectorsY1',
           'CountyRegion',
           'MainIndustrySector',
           'SICCodeRecordedUKCompaniesHouse1',
           'SICCodeRecordedUKCompaniesHouse2',
           'SICCodeRecordedUKCompaniesHouse3',
           'SICCodeRecordedUKCompaniesHouse4',
           'DepreciationAmortisationImpairmentExpenseY0',
           'DepreciationAmortisationImpairmentExpenseY1',
           'PatentsTrademarksLicencesConcessionsSimilarY0',
           'PatentsTrademarksLicencesConcessionsSimilarY1',
           'TotalSubsidiariesDefaultY0',
           'TotalSubsidiariesDefaultY1',
           'TotalReportableMajorCustomersIncludingAnyUnallocatedAmountY0',
           'TotalReportableMajorCustomersIncludingAnyUnallocatedAmountY1',
           'StartDateForPeriodCoveredByReport',
           'EndDateForPeriodCoveredByReport',      
           'filename']
'''

Gathering Data

'''
with open(r'C:\Users\Clamfighter\Machine_Learning_Project\my_env\Heggle\B2B Customer Identification\Data Gathering\Data\November.csv','w', newline='', encoding="utf-8") as fd:
    writer = csv.writer(fd)
    writer.writerow(columns)


    with tqdm(total=leng) as pbar:  #Progress Bar
        for filename in os.listdir(directory): #For each file in fodler
            pbar.update(1)
            currentlen += 1
            if filename.endswith(".html"):#only html files
                
                with open(directory+'\\'+filename, "r", encoding="utf8") as f:#open the html file
                    contents = f.read()
                    soup = BeautifulSoup(contents, 'lxml')#read the file
                    tag_list = soup.find_all()#find all the tags

                    #Regenerate Variables

                    Wanted_Tags = [
                        {'Tag':'bus:UKCompaniesHouseRegisteredNumber','ValueY0':None,'ValueY1':None},
                        {'Tag':'bus:EntityCurrentLegalOrRegisteredName','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:TurnoverRevenue','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:CostSales','ValueY0':None,'ValueY1':None},

                        {'Tag':'core:GrossProfitLoss','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:DistributionCosts','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:AdministrativeExpenses','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:RawMaterialsConsumablesUsed','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:StaffCostsEmployeeBenefitsExpense','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:OperatingProfitLoss','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:ProfitLossOnOrdinaryActivitiesAfterTax','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:ExtraordinaryProfitLossAfterTax','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:OtherTaxesNotAlreadyShown','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:TotalAssetsLessCurrentLiabilities','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:TotalAssets','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:TotalLiabilities','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:NetCashGeneratedFromOperations','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:NetCashFlowsFromUsedInInvestingActivities','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:NetCashFlowsFromUsedInFinancingActivities','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:NameParentEntity','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:NameUltimateParentGroupIfNotParentEntity','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:NameUltimateControllingPartyIfNotUltimateParent','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:NameMostSeniorParentEntityProducingPubliclyAvailableFinancialStatements','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:ParentLargestGroupInWhichResultsAreConsolidatedHeading','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:WagesSalaries','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:PremisesCosts','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:UtilitiesCosts','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:TaxTaxCreditOnProfitOrLossOnOrdinaryActivities','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:AverageNumberEmployeesDuringPeriod','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:ProductionAverageNumberEmployees','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:SalesMarketingDistributionAverageNumberEmployees','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:IncomeStatementBankingFinanceSectorHeading','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:TotalOperatingIncome','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:NetOperatingIncome','ValueY0':None,'ValueY1':None},

                        {'Tag':'core:EmployeesTotal','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:AverageNumberDirectors','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:CountyRegion','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:MainIndustrySector','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:SICCodeRecordedUKCompaniesHouse1','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:SICCodeRecordedUKCompaniesHouse2','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:SICCodeRecordedUKCompaniesHouse3','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:SICCodeRecordedUKCompaniesHouse4','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:DepreciationAmortisationImpairmentExpense','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:PatentsTrademarksLicencesConcessionsSimilar','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:TotalSubsidiariesDefault','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:TotalReportableMajorCustomersIncludingAnyUnallocatedAmount','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:DateFormationOrIncorporation','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:StartDateForPeriodCoveredByReport','ValueY0':None,'ValueY1':None},
                        {'Tag':'core:EndDateForPeriodCoveredByReport','ValueY0':None,'ValueY1':None},
                        
                    ]
                    '''

                    For each tag found, checks against wanted information
                    If information is wanted, saves the data to a variable
                        
                    '''
                    
                    for tag in tag_list:          
                        for Wanted_tag in Wanted_Tags:
                            if tag.has_attr('name') and (tag['name'] == Wanted_tag['Tag']):
                                if tag['contextref']  in PeriodOneTags:
                                    Wanted_tag['ValueY1'] = tag.text
                                else:    
                                    Wanted_tag['ValueY0'] = tag.text

                Line = [
                    "November",
                    Wanted_Tags[0]['ValueY0'],
                    Wanted_Tags[1]['ValueY0'],
                    Wanted_Tags[2]['ValueY0'],
                    Wanted_Tags[2]['ValueY1'],
                    Wanted_Tags[3]['ValueY0'],
                    Wanted_Tags[3]['ValueY1'],
                    Wanted_Tags[4]['ValueY0'],
                    Wanted_Tags[4]['ValueY1'],
                    Wanted_Tags[5]['ValueY0'],
                    Wanted_Tags[5]['ValueY1'],
                    Wanted_Tags[6]['ValueY0'],
                    Wanted_Tags[6]['ValueY1'],
                    Wanted_Tags[7]['ValueY0'],
                    Wanted_Tags[7]['ValueY1'],
                    Wanted_Tags[8]['ValueY0'],
                    Wanted_Tags[8]['ValueY1'],
                    Wanted_Tags[9]['ValueY0'],
                    Wanted_Tags[9]['ValueY1'],
                    Wanted_Tags[10]['ValueY0'],
                    Wanted_Tags[10]['ValueY1'],
                    Wanted_Tags[11]['ValueY0'],
                    Wanted_Tags[11]['ValueY1'],
                    Wanted_Tags[12]['ValueY0'],
                    Wanted_Tags[12]['ValueY1'],
                    Wanted_Tags[13]['ValueY0'],
                    Wanted_Tags[13]['ValueY1'],
                    Wanted_Tags[14]['ValueY0'],
                    Wanted_Tags[14]['ValueY1'],
                    Wanted_Tags[15]['ValueY0'],
                    Wanted_Tags[15]['ValueY1'],
                    Wanted_Tags[16]['ValueY0'],
                    Wanted_Tags[16]['ValueY1'],
                    Wanted_Tags[17]['ValueY0'],
                    Wanted_Tags[17]['ValueY1'],
                    Wanted_Tags[18]['ValueY0'],
                    Wanted_Tags[18]['ValueY1'],
                    Wanted_Tags[19]['ValueY0'],
                    Wanted_Tags[20]['ValueY0'],
                    Wanted_Tags[21]['ValueY0'],
                    Wanted_Tags[22]['ValueY0'],
                    Wanted_Tags[23]['ValueY0'],
                    Wanted_Tags[24]['ValueY0'],
                    Wanted_Tags[24]['ValueY1'],
                    Wanted_Tags[25]['ValueY0'],
                    Wanted_Tags[25]['ValueY1'],
                    Wanted_Tags[26]['ValueY0'],
                    Wanted_Tags[26]['ValueY1'],
                    Wanted_Tags[27]['ValueY0'],
                    Wanted_Tags[27]['ValueY1'],
                    Wanted_Tags[28]['ValueY0'],
                    Wanted_Tags[28]['ValueY1'],
                    Wanted_Tags[29]['ValueY0'],
                    Wanted_Tags[29]['ValueY1'],
                    Wanted_Tags[30]['ValueY0'],
                    Wanted_Tags[30]['ValueY1'],
                    Wanted_Tags[31]['ValueY0'],
                    Wanted_Tags[31]['ValueY1'],
                    Wanted_Tags[32]['ValueY0'],
                    Wanted_Tags[32]['ValueY1'],
                    Wanted_Tags[33]['ValueY0'],
                    Wanted_Tags[33]['ValueY1'],
                    Wanted_Tags[34]['ValueY0'],
                    Wanted_Tags[34]['ValueY1'],
                    Wanted_Tags[35]['ValueY0'],
                    Wanted_Tags[35]['ValueY1'],
                    Wanted_Tags[36]['ValueY0'],
                    Wanted_Tags[37]['ValueY0'],
                    Wanted_Tags[38]['ValueY0'],
                    Wanted_Tags[39]['ValueY0'],
                    Wanted_Tags[40]['ValueY0'],
                    Wanted_Tags[41]['ValueY0'],
                    Wanted_Tags[42]['ValueY0'],
                    Wanted_Tags[42]['ValueY1'],
                    Wanted_Tags[43]['ValueY0'],
                    Wanted_Tags[43]['ValueY1'],
                    Wanted_Tags[44]['ValueY0'],
                    Wanted_Tags[44]['ValueY1'],
                    Wanted_Tags[45]['ValueY0'],
                    Wanted_Tags[45]['ValueY1'],
                    Wanted_Tags[46]['ValueY0'],
                    Wanted_Tags[46]['ValueY1'],
                    filename
                    ] 
                writer.writerow(Line)
                        
                        
                continue
            else:
                continue

loop.close

df = pd.DataFrame(Lines,columns = columns)
print(df)
print('Number of blank files: ',NumBlankFiles)

df.to_csv(r'C:\Users\jacks\OneDrive\Documents\Work\CSR\XBRL\DirRem.csv',index = False)



