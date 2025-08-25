from loguru import logger

labour_with_cost ={"Mahesh":500,"Ramesh":400,"Mithilesh":400,"Sumesh":300}

labour_with_cost["jagmohan"] = 1000

labour_with_cost["rampyare"] = 800

totalday = 50

for i in labour_with_cost:
    if i=="Mahesh":    
        absent = 3
    elif i=="jagmohan":
        absent = 7
    else :
        absent = 0

    logger.info(f"total labour cost of {i} for {50-absent} days is {labour_with_cost[i]*(totalday - absent)}")
