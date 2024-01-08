import sysImage
import myImageManip

#Intro message
print("\n" + "Welcome to the image processor!")
print("\n" + "Here are your options: ")
print("0: Quit" + "\n"
      "1: Interlace with black lines" + "\n"
      "2: Invert the colour of the image" + "\n"
      "3: Convert the colour of the image into grayscale" + "\n"
      "4: Adjust the saturation")

#Set flag variable for the while loop to initiate
choice = 1

#Allow the user to input while the input is not 0
while int(choice) != 0:

    choice = input("Enter your choice (0/1/2/3/4): ")

    #If the input is not one of the options, ask again
    while choice.isdigit() == False or 0 < int(choice) < 1 or int(choice) > 4:

        print("\n" + "Sorry I dont understand " + str(choice))
        choice = input("Enter your choice (0/1/2/3/4): ")

    #If the input is 0, break the loop
    if int(choice) == 0:
        break

    if int(choice) == 1:
        interlaced = sysImage.getImage('ngc3132.jpg')
        myImageManip.interlace(interlaced)
        sysImage.saveImage(interlaced, "result-option1.jpg")
        print("Alright... image saved as 'result-option1.jpg'" + "\n")

    elif int(choice) == 2:
        inverted = sysImage.getImage('ngc3132.jpg')
        myImageManip.invert(inverted)
        sysImage.saveImage(inverted, "result-option2.jpg")
        print("Alright... image saved as 'result-option2.jpg'" + "\n")

    elif int(choice) == 3:
        grayscaled = sysImage.getImage('ngc3132.jpg')
        myImageManip.grayscale(grayscaled)
        sysImage.saveImage(grayscaled, "result-option3.jpg")
        print("Alright... image saved as 'result-option3.jpg'" + "\n")

    elif int(choice) == 4:
        saturated = sysImage.getImage('ngc3132.jpg')
        scale = float(input("Please enter a scale to saturate by: "))
        myImageManip.saturation(saturated, scale)
        sysImage.saveImage(saturated, "result-option4.jpg")
        print("Alright... image saved as 'result-option4.jpg'" + "\n")

#Exit message
print("\n" + "Thank you for using the image processor.")
input("Please press enter to exit")
