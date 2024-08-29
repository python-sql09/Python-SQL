STEP 1: GATHER REQUIREMENTS
----------------------------
Before you begin to write code for any program, you should take the time to identify the requirements and expected use of that application. 

When you are working with a client,you should agree on the requirements early in the process, both to be sure that you understand what the client expects and to ensure that your final program meets those expectations.

In this case, the client wants a simple income tax calculator that will calculate the tax obligation for an individual, single filer, based only on income from wages and tips, as reported on a U.S. W-2 form. Remember that for many people, calculating income tax can be complicated by other forms of income, such as dividends and interest payments, so if you were going to create a calculator for more complicated returns, you should consult a tax expert to understand how other forms of income can affect a tax return.

Values in Use For this example, we are using values from U.S. Tax Law for the year 2024. If you want to calculate income taxes for another year, you may need to update the values used in the
calculations.
Specifically, we are assuming the following values to calculate taxable income based on gross income:
• All taxpayers are allowed a $12,200 standard deduction.
• For each dependent, a taxpayer is allowed an additional $2,000 deduction.
U.S. tax rates vary based on the amount of money earned. In 2024, the values in Table 6.1 are used to calculate a person’s income tax based on their taxable income.

# 2024 Tax Rates
# -------------------------------------------
# Tax Rate    Income for Single Individuals #
# -------------------------------------------
#   10%             Up to $11,600            #             
#   12%             $11,601 to $47,150       # 
#   22%             $47,151 to $100,525      #
#   24%             $100,526 to $191,950     #
#   32%             $191,950 to $243,725    #
#   35%             $243,726 to $609,350    #
#   37%             $609,350 or more        #
#--------------------------------------------

User Interface
---------------
We want the program to accept the following input values from the user:
• Gross income
• Number of dependents
At this point, we will also assume that the user will access the program through a terminal window, rather than through a form.

Other Standards
----------------
The number standards are as follows:
• Gross income must be entered to the nearest cent.
• The taxable income is expressed as a decimal number.
• The tax due is expressed as an integer.
All text that appears to the user should use correct grammar and spelling