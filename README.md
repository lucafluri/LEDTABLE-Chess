# CHESS for LED-TABLE

Chess Application for my LED-TABLE.  
https://github.com/lucafluri/LEDTABLE

**Status:** Base App finished

### Idea  
Chess App (for starting and simplicity purposes without Computer at the beginning).  
And due to only being able to display color, the 12 pieces (6 per Side) have to be displayed in different differentiable colors. As the Table has a  10x10 LED Array there will be a 1 thick LED Border around the Chessboard in which additional information can be stored (as in whos turn it is and check/mate warnings).
Obviously there wont be any checkerboard pattern during play, but i might use it as a startup animation.


### Color Scheme  

<img src="https://github.com/lucafluri/LEDTABLE-Chess/blob/master/chessBoard.png" alt="chessboard" height="300">  

The above Picture represents the chessboard with all correct RGB Values. The general Idea is that the color for the white pieces look a bit lighter/washed out.  
One can rarely see the difference between the black Rooks and Pawns on a normal Screen, but since the LED's in the Table aren't perfect, the difference is very noticable and the black Rooks look a lot more purple. I might change the colors of the Rooks to a cyan color.


### Current State
The Program is currently able to correctly validate any move, all special Chess Rules (Castling, En Passant and Promotions) have been accounted for. It is also possible to load PGN files and "let it play".  
The Base App is therefore finished.




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
