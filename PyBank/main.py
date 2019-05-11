import csv
import os
import math

# path to source data
file_to_load = os.path.join("..", "Resources", "PyBank_budget_data.csv")

    
# with open(cvspath, newline="", encoding='utf-8') as csvfile:
with open(file_to_load, newline="",  encoding='utf-8') as pybank_data:

    reader = csv.reader(pybank_data)

    # skip header row in csv file
    next(reader) 

    profit_loss= []
    date = []
    pl_change = []


    for row in reader:
        avgchgtotal = 0
        current_max = 0
        current_min = 0
        max_diff = 0
        min_diff = 0
        date_max = 0
        date_min = 0
        profit_loss.append(float(row[1]))
        date.append(row[0])
    #loop to find monthly change in profit and loss and append to the new list rev_change
    for i in range(0,len(profit_loss)):
        if i == 0:
            pl_change.append(0)
        else:
            pl_change.append(profit_loss[i] - profit_loss[i-1])
 
    # average change of profit_loss        
            avgchgtotal = sum(pl_change) / (len(pl_change)-1)
    # max / min change values
            max_diff = max(pl_change)  
            min_diff = min(pl_change)
    # max / min change dates
            date_max = str(date[pl_change.index(max(pl_change))])
            date_min = str(date[pl_change.index(min(pl_change))])

    print("Financial Analysis")
    print(".................................")
    print(f"Total Months: {len(date)}")
    print(f"Total: {('${:,.0f}'.format(sum(profit_loss)))}")
    print(f"Average Change: {('${:,.2f}'.format(avgchgtotal))}")
    print(f"Greatest Increasein Profits: {date_max}  {('${:,.0f}'.format(max_diff))}")
    print(f"Greatest Decrease in Profits: {date_min} {('${:,.0f}'.format(min_diff))}")

    # variable for output file
output_file = os.path.join("PyBank_budget_data.txt")
#Open the output file
with open(output_file, "w", newline="") as text_file:
    print("Financial Analysis", file=text_file)
    print(".................................", file=text_file)
    print(f"Total Months: {len(date)}", file=text_file)
    print(f"Total: {('${:,.0f}'.format(sum(profit_loss)))}", file=text_file)
    print(f"Average Change: {('${:,.2f}'.format(avgchgtotal))}", file=text_file)
    print(f"Greatest Increasein Profits: {date_max}  {('${:,.0f}'.format(max_diff))}", file=text_file)
    print(f"Greatest Decrease in Profits: {date_min} {('${:,.0f}'.format(min_diff))}", file=text_file)