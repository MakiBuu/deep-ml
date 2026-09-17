import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
            a = np.array(a)
            b  = np.array(b)

            shapea = a.shape
            shapeb = b.shape
                        
            if shapea[1] != shapeb[0]:
                return -1
                
            c = np.dot(a,b)

            return c


    