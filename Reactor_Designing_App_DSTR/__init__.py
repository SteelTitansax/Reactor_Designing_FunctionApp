#Libraries
import logging
from scipy.integrate import quad
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Reactor designing Begins...')
    
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        # Variable declarations
        # ---------------------
        k = 0.3  # 1/min
        logging.info('k: ' + k )
        Ca0 = 10  # mol/l
        logging.info('Ca0: ' + Ca0 )
        X = 0.8
        logging.info('X: ' + X )

        # Kinetics
        # --------
        def rA(X):
            Ca = Ca0 * (1 - X)
            return k * Ca

        def integral(X):
            return X / rA(X)


        IntergerResult, err = quad(integral, 0, X)
        T = Ca0 * IntergerResult # hours
        logging.info("Reaction time : " + str(T))   
         
    return func.HttpResponse("Reactor designed successfully")
   






