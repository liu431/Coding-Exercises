## Excel Notes

### Functions

#### String
=TRIM()
Removes leading and trailing spaces from the text in the formula

##### Conditions
[=IF(A1='Yes',1,2)](https://support.microsoft.com/en-us/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2) - IF(A1 = Yes, then return a 1, otherwise return a 2)

=IF(A1>=80, 'Senior',IF(AND(B1>21, B1<70), "Adult", "Young")): [Nesting IFs to handle more conditions](https://exceljet.net/formula/if-else)

[=CHOOSE(index_num, value1, [value2], ...)](https://support.microsoft.com/en-us/office/choose-function-fc5c184f-cb62-4ec7-a46e-38653b98f5bc): return a value from the list of value arguments

Ex. =CHOOSE(WEEKDAY(A1,1),"S","M","T","W","T","F","S"): return first letter of week days (Numbers 1 (Sunday) through 7 (Saturday))

[=IF(OR(A1>=0,A1<=100),A2,"The grade is out of range")](https://support.microsoft.com/en-us/office/or-function-7d17ad14-8700-4281-b308-00b131e22af0): displays the value in cell A2 if A1 is between 0 and 100, otherwise it displays a message.

#### Calculate values

[=SUMIF(range, criteria, [sum_range])](https://support.microsoft.com/en-us/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b): sum the values in a range that meet criteria that you specify

[=COUNT(value1, [value2], ...)](https://support.microsoft.com/en-us/office/count-function-a59cd7fc-b623-4d93-87a4-d23bf411294c): get the number of entries in a number field that is in a range or array of numbers

[=COUNTIF(Where do you want to look?, What do you want to look for?)](https://support.microsoft.com/en-us/office/countif-function-e0de10c6-f885-4e71-abb4-1f464816df34): count only numbers that meet certain criteria

[=COUNTIFS(criteria_range1, criteria1, [criteria_range2, criteria2]…)](https://support.microsoft.com/en-us/office/countifs-function-dda3dc6e-f74e-4aee-88bc-aa8c2a866842): count cells using multiple criteria

Ex. [Count Duplicate Values in Excel](https://www.got-it.ai/solutions/excel-chat/excel-tutorial/count/count-duplicates-in-excel)

[=COUNTA(value1, [value2], ...)](https://www.wallstreetmojo.com/counta-excel-function/#:~:text=The%20COUNTA%20function%20is%20an,but%2C%20cell%20A2%20is%20empty.&text=The%20COUNTA%20function%20can%20count%20cells%20containing%20several%20types%20of%20data%20values.): count the number of non-blank cells (not empty) in a cell range or the cell reference; used for logical values, text, and errors

[=COUNTBLANK(range)](https://support.microsoft.com/en-us/office/countblank-function-6a92d772-675c-4bee-b346-24af6bd3ac22): count the number of empty cells in a range of cells



#### Look up values
[=VLOOKUP(What you want to look up, where you want to look for it, the column number in the range containing the value to return, return an Approximate or Exact match – indicated as 1/TRUE, or 0/FALSE)](https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1):  (when you need to find things in a table or a range by row)

[=HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])](https://support.microsoft.com/en-us/office/hlookup-function-a3034eec-b719-4ba3-bb65-e1ad662ed95f)

[INDEX and MATCH](https://exceljet.net/index-and-match)

#### Pivot Tables
Purpose: quickly summarize data; interactive report

[Example](https://exceljet.net/excel-pivot-tables)

#### Dates
[=NETWORKDAYS(A1,B1)](https://support.microsoft.com/en-us/office/networkdays-function-48e717bf-a7a3-495f-969e-5005e3eb18e7) - return number of workdays between the start (A1) and end date (B1).

[=TODAY()](https://exceljet.net/excel-functions/excel-today-function) - returns the current date
