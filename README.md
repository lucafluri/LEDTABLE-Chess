# CHESS for LED-TABLE

Chess Application for my LED-TABLE.  
https://github.com/lucafluri/LEDTABLE

**Status:** In Progress

### Idea  
Chess App (for starting and simplicity purposes without Computer at the beginning).  
And due to only being able to display color, the 12 pieces (6 per Side) have to be displayed in different differentiable colors. As the Table has a  10x10 LED Array there will be a 1 thick LED Border around the Chessboard in which additional information can be stored (as in whos turn it is and check/mate warnings).
Obviously there wont be any checkerboard pattern during play, but i might use it as a startup animation.

### TODO
- ~~Start~~
- ~~Program base App~~
- ~~Choose and test Colors for Pieces~~
- ~~Check for Checks and Mates~~
- ~~ListPossibleMoves(side)~~
- ~~Check for Stalemates~~
- ~~Correct Chess Notation output~~
  - ~~Check for same piece that might be able to move to Square (No Pawns)~~
- ~~Chess Notation Parser for Input~~
  - ~~Find Piece and execute move~~
  - ~~File Input for PGN Files~~
    - ~~Speed Control~~, and Reverse Move
- Update Android/Kivy App
  - ~~Decide on Input Method~~
  - ~~Several Screens are needed Menu~~
    - ~~Mode Selection~~
    - ~~Send Move in Notation Style~~
    - ~~(Input PGN)~~
  - Button to highlight own Pieces
  - (Two Way Communication, simple Text information in App)?
- highlightOwnPieces(side) because differentiating the Pieces becomes increasingly difficult the fewer there are
- highlightPossibleMoves(piece) (by turning all reachable Squares white for 0.5 sec)
- (List capture Pieces per Side)?
- (Computer) (The App is currently not very good coded, but it works very well. But the Pi has to do a lot of Computation per Move, so adding more for "Chess Computer" Purposes adds a lot of calculation time. But that shouldn't be a problem because moves should not be executed instantly...)
  - Running Score per Side (Piece Advantage)
  - Move Eval()
    - For each Piece, list all pieces it is protected by
    - Update all piece information  

.  
.  
.    
