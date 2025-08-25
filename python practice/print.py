# from loguru import logger



# length_of_land = 100
# breadth_of_land = 100
# bricks_cost_per_piece = 10.5
# labour_misri1 = "Yas"
# labour_misri2 = "Yone"
# is_home = True
 

# logger.info("bricks cost per unit is {}\nlength of land is {}".format(bricks_cost_per_piece,length_of_land))

from loguru import logger

# labour_1_name,labour_2_name,labour_3_name,labour_4_name = "Mahesh","Mithilesh","Ramesh","Sumesh"
# labour_1_wages = 500
# labour_2_wages = 400
# labour_3_wages = 400
# labour_4_wages = 300

# logger.info(f"labour_1 name is {labour_1_name} and his wages are {labour_1_wages}"))

a = int(input("Enter the number 1 =  "))
b = int(input("Enter the number 2 =  "))

logger.info(f"Addition of your Given Number is {a+b}")
logger.info(f"Subtraction of your Given Number is {a-b}")
logger.info(f"Multiplication of your Given Number is {a*b}")
logger.info(f"Division of your Given Number is {a/b}")
logger.info(f"Square of your Given Number 1 is {a*a}")
logger.info(f"Square of Given Number 2 is {b*b}")

