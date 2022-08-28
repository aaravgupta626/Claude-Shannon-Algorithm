import random,numpy as np
inputs= np.zeros((2,2,2),dtype=int)
second_last = 0
last = 0
scores = [0,0]

# Create the 'update_inputs()' function.
def update_inputs(current):
  if inputs[last_2][last_1][0] == current:
    inputs[last_2][last_1][1] = 1 
    inputs[last_2][last_1][0] = current
  else:
    inputs[last_2][last_1][1] = 0 
    inputs[last_2][last_1][0] = current
 
  last_2 = last_1 
  last_1 = current 

# Create the 'prediction()' function which returns the predicted value.
def prediction():
  if inputs[last_2][last_1][1] == 1: 
    predict = inputs[last_2][last_1][0]    
  else:
    predict = random.randint(0, 1)  
  return predict


#Create the 'update_scores()' function to keep the scores for both the computer and the player. It should not return anything.
scores=[0,0]
def update_scores(predicted,player_input):
  if player_input == predicted:
    scores[0] +=1
    print("Computer score: ",score[0],"\nPlayer score: ",score[1])
  else:
    scores[1]+=1
    print("Computer score: ",score[0],"\nPlayer score: ",score[1])

#Create the 'reset()' function which resets the values of the 'inputs' items to 0.
def reset():
  for i in range(2):
    for j in range(2):
      for k in range(2):
        inputs[i][j][k] = 0
  for i in range(2):
    scores[i]=0

#Create the 'gameplay()' function
def gameplay():
  reset()
  print(inputs)
  print(scores)
  valid_entries=["0","1"]
  while True:
    predicted = prediction()
    player_input = input("Enter either 0 or 1: ")
    while player_input not in valid_entries:
      print("Invalid input")
      player_input = input("Enter either 0 or 1: ")
    player_input = int(player_input)
    update_inputs(player_input)
    update_scores(player_input,predicted)
    if scores[0] == 10:
      print("Computer Wins!")
      break
    elif scores[1] == 10:
      print("You Win!")
      break

gameplay()