#### 1. leap_year.py - Leap Year Checker 
**What it does:** User se ek year leta hai aur check karta hai ke wo Leap Year hai ya nahi.  
**Logic Used:** Pure Nested if-else + Modulo % operator.  
**Rule:** Ek year leap hota hai agar: 
1.  % 400 == 0 ho, YA 
2.  % 4 == 0 ho lekin % 100 != 0 ho.  
**Example:** Input 2024 → Output 2024 is a Leap Year  
**Example:** Input 1900 → Output 1900 is not a Leap Year


#### 2. discount_calculator.py - Age + Membership Discount 
**What it does:** User ki age aur membership status le ke total discount % batata hai.  
**Logic Used:** Ladder if-elif-else for 3 age slabs + Nested if for member check.  
**Discount Slabs:** 
- Child < 18 = 20% + 5% if member = 25% total
- Senior >= 60 = 30% + 5% if member = 35% total  
- Adult else = 10% + 5% if member = 15% total
**Example:** Age 65, Member True Output total discount: 35%



  #### 3. temperature_system.py - Temperature Alert System  
**What it does:** Temperature aur Unit C/F leta hai, phir uske hisaab se alert deta hai.  
**Logic Used:** Pehle if-else se Unit check Celsius ya Fahrenheit + andar if-elif-else se Range check.  
**Alert Levels:** 
- Celsius: <=0 = FREEZING, <=30 = Normal/Warm/Cold, >30 = HOT + >=40 = EXTREME HEAT
- Fahrenheit: <=32 = FREEZING, <=86 = Normal, >86 = HOT
**Example:** Input 38, C → Output HOT! Temperature above 30°C + Heat alert: Stay hydrated

  
#### 4. atm_withdrawal.py - ATM Withdrawal System 
**What it does:** ATM se paise nikalne ka system. Balance, Daily Limit, aur 100 ke multiples check karta hai.  
**Logic Used:** 3-Level Nested if-else for validation + Modulo % operator.  
**Validation Checks in Order:**
1.  Balance Check: withdrawal_amount <= balance? Nahi to Insufficient balance!
2.  Daily Limit Check  withdrawal_amount <= (daily_limit - daily_withdrawn)? Nahi to Daily limit exceeded!
4.  Denomination Check: withdrawal_amount % 100 == 0? Nahi to Enter multiples of 100
**Example:** Balance 5000, Withdraw 3000 → Output Transaction Successful! Remaining Balance: 2000

#### 5. Profit & Loss Calculator
1. Show the title **"Profit & Loss Calculator"**.
2. Ask the user to enter the **cost price** (the price at which the item was bought).
3. Ask the user to enter the **selling price** (the price at which the item was sold).
4. Compare the selling price with the cost price.
5. If the selling price is **higher** than the cost price:
   * Find the profit by subtracting the cost price from the selling price.
   * Calculate the profit percentage.
   * Show the profit amount and the profit percentage.
6. If the cost price is **higher** than the selling price:
   * Find the loss by subtracting the selling price from the cost price.
   * Calculate the loss percentage.
   * Show the loss amount and the loss percentage.
7. If both prices are **equal**:
   * Show the message **"No profit, no loss."**



##### 6. Currency Converter
1. Display the title **"Currency Converter"**.
2. Ask the user to enter an amount in **Indian Rupees (INR)**.
3. Show a menu of currencies the user can convert the amount into:

   * USD (US Dollar)
   * EUR (Euro)
   * GBP (British Pound)
   * JPY (Japanese Yen)
4. Ask the user to choose one of the four currencies by entering a number from **1 to 4**.
5. Check the user's choice:
   * If the user chooses **1**, convert the INR amount to **US Dollars (USD)** using the given exchange rate and display the converted amount.
   * If the user chooses **2**, convert the INR amount to **Euros (EUR)** using the given exchange rate and display the converted amount.
   * If the user chooses **3**, convert the INR amount to **British Pounds (GBP)** using the given exchange rate and display the converted amount.
   * If the user chooses **4**, convert the INR amount to **Japanese Yen (JPY)** using the given exchange rate and display the converted amount.
6. Also display the exchange rate that was used for the conversion.
7. If the user enters any number other than **1, 2, 3, or 4**, display the message **"Invalid choice!"**






