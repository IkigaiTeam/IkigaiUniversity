default menuset = set()
label test:
    scene black
    with dissolve
    scene bg void
    with fade
    "You wake up in a dark room."
    "It’s cold."
    "Really cold."
    "Your fur’s standing on end."

    Andee "...Ugh-"
    Andee "Where... am i?"
    "You stumble to your feet."
    Andee "H-Hello?"
    Andee "ugh, my head..."
    whotf2 "Welcome."

    play music "audio/Music/a shock wave.mp3" volume 0.5

    Andee "G-Gah-!"
    "The voice startles you. Something feels very wrong about it, like a whisper in your neck that echoed from miles away."
    Andee "W-Who's there?! Is this some kind of prank?!"
    whotf2 "Calm yourself, young one."
    whotf2 "We are only going to run a assessment to gauge how you may respond in... certain scenarios."
    Andee "...We?"
    "A blinding light snaps on above you. Three shadowed figures stand behind a pane of glass, their faces obscured."
    "You've just noticed now that you're only wearing underwear-..."
    Andee "W-what the-... WHERE ARE MY CLOTHES?!"
    whotf2 "State your first and last name please."
    Andee "My... name?"
    "You begin to speak with hesitation."
    Andee "A-Anden..Anden Indou.."
    "One of the figures scribbles something in what looks to be a notepad, but it's hard to tell in the darkness."
    whotf2 "State your age please."
    Andee "I'm 19...?"
    "They scribble something loudly again."
    whotf2 "What is the last memory you recall before arriving here?"
    Andee "Arriving where??"
    "..."
    Andee "Look, mysterious voices or whatever, are you gonna keep being cryptic or are you gonna tell me what's going on here already?"
    "Suddenly, your head pounds."
    Andee "A-ARGH-..."
    "The figure waits silently"

    Andee "T-The last thing i remember was... Being on the flight to Hibana..."
    "Hibana...."
    Andee "...Dang it, i'm gonna miss my first day."

    "The figure jots down something again"

    whotf2 "We will now begin a series of personal questions. Please answer them to the best of your ability."

    Andee "Personal questions? Like what?"

    "You wouldnt call yourself a particularly secretive person, but you still feel a bit uncomfortable sharing anything personal with whoever these guys were."

    whotf2 "Do you trust easily?"
    Andee "I-..."
    "You stay silent for a moment, thinking about how you should answer."
    Andee "Maybe... sometimes-...?"

    "..."
    whotf2 "Would you consider yourself a forgiving person?"
    "..."
    "Its not exactly a question you were expecting, nor want to answer, but you get the feeling these guys know alot more about you than theyre letting on, so you decide to just answer as honestly as you can."
    Andee "...Yeah."

    "One of them scribbles something again"
    "The air feels like its getting colder and colder as time goes on and the silence grows heavier and heavier."
    whotf2 "Would you consider yourself.. loyal?"
    "..."
    "Something about these questions feel far too.. specific, its unnerving to say the least, but the thought of upsetting these guys by not answering or being purposefuly vague is even more terrifying."
    Andee "I guess so?" # would be nice to make a tiny pause at the "id" (yeah lets do that)
    "The room goes completely silent."
    "You hear them muttering to each other silently... you cant make out what they're saying, but it sounds like they're debating something."
    "After what feels like an eternity, the head figure finally speaks again."

    whotf2 "In the event of disaster, who would you be more likely to save... yourself, a loved one, or a stranger?"
    Andee "W-What?! what kind of question is that??"
    whotf2 "Just answer the question, Mr. Indou."
    Andee "..."

    menu:
        "Myself":
            Andee "I'd... save myself."
            "I mean, I wouldn't wanna die, right? I think most people would say that..."
            "The head figure nods and jots something down again."

        "A loved one":
            Andee "I'd save a loved one, without a doubt."
            "One of the figures next to the head figure seems to nod in approval as they jot something down."

        "A stranger":
            Andee "I'd help anyone I could... whether it's a stranger or a loved one."
            "One of the figures groans in annoyance. It's hard to tell which one, but they jot something down anyway."
    
    # aligned with menu (not indented)
    whotf2 "Interesting..."
    whotf2 "Very interesting..."
    "..."
    whotf2 "Thank you for your cooperation, Mr. Indou we will be in touch"
    "The lights suddenly snap off, leaving you in complete darkness again."
    Andee "W-who are you guys? .. Look, this is really freaking me out. i-i just wanna go home-..."
    scene bg white
    stop music fadeout 1.0
    # beeping sounds pls + music stops (I do plan to make beeping files lol I jus dont know how, ima figure it out tho😭)
    # should prob makes another file for the rest

# its pure copypasting from here lollll
    whotf2 "An…"
    Andee  "nghhh.."
    whotf2 "Ande…."
    Andee  "Wha?.."
    whotf2 "Andee !"
    Andee  "IM UP!!"

    scene bg Bedroom
    with fade

    "You quickly jolt awake, taking in your surroundings…"
    Andee "(Right.. It's my first day. Though when did I get to my dorm?... That's where I am, right?)"
    Reo "Dude, get the hell up!!"
    play music "audio/Music/A moment between two.mp3" volume 0.5
    # Enter character Reo/ Andee 
    Andee  "Ughh, what time is it.."
    "Your head is pounding from the sudden awakening, and that weird dream you had is still fresh in your mind to make things worse"
    Reo "It's late, that's what it is, of course you'd sleep in on your first day. unbelivable.."
    Reo "C'mon you gotta see the headmaster since your dumbass decided to miss orientation."
    Andee  "Ugh, you sound like my mom."
    Andee  "And I was excused!"
    Andee  "I thought I set my alarm to wake me up at 7am, I didnt hear it go off."
    Reo "Excuses, excuses"
    Reo "And your alarm DID go off, it seems like it woke up everyone else on campus besides you"
    Andee  "So why didnt YOU just wake me up?"
    Reo "Well I uh..."
    "the snow leopard begins to blush"
    Reo "Well y-yknow how grumpy you get in the mornings.. and uhh..."
    Andee "Yes?..."
    Reo "and well... you looked really peaceful in your sleep, so i didnt want to wake you."
    "your heart melts a little at the big cats confession."
    Andee "Dawww, youre a sweetheart y'know that Reo."
    Reo "S-shut up.."
    Reo "Now hurry up and get ready, we already wasted enough time.."
    
    Andee "Shit your right"
    Reo "I'll be in the living room, don't keep me waiting."
    Andee "Yes Sir!"

    "The Snow Leopard exits the room, leaving you alone in your bedroom"

    # Exit Character Reo

    Andee "(I feel weird.)"
    Andee "(Maybe it's just first-day jitters or something?..)"
    "Though something about that dream is still rubbing you the wrong way..."
    Andee "(I shouldn't dwell on it. Let's get ready for the day!)"
    "You quickly head to the bathroom to start your day."
    stop music fadeout 1.0

    scene bg Bathroom
    with dissolve

    play music "audio/Music/Wild Flower.mp3" volume 0.5

    # haha this is gonna take so much time to add the characters and transitions
    # determination though i love my job
    # malevolent you should pay me more than 0$ for that/j

    Andee "(I can't let one weird dream screw up my day, especially one like this.. I'm already late.)"
    Andee "(God, i hate rushing.)"
    "You wouldnt have to be rushing if you had just been a responsible adult and woke up on time, but you decide to ignore that thought for now."
    Andee  "(Whatever, let's just start with brushing these canines)" # Is the joke about the teeths really necessary lol
    "After all, you don't want to have dog breath. Especially if there's gonna be cute guys here."
    Andee "SHUT UP BRAIN!"
    "You just realized how ridiculous it was of you to shout that out loud and its made worse by the fact that Reo heard you."
    Reo "Bro, you good in there?"
    "The Large Cat questions from outside the door." 
    Andee  "Yeah All good haha, just nervous is all..."
    Reo "Ugh you're such a dork y'know that? quit talking to yourself and focus on getting ready, we dont have all day!"
    Andee "I know, i know, just give me a sec.."
    Andee "(He's right, I should just focus on getting ready instead of overthinking everything"

    scene bg Bathroom steamy
    with dissolve

    "After brushing your teeth, and showering you head to the kitchen to make yourself some quick breakfast"

    scene bg Bathroom
    with dissolve
    Andee "(I should probably eat something before I go see the headmaster, food helps with stress right?)"
    Andee "(Hopefully Reo has some decent food here...)"

    scene bg Kitchen
    with fade

    "As you step into the kitchen, you hear Reo’s voice call out to you."

    Reo "Dude we have no time for breakfast, the headmaster wants to see you as soon as possible"
    Andee "Look im just gonna grab something quick to eat alright?, unlike you i actualy like eating."
    Reo "Yeah clearly, just hurry up please, or else your gonna be on your own, ill be damned if im late to class because of you."
    Andee  "Oh relax, you make it seem like food isnt important fo-."

    stop music

    "You suddenly stop as you open the fridge door. the only food here is a jug of milk, a half empty package of string cheese and left over takeout"

    play music "audio/Music/Pom Pom _ ぽむぽむ .mp3" volume 0.5

    "A deep primal growl escapes your stomach as you stare at the contents of the fridge."

    "You were hoping for something a bit more... substancial, you cant even make due with any of this."

    Andee  "Reo, wheres the food."
    "The snow leopard apporaches you with a guilty look as his face as he looks inside the damn near empty fridge"

    Reo "Ah right... i was supposed to go grocery shopping before your arrival, sorry about that..."
    Andee  "Dude c'mon what have you even been eating??"
    Reo "Uhh... well... mostly just takeout and if im low on cash i just eat ramen or something.. oh the cafeteria food is actually pretty good here too!"
    "You're getting some bad memories of the cafeteria food from high school, and you cant help but feel a little bit of dread at the thought of having to eat that again."
    Andee  "Reo i am not eating cafeteria food, looks like ill be starving for the day..."
    Reo "Don't be so dramatic, the cafeteria food isnt anything like the one from high school trust me, ill take you there after our tour alright? my treat."
    "You have no real reason to argue with him further, and you've never been a particularly picky eater so you decide to take his word for it."
    "Your stomach growls loudly at the thought of waiting to eat, but you dont really have a choice right now."
    Andee  "Well ill trust you on that, in that case i guess im ready to head out then."
    "You dont sound very ready at all, but you decide its due time to just get going."

    scene bg Livingroom
  

    Reo "Hey relax dude, as long as you stick with me, youll be fine, i promise."
    "The thought of that makes you feel a bit better."
    Andee "thanks Reo, i really appreciate that."
    Reo "Yeah yeah, dont get too sappy on me now, lets get going!"

    "With that, the two of you grab your things and head out to begin your day."

    # lets try to add a cute episode title card here or something

    stop music fadeout 1.5

    pause 3.0

    scene bg Campus Outside
    with fade

    play music "audio/Music/Enjoy life to the full.mp3" volume 0.5

    # [camera pans over the different locations on the university  Dorm Hallway.png -> Campus Lobby.png -> Campus Ouside.png]
    Reo "Well my friend.. Welcome to Ikigai University"
   
    "You cant help but snark at his enthusiasm for the place"
    Reo "Take in that fresh campus air."

    "The two of you arrive outside the dorms and see the main campus building in the distance, and you cant help but feel a little in awe at the sight of it all."

    Andee "Man hibana is so much prettier than i imagined it would be, feels like im on vacation or something."
    "the crisp smell of the ocean and palm trees graces your nostrils as you take it all in, you cant help but feel a little excited about the journey ahead."

    Andee "I cant belive were really gonna be staying here for the next few years, is this what rich people feel like??"

    Reo "Pfft as if Id know, and yeah this place is pretty nice, it does get kind of old after a while though, but i mean that is college for ya."

    scene bg Hallway
    with fade

    Andee  "(As we walk to the side of campus where the headmaster and all the classes are located, I can't help but feel nervous. me and him have been waiting for this moment for years, and now here we are, living it.)"
    Andee "(its pretty surreal to be honest, though i cant help but feel a little anxious about the day ahead. I know Reo is gonna be there to help me through it, but still, its a lot to take in.)"

    "The snow leopards ears perk up and he seemks to pick up on the internal conflict your having right now."
    Reo "How ya feelin’ so far, nervous? Excited? Both?!"
    Andee  "Haha.. Yeah, I guess I am a little nervous."
    Andee "But im also really excited too yknow."
    Andee "Obviously we've been planning this for a whle, but outside of that ive always kind of been waiting for the day i could finally be on my own and start actually living my life."
    Reo "Yeah i feel you there, the first year here was pretty surreal for me too, i just remember wishing you were here to experience it with me."
    Andee "Awww Reo..." 
    Reo "Bleh, i feel cringy saying that out loud, but its true."
    Andee "Heh you really do have a heart somewhere in there"
    Reo "Ugh, how dare you."
    "The big cat says with with a smirk, but you can tell the complement touched him a little bit."

    "As you both walk, a group of what you can only assume are fraternity dudes walk past you, and you cant help but check them out a little bit."
    "But it seems like Reo notices this and bumps you with his hip a little bit, making you stumble."

    Reo "Y'know, theres another reason why i think you'll like it here."
    "Hes doing that stupid eyebrow thing, so you already know hes about to say something stupid."

    Andee "Oh yeah? and whats that?"

    "The snow leopard lets out a deep chuckle"

    Reo "Well, you know how you always had a thing for big strong dudes, right?"


    "Suddenly your face goes red."

    Andee "And what's THAT supposed to mean??"

    Reo "Oh relax, I meant it in a completely platonic way."
    Andee "Yeah right."
    "The large feline chuckles"
    Reo "Hey, im not the one with dude on the brain 24/7."
    Andee  "*Gasp* I do not have DUDE on the brain, alright."
    Reo "Yeah? So what about all the times I caught you gawking at the entire football team back in high school, or the soccer team, or the basketball team, or the baseball team, or the-"
    Andee "Okay, okay, I get it, i was a little obsessed with the sports teams, but that was back in high school, and besides, i was just admiring their athleticism, okay.. not their looks."
    Reo "Ok sure, but you gotta admit you werent exactly subtle about it."
    Andee  "W-whatever, Jerk head."
    Reo "Owch, my feewings, Andee called me a Jwerk hwead."
    "He says in a mocking voice"
    Reo "What happened to the sweet wittle pup i weft last year?"
    Andee "Stop talkingggg!"

    Andee "(Ugh, he hasn't changed a bit in the year we've been apart.)"

    Andee "I'm glad we're together again.."

    Reo "Heh, you thinkin’ about me or somethin'?"
    "Your face goes red instantly."

    Andee  "I WAS NOT!!"

    "You totally were."

    Andee  "Ughhh... you’re an ass, y'know that?"

    Reo "Ive been called worse pup, believe me"
    "We continue to joke and make small talk for the rest of our walk."
    "Eventually, the both of you approached an ominous door at the end of the hallway."

    stop music fadeout 2.0

    # scene Office Door.png]
    scene bg Office Door
    with fade
    # [music stops]

    Andee "This must be the headmaster's office."

    play music "audio/Music/loneliness.mp3" volume 0.5


    Andee  "Uhh.. Is it suddenly cold in here, or is it just me?"
    Reo "Hey, loosen up a little, she's not gonna bite your head off or anything. Just try not to show any signs of fear when we step inside alright?"
    Andee "(Thats an ominous warning...)"

    "With that, he does a gentle knock on the door.. And once he gets a response we make our way inside.."
    scene bg haddiesoffice
    with fade


    "The office is relatively small yet tidy, with an office desk in the middle and picture frames and fake plants everywhere. A strong scent of peppermint from the nearby diffuser and incense blasts your nostrils"
    "Behind the desk in front of you, a very well put together Vixen is typing away at her keyboard.. She barely seems to notice the two of you.."

    Reo "U-uhm Morning, Dr. Ha-"
    Haddie "You're late."
    "Without even looking up she responds in a cold sharp tone.. "
    Reo "Apologies, Dr. Haddie, i overslept and forgot to tell him."

    Andee "(Hes lying for me?!)"

    Haddie "This behavior is unexpected from you, Reo. I won't tolerate it again."
    Andee "(I get the feeling that if i werent here it would be a very different outcome for him.)"

    "You notice the snow leopard shifting nervously.."

    stop music fadeout 1.5

    Haddie "As for you, young man.."
    "Her demeanor changes… she smiles"

    play music "audio/Music/Dream Butterfly _ 夢想蝶 (Dr. Haddies Theme).mp3" volume 0.5 fadein 2.0

    Haddie "i deeply apologize for making such a poor first impression, welcome to Ikigai University."
    Haddie "Reo here is gonna show you all of what our university has to offer since unfortunately you missed our orientation"

    Andee "uhh, thanks?"
    "Reo gives an awkward smile and a thumbs up"
    Haddie "No, thank you for choosing our amazing university, since the two of you are already running late.. I'll keep our little introduction short and just go over some of the more significant rules here on Campus."

    Andee "(Ah right.. rules)"
    Andee "(im good at following those... i think.)"

    Haddie "First, punctuality is paramount. Classes, meetings, events… this school does not wait for stragglers." 

    "She gives a sharp glance at Reo and you can basically feel all of his earlier confidence melt away."

    Haddie "Second, respect. To your professors, to your peers, to the traditions of Hibana."


    Haddie "As you may already know, this island is sacred. Those who reside here do not tolerate disrespect, toward themselves, or toward their land."
    Haddie "Any Violations to the laws of Hibana Island will result in Instant Removal from our university and the island itself."
    "You can only nod quietly.."
    Haddie "Consequences for disrespect are… contextual. You’ll know when you’ve crossed the line."
    Andee "U-understood ma’am.."
    Haddie "Third, boundaries. Certain areas of this campus, and this island, are strictly off-limits. I expect you to remember that… for your own safety."
    Haddie "If you have any questions about restricted areas just ask either me or one of our wonderful staff members. But for the most part it should be fairly obvious, as we have signs set around all restricted areas."
    Andee "that shouldnt be too hard to follo-"
    
    stop music

    play music "audio/Music/Confine.mp3" volume 0.5
   
    Haddie "However"
    Andee " …"
    Haddie "There is one area… deep within the forest that surrounds our campus that you are absolutely NOT prohibited to trespass.."
    Andee  "I-"
    Haddie "Island natives call it Yomi no Kuni. Once you step foot there… There is no saying what can happen. Our security lines do not reach that far. You will no longer be under our responsibility. We have lost many students from failure to follow that one rule. So be warned."
    Andee "(I think the color just completely drained from my face...)"

    stop music fadeout 2.0
    
    Haddie "*Ahem*"
    

    play music "audio/Music/Dream Butterfly _ 夢想蝶 (Dr. Haddies Theme).mp3" volume 0.5

    "..."
    Haddie "lastly… conduct. We maintain an environment of excellence here. One stain on this university’s reputation, and you will find yourself on the next ferry home."
    "She straightens a stack of papers, her voice softening for just a moment as her eyes flick back to you."
    Haddie "Abide by these, and your time at Ikigai will be… enlightening."
    Andee "U-Understood"
    Andee "(Those shouldn't be too hard to follow… so why am i shaking?)"
    Andee "(Why do I feel like I'm doing something wrong just being here…)"
    Andee "(Why do I feel like there's more to this than she's letting on…)"
    Reo "Alrighty then Dr. Haddie, we’ll get outta your fur for now, r-right Andee ?"
    Andee  "uh y-yeah, later Miss"
    stop music

    "Her eye visibly twitches at that.."
    Haddie "ah I worked very hard for my title, dear.. It's DR. Haddie"
    Andee  "M-my apologies.. D-Dr. Haddie.."
    Reo "C'mon dumbass.. Your already pushing her buttons"
    "Reo mutters as he pulls you out the door"
    "But even as the door shut behind you, you couldn’t shake the feeling of her gaze still on your back."
    #[scene hallway.png]

    scene bg Hallway
    with fade
    Andee "(That was... Something.)"
    "You finally see Reo relax a bit"
    Reo "Phew… I promise she isn't always like that.."
    Andee "I sure the hell hope not."
    Reo "Just most of the time..."
    Andee "Goddammit-"
    Andee "She was kinda. intense.."
    Reo "I mean yeah, but that just means she cares."
    "You relax a little at that."
    Reo "I mean, that's what I think at least."
    Andee "(Motherfu-)"
    Reo "Relax dumbass. She's the headmaster. She's gotta be a little strict, it's her job. You'll be fine."
    Andee  "Yeah.. You're right.."
    "You relax a little after his reassurance. The day had barely begun and here you are already stressed." 
    Andee "(Besides that I'm still excited to see what's next!)"

    play music "audio/Music/One day.mp3" volume 0.5

    Andee  "Well, where are we going first?!"
    "Excitement begins to consume you and your tail begins to wag."
    "You’re acting just like an excited puppy right now."
    Reo "Aww easy there little dude, you've got class next."
    Andee "(Ah.. right.. This is still school after all.)"
    Andee "Dammit.. Wait, what class do I even have today?"
    "You begin to internally panic and Reo seems to notice immediately." 
    Reo "Just check your phone, i sent you the app to check your schedule, like, weeks ago."
    Andee "ahh right"
    "You open your phone and check the My Ikigai App"
    Andee "Introductory Psychology.."
    Reo "Guess we aren't in the same class today then."
    Andee "What do you have?"
    Reo "Software Engineering!"
    Andee "heh nerd"
    Reo "S-Shut up..."
    Andee "(he always gets so into his tech stuff, its fun to tease him about it every now and then.)"
    Reo "A-anyways, go get to your brain studies class or something, we can start our tour when you're finished."
    Andee  "Sounds good!, see ya later"
    Reo "Laters! Text me if you need anything alright."
    Andee  "Will do, mom" 
    Reo "Oh Bite me.."
    "He mutters as he walks off to his class leaving you alone for the first time…"

    stop music fadeout 1.0

    Andee "Dammit… I have no idea where my class even is.."
    #[ambience crowded hallway.mp3]
    "The chatter of students and the sound of movement around the halls suddenly fills your ears..."
    Andee "(This is a bit overwhelming.)"
    "You start aimlessly walking around hoping to find maybe a staff member or someone you can ask to show you around when-"
    # *SFX Thud*
    Andee  "Ouch!!"
    "You're suddenly knocked over by a much larger beast"

    whotf2 "shoot i-im sorry i wasnt- uhh h-here"

    "He offers his large paw to help you up."

    menu:
        "Accept his help":
            "You grab his paw as he practically lifts you into the air for a moment."

        "I'm a strong independent man.":
            "You decide you don't need his help getting up.. This was already embarrassing enough as is."
            "He seems to notice this and physically shrinks a bit.."

    # This line must be aligned with the 'menu' statement to play AFTER the choice
    "Suddenly you’re face to face with a large black and white canine.. A husky right?.. Or maybe a malamute?.. Yeah judging by his size he's definitely a Malamute.."
    whotf2 "Ah, sorry about that. I really need to be more mindful of my surroundings."
Andee "You're all good, no worries."

"You dust yourself off a bit. Man, that was embarrassing..."
"It feels like everyone's eyes are on you."
"And it seems like big guy over here is taking it just as bad as you are."

Andee "It's fine, really!"
"You give him a gentle smile, letting him know you're not mad at him or anything."

Andee "And if anything, it's my fault. I wasn't exactly paying attention either."
whotf2 "Heh, I suppose that makes both of us, then."

whotf2 "Say, I don't think I've seen you around campus before. Are you new here?"

Andee "(Is it really that obvious?)"
"Yes."
"Yes, it is."

Andee "Yeah, this is actually my first day."
whotf2 "Hehe. Well, don't let my reckless introduction ruin this otherwise momentous occasion. Welcome to Ikigai, my friend."

Andee "(Why does he talk like that...? It's so formal...)"
Andee "(It's actually kinda cute...)"
Andee "(Ugh, no. We're not here for that.)"

whotf2 "You good there?"
Andee "(Crap!)"

Andee "Ah, yeah. Just spaced out for a sec, hehe. Don't worry about me."

whotf2 "Say, what class are you heading to next?"
Andee "Something about psychology, I think? But, uh... I kinda don't know where the room is, hehe..."

whotf2 "Introductory Psychology, correct? I was actually heading there myself. I have to drop something off to the professor."
whotf2 "Would you like to come with me?"

Andee "(Aww... I was hoping he'd be in my class...)"
Andee "(Oh well. At least I've got someone to show me the way.)"
Andee "(And walking with him even for a little bit does sound really nice.)"

play music "audio/Music/Morning Light_朝の光(Theme of Hiroshi).mp3" volume 0.5

Andee "Yes. That's perfect, actually. Thanks, er..."

Hiroshi "Ah, excuse my manners. My name is Hiroshi."
Hiroshi "But, uh, you can call me Hiro for short. May I ask yours?"

Andee "Ah, my bad. My name's Andee. It's nice to meet you, Hiro."
Hiro "Likewise. I see us becoming great friends in the future!"
Hiro "Now let's get going. I wouldn't want to make you late to your class."

Andee "(A little too late for that, I think...)"
Andee "(Ugh... Reo, why didn't you wake me up sooner?)"
Andee "(To be completely fair, it wasn't his fault. You're the one who decided to sleep in...)"
Andee "(Well... less decided. More like it just kinda happened.)"

Hiro "Um... Andee?"
Andee "Spaced out again, sorry!"

"You smile and wave him off dismissively as you jog to catch up with him."

Hiro "Are you getting enough sleep? I hear that's usually the cause of lack of focus during the day."
Andee "Uh... no. Probably not, hehe."

Andee "(Not to mention that weird dream I had...)"
Andee "(Actually... what was that about again?)"
Andee "(I can't seem to remember now that I think about it...)"
Andee "(Best not to dwell on it and space out again.)"

Hiro "Heh, don't worry. It happens to the best of us."
Hiro "Y'know, my roommate has a similar issue..."

"We continue to walk and talk until we arrive at the classroom."

stop music fadeout 2.0

Hiro "Well, it seems this is where we part ways."

Andee "(If only it could last longer...)"
Andee "(I could listen to him talk about the most mundane things for hours...)"

Andee "Unfortunately, yeah..."

Hiro "But hey, don't worry."
Hiro "After your class is done, I should be in the library. I'm helping my roommate study."
Hiro "So if you wanna join us, feel free."

Andee "That sounds great, actually!"
Andee "(Hopefully Reo won't mind if we take a stop at the library during our tour.)"

Hiro "Well then, Andee... it was a pleasure. But I shall leave you to your class now."
Andee "Alrighty. Thanks for showing me the way here, Hiro. I really appreciated it!"

Hiro "It was my pleasure. And I enjoyed the walk as well!"
Andee "Hehe, same here. I'll see you later, Sir Hiroshi."

"His face goes red at the nickname."

Hiro "A-ah... y-yeah. See ya later."

"His large frame shuffles away into the crowd awkwardly."

Andee "(He was really sweet...)"
Andee "(And handsome...)"
Andee "(Weird thoughts, go away!!)"