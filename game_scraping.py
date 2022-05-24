#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Database connectivity
import mysql.connector
import time
while True:
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database='test')
    cursor = mydb.cursor(buffered=True)
    test = driver.page_source
    soup = BeautifulSoup(test, 'html.parser')
    for row in soup.findAll('div',attrs = {'class':'hawk-results-item'}):
    #     print(row)
        print("-----------------------")
        title = row.find('h2', attrs={'class': 'hawk-results-item__title'}).getText()
    #     print(title)
        Edition = row.find('p', attrs={'class': 'hawk-results-item__category'}).getText()
    #     print(Edition)
        language = row.find_all('div', attrs={'class': 'hawk-results-item__options-table-cell hawk-results-item__options-table-cell--name childCondition'})
    #     print(language)
        langs=[]
        for lang in language:
    #         print(lang.getText().strip())
            langs.append(lang.getText().strip())
    #     print(langs)

        Price = row.find_all('div', attrs={'class': 'hawk-results-item__options-table-cell hawk-results-item__options-table-cell--price childAttributes'})
    #     print(Price)
        price=[]
        for pric in Price:
            price.append(pric.getText())
    #     print(price)

        QTY = row.find_all('div', attrs={'class': 'hawk-results-item__options-table-cell hawk-results-item__options-table-cell--qty childAttributes'})
        qty=[]
        for qt in QTY:
            qty.append(qt.getText().strip())
    #     print(qty)
        connection = mysql.connector.connect(host="localhost",user="root",password="",database='test')
        mycursor = connection.cursor()
    #     mycursor.execute("Select * from startcity where Name=%s AND  Edition=%s")
    #     values = (title, edition )
    #     mycursor.execute(query, values)
    #     myresult = mycursor.fetchall()

        kwargs = {'Name': str(title),'Edition':str(Edition)}
        where_clause = 'WHERE ' + ' AND '.join([' ' + k + ' = %s' for k in kwargs.keys()])
        values = tuple(kwargs.values())
        sql = "SELECT *  FROM startcity " + where_clause
        mycursor.execute(sql, values)
        myresult = mycursor.fetchall()
        print("myresultmyresultmyresult",len(myresult),myresult)

        print(myresult,"-----------------")
        if len(myresult)>0:
            print("no")

        if len(myresult)==0:
            print("save,ffffffffffffffffff")
            connection = mysql.connector.connect(host="localhost",user="root",password="",database='test')
            mycursor = connection.cursor()
            sql = "INSERT INTO startcity (Name, Edition) VALUES (%s, %s)"
            val = (str(title), str(Edition) )
            print(val,"valllllllllllllllllll")
            mycursor.execute(sql, val)
            connection.commit()
            print("yhhhhhhhhhhhhhhhhhhh!@")

            connection = mysql.connector.connect(host="localhost",user="root",password="",database='test')
            mycursor = connection.cursor()
            kwargs = {'Name': str(title),'Edition':str(Edition)}
            where_clause = 'WHERE ' + ' AND '.join([' ' + k + ' = %s' for k in kwargs.keys()])
            values = tuple(kwargs.values())
            sql = "SELECT *  FROM startcity " + where_clause
            mycursor.execute(sql, values)
            myresult = mycursor.fetchall()
            print(myresult,"muuuuuuuuuuuuuuuuuuuuuuuuu")
            print(myresult[0][0])
            mainid=myresult[0][0]
            for l,p,q, in zip(langs,price,qty):
                print(l,p,q)
                connection = mysql.connector.connect(host="localhost",user="root",password="",database='test')
                mycursor = connection.cursor()
                sql = "INSERT INTO starcity (ID ,LANGUAGE, Qty,Price) VALUES (%s,%s, %s,%s)"
                val = (int(mainid),l,q,p )
                mycursor.execute(sql, val)
                connection.commit()
        
                
            
    try:
        driver.find_element_by_xpath("//a[@class='hawk-arrowRight hawk-pageLink ']").click()
        time.sleep(12)
    except:
        break


# In[ ]:




