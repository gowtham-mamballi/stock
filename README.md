# stock
simple scripts to help in stock market trading/Investing.
Trading_setup.sh

This is simple bash script , which opens all the required internet tabs used for trading , like ticker tape , your broker account . Tabs are opened on Firefox session .

Ideal setup Instruction: 1.Create a file and paste the contents .eg : /home/mamballi/scripting/trading_setup.sh 2.Assign a ALIAS to that file as Bash executable. eg: alias Trade='bash /home/mamballi/scripting/trading_setup.sh' add the alias in vi ~/.bashrc and add the same line as above to create a permanent alias. 3.use the alias to open the sessions . eg : Trade 4.better result when the Firefox is opened before launching the script.

simple_stock_details.py

This script will give the opening and closing along with high and low of all the trading sessions from start date specified , and moving average data for all the sessions .

Install below packages before starting the script.

    datetime
    pandas
    pandas_datareader.data

Results are generated as .CSV file .
