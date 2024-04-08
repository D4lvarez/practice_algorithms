# “Accordian” Patience
You are to simulate the playing of games of “Accordian” patience, the rules for which are as follows:

- Deal cards one by one in a row from left to right, not overlapping. Whenever the card
matches its immediate neighbour on the left, or matches the third card to the left, it may
be moved onto that card. Cards match if they are of the same suit or same rank. After
making a move, look to see if it has made additional moves possible. Only the top card of
each pile may be moved at any given time. Gaps between piles should be closed up as soon
as they appear by moving all piles on the right of the gap one position to the left. Deal out the whole pack, combining cards towards the left whenever possible. The game is won if
the pack is reduced to a single pile.

Situations can arise where more than one play is possible. Where two cards may be moved, you should adopt the strategy of always moving the leftmost card possible. Where a card may be moved
either one position to the left or three positions to the left, move it three positions.
## Input
Input data to the program specifies the order in which cards are dealt from the pack. The input contains pairs of lines, each line containing 26 cards separated by single space characters. The final line of the input file contains a ‘#’ as its first character. Cards are represented as a two character code. The first character is the face-value (A=Ace, 2–9, T=10, J=Jack, Q=Queen, K=King) and the second character is the suit (C=Clubs, D=Diamonds, H=Hearts, S=Spades)