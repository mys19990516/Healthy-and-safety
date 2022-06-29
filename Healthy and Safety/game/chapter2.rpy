init python:
    GuessMoney=False
    isNumber=False
    ReLab1=False
    ReLab2=False
    ReLab3=False
    ReLab4=False
    ReLab5=False
    lentKevin=False
    wearclothe=False
    wearsandals=False
label chapter2:

    # scene white
    # with dissolve
    #
    # show text "After a painful exam week, your long-awaited summer holiday finally arrive."
    # pause
    #
    # show text "You have made many fulfilling travel plans."
    # pause
    #
    # show text "But! A virus called the Covid-19 suddenly begin to spread rapidly in the world."
    # pause
    #
    # show text "Sudden pandemic causes travel restrictions"
    # pause
    #
    # show text "It puts a damper on all your travel plans."
    # pause
    #
    # show text "You have to stay inside the school for the whole holiday."
    # pause
    #
    # show text "And your parents tell you that you must be responsible for your own living expenses for the summer."
    # pause
    #
    # show text "As the impact of the lockdown on the economy is huge."
    # pause
    #
    # show text "In order to earn money for the summer holidays, you decide to get a job."
    # pause
    #     #After your screening, you have decided to attend
    #     #(options can be added, restaurant waiter, courier)
    #
#     scene bg bedroom
#     with fade
#
#     show player_a:
#         zoom 0.5
#         xalign 0.2 yalign 0.35
#
#     Mys "I have to get a job, or I won't have any money to buy food!!!"
#     Mys "Missy said I could go to her office if I have difficulty, so I could ask her."
#
#     scene bg office
#     with fade
#
#     show player_a:
#         zoom 0.5
#         xalign 0.2 yalign 0.35
#
#     show Missy Normal at center:
#         xalign 0.7
#
#     Mys "Hi Missy, I have  some difficulties recently."
#     Missy "Hi, Mys, what difficulties are you having?"
#     Mys "Due to the new crown epidemic, our family is in a financial situation"
#     Mys "I have to earn my own living for the summer"
#     Mys "so I want to know if you could help me find a job."
#     Missy "Wow, what a coincidence, I have just recently received a notice from the university. "
#     Missy "I'm going to be in charge of recruiting cleaning staff for the new lab building. "
#     Missy "They will be paid. I think this is a great option for you."
#     Mys "Fantastic, can you sign me up?"
#     Missy "No problem, Guess how much money you will get?"
# label guess:
#     python:
#         # Ask player to enter his/her name
#             isNumber=False
#             money = renpy.input("Please enter the salary you expect here: ")
#
#             if money.isdigit():
#
#                 isNumber=True
#
#                 money=int(money)
#
#                 if money>=5000:
#                     GuessMoney=True
#     if not isNumber:
#         Missy "You didn't input a number, please input a number."
#         jump guess
#
#     if GuessMoney:
#         Missy "That's right, the school pays the staff [money]£ a month."
#         Mys "What??? Are you serious??"
#         Missy "Of course!"
#     else:
#         Missy "That's not correct, it's more than your expect"
#         jump guess
#
#     Mys "[money]£ is a lot. "
#     Mys "It is enough to live on for a month. "
#     Mys "Thank you very much."
label training:

    # scene white
    # with dissolve
    #
    # show text "With the help of Missy, you have managed to get a job. "
    # pause
    #
    # show text "The job involves cleaning the laboratory building for Manchester University."
    # pause
    #
    # show text "The first thing you need to do is get the relevant training."
    # pause

    scene bg classroom
    with dissolve

    show Missy Normal at center:
        xalign 0.7

    # Missy "I'm here today to give a training session."
    # Missy "Cleaning in the laboratory is different from normal cleaning work. "
    #
    # show player_a:
    #     zoom 0.5
    #     xalign 0.2 yalign 0.35
    #
    # Mys "what's the difference?"
    #
    # hide player_a
    #
    # Missy "When cleaning a laboratory, you not only have to clean the laboratory environment, "
    # Missy "but also clean the laboratory instruments and sort out the laboratory equipment. "
    # Missy "If the laboratory equipment becomes inoperable or causes a safety problem due to your improper handling, "
    # Missy "These are losses that the school cannot afford."
    # Missy "Therefore you need to be trained."
    # Missy "Now, I would like to tell you about the things to look out for when cleaning."
    # Missy "We have laboratories for various subjects in this building"
    #
    # show player_a:
    #     zoom 0.5
    #     xalign 0.2 yalign 0.35
    #
    # Mys "How many laboratories do we have? "
    # Missy "Five!"
    # Mys "Got it."
    #
    # hide player_a
    #
    # Missy "These laboratories carry out important experiments in the next semester, "
    # Missy "which can affect the international reputation of our school. "
    # Missy "So your work is very demanding and important."
    #
    # Missy "There are many sorts of signs in the laboratory."
    # Missy "First, you need to be clear about what these standards mean."

#     show red circul at center:
#         zoom 1.5
#         xalign 0.5 yalign 0.15
#     Missy "Circular signs with a red border and diagonal line are prohibition signs."
#     Missy "For this sign, it means you must not do something. ln this example, no smoking."
#     hide red circul
#
#     show red sign at center:
#         zoom 1.5
#         xalign 0.5 yalign 0.15
#     Missy "Red signs are also used for fire-related equipment such as fire fighting equipment."
#     hide red sign
#
#     show blue sign at center:
#         zoom 1.5
#         xalign 0.5 yalign 0.15
#     Missy "Blue signs are mandatory signs. "
#     Missy "This means that you MUST do something, such as wear hearing protection in this case."
#     hide blue sign
#
#     show yellow sign at center:
#         zoom 1.5
#         xalign 0.5 yalign 0.15
#     Missy "Yellow triangular signs are used to warn against hazards, such as electrical dangers as shown here."
#     hide yellow sign
#
#     show green sign at center:
#         zoom 1.5
#         xalign 0.5 yalign 0.15
#     Missy "Green signs indicate safe conditions such as emergency escape routes or where to get first aid."
#     hide green sign
#
#     Missy "Always remember to wear PPE when entering certain laboratories."
#     show player_a:
#         zoom 0.5
#         xalign 0.2 yalign 0.35
#
#     Mys "But what is PPE? "
#     hide player_a
#
#     Missy "Sorry my fault!"
#     Missy "Personal protective equipment, or PPE, is designed to protect you from injury or illnesses caused by exposure to something harmful. "
#     Missy "lt should be supplied and used wherever there are risks that cannot be adequately controlled by other means."
#     Missy "PPE includes familiar items like safety glasses and gloves, "
#     Missy "but also things like face-shields, goggles, hard hats, safety shoes, hi-visibility vests, and earplugs."
#     Missy "lf you have been provided with PPE, ensure you know how to wear it correctly."
#     Missy "PPE has to be selected for the particular hazard. "
#     Missy "For example there are many different types of gloves, "
#     Missy "some protect against heat or cold, or sharp edges,"
#     Missy "while others are designed to protect the user from different types of chemical exposure."
#     Missy "Make sure you use the correct type."
#     Missy "One size does not fit everyone. For your PPE to be effective it must fit you properly."
#
#     show player_a:
#         zoom 0.5
#         xalign 0.2 yalign 0.35
#
#     Mys "What happens if the PPE breaks down? "
#     hide player_a
#
#     Missy "lf your PPE is faulty or damaged, speak to me."
#     Missy "I will send it to you after the training."
#     Missy "PPE assigned for wear in laboratories and workshops should not be used at home."
#
#     show player_a:
#         zoom 0.5
#         xalign 0.2 yalign 0.35
#
#     Mys "But these PPEs can be used in many places in daily life. "
#     Missy "Even so you are still forbidden to use it anywhere other than in the laboratory."
#     Mys "That's a shame."
#     hide player_a
#
#
#     Missy "Even in labs where you don't need to wear personal protective equipment, "
#     Missy "you should dress appropriately and wear the right clothes and shoes. "
#     Missy "For example, tie your long hair at the back of your head and keep it inside your clothes. "
#     Missy "If headwear must be worn, it must be secured and fit snugly. "
#     Missy "Loose clothing can be dangerous when near certain machines, so try to choose tight-fitting clothes. "
#     Missy "Open-toed sandals must be prohibited."
#     Missy "This is because any chemical spills or heavy objects dropped on the toes can cause serious injury!"
#
#
#     Missy "Next, I'll talk about what to look for in a specific lab."
#
# label ElectricalLab:
#     Missy "Firstly, the electrical lab."
#     Missy "When handling any electrical equipment, "
#     Missy "you must ensure that cables do not create a tripping hazard or drag across sinks or heating unit equipment."
#     Missy "Do not overload plug sockets or plug one extension lead into another. "
#     Missy "Do not place items that may leak or spill on top of the equipment."
#     Missy "Do not use the equipment unless you have been shown how to use it properly. "
#     Missy "If the equipment is labelled as faulty, please never touch it. "
#
#     show labdonotuse at center:
#         zoom 1.5
#         xalign 0.5 yalign 0.15
#
#     Missy "Like this sign."
#
#     hide labdonotuse
#
#     Missy "The school will have professional maintenance staff to deal with it."
#
# label ChemistryLab:
#     Missy "Next, chemistry lab."
#     Missy "Avoiding chemicals entering the body in the chemistry lab. "
#     Missy "Chemicals can enter the body in four main ways. "
#     Missy "lngestion, by swallowing and transferring chemicals from hand to mouth when eating or smoking without first washing your hands."
#     Missy "lnhalation, by breathing in gases, fumes, mist or dusts. "
#     Missy "Once breathed insome substances can attack the nose, throat or lungs,"
#     Missy "while others get into the bodythrough the lungs and harm other parts, e.g.the liver."
#     Missy "lnjection, by skin puncture."
#     Missy "Hypodermic needle injuries can involveinfectious agents or very harmful substances and care should be taken when using them."
#     Missy "Direct contact with the skin. "
#     Missy "Some substances damage skin, while others passthrough it and damage other parts of the body."
#     Missy "Some vapours, gases and dusts are irritating to eyes."
#     Missy "Corrosive liquid splashes can permanently damage eyesight."
#     Missy "The safety signs associated with chemical hazards are diamond in shape with a red border."
#     Missy "Here are some of the common ones."
#
#     show chemistrysign at center:
#         zoom 1.5
#         xalign 0.5 yalign 0.15
#
#     Missy "Please remember them."
#
#     hide chemistrysign
#
# label MechanicalLab:
#
#     Missy "In a mechanical laboratory, you should avoid hurting the machine, rr avoid the machine hurting you."
#
#     Missy "If used incorrectly, the machine or equipment may cause you injury by touching or entangling any moving parts;"
#     Missy "crushed between moving parts and fixed structures -for example -wall;"
#     Missy "hit by objects or materials ejected by machines"
#     Missy "Some typical yellow triangular warning signs of mechanical hazards are shown."
#
#     show machsign at center:
#         zoom 1.0
#         xalign 0.5 yalign 0.15
#
#     Missy "To reduce the risk of injury, you must ensure that you are supervised and follow any instructions given. "
#
#     hide machsign
#
#     Missy "Wear any personal protective equipment provided for your use. "
#     Missy "Know the location of the emergency stop button on workshop equipment. You may need it!"
#     Missy "Make sure any loose clothing and anything that might get tangled or caught is securely fastened before you start work."
#     Missy "Never attempt to bypass or remove any guards or interlocks - they are there to protect you."
#
# label BioLab:
#     Missy "Next up is the bio lab. "
#     Missy "When you enter the lab, check for warnings firstly, Biological hazards are identified by this warning sign."
#
#     show biosign at center:
#         zoom 1.5
#         xalign 0.5 yalign 0.15
#
#     Missy "To reduce the risk of becoming infected, here are some do's and don'ts."
#
#     hide biosign
#
#     Missy "Do not do anything to increase the risk of passing hazardous materials from your hands into your mouth. "
#     Missy "This is why eating, drinking, applying cosmetics and storing food in labs are all prohibited."
#     Missy "Never pipette by mouth."
#     Missy "Do minimize aerosols and splashes, and deal with spills immediately."
#     Missy "Do disinfect working surfaces after use."
#     Missy "Do wash your hands before leavingthe work area."
#     Missy "Wear your lab coat only in the lab."
#     Missy "Keep your work area clean and tidy."
#     Missy "Keep writing and experimental areas separate."
#
# label NuclearLab:
#     Missy "Finally, there is the nuclear laboratory. "
#     Missy "Different types of ionising and non-ionising radiation produce different types of damage."
#     Missy "Some not detected by our senses, so you may not know they are present or if you are being effected."
#     Missy "When working with any type of radiation source you must follow all instructions,"
#     Missy "wear PPE as required,"
#     Missy "do not eat, drink, or chew gum in any area designated for work with radioactive materials"
#     Missy "Here are some warning signs."
#
#     show nuclearsign at center:
#         zoom 1.0
#         xalign 0.5 yalign 0.15
#
#     Missy "Don't forget them."
#
#     hide nuclearsign
#
# label waste:
#     Missy "Please dispose of the waste generated in the laboratory correctly."
#     Missy "Different laboratories or workshops have different waste disposal systems. "
#     Missy "Please ensure that waste is disposed of in the correct waste disposal system. "
#     Missy "A special reminder is to never put sharp objects such as glass or needles into plastic bags. "
#     Missy "This is because they may puncture the plastic bags."
#
# label collectPPE:
#     Missy "That's what I'm trying to say. "
#     Missy "I know there are a lot of points to be aware of, "
#     Missy "but that's why you are paid very well. "
#     Missy "If something goes wrong on the job, all the damage will be paid for by you. "
#     Missy "And you will lose your well-paid job. "
#     Missy "Please be careful when working!"
#
#     show player_a:
#         zoom 0.5
#         xalign 0.2 yalign 0.35
#     Mys "It sounds like such a hassle, "
#     Mys "but I'm willing to spend the time and experience to clean it for my living expenses."
#
#     Missy "Now, Please come to me to collect your PPE."
#
#     Mys "Wow, this PPE looks so advanced."
#     Mys "I'll keep it well"

label Evening:

    $lentKevin=False

    scene bg kitchen2
    with dissolve

    "Evening."

    show player_a at speaking:
        zoom 0.5
        xalign 0.0 yalign 0.35
        linear 0.5 xalign 0.2

    show kevin:
        zoom 0.5
        xalign 1.0 yalign 0.35
        linear 0.5 xalign 0.7

    Kevin "So you're back, how was the training today?"
    Mys "There are so many situations to be aware of when working."
    Mys "It's not an easy job."
    Kevin "What do you have in your hand? "
    Kevin "It looks very advanced."
    Mys "This is the PPE we may have to wear at work."
    Mys "It can protect us from injury."
    Kevin "Wow, I'm baking a pizza and the baking tray is too hot."
    Kevin "Can I borrow the glove inside your PPE?"
    Kevin "I'll try it out and see if it works."

    hide player_a
    hide kevin

    menu:
        "Lend it to Kevin":

            show player_a at speaking:
                zoom 0.5
                xalign 0.0 yalign 0.35
                linear 0.5 xalign 0.2

            show kevin:
                zoom 0.5
                xalign 1.0 yalign 0.35
                linear 0.5 xalign 0.7

            Mys "I can lend it to you, I would also like to know if the PPE's will work."
            Kevin "Thank you so much."
            "Kevin accidentally touched the knife while using it, resulting in a very small crack in the glove"
            Kevin "It's over, but there's a crack in the glove. "
            Kevin "But the crack is so small, it shouldn't matter. "
            Kevin "It's better not to tell Mys. Or he'll argue with me. That's terrible."
            Kevin "I'm done with it. Give it back to you."
            Mys "How does it feel?"
            Kevin "It's really good quality, thanks a lot."

            $lentKevin=True

        "Don't want to lend to Kevin":

            show player_a at speaking:
                zoom 0.5
                xalign 0.0 yalign 0.35
                linear 0.5 xalign 0.2

            show kevin:
                zoom 0.5
                xalign 1.0 yalign 0.35
                linear 0.5 xalign 0.7

            Mys "I'm very sorry, Missy said they are forbidden in the house because of the risk of damage when using them at home."
            Kevin" Well, it's okay, I'll think of another way."
label Day2:

    $wearclothe=False
    $wearsandals=False

    scene bg bedroom2
    with dissolve

    "Day2"

    show player_a at speaking:
        zoom 0.5
        xalign 0.0 yalign 0.35
        linear 0.5 xalign 0.2

    Mys "The first day of work, I need to prepare well. "
    "I can't lose my job on the first day."
    Mys "I should pick out the right clothes to wear for work."
    Mys "Let's start by looking at the temperature today..."
    Mys "what? I can't believe it."
    Mys "It's 36 degrees Celsius. It's so hot!"
    Mys "I want to wear something cooler."
    menu:
        "wear loose clothing":

            $wearclothe=True

            Mys "wearing loose clothing makes me cool, which is a wise choice."
        "Wear close-fitting clothing":
            Mys "I should wear close-fitting clothing in the laboratory."

    menu:
        "Wearing trainers":
            Mys "Wearing trainers makes it easier for me to do my job."
        "Wearing sandals with a missed toe":

            $wearsandals=True

            Mys "Wearing sandals can make me very comfortable and cool."

    Mys "Going to work next."

label work:

    scene bg electrical
    with fade

    show player_a at speaking:
        zoom 0.5
        xalign 0.0 yalign 0.35
        linear 0.5 xalign 0.2
    Mys "Let's start by cleaning up the electrical lab."
    Mys "Oh my god!! It's such a mess, all sorts of wires are tangled together."
    Mys "The plugs are not used properly."
    Mys "Some are full and some are not plugged in at all."
    Mys "The floor was also covered in stains. "
    Mys "Started cleaning!!"
    Mys "First I should tidy up the wires."
    # menu:
    #     "Place the wire against the wall":
    #              #Result "damage to the apparatus due to overloading of the wire
    #     "Untie the wires and keep the board from overloading":
    #              #causing damage to the appliance
    #     "Check that the wires will not drag the appliance before tidying":
    #              #stumble
    #     "Select all of the above":

    Mys "Finally finished, now it's time to sweep the floor."

    scene bg chemistry
    with dissolve

    show player_a at speaking:
        zoom 0.5
        xalign 0.0 yalign 0.35
        linear 0.5 xalign 0.2

    Mys "Next is the chemistry lab."
    Mys "My role is not only to clean the floor, but also to clean up the lab equipment."
    Mys "There are chemical waste products that could harm me."
    Mys"First I need to recall how chemicals get into the body."
    menu:
        "Through the mouth and skin ":
            Mys "Chemicals enter through mouth and skin."
            Mys "I should have a mask, clothes, and gloves ready."
        "Through the skin and nose":
            Mys "Chemicals enter through skin and nose."
            Mys "I should have a mask, clothes ready."
        "Through the mouth, skin,nose, eyes and by injection":
            Mys "Chemicals enter through the mouth, skin,nose, eyes and by injection."
            Mys "I should be prepared with a mask, clothes, gloves, glasses."
        "Through the nose, skin and eyes":
            Mys "Chemicals enter through the nose, skin and eyes."
            Mys "I should have a mask, glasses and gloves ready."

    if lentKevin:
        "While cleaning the cup containing sulphuric acid, you suddenly feel a sharp pain."
        Mys "It hurts so much. What happpened?"
        Mys "How did the sulfuric acid get to my skin?"
        Mys "Why does my glove have a small crack?."
        Mys "It must have been broken when it was loaned to kevin!"
        Mys "Missy is right, I shouldn't use PPE at home."
        "Let's choose again"
        jump Evening


    Mys "cleaned up, now it's time to get into the mechanical lab."

    scene bg mechanical
    with dissolve

    show player_a at speaking:
        zoom 0.5
        xalign 0.0 yalign 0.35
        linear 0.5 xalign 0.2

    Mys "I'm so tired, but I still have to clean the mechanical lab."
    "When cleaning, you find that some of the machinery's guards are also dirty."
    menu:
        "remove the guards and clean them":
             Mys "It shouldn't be a problem to take them off, clean them and put them back on."
             Mys "My Obsessive-compulsive disorder won't allow that dust to exist!"


        "Ignore them":
             Mys "Missy said we shouldn't touch those devices."
             Mys "I'll leave them alone."

    if wearclothe:
        "You are cleaning up and suddenly find that your clothes are stuck inside the machine."
        Mys "Oh my god, how did it get stuck inside the machine."
        Mys "I wear clothes that are too baggy!"
        Mys "Missy said not to wear anything too baggy."
        Mys "It's over, the clothes and the machine are broken"
        "At this point issy passed by and"
        Missy "Mys!"
        Missy "You broke the machine. You're fired!"
        "Please choose again, this time with care."
        jump Day2


    Mys "Clean up is done, now it's time to move on to the biology lab."

    scene bg bio
    with dissolve

    show player_a at speaking:
        zoom 0.5
        xalign 0.0 yalign 0.35
        linear 0.5 xalign 0.2

    Mys "I seem to need to sort out my clothes after entering or exiting. "
    menu:
        "Disinfect clothing on entry and exit":
            Mys "I should disinfect the clothes, biology labs are very sensitive to bacteria."

        "Enter directly after putting on PPE":
            Mys "The PPE is of very good quality and clean, and it is fine without sterilisation."

    if wearsandals:

        "When cleaning biological lab equipment,"
        "bacteria-laden liquids fly up to your toes due to the sandals you're wearing."
        "After cleaning up, you forget to clean your toes."
        "When you go back home, you unfortunately get a fungal infection. "
        "You can't work for the whole holiday. "
        "Please choose again, this time with care."

        jump Day2



    Mys "Clean up is done, now it's time to get into the nuclear lab."

    scene bg nuclear
    with dissolve

    show player_a at speaking:
        zoom 0.5
        xalign 0.0 yalign 0.35
        linear 0.5 xalign 0.2

    "While cleaning you suddenly get hungry"
    Mys "I'm so hungry, it's been a busy morning. "
    Mys "I need to get some energy."
    Mys "I brought a sandwich in the morning."
    Mys "It's time to eat it."
    menu:
        "Can't see anything dirty, eat sandwich for energy":
            Mys "Eat the sandwich before you work, it will give me more energy."
        "It's better to eat after cleaning":
            Mys "Missy said there was radiation in the nuclear lab. "
            Mys "I can't see this radiation."
            Mys "It's still dangerous to take off the PPE. "
            Mys "Let's eat after cleaning up."

    Mys "finally finished the job!I can rest now."
    Mys "I have to go and report to Missy about my work."
    Mys "Hi, Missy I am here to give you a report about my work."
    Missy "No need to report, there are security cameras in every lab. I can see everything."
    # Wrong choice.
    # Electrical
    # "Place the wire against the wall"     #You didn't notice that the wire is overloaded, so the wire is overloaded causing damage to the instrument
    # "Untie the wires and keep the board from overloading"     #You moved the appliance while unplugging the cord.That caused damage to the appliance.
    # "Check that the wires will not drag the appliance before tidying"     #You didn't put the wire in the corner so that the wire tripped up people.
    #
    #
    # Chemistry "I saw that you did not wear the PPE correctly, even if there was no safety incident this time it was still very dangerous."
    # Choose the wrong two
    #
    # Machinery "You touched the guards of the machinery. "
    # "After you finished cleaning, the staff found that the guards were broken,"
    # "so you should pay for the damage."
    #
    # Biology "You did not sterilize before entering the biological laboratory. "
    # "That caused the death of experimental bacteria we cultivated."
    # " This was a failure in your work."
    #
    # Nuclear "You ate in a nuclear laboratory.""That behaviour is very dangerous. "
    # "It could expose you to radiation. "
    # "You should not behave in that way."
    #
    # Correct "You finished your job without any mistakes and performed very well. Well done!"
    # Mys "Thanks!  I will definitely work hard!"
    # Choose the wrong one "You made some mistakes at work, but people always make mistakes sometimes."
    # " You didn't make many mistakes. Try better next time."
    # Choose two wrong ones "You are unable to do this job because you have made too many mistakes. "
    # "I am very sorry, but you are fired."
    # "Let's start the selection again, this time with care."