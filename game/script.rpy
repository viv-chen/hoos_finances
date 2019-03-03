# The script of the game goes in this file.
# characteristics

screen stats_screen:
    frame:
        align(0.05,0.05)
        xysize(250, 450)
        vbox:
            align(0.0, 0.5)
            text "{u}Stats:{/u}"
            null height 10
            text "Age: [age]"
            null height 10
            text "Health: [health]"
            null height 10
            text "Balance: [account_balance]"
            null height 10
            text "Debt: [debt]"
            null height 10
            text "Credit Score: [credit_score]"
            null height 10
            text "Happiness: [happiness]"
            null height 10
            text "GPA: [gpa]"
            null height 10
            text "Network Score: [networking]"
            null height 10
            text "Investments: [investments]"
            null height 10
            text "401k: [fourk_account]"
# characteristics button
screen one_button_screen:
    textbutton "Stats" action If(renpy.get_screen("stats_screen"), Hide("stats_screen"), Show("stats_screen")) align (0.95, 0.05)

# Declare images used by this game
image counselor_office = "counseloroffice.png"
image hooville= "hooville.jpg"
image school="school.jpg"
image letter="letter.png"
image bedroom="bedroom.jpg"
image university = "university.png"
image bg moneys = "nothing.png"
image bg dorm = "dorm.png"
image bg freetime = "library.png"
image bg club = "tenniscourt.png"
image bg lecture = "lecture.png"
image financeoffice = "financeoffice.png"
image Landlord = "landlord.png"
# image accountant = "accountant.png"
image finadvisor = "financialad.png"

image bg internship = "internship.png"
image bg research = "research.png"
image bg parttime = "parttime.png"
image cherry= "cherry.jpg"
image dolphin="dolphin.png"

image bg sports = "tenniscourt.png"
image bg nothing = "nothing.png"
image bg social = "social.png"
image bg business = "business.png"

image bg study = "library.png"
image bg playy = "play.png"

# image bg richhouse = "rich_house.jpg"

image counselor="counselor1.png"

# Declare  characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[name]", color="#0c4687")
define c = Character("Guidance Counselor", color="#A52A2A")

define bff = Character("Celia", color = "#ffa07a")
image bff chill = "bff.png"

define fa = Character("Financial Advisior", color="#00954a")
define l = Character("Landlord", color="#A52A2A")
define b =  Character("Boss", color="#A52A2A")
define ac = Character("Accountant", color="#A52A2A")

# Defining variables for second priority check
define studied = 0
define played = 0
define studyB = 0
define playB = 0
define second = 0
define sportsB = 0
define socialB = 0
define businessB = 0
define nothingB = 0
define internshipB = 0
define researchB = 0
define parttimeB = 0

# The game starts here.
label start:
    $ import random
    default health = 5
    default account_balance = 500
    default debt = 0 #make red
    default credit_score = 650
    default happiness = 3
    default gpa = 3.0
    default investments = 0
    default networking = 0
    $ diploma = 0
    default salary = 0
    default age = 17
    default rent = 0
    default housing_costs = 0
    default transportation_costs = 0
    default fourk_account = 0
    $ effective_salary = salary
    $ tax_rate = 0

    play music "hoosfinance_sound.mp3" loop

    show screen one_button_screen
    scene hooville
    with fade
    "Welcome to Hooville."

    #input playername
    $ name = renpy.input("What's your name?")
    $ name = name.strip()

    scene school
    with fade
    p "I'm [name], a 17-year-old at Hooville High School wondering what to do with my life!"

label highschool:
    $ noSchool = False
    $ goTS = False
    $ goCC = False
    $ goSS = False
    $ goPC = False

    scene counselor_office
    with dissolve
    show counselor
    with dissolve

    c "[name], have you thought about what you want to do after high school?"

    menu: 
        "After high school, I want to:"

        "Go to Technical School.":
            $ goTS = True
            $ diploma = 1
            p"I think I want to go to Technical School!"
            c"Great! Technical School seems right up your alley! You'll receive more hands-on experience in the field of your interest."
            c"Tuition and fees will cost $16,500 per year for 2 years."
            c "You should fill out the FAFSA online to receive financial aid so you won't be in as much debt in the future."
            p"Great, thanks!"

        "Go to Community College":
            $ goCC = True
            $ diploma = 1
            p"I want to go to Community College!"
            c"Awesome! I think Community College will be a good fit for you. You'll also save a lot of money."
            c"Tuition costs $5,000 per year for 2 years and you're going to save a lot of money by living and eating with your parents."
            c "You should fill out the FAFSA online to receive financial aid so you won't be in as much debt in the future."
            p"Great, thanks!"

        "Go to a State School (Pay In-State Tuition)":
            $ goSS = True
            $ diploma = 2
            p"I want to go to a State school. I want to get in to HooVA!"
            c"I think HooVA will be a great fit for you. If you keep up your current GPA and study for the SAT getting in shouldn't be a problem."
            c"Tuition, fees, housing, and a meal plan for a year will cost $27,000 per year for 4 years."
            c"You should fill out the FAFSA online to receive financial aid so you won't be in as much debt in the future."
            p"Great, thanks!"

        "Go to a Private College":
            $ goPC = True
            $ diploma = 2
            p"I want to go to a Private College. I heard great things about William & Harry in Williamsburg!"
            c"I think William & Harry is a small college with a close-knit community. If you keep up your current GPA and study for the SAT getting in shouldn't be a problem."
            c"Tuition, fees, housing, and a meal plan for a year will cost $45,000 per year for 4 years."
            c"You should fill out the FAFSA online to receive financial aid so you won't be in as much debt in the future."
            p"Great, thanks!"

        "Not go to college and work!":
            $ noSchool = True
            $ diploma = 0
            p"I don't think I want to go to college right now. I might change my mind in the future but right now it's just not for me."
            c"Okay, you should look around and find a job that you're really passionate about that doesn't require a degree."
            c"Some jobs want a college graduate. But there are plenty that don't and still make a decent amount of money."
            p"Great, thanks! I'll look around!"
            jump adulthood

    
    #scene changes to black or to a room
    scene bedroom
    with fade
    
    if goSS:
        show letter at truecenter
        with dissolve
        "6 months later you received an acceptance letter from HooVA!!!! Congratulations!!! YOU'RE A HOOT NOW!"
        $ debt = debt + 27000
        hide letter
        with dissolve
    if goPC:
        show letter at truecenter
        with dissolve
        "6 months later you received an acceptance letter from William and Harry!!!! Congratulations!!!"
        $ debt = debt + 45000
        hide letter
        with dissolve
    if goTS:
        show letter at truecenter
        with dissolve
        "6 months later you received an acceptance letter from your local technical school, HooTech!!!! Congratulations!!!"
        $ debt = debt + 16500
        hide letter
        with dissolve
    if goCC:
        show letter at truecenter
        with dissolve
        "6 months later you received an acceptance letter from your local community college!!!"
        $ debt = debt + 5000
        hide letter
        with dissolve

    #Finaid
    if noSchool == False:     
        p"I'm kind of lazy... Is it worth my time to fill out the FAFSA?"
        if goSS:
            p"Agh and FAFSA is only for federal aid. HooVA even requires me to fill out their CSS profile for financial aid from the University itself. Ugh."
        if goPC:    
            p"Agh and FAFSA is only for federal aid. William & Harry even requires me to fill out their CSS profile for financial aid from the University itself. Ugh."
        menu:
            "Fill out the FAFSA. You'll save so much in the long-term. So it'll be worth.":
                if goSS:
                    $ debt = debt - 4000 
            "Nah, I have better things to be doing like my Biology homework that's due tomorrow.": 
                p"This probably won't become a big deal in the future right?"

call join_club

call priorities

call job

call priorities

call graduation

call adulthood

call retirement

return

####### THE CLUB ########

label join_club:
    scene university
    show bff chill
    with dissolve

    bff "Hey, [name]!"

    bff "I can't believe we're actually finished with high school!"

    bff "No more Mr. Evans to boss us around, am I right?"

    bff "By the way, have you thought of what kind of club you want to join?"

    menu:

        "Sports club":
            jump sports_club

        "Business Frat":
            jump business_club

        "Social club":
            jump social_club

        "Maybe nothing":
            jump nothing



label sports_club:
    scene university
    show bff chill

    $ sportsB = 1

    bff "I should've guessed haha."

    bff "Make sure to get me a ticket to one of your games!"

    bff "They better be in the front row!"
 
    jump after_club_scene



label business_club:
    scene university
    show bff chill

    $ businessB = 1

    bff "Haha. You were always the business-y one."

    bff "I don't get how you can stand all that even after school"

    jump after_club_scene



label social_club:
    scene university
    show bff chill

    $ socialB = 1

    bff "Oh snap."

    bff "Are you thinking of getting into an ethic org?"

    bff "Maybe we can go to a party together!"    

    jump after_club_scene


label nothing:
    scene university
    show bff chill

    $ nothingB = 1
    
    bff "What, why not?!"

    bff "Maybe you should come with me."

    jump after_club_scene


label after_club_scene:
    scene university
    show bff chill

    bff "I was thinking of trying to join a dance group, but who knows if I'll get in haha."
    
    bff "Well, can't hurt to try."

    bff "I gotta go now, but make sure to text me later, okay?"

    bff "See ya!"

    hide bff chill
    with dissolve

    return



######### PRIORITIES CHOICE #########


label priorities:

    scene bg lecture
    with fade

    if socialB:
        $ networking += 2
        $ happiness += 2
        scene bg social
        with fade
    if businessB:
        $ networking += 3
        scene bg business
        with fade
    if nothingB:
        $ happiness += 1
        $ gpa += .2
        scene bg nothing
        with fade
    if sportsB:
        $ health += 3
        $ networking += 1
        $ happiness += 1
        scene bg sports
        with fade

    if internshipB:
        scene bg internship
        with fade
    if researchB:
        scene bg research
        with fade
    if parttimeB:
        scene bg parttime
        with fade

    if studyB:
        scene bg study
        with fade
    if playB:
        scene bg playy
        with fade

    scene bg dorm
    with fade

    p "After a busy day, I finally get back to my dorm."


    p "I jump onto my bed and close my eyes for a bit"

    p "I wonder what I should focus on doing this year..."

    menu:

        "Study hard.":
            jump study

        "Play hard.":
            jump playy



label study:

    if studied:

        p "I should continue trying to study hard."

        p "My GPA is already so good, wouldn't want to bring it down now!"

        $ gpa += 0.2

        $ studyB = 1

        $ playB = 0

    else:

        p "I should try to focus on studying."

        p "GPA is pretty important isn't it?"

        p "I'm pretty sure if I study hard now, I can relax more in the future."

        p "There's a ton of cool classes anyways!"

        $ gpa += 0.3

        $ studied = 1

        $ studyB = 1

    if second:
        jump after_priority2
    else:
        jump after_priority1


label playy:
    
    if played:

        p "I made a ton of friends last year. I wouldn't want to lose out on fun memories with them"

        $ gpa += -0.1

        $ playB = 1

        $ studyB = 0

    else:

        p "You know what?"

        p "I'm young!"

        p "I shouldn't waste my youth working away!"

        p "Besides, I heard it's good to make strong connections in college."

        p "I'm sure this will help me a lot in the future."

        $ gpa += -0.1

        $ played = 1

        $ playB = 1

    if second:
        jump after_priority2
    else:
        jump after_priority1



label after_priority1:

    p "Oh!"

    p "It's Celia!"

    p "I should go hang out with her."

    # hide bg dorm
    # with dissolve
    scene black 
    with fade

    p "After a year of college, it feels like it was just a blur and another year goes by."

    return



label after_priority2:

    p "AGH!"

    p "I have no time to think about this!"

    p "I have an exam and a paper due tomorrow."

    scene black
    with fade

    p "After a year of college, it feels like it was just a blur and another year goes by."

    return

##########  JOB CHOICES  ###########

label job:

    scene bg lecture
    with fade

    if socialB:
        $ networking += 2
        $ happiness += 2
        scene bg social
        with fade
    if businessB:
        $ networking += 3
        scene bg business
        with fade
    if nothingB:
        $ happiness += 1
        $ gpa += .2
        scene bg nothing
        with fade
    if sportsB:
        $ health += 3
        $ networking += 1
        $ happiness += 1
        scene bg sports
        with fade

    if internshipB:
        scene bg internship
        with fade
    if researchB:
        scene bg research
        with fade
    if parttimeB:
        scene bg parttime
        with fade

    if studyB:
        scene bg study
        with fade
    if playB:
        scene bg playy
        with fade
    else:
        scene bg study

    scene bg dorm
    with fade

    p "I feel like I should try and focus on getting some money..."

    p "I wonder if I should try doing something..."

    menu:

        "Part-time Job":
            jump part_time

        "Internship":
            jump internship

        "Research":
            jump research


label part_time:

    p "I should probably get a part-time job."

    p "I heard that you can get a lot of money off of it."

    p "Maybe I can pay off my loans easier in the future."

    $ account_balance += 14400 # 2400 * 6 semesters
    $ networking += 1
    $ happiness -= 1
    $ parttimeB = 1

    jump after_job


label internship:

    p "I should start applying for internships."

    p "I heard from my friend I have to apply to at least a 100 or so to get one."

    p "Maybe I can get some money that way and get some work experience along with that too."

    $ account_balance += 8160 # 4080 * 2 summers
    $ networking += 3
    $ happiness -= 1
    $ internshipB = 1

    jump after_job



label research:

    p "I should ask my professor for a research position."

    p "It would probably be good for me to get close to my professor too."

    p "I heard they might not pay, but hopefully I'll earn some cash along the way."

    $ networking += 2
    $ gpa += 0.2
    $ happiness -= 1
    $ researchB = 1

    jump after_job



label after_job:

    p "Well, I can do that sometime this week."

    p "I should start working on that coding project I told myself I would do."

    scene bg dorm
    with dissolve

    return

############ GRADUATION SCENE ###############

label graduation:
    scene bg lecture
    with fade

    if socialB:
        $ networking += 2
        $ happiness += 2
        scene bg social
        with fade
    if businessB:
        $ networking += 3
        scene bg business
        with fade
    if nothingB:
        $ happiness += 1
        $ gpa += .2
        scene bg nothing
        with fade
    if sportsB:
        $ health += 3
        $ networking += 1
        $ happiness += 1
        scene bg sports
        with fade

    if internshipB:
        scene bg internship
        with fade
    if researchB:
        scene bg research
        with fade
    if parttimeB:
        scene bg parttime
        with fade

    if studyB:
        scene bg study
        with fade
    if playB:
        scene bg playy
        with fade
    else:
        scene bg study

    $ happiness += 3

    scene bg dorm
    with fade

    # hide bg dorm
    # with dissolve

    p "And with this ended my final year at university"

    scene cherry
    show bff chill

    bff "We're finally graduating!!"

    bff "I can't believe after all those years we're actually going out into the real world."

    p "It's kind of scary if you think about it isn't it?"

    bff "I don't know about you, but I can't wait to get out there and be free from 10-page essays and constant allnighters."

    p "That's fair."

    hide bff chill
    with dissolve
    scene black
    with fade
    # hide bg university
    # with dissolve

label adulthood:

    "After finishing your schooling, you've decided that it's time to find a job."

    "Several options are open to you, depending on where you went to school and what you did there."

    call get_job

    call get_housing

    call get_transportation

    $ age +=5
    $ account_balance = account_balance + effective_salary*5

    "Five years pass..."

    while age<65:
        call my_investments
        
        call my_taxes

        "Account Balance: [account_balance]"

        call housing_payments

        "Account Balance: [account_balance]"

        if debt > 0:
            call repay_loans

        $debt = debt + transportation_costs

        call random_events
        $ age +=5
        $ account_balance = account_balance + effective_salary*5
        $ account_balance = account_balance -20000

        if account_balance < 0:
            $debt = debt - account_balance
            $account_balance = 0
        if debt < 0:
            $debt = 0

    return

label get_job:

    scene visual-novel-background-12

    menu get_job1:

        "After interviewing for several positions, you decide to ..."


        "work as a Machine Learning Engineer" if diploma>=3 and gpa>=3:
            $ salary  = random.randint(100000+networking*2000, 120000+networking*2000)
            $ effective_salary = salary

            """
            Your work now involves core and applied machine learning research focused on both algorithm development and integration.
            """

            "Your salary will be set to $[salary]."

            "Congrats on the new position!"

        "work as a Software Developer" if diploma>=2 and networking>=1:
            $ salary  = random.randint(70000+networking*2000, 90000+networking*2000)
            $ effective_salary = salary

            """
            You have been hired as a full-time software developer to join a growing team developing an internal point 
            of sale and management software systems.
            """

            "Your salary will be set to $[salary]."

            "Congrats on the new position!"

        "work as a IT Administrator" if diploma>=1:
            $ salary  = random.randint(35000+networking*2000, 70000+networking*2000)
            $ effective_salary = salary

            """
            Your work now provides specialized capacity to support existing systems,
            software and equipment and the people who use them,and to facilitate company-wide information sharing and communication.
            """

            "Your salary will be set to $[salary]."

            "Congrats on the new position!"

        "work as a Uber Driver" if diploma>=0:
            $ salary  = random.randint(25000+networking*2000, 50000+networking*2000)
            $ effective_salary = salary

            """
            Your work will consist of fairly long days, driving people around, and sometimes making conversation.
            """

            "Your salary will be set to $[salary]."

            "Congrats on the new position!"
        
    return

label get_housing:
    scene rich_house
    menu housing_menu:
        "After considering several housing options and given your current credit score, you decide to ..."
        
        "buy a nice House ($20,000 down payment, $1000/month mortgage)" if credit_score>=620 and account_balance>= 20000:
            "As you look over your handsome villa, you question how you could have lived anywhere else"
            $ rent = 1000
            $ account_balance = account_balance-20000
            if account_balance < 0:
                $debt = debt - account_balance
                $account_balance = 0
            $ happiness = happiness + 2
            
        "rent a Penthouse apartment ($1500/month rent)" if credit_score>=620:
            "The breathtaking view of the city almost makes the price worth it, although you wonder whether"
            "maybe somewhere simpler would have done the same."
            $ rent = 1500
            $ happiness = happiness + 1

        "rent a normal apartment ($900/month rent)" if credit_score>=500:
            "It's not exactly a mansion but, it'll do."
            $ rent =  900

        "rent out someone's shady basement ($500/month rent)":
            "As you walk down the stairs into the basement, you consider the musty smell..."
            "and regret the choice you made even if it was the only option."
            $ rent = 500
            $ happiness = happiness - 2
    
    return


label get_transportation:
    scene hana
    menu transportation_menu:
        "Now that you have your job and housing secured, it's time to decide on how to get to work!"

        "Ride the Bus everyday ($100/month ticket)":
            "You don't love the people on the bus, but it gets you where you need to go and its cheap."
            $ transportation_costs = 100
            $ happiness = happiness - 1
        "Drive to work in an old used car ($1500 downpayment, $381/month payment + car insurance)" if account_balance>=1500:
            "It's a bit of a beater car, but it sure beats riding on the bus!"
            $ transportation_costs = 381
            $ account_balance = account_balance - 1500
        "Drive to work in a shiny new car ($2500 downpayment, $530/month payment + car insurance)" if account_balance>=2500:
            "Riding down the highway with the wind in your hair, you reflect on life and its imperminance..."
            "...you love your new car and hopefully you can afford it!"
            $ happiness = happiness + 1
            $ transportation_costs = 530
            $ account_balance = account_balance - 2500
            if account_balance < 0:
                $debt = debt - account_balance
                $account_balance = 0

    return

label my_investments:
    scene financeoffice
    show finadvisor
    "You arrive at your financial advisor's office : Hoosbanking "
    "My Financial Advisor waits for me to sit down in your chair and then bursts into a flurry of motion..."
    if investments == 0  or fourk_account == 0:
        fa "How much have you invested recently!?!?"
        "I simply shrug my shoulders sheepishly"
        fa "What about your 401k?"
        "Again I blankly stare at him..."
        fa "How can you not know that a A 401(k) is a retirement savings plan sponsored by an employer."
        fa "It lets workers save and invest a piece of their paycheck before taxes are taken out. Taxes aren’t paid until the money is withdrawn from the account."
        "He clicks his pen, then paces the room..."
        fa "At [age], you'd someone like you would know more about this now, what do you think?"
    
    menu z:
        "I would like to start/put more money into a 401k? (15%% of your salary per year until retirement)":
            fa "Great Choice!"
            "It feels good to invest in your future, but how will I pay for Starbucks everyday?"
            $fourk_account = fourk_account + salary*.15
            $effective_salary = salary - salary*.15
            hide finadvisor
            with dissolve
        "I would like to start/continue investing some of my salary? (5%% of your salary per year, 6.5%% return)":
            fa "I suppose that's a start."
            "It feels good to put some money aside, but how will I afford Beats Headphones?"
            $investments = investments*.05 + salary*.05
            $effective_salary = salary - salary*.05
            hide finadvisor
            with dissolve
        "I would like to do both?":
            fa "Wonderful!, He clicks his pen and signs some papers as I leave the office."
            "It feels great to invest your money, but I'm afraid I'll have to eat cup ramen for a month..."
            $fourk_account = fourk_account + salary*.15
            $investments = investments*.05 + salary*.05
            $effective_salary = salary - salary*.20
            hide finadvisor
            with dissolve
        "I would like to do neither?":
            fa "Why even hire me??????????"
            $investments = investments + investments*.05;
            "It feels great to have so much spending money. It'll probably all work out right?"
            hide finadvisor
            with dissolve
    return

label repay_loans:
    scene financeoffice
    show finadvisor
    with dissolve
    "I'm back in the office with my financial advisor and he looks far too cheery for the given situation. "
    fa "Now it's time to repay your loans!"
    fa "I suggest you attempt to pay all of your loans off ASAP but, I understand that's not likely in your financial situation."
    fa "Make sure you at least try to pay off some of your loans or your credit score could go down which can affect things like your ability to buy a car."
    hide finadvisor
    with dissolve
    menu:
        "Would you like to repay your college loans incrementally ($300/month)?":
            "I feel better about paying back at least some of your debt."
            $happiness = happiness + 1
            $debt = debt - 5*12*300
            if debt <= 0:
                $debt = 0
            $account_balance = account_balance - 5*12*300
            if account_balance < 0:
                $debt = debt - account_balance
                $account_balance = 0
        "Would you like to repay your other loans incrementally ($300/month)?":
            "I feel better about paying back at least some of your debt."
            $happiness =  happiness + 1
            $debt = debt - 5*12*300
            if debt <= 0:
                $debt = 0
            $account_balance = account_balance - 5*12*300
            if account_balance < 0:
                $debt = debt - account_balance
                $account_balance = 0
        "Would you like to repay both incrementally ($600/month)?":
            "Although I feel overwhelmed, I feel better about paying back at least some of your debt."
            $happiness = happiness + 2
            $debt = debt - 5*12*600
            if debt <= 0:
                $debt = 0
            $account_balance = account_balance - 5*12*600
            if account_balance < 0:
                $debt = debt - account_balance
                $account_balance = 0
        "Would you like to repay all of your current debt($[debt])?" if account_balance>=debt:
            "It feels great to finally be debt free!"
            $happiness = happiness + 3
            $account_balance = account_balance - debt
            if debt <= 0:
                $debt = 0
            $credit_score = credit_score + 20
            $debt = 0
        "Would you like to not pay anything and suffer the consequences?":
            "I feel terrible about not being able to pay your loans back."
            $happiness = happiness - 2
            $credit_score = credit_score - 20
    return

label my_taxes:
    scene taxes
    if salary<=20000:
        $tax_rate = .15
    elif salary<=40000:
        $tax_rate = .20
    elif salary<=60000:
        $tax_rate = .23
    elif salary<=80000:
        $tax_rate = .26
    elif salary<=100000:
        $tax_rate = .28
    elif salary<=120000:
        $tax_rate = .30
    elif salary<=140000:
        $tax_rate = .30
    elif salary<=160000:
        $tax_rate = .30
    elif salary<=180000:
        $tax_rate = .31
    elif salary<=200000:
        $tax_rate = .31
    elif salary<=400000:
        $tax_rate = .37
    elif salary<=600000:
        $tax_rate = .39
    elif salary<=800000:
        $tax_rate = .42
    else:
        $tax_rate = .45

    $tax = salary*tax_rate
    scene financeoffice
    show accountant
    with dissolve
    "In your accountant's office she pushes her glasses up against her nose..."
    ac "Time to pay your yearly Federal and State Income Taxes!"
    ac "Due to the fact that you currently earn $[salary], you will have to pay $[tax] when you file your taxes. Make sure you do this everyyear and have the proper forms!."
    ac "Visit this site to figure out how to pay your taxes https://www.irs.gov/payments , but here I'll deduct it for you."
    hide accountant
    with dissolve
    $account_balance = account_balance - tax*5
    if account_balance < 0:
                $debt = debt - account_balance
                $account_balance = 0
    return

label housing_payments:
    scene rich_house
    show Landlord
    with dissolve
    if account_balance>0:
        l "Time to pay your rent/mortgage!"
        l "Your rent comes up to be $[rent] and not a minute too late!"
        l "If it feels too expensive, make sure that you rent/mortgage a place you can afford nexttime."
        hide Landlord
        with dissolve
        $account_balance = account_balance - rent*12*5
        if account_balance < 0:
                $debt = debt - account_balance
                $account_balance = 0
    else:
        l "I can't believe you wouldn't pay your rent on time!"
        "I feel a little bad about this and will make sure I have the money next time"
        $credit_score = credit_score - 20
        $debt = debt + rent*12*5
        hide Landlord
        with dissolve
    return


label random_events:
    $ rng = random.randint(1,11)

    if rng == 1:
        scene tenniscourt
        "Agh!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        "You sprained your ankle playing sports."
        "You've incurred debt from medical bills and your health has deteriorated"
        "Next time, do be more careful."
        $health = health - 1
        $debt = debt + 200

    elif rng == 2:
        scene visual-novel-background-12
        "Sitting in your seat one day at work you feel yourself dozing off..."
        "You lean forward and back in your chair but you just can't keep awake..."
        "ZZZZZzzzz"
        "ZZZZZZZZZZZzzzzzzzz"
        "ZZZZZZzzzzz"
        show boss
        with dissolve
        b "WHAT DO YOU THINK YOU'RE DOING!!!"
        b "YOUR'RE FIRED"
        b "Don't bother shutting the door on the way out!"
        "Guess it's time to search for another job..."
        hide boss
        with dissolve
        $happiness  = happiness - 2
        call get_job

    elif rng == 3:
        scene hana
        "On your way to work one day, your car is damaged in a freak windstorm"
        "It is totalled :("
        "You were in the hospital for a week to recover, left without a car, and unhappy about it's loss."
        $happiness = happiness - 1
        $health = health - 2
        $debt = debt + 1000
        call get_transportation

    elif rng == 4:
        scene visual-novel-background-12
        "Inexplicably, you got a bonus this year even though your performance consisted of you practicing your basketball skills on the wastebin."
        $account_balance = account_balance + 2500
        $happiness = happiness + 1

    elif rng == 5:
        scene visual-novel-background-12
        "Another day, and it seems like 5 years has passed..."
        "You wake up and go to the same job that you've been working at..."
        "Attending the same meetings with your bosses..."
        "Maybe one day you'll retire somewhere nice, let's hope you've been putting money in that 401k!"
        $happiness = happiness - 1

    elif rng == 6:
        "After being out of shape for awhile, you decide to get back into your local tennis club!"
        show bff
        with dissolve
        bff "Come on!"
        bff "I'll beat you just like I did when we were in college!"
        p "I'm not sure you ever beat me!"
        p "I'm coming!"
        hide bff
        with dissolve
        $happiness = happiness + 1
        $health = health + 2

    elif rng == 7 or rng == 8:
        scene parttime
        "Everyday, I swing by the lottery stand and try to see if I can win anything..."
        "... sadly your luck comes up short and you walk away with nothing but scratched tickets."
        $happiness = happiness - 1
        $account_balance = account_balance - 50
        if account_balance < 0:
                $debt = debt - account_balance
                $account_balance = 0

    elif rng == 9:
        scene parttime
        "Everyday, I swing by the lottery stand and try to see if I can win anything..."
        p "WOW!"
        "You won $25!"
        "It's not a ton of money, but it feels good to win something."
        $account_balance = account_balance + 25
        $happiness = happiness + 1

    elif rng == 10:
        scene play
        "After working such long hours, I finally get to go out with Celia again."
        show bff
        with dissolve
        bff "It's so fun to get to go out again!"
        p "Yeah, it's been like forever!"
        bff "Hey! Let's go Dance!"
        "You feel a bit worn out when you wake up but, it's always so fun to see Celia."
        hide bff
        with dissolve
        $happiness = happiness + 2
        $account_balance = account_balance - 15 
        if account_balance < 0:
                $debt = debt - account_balance
                $account_balance = 0
        $health = health - 1

    else:
        scene visual-novel-background-12
        "After sitting through meetings for years after years at your company, "
        "Your bosses have deemed you worthy of a measely 2%% raise..."
        "Congrats?"
        $happiness = happiness + 2
        $salary = salary + salary*.05

    return

label retirement:
    "Happy birthday! You are officially 65 years old!"
    if ((account_balance + investments + fourk_account > 999999) and (health > 4) and (happiness > 2)):
        scene beach
        "You saved up for a dope vacation in the Bahamas. You will live the rest of your long life in comfort. You did well in life. Good work [name]."
        p"I worked really hard for this. It all paid off in the end."
        show dolphin at truecenter
        with dissolve
        p"IT'S A DOLPHIN!"
    elif ((account_balance + investments + fourk_account > 100000) and (health > 4) and (happiness > 2)):
        scene rich_condo
        "You've made it. You saved so much with your investments and retirement fund. Now you get to reap the benefits and spend the rest of your life in comfort. Good work [name]."
        p"I worked really hard for this. It all paid off in the end."
    elif ((account_balance + investments + fourk_account > 100000) and (health > 4) and (happiness > 0)):
        scene visual-novel-background-12
        "You've saved a decent amount. You've worked hard. But you aren't happy."
        p"I worked so hard. Why am I so miserable?"
        "Maybe you should have saved more in your younger years."
        "Also you might want to do some self-reflection and read some self-help books about happiness."
    elif (health < 3):
        scene hospital
        with fade
        "You've worked so hard but you've also worked yourself into sickness."
        "The rest of your savings and investments will be used to pay hospital bills."
        "The doctor says you only have 10 more years to live."
        p"I wish I could've taken care of myself more."
        p"I'm going to try to enjoy my remaining 10 years."
    elif (account_balance + investments + fourk_account < 99999):
        scene visual-novel-background-12
        "You did not save enough to retire at the age of 65. You'll have to keep working until you die. It's not so bad though. You're not too miserable"
        p"I should have worked harder. I guess I'll just keep working forever."
        "Maybe you should have saved more in your younger years."
        "Also you might want to do some self-reflection and read some self-help books about happiness."
    else:
        scene graveyard
        "You fell down the stairs and died."
    return  # This ends the game.
