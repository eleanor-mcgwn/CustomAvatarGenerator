from PIL import Image

# Start an infinite loop to continuously generate avatars
while True: 
    # Prompt the user for various component ID codes
    BackgroundID = input("ID code Background: ")
    FaceID = input("ID code Face: ")
    ClothingID = input("ID code Clothing: ")
    
    # Optional selection - enter '0' to not select
    HairID = input("ID code Hair (with colour, e.g., 1a, || enter '0' to skip): ")
    FacialHairID = input("ID code Facial Hair (with colour, e.g., 5e || enter '0' to skip): ")
    LipsID = input("ID code Lips (enter '0' to skip): ")
    AccessoriesID = input("ID code Accessories (enter '0' to skip): ")
    SpecialID = input("ID code Special (enter '0' to skip): ")

    # Load images based on user input
    Background = Image.open("Assets/Background/" + BackgroundID + ".png")
    Face = Image.open("Assets/Face/" + FaceID + ".png")
    Clothing = Image.open("Assets/Clothing/" + ClothingID + ".png")
    
    # Load optional images if the corresponding ID is not '0'
    if HairID != "0":
        Hair = Image.open("Assets/Hair/" + HairID + ".png")
        
    if FacialHairID != "0":
        FacialHair = Image.open("Assets/FacialHair/" + FacialHairID + ".png")

    if LipsID != "0":
        Lips = Image.open("Assets/Lips/" + LipsID + ".png")

    if AccessoriesID != "0":
        Accessories = Image.open("Assets/Accessories/" + AccessoriesID + ".png")

    if SpecialID != "0":
        Special = Image.open("Assets/Special/" + SpecialID + ".png")

    # Compose the final image by pasting components onto the background
    Background.paste(Face, (0, 0), Face)
    Background.paste(Clothing, (0, 0), Clothing)
    
    if HairID != "0":
        Background.paste(Hair, (0, 0), Hair)

    if FacialHairID != "0":
        Background.paste(FacialHair, (0, 0), FacialHair)

    if LipsID != "0":
        Background.paste(Lips, (0, 0), Lips)

    if AccessoriesID != "0":
        Background.paste(Accessories, (0, 0), Accessories)
        
    if SpecialID != "0":
        Background.paste(Special, (0, 0), Special)
    
    # Display and save the final composed image
    Background.show()
    Background.save("Output/" + BackgroundID + FaceID + ClothingID + HairID + FacialHairID + LipsID + AccessoriesID + SpecialID + ".png")
    
    # Print a completion message
    print("Complete: " + BackgroundID + FaceID + ClothingID + HairID + FacialHairID + LipsID + AccessoriesID + SpecialID + ".png\n")
