import matplotlib.pyplot as plt

initial_weights = [-0.6, 0.7, 0.5]
train_Input = [[1,1],
              [9.4,6.4],
              [2.5,2.1],
              [8,7.7],
              [0.5,2.2],
              [7.9,8.4],
              [7,7],
              [2.8,0.8],
              [1.2,3],
              [7.8,6.1]]

train_Output = [1, 1 ,1, -1, -1, -1, -1, 1, -1, 1]

count = 0
while count < 30:

    for i in range(len(train_Input)):
        sublist = train_Input[i]
        sum = initial_weights[0] + initial_weights[1]*sublist[0] + initial_weights[2]*sublist[1]
            
        '''---activation function to map output of sum on 1 and -1--- '''
        if sum >= 0:
            actual_output = 1
        else:
            actual_output = -1

    
        if train_Output[i] == actual_output:
            pass
        else:
            '''     
                    ---formula to update weight---
            w_new = w_old + delta_w
            delta_w = learning_rate(actual_output - desired_output)xi
            '''
            desired_output= train_Output[i]   
            delta_w = (0.02* (actual_output - desired_output))
            w0_new = initial_weights[0] + (delta_w)*1 
            w1_new = initial_weights[1] + (delta_w)*sublist[0]
            w2_new = initial_weights[2] + (delta_w)*sublist[1]
            
            
            ''' ---weight updation in initial weight list--- '''
            initial_weights[0], initial_weights[1], initial_weights[2] = w0_new, w1_new, w2_new 
    print(initial_weights)
    count += 1


    ''' ---Graph Draw & boundry line between two data--- ''' 

for i in range(len(train_Input)):
    sublist = train_Input[i]
    desired_output_point = train_Output[i]
    if desired_output_point == 1:
        plt.scatter(sublist[0], sublist[1], label= "circle", color= "Red", marker= "o", s=30)
    else:
        plt.scatter(sublist[0], sublist[1], label= "cross", color= "blue", marker= "x", s=30)
        
                
        
    ''' ---To draw separator line--- '''
x = [] # x_point to draw separation line in graph
y = [] # Y_point to draw separation line in graph
for num in range(0,15):
    x.append(num)
        
    x2 = ((initial_weights[0]) + (initial_weights[1]*num))/initial_weights[2]
    y.append(x2)

plt.plot(x, y, color="green", linewidth = 1)        
plt.show()