# 백준 3085, 사탕 게임
def count_max_candies(board):
    max_candies = 0
    n = len(board)

    # 가로로 연속한 사탕들을 교환하며 최대 사탕 수 계산
    for i in range(n):
        for j in range(n - 1):
            if board[i][j] != board[i][j + 1]:
                # 교환
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                # 현재 보드에서 최대 사탕 수 계산
                max_candies = max(max_candies, count_max_candies_in_board(board))
                # 원래대로 돌려놓음
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

    # 세로로 연속한 사탕들을 교환하며 최대 사탕 수 계산
    for i in range(n - 1):
        for j in range(n):
            if board[i][j] != board[i + 1][j]:
                # 교환
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                # 현재 보드에서 최대 사탕 수 계산
                max_candies = max(max_candies, count_max_candies_in_board(board))
                # 원래대로 돌려놓음
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

    return max_candies

def count_max_candies_in_board(board):
    n = len(board)
    max_candies = 0

    # 가로로 연속한 사탕 수 계산
    for i in range(n):
        count = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                count += 1
            else:
                max_candies = max(max_candies, count)
                count = 1
        max_candies = max(max_candies, count)

    # 세로로 연속한 사탕 수 계산
    for j in range(n):
        count = 1
        for i in range(1, n):
            if board[i][j] == board[i - 1][j]:
                count += 1
            else:
                max_candies = max(max_candies, count)
                count = 1
        max_candies = max(max_candies, count)

    return max_candies

def main():
    n = int(input())
    board = [list(input()) for _ in range(n)]
    
    result = count_max_candies(board)
    print(result)

if __name__ == "__main__":
    main()
