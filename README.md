# Chess
Chess implemented in python

  * Castle not included

## Times
| sessions | time    |
| -------- | ------- |
| 1        | 1:34:58 |
| 2        | 0:39:20 |
| 3        | 1:39:36 |
| 4        | 2:06:39 |
| -------- | ------- |
| Total    | 6:00:23 |

## Claude review
Critical bugs:
  - range(position[0] - 1, -1) -> range(position[0] - 1, -1, -1) bug in Queen, Bishop, and Rook protects \[FIXED\]
  - Pawn checks wrong player in protects() \[FIXED\]
  - No discovered check validation. Pieces cannot get pinned. Pieces can move the king into check. \[FIXED\]
  - Pawns can capture forward \[FIXED\]
  - Pawns can jump over pieces \[FIXED\]

Missing features:
  - Castling
  - En passent
  - Pawn promotion
  - Stalemate

