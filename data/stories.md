
## interactive_story_1
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* goodbye

## interactive_story_1
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* goodbye
    - action_restart

## interactive_story_2
* goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* location{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "bengaluru"}
    - utter_request_email
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "shanmukhanaidu9@gmail.com"}
    - slot{"email": "shanmukhanaidu9@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - action_restart

## interactive_story_1
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "bengaluru"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"got_all": "yes"}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "asdfg7@gmail.com"}
    - slot{"email": "asdfg7@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "asdfg7@gmail.com"}
    - slot{"email": "asdfg7@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "north indian", "location": "new delhi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "new delhi"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* not{"not": "no"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low", "location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "srinivas111@gmail.com"}
    - slot{"email": "srinivas111@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - action_restart

## interactive_story_1
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "srinivas111@gmail.com"}
    - slot{"email": "srinivas111@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "italian", "location": "Delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Delhi"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "qwerty@protonmail.com"}
    - slot{"email": "qwerty@protonmail.com"}
    - action_send_email
    - utter_mail_sent
    - action_restart

## interactive_story_1
* restaurant_search{"price": "high", "location": "Delhi"}
    - slot{"location": "Delhi"}
    - slot{"price": "high"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "italian", "location": "bengaluru"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bengaluru"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
* not
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"price": "high", "cuisine": "indian", "location": "jaipur"}
    - slot{"cuisine": "indian"}
    - slot{"location": "jaipur"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* location{"location": "jalandhar"}
    - slot{"location": "jalandhar"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "srinivas.soma@gmail.com"}
    - slot{"email": "srinivas.soma@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "italian", "location": "warangal"}
    - slot{"cuisine": "italian"}
    - slot{"location": "warangal"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "gajulajagadeesh7@gmail.com"}
    - slot{"email": "gajulajagadeesh7@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "american"}
    - slot{"cuisine": "american"}
    - slot{"price": "low"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "dharmavaram"}
    - slot{"cuisine": "italian"}
    - slot{"location": "dharmavaram"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - reset_slots
    - utter_email_prompt
* email{"email": "admin@cpanel.com"}
    - slot{"email": "admin@cpanel.com"}
    - action_send_email
    - reset_slots
    - utter_mail_sent
    - action_restart

## interactive_story_1
* restaurant_search{"price": "high", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - action_search_restaurants
    - slot{"location": "jodhpur"}
    - slot{"price": "high"}
    - slot{"cuisine": "italian"}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "emantav@gmail.com"}
    - slot{"email": "emantav@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_mail_sent
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "bengaluru"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bengaluru"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "gajulajagadeesh7@gmail.com"}
    - slot{"email": "gajulajagadeesh7@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_mail_sent
    - action_restart

## interactive_story_1
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* cuisine{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "gajulajagadeesh7@gmail.com"}
    - slot{"email": "gajulajagadeesh7@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "asdfg7@gmail.com"}
    - slot{"email": "asdfg7@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_mail_sent
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* goodbye{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "mexican", "location": "jodhpur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "jodhpur"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "asdfg7@gmail.com"}
    - slot{"email": "asdfg7@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_mail_sent
    - action_restart

## interactive_2
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "shanmukhanaidu9@gmail.com"}
    - slot{"email": "shanmukhanaidu9@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_mail_sent

## interactive_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - utter_ask_price
* price{"price": "<300"}
    - slot{"price": "<300"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - reset_slots
    - utter_default
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "shanmukhanaidu9@gmail.com"}
    - slot{"email": "shanmukhanaidu9@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_mail_sent

## interactive_5
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh", "cuisine": "Rishikesh"}
    - slot{"cuisine": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - utter_ask_cuisine
* cuisine{"cuisine": "chines"}
    - slot{"cuisine": "chines"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - reset_slots
    - utter_default
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "shanmukhanaidu9@gmail.com"}
    - slot{"email": "shanmukhanaidu9@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_mail_sent
    - action_restart

## interactive_6
* greet
    - utter_greet
* restaurant_search{"price": "cheap", "cuisine": "thai", "location": "delhi"}
    - slot{"cuisine": "thai"}
    - slot{"location": "delhi"}
    - slot{"price": "cheap"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "shanmukha.ravi@gmail.com"}
    - slot{"email": "shanmukha.ravi@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_mail_sent
    - action_restart

## interactive_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "shanmukhanaidu9@gmail.com"}
    - slot{"email": "shanmukhanaidu9@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_mail_sent
    - action_restart

## interactive_8
* greet
    - utter_greet
* restaurant_search{"location": "cuttack"}
    - slot{"location": "cuttack"}
    - utter_ask_cuisine
* cuisine{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "shanmukhanaidu9@gmail.com"}
    - slot{"email": "shanmukhanaidu9@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart

## interactive_9
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_10
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_11
* greet
    - utter_greet
* restaurant_search{"price": "expensive", "cuisine": "italian", "location": "new delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "new delhi"}
    - slot{"price": "expensive"}
    - action_search_restaurants
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_12
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* cuisine{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* price{"price": "300-700 range"}
    - slot{"price": "300-700 range"}
    - action_search_restaurants
    - utter_email_prompt
* email{"email": "shanmukhanaidu9@gmail.com"}
    - slot{"email": "shanmukhanaidu9@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_mail_sent
    - action_restart
