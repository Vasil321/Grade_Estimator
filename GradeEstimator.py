from graphics import *

# Decides the progress
def progress_decision(pass_credit, defer_credit):
    global count_prog, count_trail, count_retr, count_exc
    if pass_credit == 120:
        print("Progress\n")
        count_prog = count_prog + 1

    elif pass_credit >= 100:
        print("Progress(module trailer)\n")
        count_trail = count_trail + 1

    elif pass_credit + defer_credit >= 60:
        print("Do not progress - module retriver\n")
        count_retr = count_retr + 1
    else:
        print("Exclude\n")
        count_exc = count_exc + 1

# Checks if the input is out of range
def out_Of_Range(credit):
    if 20 > credit > 120 or ( credit % 10 != 0 or (credit / 10) % 2 != 0):
        print("Input Out of range\n")
        return True

# Checks if the total value is correct
def incorrect_total(pass_credit, defer_credit, fail_credit):
    if pass_credit + defer_credit + fail_credit != 120:
        print("Total Incorrect!\n")
        return True

#forces and stores the inputs
def inputs(inputed_var):
    global pas, defer, fail
    match inputed_var:
        case 1:
            pas = int(input("\nInput credits at pass: "))
            if out_Of_Range(pas):
                return True
        case 2:
            defer = int(input("Input credits at defer: "))
            if out_Of_Range(defer):
                return True
        case 3:
            fail = int(input("Input credits at fail: "))
            if out_Of_Range(fail):
                return True

# Main function
def main():
    while True:
        try:
            
            # loops through all the cases for the credits input
            i = 1
            while i != 4:
                if inputs(i):
                    continue
                i += 1

            # Checks if the sum of all the credits in larger than 120
            if incorrect_total(pas, defer, fail):
                continue 

            #Cases
            progress_decision(pas, defer)
        
            # quit or continue
            choice = input("Would you like to enter more data 'q' to quit or 'y' to continue: ")
            if choice.lower() == "q" or choice.lower() == "quit":
                break
    
        # If the input is not an integer!
        except ValueError:
            print("Integer required!\n")
            continue


count_prog, count_trail, count_retr, count_exc = 0, 0, 0, 0
main()


"""Histogram"""
count_list=[count_prog, count_trail, count_retr, count_exc]
total_outcomes = sum(count_list)

# Creates the layout of the bar
def create_bar(win, x, y, width, height, value, color, name):
    #the size and position of the bar
    bar = Rectangle(Point(x, y), Point(x + width, y - height))
    bar.setFill(color)
    bar.draw(win)

    # Outputs the number over the bar
    num_outcomes = Text(Point(x + width/2, y - height - 15), str(value))
    num_outcomes.draw(win)

    # The name under the bar
    labels = Text(Point(x + width/2, y + 20), name)
    labels.draw(win)

def hist():
    #Size of window
    win = GraphWin("Histogram", 600, 600)
    

    colors =["green", "yellow", "red", "purple"]
    names = ["Progress", "Trailer", "Retriver", "Excluded"]
    bar_width = 100
    spacing = 30
    x = 50
    y = 500

    # Total number of outcomes
    total_num_outcomes = Text(Point(x + 50, y + 80), str(total_outcomes) + " Total Outcomes")
    total_num_outcomes.draw(win)
    
    # Creates 4 bars each with diferent color and name
    for value, color, name in zip(count_list, colors, names):
        create_bar(win, x, y, bar_width, value * 20, value, color, name)
        x += bar_width + spacing
    
    # Closes the window on click
    win.getMouse()
    win.close()

hist()




"""List of inputs"""
print("\n Part 2: \n")

all_outcomes = [[120, 0, 0], [100, 0, 20], [60, 0, 60], [20, 20, 80]]

# Incorrect inputs
for outcome in all_outcomes:
    for credit in outcome:
        if (20 > credit or credit > 120) or (credit % 10 != 0 or (credit / 10) % 2 != 0):
            print("Input Out of range")
            continue
        


# Incorrect total
for outcome in all_outcomes:
    if sum(outcome) != 120:
        print("Total Incorrect!")
        continue

# Predicts the outcome
for outcome in all_outcomes:
    if outcome[0] == 120:
        print("Progress - " + ", ".join(str(credit) for credit in outcome))
    elif outcome[0] >= 100:
        print("Progress(module trailer) - " + ", ".join(str(credit) for credit in outcome))
    elif outcome[0] + outcome[1] >= 60:
        print("Do not progress (module retriver) - " + ", ".join(str(credit) for credit in outcome))
    else:
        print("Exclude - " + ", ".join(str(credit) for credit in outcome))
        

"""Text file data"""
print("\n Part 3: \n")


# Opens the text file
file = open("w1989035.txt", "r")

all_credits = []

# adds the data into a nested list
for line in file:
    # Creates a list for each row in the file
    credits_row = line.strip().split()

    # Coverts each item in the list created into integers
    credits_row = [int(credit) for credit in credits_row]

    # Adds the created lists into a nested list 
    all_credits.append(credits_row)
file.close()


# Incorrect inputs
for row in all_credits:
    for credit in row:
        if 20 > credit > 120 or (credit % 10 != 0 or (credit / 10) % 2 != 0):
            print("Input Out of range")
            continue

# Incorrect total
for row in all_credits:
    if sum(row) != 120:
        print("Total Incorrect!")
        continue

# Predicts outcomes
for row in all_credits:
    if row[0] == 120:
        print("Progress - " + ", ".join(str(credit) for credit in row))
    elif row[0] >= 100:
                print("Progress(module trailer) - " + ", ".join(str(credit) for credit in row))
    elif row[0] + row[1] >= 60:
        print("Do not progress - module retriver -- " + ", ".join(str(credit) for credit in row))
    else:
        print("Exclude - " + ", ".join(str(credit) for credit in row))
        
        
    