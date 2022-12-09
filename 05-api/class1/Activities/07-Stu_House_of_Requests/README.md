# House of Requests

You've been challenged to a game of BlackJack, but you don't have any playing cards on-hand. Instead of spending money to buy a set, find a way to programmatically play the game. Use the `Deck of Cards API`, an API that simulates card games through API calls, to play against a classmate or an imaginary dealer. The player with the number of points closest to 21 is the winner!

While you won't actually win any real prizes in this game, you will get the opportunity to crush opponents in Python BlackJack and gain the respect of your peers.

API URLs (store these as variables)

* Create a deck and shuffle -> `f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6" `

* Draw cards -> `f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"`

* Shuffle pre-existing deck -> `f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/"`

Rules of the Game

* The first to 21 wins!

* Scoring over 21 means you automatically lose.

* Each player-turn consists of one to two drawings. Decide if you should draw two or three cards for your turn. The closer to 21 you are, the less rounds you should take, unless you're feeling risky.

  * An initial drawing of 2 cards

  * A second drawing of 1 additional card (optional)

## Instructions

Prep for the Game

1. Submit a `parameterized` `GET` request to create and shuffle a deck of cards.

2. Extract the value of `deck ID` from the JSON output, and store it as a variable. This value will be interpolated into the `Draw Cards` and `Shuffling Deck` `request urls`.

3. `Parameterize` the `request url`. Pass in the `deck_id`, and set the `count` parameter to 2 via interpolation.

Player 1 Turn

4. Execute a `GET` request using the `draw_cards_url`.

5. Parse the JSON and extract values for elements `suit` and `value` for each card. Store `suit` and `value` for each card into respective variables (i.e. `player_1_card_1`).

6. Manually add the numeric values to determine your points. How close to 21 did you get? If you scored 21 or below, you can consider drawing another card for yourself, or you can decide to end your turn, and let the dealer go next.

    * Cards with numbers from 2 to 10 gain respective points (have their face value).

    * Jacks, Queens, and Kings gain 10 points.

    * Aces might be counted as 11 or 1 point, depending on the value needed for a best hand.

7. If you're taking another turn, complete step 8. Otherwise, skip to step 9.

8. `Parameterize` the `request url` to return 1 additional card for you. Re-calculate your total points.

Player 2 Turn

9. Execute a `GET` request using a parameterized `request url` that will draw `2` cards for the dealer. Hint: Make sure to check the latest `request_url` parameters. `Count` might not equal `2`.

10. Repeat steps 5-8 for the dealer, and then compare scores. The player closest to 21 wins! Anyone with more than 21 points automatically loses.

### Hint

Interpolation can be achieved by using the literal `f` prefix before a string. Consult the [documentation](https://www.programiz.com/python-programming/string-interpolation) for assistance.

When extracting values from the `Draw Cards` request, an index will have to be provided to extract values whenever more than one card is returned (i.e. `drawn_cards['cards'][0]['value'] + " of " + drawn_cards['cards'][0]['suit']`).

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
