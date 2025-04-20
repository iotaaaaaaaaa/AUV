Kovuru Girish Chandra
me24b1048


Hi,I'm Girish . I love solving problems  , I'm a  CP enthusiast.Though im a mech student my interest in cs comes purely from the joy of problem-solving. Solving problems on Codeforces gives me dopamine like its like a detox. I like thinking on that particular question in the contest and the timer tiking  , i dont know i like thinking at those times. My goal is to reach ICPC wfinals represnt my country and be the firstone from our clg. In the upcoming end sem holidays hoping to practice and reach a level so that i can quailfy to regionals in the upcoming premilinary round this year. Also  i love to solve rubix-cube and listen music. Newbie in dev.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Prob1   - Approach 

  So , Given was u need to create a chat convo between two people on same node and same topic so i created  the node and intialised the topic as chat and then runned the program initally i took the input of the user and  with the user name i.e i sent it like user: msg he texted like that to the callback so that it identifies who is sending the message\

Prob1 - problem faced 

problem was when i ran initially with two same names in the diff terminals in my initial code i wrote like if the user types his nmae intially as jolyne then other name = joestar or viceversa and was checking if username = othername then dont printthe msg but as the variables are local to the terminal i didnt know that so what i did was i just wrote that thing i sent msg liek this uername : and the msg so when this goes into the call back function it will split :  and take the name and check if name is same then dont print inthe terminal .
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Prob 2 - Appraoch 
So , this was like u need to create a node publisher which publishes multiples of 2 and a subscriber node 1 recieves it and multiplies with 10 and send it to anotehr publiehr node of some other topic and then this is sent to subscriber node 2 and add plus to the result.  so i just followed the process just creation and recieving 

Prob2 - problems faced 
NO problems faced i was able to get the output

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Prob 3 - Approach 
So , in the question u  were needed to generate a custom msg name it as bot_msg and then simulate the botmovement consdiering that the bot starts at origin (0,0). and also extra marks were to be rewarded for the statemeachine path . the only problem was the custom msg part bcuz of that the code is not compiling i dont know what the problem is other than that coming tothe approach so i assumed bot either moves +1 or -1 for each step / directional movement consdiering intially some random direction say rigt in my case i wrote if else condn for each direction and incremented my varaibles based on that if it was forward then x+=1 like that  for this i used states and stored them as up lefft right down  and also maitained the path using modulo part so that the cirular path is maintained thats it and then published coming to the reciver part it was suppposed to print the bot posiition is x,y coords but due tto the custom msg error bot_msg it didnt run same

prob3 - PRoblem faced 
the custom msg part gave me a headache a lot i use gpt for this to know what is the error but still i diddnt get it i did the process correct but still i dont know even the statemachine parth was also written in the subscriber the only error 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Prob4 - Approach
So , int this question u were asked to create a pipline to show the camera output with the help of openCv . Honestly these two  problems ate my brain ill work on this after submission , so my approach was i imoprted allthe dependenies then init node and a bridge and i wrote the normal code initalising camera that is my laptop cam  and and also checked that frame or cap.read() empty hthen no camera is detected should get displayed so this was my approiach i thought lets intialise cam to videocapture to default and then run the code so when i run it pipline gets created but the no camera is detected should get displayed as a msg 


PRob4 - problem faced 
So, there was a problem here when i ran it it showed me gstreamer error pipline not created and then displayed NO camera detected. I dont know i took help of gpt also but still the installaton problem was not solved 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


prob5 - Approach 
So , again u need to create a pipeline to get teh camera output also run edge detection and publish img to ros show this image to sub script  i took a node init it and camera again with default i.e 0 laptop cam and then implemented edge detection 100 , 200 i took the help of gpt to implement it and understand the algorithm behind it . and then wrote sub code for it and then just converting the ros image and call back 
prob5 - problem faced 
Same issue , the camera was not getting detected the piplne was not created and eventually it showef an error gstreamer error something that pipeline was not created 


_-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Conclusion: 

It was nice solving those problems especially the third one was interesting i like those kindaproblems in which visulaisation is there and i didnt quite  perform  to my peak ,  there was a lot of installtion erros and package not detecting error ,  will surely learn and try to add some stronger value.

