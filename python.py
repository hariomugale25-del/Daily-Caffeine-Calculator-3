

print("______Daily Cafeine Intake calculator___")

total_caffeine = 0.0
LIMIT = 400

print("Espresso                  : 61g")
print("Americano                 : 90mg")
print("Drip Coffee (240ml)       : 95mg")
print("Latte/Cappuccino          : 63mg")
print("Cold Brew (240ml)         : 165mg")
print("Instant Coffee            : 57mg")
print("Decaf Coffee              : 7mg")
while True:
    print(f"\nCurrent Caffeine Intake: {total_caffeine}mg")
    print(f"Daily Limit: {LIMIT}mg")
   
    print("\n1. Add Caffeine Intake (mg)")
    print("2. Exit")
   
    choice = input("Choose: ")
   
    if choice == '1':
        amount = float(input("Amount to add (mg): "))
       
       
        if total_caffeine + amount > LIMIT:
            print(f"\nALERT: Caffeine limit will exceed!")
            print(f"Current: {total_caffeine}mg")
            print(f"After taking: {total_caffeine + amount}mg")
            print(f"Limit: {LIMIT}mg")
           
            if input("Proceed? (y/n): ").lower() != 'y':
                print("Intake cancelled.")
                continue
        total_caffeine += amount
        print(f"Added {amount}mg of caffeine")
       
        if total_caffeine > LIMIT:
            print(f"WARNING: Limit exceeded by {total_caffeine - LIMIT}mg!")
           
    elif choice == '2':
        print("Goodbye!")
        
    else:
        print("Incorrect Choice ")

