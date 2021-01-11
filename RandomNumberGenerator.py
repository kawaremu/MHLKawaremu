import os,time  #Let's import the OS and time library

#We trying to make a random number generation out of scratch using real numbers from the computer of the hardware

def randomNumber(suprema):
  #The number we gonna return is gonna divide the processus ID by the time of the processor clock of the computer, modulo the number
  #given by the user.
  number = os.getpid()*time.time_ns()%(suprema/3) 
  return int(number)


print(randomNumber(456)) 
