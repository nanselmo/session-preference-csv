# Session Preference Slotrer
Takes session preference inputs from attendees and outputs the session rosters. 
* First submissions get first preference until that session is a their max.
* Once the max for a session is reached, attendees will get their second choice
* If neither are available, the attendee is not "slotted" and can be added to a slot manually

**Input:** CSV, one name per row, with time stamp and preference of sessions (A-D)

**Output:** CSV, same input CSV with two columns showing which session the attendee has been slotted for. 
