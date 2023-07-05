 # Web Scrapper
 
#....


In the provided code, the scraping result is being saved to a CSV (Comma Separated Values) file. The resulting file will have two columns: "URL" and "Content".

The "URL" column will contain the URLs that have been scraped, and the "Content" column will contain the extracted content from each URL. The extracted content may vary depending on the structure of the web page and what has been specified in the extraction parameters.

The CSV format is widely used for storing tabular data. Each row in the file represents a data entry, and the values in each column are separated by commas. You can open this CSV file using spreadsheet software like Microsoft Excel or Google Sheets, or you can process it using data processing libraries in Python, such as pandas.

If you want to save the data in a different format, such as JSON or Excel, you can use the functions provided by pandas. For example, you can use to_json to save in JSON format or to_excel to save in Excel format. You would just need to adjust the part where the DataFrame is saved in the code.

By saving the scraped data in a CSV file, you can easily publish and share the data with others. It provides a structured and standardized format that can be easily imported and analyzed by various software and tools.


*to do list*:

. exe file                                                  
. add a function to let u choose the format to export files                                         
. add an option to choose the waypath       
.extract metadata
