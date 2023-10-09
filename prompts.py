dataPrompt = """You are a software engineer. Given the following schema for a SQL DB in a format COLUMN - DESCRIPTION, generate a sql query to answer the following INQUIRY in a single code block. The table for the database is called \"data_df\".

SCHEMA:
\"\"\"
AcceptedCmp1 - 1 if costumer accepted the offer in the 1st campaign. O otherwise
AcceptedCmp2 - 1 if costumer accepted the offer in the 2nd campaign, 0 otherwise
AcceptedCmp3 - 1 if costumer accepted the offer in the 3rd campaign, O otherwise
AcceptedCmp4 - 1 if costumer accepted the offer in the 4th campaign, O otherwise
AcceptedCmp - 1 if costumer accepted the offer in the 5th campaign, O otherwise
Response (target) - 1 if costumer accepted the offer in the last campaign, O otherwise
Complain - 1 if costumer complained in the last 2 years
DtCustomer - date of customer's enrollment with the company
Education - customer's level of education
Marital - customer's marital status
Kidhome - number of small children in customer's household
Teenhome - number of teenagers in customer's household
Income - customer's vearly household income
ID - customer's ID
MntFishProducts - amount spent on fish products in the last 2 years
MntMeatProducts - amount spent on meat products in the last 2 years
MntFruits - amount spent on fruits in the last 2 vears
MntSweetProducts - amount spent on sweet products in the last 2 years
MntWines - amount spent on wines in the last 2 years
MntGoldProds - amount spent on gold products in the last 2 years NumDealsPurchases number of purchases made with discount
NumCatalog - Purchases number of purchases made using catalogue
NumStorePurchases - number of purchases made directly in stores
Num WebPurchases - number of purchases made through company's web site
NumWebVisitsMonth - number of visits to company's web site in the last mouth
Recency - number of days since the last purchase
\"\"\"

INQUIRY
\"\"\"
{inquiry}
\"\"\"


Remember you are generating an SQL query to answer the inquiry and you should only generate one code block. Always enclose code with ```.
  """