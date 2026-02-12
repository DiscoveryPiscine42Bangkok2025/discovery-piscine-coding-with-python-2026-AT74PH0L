def checkmate(board):
    try:
        lines = board.split("\n")
        size = len(lines) # row

        arr = []
        for i in range(size):
            row = []
            for j in range(len(lines[i])):
                if(size != len(lines[i])):
                    return
                row.append(lines[i][j])
            arr.append(row)
        
        king_x = -1
        king_y = -1

        for i in range(size):
            for j in range(size):
                if arr[i][j] == "K":
                    king_x = i
                    king_y = j
        
        if king_x == -1:
            return

        # Pawn
        if king_x + 1 < size and king_y - 1 >= 0:
            if arr[king_x + 1][king_y - 1] == "P":
                print("Success")
                return

        if king_x + 1 < size and king_y + 1 < size:
            if arr[king_x + 1][king_y + 1] == "P":
                print("Success")
                return


        # Rook / Queen
        i = king_x - 1
        while i >= 0:
            if arr[i][king_y] != ".":
                if arr[i][king_y] == "R" or arr[i][king_y] == "Q":
                    print("Success")
                    return
                break
            i -= 1

        i = king_x + 1
        while i < size:
            if arr[i][king_y] != ".":
                if arr[i][king_y] == "R" or arr[i][king_y] == "Q":
                    print("Success")
                    return
                break
            i += 1

        j = king_y - 1
        while j >= 0:
            if arr[king_x][j] != ".":
                if arr[king_x][j] == "R" or arr[king_x][j] == "Q":
                    print("Success")
                    return
                break
            j -= 1

        j = king_y + 1
        while j < size:
            if arr[king_x][j] != ".":
                if arr[king_x][j] == "R" or arr[king_x][j] == "Q":
                    print("Success")
                    return
                break
            j += 1

        # Bishop / Queen
        i = king_x - 1
        j = king_y - 1
        while i >= 0 and j >= 0:
            if arr[i][j] != ".":
                if arr[i][j] == "B" or arr[i][j] == "Q":
                    print("Success")
                    return
                break
            i -= 1
            j -= 1

        i = king_x - 1
        j = king_y + 1
        while i >= 0 and j < size:
            if arr[i][j] != ".":
                if arr[i][j] == "B" or arr[i][j] == "Q":
                    print("Success")
                    return
                break
            i -= 1
            j += 1

        i = king_x + 1
        j = king_y - 1
        while i < size and j >= 0:
            if arr[i][j] != ".":
                if arr[i][j] == "B" or arr[i][j] == "Q":
                    print("Success")
                    return
                break
            i += 1
            j -= 1

        i = king_x + 1
        j = king_y + 1
        while i < size and j < size:
            if arr[i][j] != ".":
                if arr[i][j] == "B" or arr[i][j] == "Q":
                    print("Success")
                    return
                break
            i += 1
            j += 1

        print("Fail")

    except:
        return
