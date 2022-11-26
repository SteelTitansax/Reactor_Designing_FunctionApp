import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Reactor designing Begins...')

    #Database insert function

    """
    server = 'SERVERNAME\INSTANCEID,64346'
    database = 'GRAPHAPI' 
    username = 'uname' 
    password = 'Happy2020'

    def insert_reactor_db(reactor_df,server,database,username,password):
    #Create a connection string
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
 
    for index in range(reactor_df.shape[0]): 
        #insert into table 
        try:
            insert_query = “INSERT INTO GRAPHAPI.dbo.[CSTR_Reactor] ([Ca0],[k],[Volume],[rA],[X]) VALUES (?,?,?,?,?)”
            cursor.execute(insert_query,reactor_df[‘Ca0’][index],reactor_df[‘k’][index],reactor_df[‘Volume’][index],reactor_df[‘rA’][index],reactor_df[‘X’][index])
        except:
            cnxn.rollback()
        finally:
            cnxn.commit()
            cnxn.close()
            #Call the function
            insert_reactor_db(users_df,server,database,username,password)
    """




    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:

        #Variable declarations
        #---------------------
        k = req_body.get('k')#1/min
        logging.info('k: ' + k )
        Ca0= req_body.get('Ca0')#mol/l
        logging.info('Ca0: ' + Ca0 )
        X = req_body.get('X')
        logging.info('X: ' + X )

    
        #Kinetics
        #--------
        def rA(X):
            Ca = Ca0*(1-X)
            return k*Ca

        #Design equation of an CSTR
        #--------------------------
        V = (-Ca0 * X) /-rA(X)
        logging.info("Volume : " + str(V) )
        # reactor_dict = {‘Ca0’:Ca0,'k':k,'Volume':V,'rA':rA,'X':X}
        # reactor_df = pd.DataFrame(data=reactor_dict)
        # insert_reactor_db(reactor_df,server,database,username,password)
        
    return func.HttpResponse("Reactor designed successfully")
    