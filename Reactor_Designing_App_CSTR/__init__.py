import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Reactor designing Begins...')

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

    return func.HttpResponse("Reactor designed successfully")
    