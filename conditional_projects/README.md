#### 1. leap_year.py - Leap Year Checker 
**What it does:** User se ek year leta hai aur check karta hai ke wo Leap Year hai ya nahi.  
**Logic Used:** Pure Nested if-else + Modulo % operator.  
**Rule:** Ek year leap hota hai agar: 
1.  % 400 == 0 ho, YA 
2.  % 4 == 0 ho lekin % 100 != 0 ho.  
**Example:** Input 2024 → Output 2024 is a Leap Year  
**Example:** Input 1900 → Output 1900 is not a Leap Year


#### 2. discount_calculator.py - Age + Membership Discount 
**What it does:** User ki `age` aur `membership status` le ke total discount % batata hai.  
**Logic Used:** `Ladder if-elif-else` for 3 age slabs + `Nested if` for member check.  
**Discount Slabs:** 
- Child `< 18` = 20% + 5% if member = 25% total
- Senior `>= 60` = 30% + 5% if member = 35% total  
- Adult `else` = 10% + 5% if member = 15% total
**Example:** Age `65`, Member `True` → Output `Total discount: 35%`



  #### 3. temperature_system.py - Temperature Alert System  
**What it does:** Temperature aur Unit `C/F` leta hai, phir uske hisaab se alert deta hai.  
**Logic Used:** Pehle `if-else` se Unit check `Celsius ya Fahrenheit` + andar `if-elif-else` se Range check.  
**Alert Levels:** 
- `Celsius`: `<=0` = FREEZING, `<=30` = Normal/Warm/Cold, `>30` = HOT + `>=40` = EXTREME HEAT
- `Fahrenheit`: `<=32` = FREEZING, `<=86` = Normal, `>86` = HOT
**Example:** Input `38, C` → Output `HOT! Temperature above 30°C` + `Heat alert: Stay hydrated`

  
#### 4. atm_withdrawal.py - ATM Withdrawal System 
**What it does:** ATM se paise nikalne ka system. Balance, Daily Limit, aur 100 ke multiples check karta hai.  
**Logic Used:** 3-Level `Nested if-else` for validation + Modulo `%` operator.  
**Validation Checks in Order:**
1.  `Balance Check`: `withdrawal_amount <= balance`? Nahi to `Insufficient balance!`
2.  `Daily Limit Check`: `withdrawal_amount <= (daily_limit - daily_withdrawn)`? Nahi to `Daily limit exceeded!`
3.  `Denomination Check`: `withdrawal_amount % 100 == 0`? Nahi to `Enter multiples of 100`
**Example:** Balance `5000`, Withdraw `3000` → Output `Transaction Successful! Remaining Balance: 2000`
