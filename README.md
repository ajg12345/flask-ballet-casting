# flask-ballet-casting
A flask version of the casting application I developed while working at the Joffrey Ballet.
Just to reinforce my understanding of flask.
The original is called SWAC and its written in php. Here is the link: https://github.com/ajg12345/SWAC


Here are some of the important CAPABILITIES:
* create productions 
* create rehearsals and performances of those productions
* create castings for those rehearsals and performances 
* create locations
* create roles and role conflicts (see restriction below)
* view and print daily rehearsal schedule
* create notifications of emergency recasting 
* view and select through monthly calendar menu
* also update and delete most of those things
* make copying roles, role conflicts, and castings easy
* error handling


Here are some of the observed CONSTRAINTS:
* no dancer can be scheduled for a rehearsal over 3 hours at a time  (union stipulation)
* no dancer can rehearse over 6 hours in a day (daily limit)
* there are roles that cannot be cast by the same dancer in a performance, so that problem casting is impossible (role conflicts)
* casting changes must have color coded text as indicator
* only logged in users can see this schedule
* only priveleged users can see or use the admin menu
* secure passwords 



