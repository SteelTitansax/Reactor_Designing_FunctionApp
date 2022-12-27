#Libraries
import logging
from scipy.integrate import quad
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Reactor designing Begins...')

    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        #Variable declarations
        #---------------------
        k = req.body('k') #1/min
        logging.info('k: ' + k )
        Ca0= req.body('Ca0') #mol/l
        logging.info('Ca0: ' + Ca0 )
        V0 = req.body('V0') #l/min
        logging.info('V0: ' + V0 )
        X = req.body('X')
        logging.info('X: ' + X )
        Fa0 = Ca0 * V0 #mol/min
        logging.info('Fa0: ' + Fa0 )

        #Kinetics
        #--------
        def rA(X):
            Ca = Ca0*(1-X)
            return -k*Ca
        #Design equation of an FPR
        #-------------------------
        def integral(X):
            return Fa0/-rA(X)

        V,err = quad(integral,0,X)
        logging.info("Volumen : " + str(V) )

        return json.dumps(
        { 
            "Volume": V,
            "Ca0": Ca0,
            "rA": rA(X),
            "k" : k,
            "X" : X
        }
        )
    return func.HttpResponse("Reactor designed successfully")
   





