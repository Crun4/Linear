import matrix 


class Correlation():
    def __init__(self,func, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.inputs = input_size / output_size
        self.func = func
        self.correlation_matrix = self.generate_corr()
        self.delta_matrix = self.generate_delta()
        return 

    def generate_corr(self):

        if self.inputs == 2:
            correlation_matrix = [0]*(1<<self.input_size)
            for i in range(0,(1<<self.input_size)):
                correlation_matrix[i] = [0]*(1<<self.output_size)

            for in_mask in range(0,(1<<self.input_size)):
                for out_mask in range(0,(1<< self.output_size)):
                    for i1 in range(0,(1<<self.input_size/2)):
                        for i2 in range(0,(1<<self.input_size/2)):
                            #print i1,i2
                            result = self.func(i1,i2)
                            #print "summ " + str(result)

                            if(self.mask(result,out_mask) == self.mask(i1+(i2<<self.input_size/2), in_mask) ):
                                correlation_matrix[in_mask][out_mask] += 1 

        return correlation_matrix
    def generate_delta(self):
        if self.inputs == 2:
            delta_matrix = [0]*(1<<self.input_size)
            for i in range(0,(1<<self.input_size)):
                delta_matrix[i] = [0]*(1<<self.output_size)

            for in_mask in range(0,(1<<self.input_size)):
                for out_mask in range(0,(1<< self.output_size)):
                    for i2 in range(0,(1<<self.input_size/2)):
                        for i1 in range(0,(1<<self.input_size/2)):
                            #print i1,i2
                            result = self.func(i1,i2)
                            

                            tmp = i1 + (i2 << self.input_size/2)
                            tmp = tmp ^ in_mask
                            #print tmp
                            #print tmp & ((1<<self.input_size/2)-1)
                            #print tmp >> (self.input_size/2)
                            #print "delta: " + str(self.func(tmp & ((1<<self.input_size/2)-1), tmp >> (self.input_size/2)))
                            #print "summ: " + str(self.func(i1,i2))
                            #print "in mask: " + str(in_mask)
                            #print "out mask: " + str(out_mask)

                            if(self.func(i1,i2) ^ self.func(tmp & ((1<<self.input_size/2)-1), tmp >> (self.input_size/2)) == out_mask):
                                delta_matrix[in_mask][out_mask] += 1 

        return delta_matrix


    def mask(self,a, mask):
        #print "data in: " + str(a)
        #print "mask in: " + str(mask)
        result = 0
        a = a & mask 
        while(a <> 0):
            result = result ^ (a & 1)
            a = a >> 1
        #print "mask result: " + str(result)
        return result

def add_mod(a,b):
    return (a+b) & 0xF

if __name__ == '__main__':

    result = Correlation(add_mod, 8,4)
    #correlation_matrix = matrix.Matrix(result.correlation_matrix)
    delta_matrix = matrix.Matrix(result.delta_matrix)
    #print correlation_matrix
    print delta_matrix
