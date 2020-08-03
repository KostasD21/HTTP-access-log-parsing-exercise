import pandas as pd
import sys

#constant fields
HOST = "host"
REQUEST = "request"
RESPONSE_CODE = "response_code"

#prints the menu
def print_menu(data):

    while(True):
        print("****** Menu *********")
        print("1. Top 10 requested pages and the number of requests made for each")
        print("2. Percentage of successful requests (anything in the 200s and 300s range)")
        print("3. Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)")
        print("4. Top 10 unsuccessful page requests")
        print("5. The top 10 hosts making the most requests, displaying the IP address and number of requests made.")
        print("Select from 1-5 (0 for exit): ")
        i = input()
        selections(i, data)


#calls the method on user's input
def selections(input, data):
    if (input=='0'):
        exit()
    elif (input=='1'):
        top_ten_pages_requested(data)
    elif (input=='2'):
        percentage_success_requests(data)
    elif (input=='3'):
        percentage_unsuccess_requests(data)
    elif (input=='4'):
        top_ten_unsuccessfull_page_requests(data)
    elif (input=='5'):
        top_ten_hosts_with_the_most_requests(data)
    else:
        print("Invalid option!")
    return;


#halts the program
def exit():
    sys.exit("Exiting the program...")


#filters from the initial dataset all the web pages
def filter_only_web_pages(data):
    #A web page contains .html or does not contain . in the request
    return data[(data[REQUEST].str.find('.html') >= 0) | (data[REQUEST].str.find('.') == -1)]


#sets a new index ranging from 0 to the dimension of axis 0
def set_new_index_for_top_results(df):
    #construct a Series from 0 to the dimension of axis 0
    new_index = pd.Series(list(range(0,10 if df.shape[0] > 10 else df.shape[0])))

    #if the number of rows are greater than 10, then display 10 elements else display the number of rows
    df = df.iloc[:10 if df.shape[0] > 10 else df.shape[0]]

    #set the new index to the dataframe
    df = df.set_index(new_index)
    return df


#Top 10 requested pages and the number of requests made for each
def top_ten_pages_requested(data):

    #filter only the web pages
    data = filter_only_web_pages(data)

    #remove the column response code
    data = data.drop([RESPONSE_CODE], axis=1)

    #group by the request column
    grouped = data.groupby([REQUEST], as_index=False).count()

    #define the new columns of the data frame
    grouped.columns = [REQUEST,'count']

    #sort the values by the count descending
    sorted = grouped.sort_values(by=['count'], ascending=False)

    #set a new index for displaying the results
    sorted = set_new_index_for_top_results(sorted)

    print(sorted)
    return sorted


#Percentage of successful requests (anything in the 200s and 300s range)
def percentage_success_requests(data):

    #remove the columns host and request
    data = data.drop([HOST,REQUEST], axis=1)

    #filter the successful requests
    successful_requests = data[(data[RESPONSE_CODE].astype(int) >= 200) & (data[RESPONSE_CODE].astype(int) < 300)]

    #calculate the percentage of successful requests
    percentage_success_requests = (successful_requests[RESPONSE_CODE].count() / data[RESPONSE_CODE].count()) * 100

    print("Percentage: ",percentage_success_requests)
    return percentage_success_requests


#Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)
def percentage_unsuccess_requests(data):

    #remove the columns host and request
    data = data.drop([HOST,REQUEST], axis=1)

    #filter the unsuccessful requests
    unsuccessful_requests = data[(data[RESPONSE_CODE].astype(int) >= 300) | (data[RESPONSE_CODE].astype(int) < 200)]

    #calculate the percentage of unsuccessful requests
    percentage_unsuccess_requests = (unsuccessful_requests[RESPONSE_CODE].count() / data[RESPONSE_CODE].count()) * 100

    print("Percentage: ",percentage_unsuccess_requests)
    return percentage_unsuccess_requests


#Top 10 unsuccessful page requests
def top_ten_unsuccessfull_page_requests(data):

    #filter only the web pages
    data = filter_only_web_pages(data)

    #remove the column host
    data = data.drop([HOST], axis=1)

    #filter the unsuccessful
    unsuccessfull_requests = data[(data[RESPONSE_CODE].astype(int) >= 300) | (data[RESPONSE_CODE].astype(int) < 200)]

    #group by the request column
    grouped = unsuccessfull_requests.groupby([REQUEST], as_index=False).count()

    #define the new columns of the data frame
    grouped.columns = [REQUEST,'count']

    #sort the values by the count descending
    sorted = grouped.sort_values(by=['count'], ascending=False)

    #set a new index for displaying the results
    sorted = set_new_index_for_top_results(sorted)

    print(sorted)
    return sorted


#The top 10 hosts making the most requests, displaying the IP address and number of requests made.
def top_ten_hosts_with_the_most_requests(data):

    #remove the column response code
    data = data.drop([RESPONSE_CODE], axis=1)

    #group by the host column
    grouped = data.groupby([HOST], as_index=False).count()

    #define the new columns of the data frame
    grouped.columns = [HOST,'requests_count']

    #sort the values by the requests count descending
    sorted = grouped.sort_values(by=['requests_count'], ascending=False)

    #set a new index for displaying the results
    sorted = set_new_index_for_top_results(sorted)

    print(sorted)
    return sorted


#Parses the file
def parse_file():
    #assume that the first row has the right schema
    data = pd.read_csv('NASA_access_log_Aug95',
                        sep=" ",
                        header=None,
                        error_bad_lines=False,
                        engine='python')

    #drop columns that not needed
    data = data.drop([1,2,3,4,7], axis=1)

    #rename the remaining columns
    data.rename(
        columns={
            0: HOST,
            5: REQUEST,
            6: RESPONSE_CODE
        },
        inplace=True
    )

    #remove this redundant string from request column
    data[REQUEST] = data[REQUEST].str.replace("HTTP/1.0", "")

    #fill any missing values with ''
    data = data.fillna('')

    print_menu(data)


if __name__ == "__main__":
    parse_file()
