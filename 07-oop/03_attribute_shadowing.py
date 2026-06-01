class Chai:
    temperature = "hot"
    strength = "strong"
    
cutting=Chai()

print(f"Before Changing/Shadowing : {cutting.temperature}")
cutting.temperature = "mild" # This is being overwrite
print(f"After Changing/Shadowing : {cutting.temperature}")

del cutting.temperature
print(f"After deleting : {cutting.temperature}") # The cutting.temperatue fallsback to the temperature of class

cutting.cup = "full"
print(f"Before deleting : {cutting.cup}")
del cutting.cup
print(f"After deleting : {cutting.cup}") # Throws error cuz the cup instance is not present in Chai , we have created it outside , so there is nothing to fall back after deletion
