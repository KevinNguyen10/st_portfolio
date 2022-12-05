# import necessary libraries
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import pandas as pd
import base64

# st.set_page_config(layout="wide")

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def intro():
    import streamlit as st
    load_css('style.css')
    # Other functions
    icons = '''                                                                                                                                                     
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">                                                                                                    
    <ul>                                                                                                                                                                                                            
        <a href=https://www.linkedin.com/in/kevin-nguyen-298bba1b9 style="color: white"><i class="fab fa-linkedin-in fa-2x"></i><a/>
        <a href=https://github.com/KevinNguyen10 style="color: white"><i class="fa-brands fa-github fa-2x"></i> <a/>                                                                                                                                                                       
    </u1>
    '''

    intro = '''
    <h3> Hello, I'm Kevin!</h3>
    '''

    st.write(intro, unsafe_allow_html=True)
    st.title('Welcome to my Data Analytics Portfolio.')
    st.markdown("""I'm a **Data Analyst** who aims to use data to make better decisions. Being able to turn raw data into information has always been something I resonated with. 
    I've always enjoyed working with data and using it to drive decisions. I'm always looking to improve my skills and learn new things. Previously,
    I have used tools such as **Python**, **SQL**, **Power BI**, **Excel/Spreadsheets** for my data analytic projects.""", unsafe_allow_html=True)
    st.write(icons, unsafe_allow_html=True)
    st.martdown("""You can find some of my projects by clicking the **>** button on the left side of the screen.""")
    resume_png = Image.open('kevinnguyenresumev1-1.png')
    st.image(resume_png, caption='PNG Resume', use_column_width=True)
    with open("kevinnguyenresumev1.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Download PDF Resume",
                    data=PDFbyte,
                    file_name="kevinnguyenresume.pdf",
                    mime='application/octet-stream')
    

def emerson_coop_experience(): # Emerson Co-op Experience SECTION DONE!
    st.title("Emerson Co-op Experience")
    st.write("""I joined the Intelligent Automation & Analytics team at Emerson Fisher Controls as a Intelligent Automation & Analytics Co-op in Marshalltown, Iowa. 
        The team's mission was to automate manual processes using RPA (Robotic Process Automation) to allow end users to focus on the more important
        tasks rather than focusing on the tedious and less important tasks. During my 7 Month Co-op, I automated a total of 15 projects saving
        the people who used the processes 1300+ hours of work a year.""")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""**Company** - Emerson Fisher Controls""")
        st.markdown("""**Timeline** - May 2022 - November 2022""")
    with col2:
        st.markdown("""**Role** - Intelligent Automation & Analytics Co-op""")
        st.markdown("""**Skills** - Python, RPA, SQL, Excel/Spreadsheets, Data Visualization, Microsoft Office Suite Products, Git/Github""")
    st.title("What did I do?")
    st.write("""During my time at Emerson, I worked on a variety of projects. For example,
    I worked on projects that automated processes that were done manually, created dashboards for reporting, 
    and created scripts to help automate the collection, moving, storing, and cleaning of data.""")
    st.write("""Overall, working at Emerson was a great experience. The work life balance was great and the people were very friendly. I had full autonomy
    when it came to working on projects and I was able to work on projects that I was interested in. I also got the opportunity to improve my technical and non-technical skills.
    For example, I had the opportunity to learn more about SQL and RPA tools and got to teach others about the tools I learned through lunch and learns. I also got to host learning events for Emerson employees 
    to learn more about RPA tools like Python, RPA framework, and low code options like power query. Furthermore, since my manager got to be a data analytics manager along with
    an intelligent automation manager I got the opportunity to work on both data analytics and automation projects and got to learn a lot more about data analytics through my mentor.""")
    st.title('Some of my projects')
    st.write('Automatic Excel File Refresh Script')
    st.write('''For this project, I created a python script that would automatically refresh 18 excel files. For the current process the end user would manually 
    open each excel file, refresh, save and close the data. This Proceess took 30 minutes to an hour to complete. The script I created would automatically open, refresh, save, and 
    close the files. This process took about 4-7 minutes to complete. This project saved the end user about 12 hours of work a year.''')
    python_code = r'''
# Import necessary libraries
import time
import win32com.client
import os
start = time.time()
# Change file path 
os.chdir(PATH) # Select path of the folders
# Get all xlsx files
file_contents = os.listdir()
for index in range(len(file_contents)):
    if (file_contents[index].endswith('.xlsx')):
        abs_path = os.path.abspath(file_contents[index])
        # Start an instance of Excel
        xlapp = win32com.client.DispatchEx("Excel.Application")
        print('created xlapp instance.')
        # Open the workbook in said instance of Excel
        wb = xlapp.workbooks.open(abs_path)
        print(f'Opened {file_contents[index]} excel file.')
        # Optional, e.g. if you want to debug
        # xlapp.Visible = True
        # Refresh data connections.
        wb.RefreshAll()
        print(f'Successfully refreshed {file_contents[index]} excel file.')
        wb.Save()
        # Change this to False if you don't want it to be printed out
        wb.Close(SaveChanges=True)
        print('Close & save changes.')
        # Quit
        xlapp.Quit()
        print('Quit xlapp.')
        # Make sure the actual instance is deleted too. 
        del xlapp
        print('Delete xlapp instance.')
print('All files have been refreshed.')
end = time.time()
total_time = end - start
runtime_in_sec = time.strftime('%H:%M:%S', time.gmtime(total_time))
print(f'total runtime {runtime_in_sec}')
'''
    st.code(python_code, language='python')
    st.write('Dwell Time Shipment Power BI Dashboard')
    st.write('''For this project, I created a Power BI dashboard that would allow the end user to see the dwell time of shipments and track
    which shipments were released on time or still in hold status. It was a interactive dashboard that allow the end user to explore the data.''')
    image = Image.open('dashboard.png')
    st.image(image, caption='Dwell TIme Dashboard')
    st.write('Selenium Web Automation Data Collection Script')
    st.write('''For this project, I created a python script that would automatically download the data from the company web report using selenium and after it would output an excel file where I would use pandas to combine all the data 
    into one csv file using pandas. that would be loaded into a power query file where the end user could connect to Power BI and make their reports. Overall, this project saved
    840 hours of work a year and the automation takes 30 minutes to run and fully extract, transform, and load the data.''')
    
    selenium_python_code = r'''
# import necessary libraries
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import datetime
from datetime import date
import pandas as pd
import shipToLaterClosedOnlyScript as closed
import win32com.client
# track time
start = time.time()
statuses = ["Open", "Released"]
# driver options
for status in statuses:
    chromeOptions = webdriver.ChromeOptions()
    download_path = PATH
    prefs = {"download.default_directory" : download_path}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromeOptions.add_argument('log-level=3')
    chromeOptions.add_argument("start-maximized")
    chromeOptions.add_argument("enable-automation")
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--disable-dev-shm-usage")
    chromeOptions.add_argument("--disable-browser-side-navigation")
    chromeOptions.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chromeOptions)
    # open chrome and start automation
    open_chrome = driver.get(URL PATH)
    # Drop down for shipping warehouse
    select_warehouse = Select(driver.find_element(By.ID, 'ctl00_mainContentPlaceHolder_ddShippingWarehouse')).select_by_visible_text('All')
    # Drop down for order status
    select_end_user_country_code = Select(driver.find_element(By.ID, 'ctl00_mainContentPlaceHolder_ddEndUserCountryCode')).select_by_visible_text('All')
    select_status = Select(driver.find_element(By.ID, 'ctl00_mainContentPlaceHolder_ddOrderStatus')).select_by_visible_text(status)
    # select dates 
    release_date_from = driver.find_element(By.ID, 'ctl00_mainContentPlaceHolder_txtFromDateTime').send_keys('')
    release_date_to = driver.find_element(By.ID, 'ctl00_mainContentPlaceHolder_txtToDateTime').send_keys('')
    # click generate report button
    generate_report = driver.find_element(By.ID, 'ctl00_mainContentPlaceHolder_btnGenerateReport').click()
    # wait until button shows
    # click Export To Excel
    download_excel = driver.find_element(By.ID, 'ctl00_mainContentPlaceHolder_btnExportToExcel').click()
    # checking if file is done downloading!
    date_created = date.today().strftime("%Y%m%d")
    file_name = f"ExpediteOrdersHeldInShipping{date_created}.xlsx"
    file_path = f"PATH\{file_name}" # change when implementing into VM
    while not os.path.exists(file_path):
        time.sleep(1)
    if (os.path.isfile(file_path)):
        print(f"The file {file_name} has completed downloading!")
        driver.quit()
    else:
        raise ValueError(f"The file {file_name} did not download properly. Run again.")
    # changing directory download location
    change_directory = os.chdir(PATH) # change when implementing into VM
    new_name = f"ExpediteOrdersHeldInShipping{status}.xlsx"
    for file in os.listdir():
        if (file == file_name):
            if (file in os.listdir()):
                os.replace(file, new_name)
                print(f'Match found! replacing {file} with {new_name}')
                break
            else:    
                os.rename(file, new_name)
                print(f'file does not exist. created {new_name}.')
                break
        else:
            print('Match not found. Going Next.')
# get the closed data from the shipToLaterClosedOnlyScript
print('getting closed data.')
closed.closed_data() # Takes about 30 minutes to run for 4 years of data
print('Completed collecting closed data.')
# Read and store content
excel_path_open = PATH
excel_path_released = PATH
# of an excel file
read_open = pd.read_excel(excel_path_open) 
read_released = pd.read_excel(excel_path_released) 
# Write the dataframe object & convert the data that was downloaded into a csv file
csv_path_open = PATH
csv_path_released = PATH
csv_path_closed = PATH
print('converting excel file to csv.')
read_open.to_csv(csv_path_open,
				index = None,
				header=True)
print('read excel file to csv.')
os.remove(excel_path_open)
print('sucessfully removed excel file.')
read_released.to_csv(csv_path_released,
				index = None,
				header=True)
print('read file to csv.')
os.remove(excel_path_released)
print('sucessfully removed.')
# read csv file and convert into a dataframe object
df_open = pd.DataFrame(pd.read_csv(csv_path_open, skiprows=10, low_memory=False))
df_released = pd.DataFrame(pd.read_csv(csv_path_released, skiprows=10, low_memory=False))
df_closed = pd.DataFrame(pd.read_csv(csv_path_closed, low_memory=False)) # rows already skipped from the closed script
data = [df_open, df_released, df_closed]
final_data = pd.concat(data, ignore_index=True, verify_integrity=True)
# ETL to split the dates and get fiscal year
final_data['Date_Packaged'] = pd.to_datetime(final_data["Date Pkg'd"]).dt.date
final_data['Release_Date'] = pd.to_datetime(final_data["Release Date"]).dt.date
final_data[['Date_Packaged', 'Release_Date']] = final_data[['Date_Packaged', 'Release_Date']].astype('datetime64[ns]')
final_data['Release_Date_Quarter'] = final_data['Release_Date'].dt.to_period('Q-MAR')
final_data['Date_Packaged_Quarter'] = final_data['Date_Packaged'].dt.to_period('Q-MAR')
final_data['Fiscal Year (Release)'] = final_data['Release_Date_Quarter'].dt.qyear
final_data['Fiscal Year (Packaged)'] = final_data['Date_Packaged_Quarter'].dt.qyear
final_data['Fiscal Year (Release)'].replace(-1, 'NaT', inplace=True)
final_data.to_csv(PATH, index=False)
print("Data appended successfully.")
end = time.time()
total_time = end - start
runtime_in_sec = time.strftime('%H:%M:%S', time.gmtime(total_time))
print(f'total runtime {runtime_in_sec}')
    '''
    st.code(selenium_python_code, language='python')
def SQL_Database_Project():# SQL Database Project SECTION DONE!
    st.title('SQL Database Project')
    st.write('''This was a project I worked on for my SQL database management class for Fall of 2021. My group and I were tasked with creating a SQL database from any data source that the group
    found interesting. We ended up doing out database project on Netflix from a data source found on Kaggle. The data was from 2011-2020 and contained information on the movies and TV shows. For this
    showcase I will be showing the Analsis portion of the project and the code and queries used.''')
    st.subheader('SQL code for the tables that were created.')
    sql_tables = """
// SHOWS
// As the parent table, SHOWS was created first.
CREATE TABLE SHOWS (
ShowID VARCHAR2 (10) NOT NULL,
Title VARCHAR2 (105) NOT NULL,
Date_Added DATE,
Release_Year NUMBER NOT NULL,
Rating VARCHAR2(10),
SHOW_TYPE VARCHAR2(10) NOT NULL,
CONSTRAINT SHOWS_PK PRIMARY KEY (ShowID)
);

INSERT INTO SHOWS (ShowID, Title, Date_Added, Release_Year, Rating, Show_Type) VALUES ('s4115', 'Barbie Dreamhouse Adventures', '02/14/2019', 2018, 'TV-Y', 'TV Show')

// LISTEDIN
CREATE TABLE ListedIn (
ShowID VARCHAR2 (10) NOT NULL,
Genre VARCHAR2 (30) NOT NULL,
CONSTRAINT ListedIn_PK PRIMARY KEY (ShowID, Genre)
);

INSERT INTO LISTEDIN (ShowID, Genre)
VALUES ('s1164', 'International TV Shows')

// COUNTRY
CREATE TABLE COUNTRY (
ShowID VARCHAR2 (10) NOT NULL,
Country VARCHAR2 (30) NOT NULL,
CONSTRAINT COUNTRY_PK PRIMARY KEY (ShowID, Country)
);

INSERT INTO COUNTRY (ShowID, Country)
VALUES ('s1241', 'United States')

// PERSON 
CREATE TABLE PERSON (
PersonID NUMBER (5) NOT NULL,
First_Name VARCHAR2 (25) NOT NULL,
Middle_Name VARCHAR2 (20),
Last_Name VARCHAR2 (25),
CONSTRAINT PERSON_PK PRIMARY KEY (PersonID)
);

INSERT INTO PERSON (PersonID, First_Name, Middle_Name, Last_Name)
VALUES (323, 'Yussra', 'El', 'Abdouni')

CASTS
CREATE TABLE CASTS (
ShowID VARCHAR2 (10) NOT NULL,
PersonID NUMBER NOT NULL,
CONSTRAINT CASTS_PK PRIMARY KEY (ShowID, PersonID),
CONSTRAINT CASTS_FK FOREIGN KEY (PersonID) REFERENCES PERSON (PersonID)
);

INSERT INTO CASTS (ShowID, PersonID)
VALUES ('s1046', 3360)

MOVIE
CREATE TABLE MOVIE (
    ShowID VARCHAR(10) NOT NULL,
    MOVIE VARCHAR(3) NOT NULL
);

INSERT INTO MOVIE (MShowID, LengthMinutes)
VALUES ('s5369', '84')

TV
CREATE TABLE TV (
    ShowID VARCHAR(10) NOT NULL,
    TV VARCHAR(2) NOT NULL
);

INSERT INTO TV (TShowID, Number_Of_Seasons)
VALUES ('s1774', '1')
    """
    st.code(sql_tables, language='sql')
    st.subheader('Analysis of Netfix using SQL')
    st.write('''
    How many shows have been added to Netflix each year and how much has it been increasing and decreasing by? To address this question, 
    we created a subquery that counts how many TV shows were added in each year since 2008. We also calculated the difference between the 
    current year and the year prior to see how much it has fluctuated over the past 13 years.
    ''')
    sql_Q1 = '''
SELECT sub.*
FROM (
    SELECT EXTRACT(YEAR FROM date_added) AS year_added,
           COUNT(showID) AS total_shows_per_year,
           COUNT(showID) - COALESCE(LAG(COUNT(showID)) OVER(ORDER BY EXTRACT(YEAR FROM date_added)), 0) AS difference
    FROM SHOWS
    GROUP BY EXTRACT(YEAR FROM date_added)
) sub
WHERE year_added IS NOT NULL
ORDER BY sub.year_added DESC;
    '''
    st.code(sql_Q1, language='sql')
    image1 = Image.open('SQLQ1.png')
    st.image(image1, caption='SQL Query 1')
    st.write('''
    What is the total number of movies currently on Netflix? What is the total number of TV shows currently on Netflix? To address this question, 
    we created a query that contains an aggregate function, COUNT, which is used to count the total number of both movies and tv shows in the Netflix data. 
    ''')
    sql_Q2 = '''
SELECT show_Type, COUNT('Movie') AS TOTAL_NUM
FROM SHOWS
WHERE show_Type = 'Movie' OR show_Type = 'TV Show'
GROUP BY show_Type;
    '''
    image2 = Image.open('SQLQ2.png')
    st.image(image2, caption='SQL Query 2')
    st.code(sql_Q2, language='sql')
    st.write('What genres does Netflix have the most of? To address this question, we created a query that contains an aggregate function, COUNT, which is used to count the total number of each genre in the Netflix data.')
    sql_Q3 = '''
SELECT COUNT(S.ShowID), Genre
FROM Shows S
INNER JOIN ListedIn L
ON S.ShowID = L.ShowID
GROUP BY Genre
order bY COUNT(S.ShowID) DESC;
    '''
    st.code(sql_Q3, language='sql')
    image3 = Image.open('SQLQ3.png')
    st.image(image3, caption='SQL Query 3')
def personal_projects():
    pass
page_names_to_funcs = {
    "Home": intro,
    "Emerson Co-op Experience": emerson_coop_experience,
    "SQL Database Project": SQL_Database_Project 
    # "Personal Projects": personal_projects,
}

demo_name = st.sidebar.selectbox("Choose a Project", page_names_to_funcs.keys())
st.sidebar.success("Select a project above.")
page_names_to_funcs[demo_name]()